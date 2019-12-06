# coding: utf-8

# Embedding する前に行う処理を集めた。

# Token（単語）に ID を振る。
# tqdm 使うために、後から追加できる形で実装。
def identify_words(all_sentences, word2id:dict):    
    for s in all_sentences:
        for token in s:
            if token in word2id:
                continue
            word2id[token] = len(word2id)
    return word2id
