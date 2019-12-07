import numpy as np
import pre
from tqdm import tqdm


class CoMatrix():
    """
    文章ベクトル
    　＝　文書中に現れた全単語の単語ベクトルを足し合わせ、総単語数で割る
    　＝　文書中に現れた単語のベクトルを、全単語 計算する。
    　　　 → 文章を入力すると、その文章に含まれる全単語ベクトルを足し合わせ、総単語数で割った値を返す。
    """
    def __init__(self, token2id, tknd_all_sentences, window_size=2):
        # 文書中に現れた単語のベクトルを、全単語分 計算する。
        vocab_size = len(token2id)
        self.co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)
        self.w2i = token2id
        # 初期化時に、共起行列ベクトルを完成させておく。
        for tknd_s in tqdm(tknd_all_sentences):
            self.update(tknd_s)

    def update(self, tknd_corpus, window_size=2):
        """
        共起行列を update する。
        次元数は self.w2i に固定される。
        self.w2i に存在しない単語は skip される。

        :param tknd_corpus(list):
            分かち書きされ、ID化された文（章）
            [['吾輩', 'は', '猫', 'である'],
             ['名前', 'は', 'まだ', 'ない']]
        :param co_matrix:
        :param window_size:
            共起判定の範囲。ウィンドウサイズ
        """
        corpus_size = len(tknd_corpus)
        try:
            for ti in range(corpus_size):
                for ci in range(1, window_size + 1):
                    if ti-ci >= 0:
                        self.update_co_matrix(tknd_corpus[ti], tknd_corpus[ti - ci])
                    if ti+ci < corpus_size:
                        self.update_co_matrix(tknd_corpus[ti], tknd_corpus[ti + ci])
        # Python の exception は早いので、速度的にも問題はないはず。
        except KeyError:  # 無視する単語は飛ばす
            pass
    
    # co_matrix を更新する定義
    def update_co_matrix(self, target_w, context_w):
        self.co_matrix[self.w2i[target_w], self.w2i[context_w]] += 1

    def embed_co_marrix(self, tknd_corpus):
        """
        全単語ベクトルを足し合わせ、総単語数で割る
        """
        sum_vec = np.zeros_like(self.co_matrix[1,:])
        for token in tknd_corpus:
            sum_vec += self.co_matrix[self.w2i[token],:]
            # print(sum_vec)
        sum_vec = sum_vec / len(tknd_corpus)  # 総単語数で割る
        return sum_vec



if __name__ == "__main__":
    try:  # 無視する単語は飛ばす
        test_dict = {'a': 3, 'b': 45}
        test_dict['c']
    except KeyError:
        print('無視する単語は飛ばす\n')


    # test
    tknd_corpus = [['吾輩', 'は', '猫', 'である', '。'],
                    ['名前', 'は', 'まだ', 'ない', '。'],
                    ['吾輩', 'は', 'ここ', 'で', '始めて', '人間', 'という', 'もの', 'を', '見た', '。']]
    # まず word2id を作る。
    token_set = set()
    for tknd_s in tqdm(tknd_corpus):
        token_set = token_set | set(tknd_s)   # Token の集合（set） を作成。（set は、dict のkeyだけ版）
    data_w2i = pre.identify_some_tokens(token_set)
    print(data_w2i)
    # word2id を元に、共起行列を作る。
    cm = CoMatrix(data_w2i, tknd_corpus)
    print(cm.co_matrix)
    # 共起行列を元に、入力文（章）をベクトル化
    for tknd_s in tknd_corpus:
        print('--------------------------')
        vec = cm.embed_co_marrix(tknd_s)
        print('sentence : {} \nlen : {}  \nvec : \n{}'.format(tknd_s, len(vec), vec))

