from transformers import BertTokenizer, BertModel
import torch

# 加载中文 BERT 模型
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-chinese')

def extract_keywords_bert(text, top_k=5):
    # 分词和生成 BERT 输入
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)

    # 获取词向量和句子向量
    token_embeddings = outputs.last_hidden_state.squeeze(0)
    sentence_embedding = torch.mean(token_embeddings, dim=0)

    # 计算余弦相似度，选择最相关的词
    scores = torch.nn.functional.cosine_similarity(token_embeddings, sentence_embedding.unsqueeze(0), dim=1)
    sorted_indices = torch.argsort(scores, descending=True)
    keywords = [tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][idx]) for idx in sorted_indices[:top_k]]
    
    return keywords
