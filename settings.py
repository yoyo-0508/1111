# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 1
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'SCF=AuReaxsSZnbOg--cLmox1B_9L8KEW40bY9b6dGrrGYaRUrT7yJbKNyySz-YxwlKNEr14t9PGKDntMnQ2g3q49zs.; UOR=,,github.com; SINAGLOBAL=3127160181291.5728.1729005488183; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWPukfSCjU3sYlSFl29zj645JpX5KMhUgL.FoMfeoqcSh20S0z2dJLoI0YLxKML1K.LB.BLxKnL122LBonLxKnLBo2L1hqLxKqLBoeLBK-LxKMLB.-L12-LxK-LBo5L1K2LxK-LBK-LBoet; XSRF-TOKEN=z0A5BW2TFB8lYUKYKXMsfc4W; _s_tentry=weibo.com; Apache=8168168072637.012.1734567173868; ULV=1734567173870:502:17:7:8168168072637.012.1734567173868:1734433832869; ALF=1737198372; SUB=_2A25KZ450DeRhGeFL6VQX9C_PzD6IHXVpHI-8rDV8PUJbkNAYLU7EkW1NQlfuyDpwBgvDJdJm70o7J60F6BtDH4Ua; WBPSESS=kKvJ0l1ShLKfwCHl8l3VFqupStiXBeIj11YMoNmbZlad82yQ-I67jUW1aPvlLiOZ3Ghxxguycp2jYXdTj1aCmY9AoRHK0hisoXehIf3Vv7kLn5tYREF8xHq-edRq_8TfvTSpSwSW5HrXW4FLIcH8dg=='
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['西北民族大学']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 0
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2024-10-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2024-10-01'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
