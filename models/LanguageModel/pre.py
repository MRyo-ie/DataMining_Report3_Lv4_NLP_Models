# coding: utf-8

# Embedding する前に行う処理を集めた。

###  Token（単語）に ID を振る  ###
# 指定した word （some_words に含まれるもののみ）にIDを振る。
# 言い換えると、some_words に ID を振る。
def identify_some_tokens(some_words):
    word2id = {}
    for i, token in enumerate(some_words):
        word2id[token] = i
    return word2id
