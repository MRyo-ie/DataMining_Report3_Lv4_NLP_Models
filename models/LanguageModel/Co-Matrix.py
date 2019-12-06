import numpy as np
from tqdm import tqdm

def create_matrix(corpus, vocab_size, num_matrix, window_size=1):
    """共起行列を作成。
    「ゼロから作るDeepLearning2 自然言語処理辺」p.72より。

    :param corpus(str): テキスト文。
    :param vocab_size: 語彙数。
    :param window_size: 共起判定の範囲。
    :return:
    """
    corpus_size = len(corpus)
    if num_matrix is None:
        num_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    # 無視する単語は飛ばす
    # ※ numpyの [インデックス] は、None でもエラーにならないらしいので、out of range させるように調整。
    for idx, word_id in enumerate(corpus):
        # 無視する単語は飛ばす
        if word_id > vocab_size:
            continue
        for i in range(1, window_size+1):
            left_idx = idx - i
            right_idx = idx + i
            if left_idx >= 0:
                left_word_id = corpus[left_idx]
                if left_word_id < vocab_size:  # 無視する単語は飛ばす
                    num_matrix[word_id, left_word_id] += 1
            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                if right_word_id < vocab_size:   # 無視する単語は飛ばす
                    num_matrix[word_id, right_word_id] += 1
    return num_matrix

word_list=['natural', 'language', 'text', 'count', 'word', 'sentence', 'python', 'program', 'programs']
word_to_id, id_to_word = preprocess(word_list)
vocab_size = len(word_list)
num_matrix = None
for text in tqdm(docs):
    corpus = build_corpus(text, word_to_id,   word_list)
    num_matrix = create_matrix(corpus, vocab_size, num_matrix, window_size=2)

# cos類似度適用前
print('\n')
pd.DataFrame(num_matrix, index=word_to_id.keys(), columns=word_to_id.keys())