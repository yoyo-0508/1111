from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import time
import random
import logging
from collections import Counter
from threading import Lock
import queue

# 配置日志记录
logging.basicConfig(filename='crawler.log', level=logging.ERROR)

# 线程池、令牌桶和防重复机制
max_workers = 16
token_bucket = max_tokens = 10
token_refill_rate = 1
lock = Lock()
url_lock = Lock()
processed_urls = set()

# 动态延迟
delay = 2.0

def adaptive_delay(success=True):
    global delay
    if success:
        delay = max(1.0, delay * 0.9)
    else:
        delay = min(10.0, delay * 1.5)
    actual_delay = delay + random.uniform(-0.5, 0.5)
    time.sleep(actual_delay)

def refill_tokens():
    global token_bucket
    while True:
        with lock:
            if token_bucket < max_tokens:
                token_bucket += 1
        time.sleep(1.0 / token_refill_rate)

threading.Thread(target=refill_tokens, daemon=True).start()

def safe_add_url(url):
    with url_lock:
        if url not in processed_urls:
            processed_urls.add(url)
            return True
    return False

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTPError for {url} - Status Code: {e.response.status_code}")
            if e.response.status_code in [500, 502, 503, 504]:
                time.sleep(2 ** attempt)
            else:
                break
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            time.sleep(2 ** attempt)
    return None

def fetch_url(url):
    if safe_add_url(url):
        with lock:
            if token_bucket > 0:
                token_bucket -= 1
                success = False
                try:
                    content = fetch_with_retry(url)
                    success = content is not None
                    return url, content
                finally:
                    adaptive_delay(success)
    return None

def crawl(url_list):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_url, url) for url in url_list]
        results = [future.result() for future in as_completed(futures)]
    return results
