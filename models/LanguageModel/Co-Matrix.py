import numpy as np
import pre
from tqdm import tqdm


class CoMatrix():
    """
    文章ベクトル
    　＝　文書中に現れた全単語の単語ベクトルを足し合わせ、総単語数で割る
    　＝　文書中に現れた単語のベクトルを、全単語分 計算する。
    　　　 → 文章を入力すると、その文章に含まれる全単語ベクトルを足し合わせ、総単語数で割った値を返す。
    """
    def __init__(self, token2id):
        # 文書中に現れた単語のベクトルを、全単語分 計算する。
        vocab_size = len(token2id)
        self.co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)
        self.w2i = token2id


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
                    if ti-ci > 0:
                        self.update_co_matrix(tknd_corpus[ti], tknd_corpus[ti - ci])
                    if ti+ci < corpus_size:
                        self.update_co_matrix(tknd_corpus[ti], tknd_corpus[ti + ci])
        # Python の exception は早いので、速度的にも問題はないはず。
        except KeyError:  # 無視する単語は飛ばす
            pass
    
    # co_matrix を更新する定義
    def update_co_matrix(self, target_w, context_w):
        self.co_matrix[self.w2i[target_w], self.w2i[context_w]] += 1

    def embed_co_marrix(self):
        """
        全単語ベクトルを足し合わせ、総単語数で割る
        """



if __name__ == "__main__":
    # word_list=['natural', 'language', 'text', 'count', 'word', 'tknd_corpus', 'python', 'program', 'programs']
    # token2id = pre.identify_some_tokens(word_list)
    # vocab_size = len(word_list)
    # co_matrix = None
    # for text in tqdm(docs):
    #     tknd_corpus = build_tknd_corpus(text, token2id,   word_list)
    #     co_matrix = update_matrix(tknd_corpus, vocab_size, co_matrix, window_size=2)

    # # cos類似度適用前
    # print('\n')
    # pd.DataFrame(co_matrix, index=word_to_id.keys(), columns=word_to_id.keys())

    try:  # 無視する単語は飛ばす
        test_dict = {'a': 3, 'b': 45}
        test_dict['c']
    except KeyError:
        print('無視する単語は飛ばす')


    # test
    tknd_corpus = [['吾輩', 'は', '猫', 'である'], ['名前', 'は', 'まだ', 'ない']]
    # まず word2id を作る。
    token_set = set()
    for tknd_s in tqdm(tknd_corpus):
        token_set = pre.add_tokens_set(token_set, tknd_s)   # Token の集合（set） を作成。（set は、dict のkeyだけ版）
    data_w2i = pre.identify_some_tokens(token_set)
    print(data_w2i)
    # word2id を元に、共起行列を作る。
    cm = CoMatrix(data_w2i)
    for tknd_s in tqdm(tknd_corpus):
        cm.update(tknd_s)  # Token の集合（set） を作成。（set は、dict のkeyだけ版）
    print(cm.co_matrix)
