
import jieba.analyse

def extract_keywords_textrank(text, top_k=10):
    # 使用 TextRank 提取关键词
    keywords = jieba.analyse.textrank(text, topK=top_k, withWeight=False)
    return keywords
