# coding: utf-8

# 参考
# ・ Bag of Wordsについて書いてみる
#     - https://www.pytry3g.com/entry/2018/03/21/181514
#     - 一部、高速化のために numpy に変更。

import numpy as np

class BoW():
    def __init__(self, word2id):
        self.w2i = word2id

    # 1文（章）ずつ処理する。
    def embed_BoW(self, sentence):
        """
        Sentences : list[][]
            Token化された文のリスト（Tokenリストのリスト）
        """
        # Bag of Wordsを作る
        bow = np.zeros( len(self.w2i) )
        for token in sentence:
            try:
                bow[self.w2i[token]] += 1
            except:
                pass
        return bow

