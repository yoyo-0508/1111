from tfidf import extract_keywords_tfidf
from textrank import extract_keywords_textrank
from bert import extract_keywords_bert

def combined_keyword_extraction(texts, top_k=5):
    tfidf_keywords = extract_keywords_tfidf(texts, top_k=20)
    textrank_keywords = [extract_keywords_textrank(text, top_k=10) for text in texts]
    final_keywords = []
    for text in texts:
        bert_keywords = extract_keywords_bert(text, top_k=top_k)
        final_keywords.append(bert_keywords)
    return final_keywords
