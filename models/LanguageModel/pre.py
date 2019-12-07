# coding: utf-8

# Embedding する前に行う処理を集めた。

###  Token（単語）に ID を振る  ###
# sentenceに含まれる、全ての Token の集合を取得する。
# 重複が削除された、Token の集合（set）が返ってくる。
def add_tokens_set(token_set:set, add_tokens_list):
    # 集合(set) に変換して、重複を削除する。
    # 和集合を取る。（重複が削除された状態の、Token の集合が得られる）
    return token_set | set(add_tokens_list)


# 指定した word （some_words に含まれるもののみ）にIDを振る。
# 言い換えると、some_words に ID を振る。
def identify_some_tokens(some_words):
    word2id = {}
    for i, token in enumerate(some_words):
        word2id[token] = i
    return word2id
