from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords_tfidf(texts, top_k=10):
    # 创建 TF-IDF 向量器
    vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    
    # 提取每条文本中的最高权重词
    keywords = []
    for row in tfidf_matrix:
        indices = row.nonzero()[1]
        tfidf_scores = zip(indices, [row[0, x] for x in indices])
        sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
        keywords.append([feature_names[idx] for idx, score in sorted_scores[:top_k]])
    
    return keywords
