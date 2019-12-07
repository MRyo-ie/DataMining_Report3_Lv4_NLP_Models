# coding: utf-8

# 参考
# ・ Bag of Wordsについて書いてみる
#     - https://www.pytry3g.com/entry/2018/03/21/181514
#     - 一部、高速化のために numpy に変更。

import numpy as np

class BoW():
    """
    分かち書き された文（章）の Token を、
    word2id に従って カウントする。
    """
    def __init__(self, word2id):
        self.w2i = word2id

    # 1文（章）ずつ処理する。
    def embed_BoW(self, tknd_corpus):
        """
        :param : tknd_corpus
            Tokenのリスト = 分かち書きされた文（章）
        :return : bow
            BoW 形式のベクトル。
            各次元は、word2id で規定される。
        """
        # Bag of Wordsを作る
        bow = np.zeros( len(self.w2i) )
        for token in tknd_corpus:
            try:
                bow[self.w2i[token]] += 1
            except:
                pass
        return bow

