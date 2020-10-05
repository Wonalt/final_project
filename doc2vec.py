import gensim
import numpy as np
import jieba
from gensim.models.doc2vec import Doc2Vec, LabeledSentence
# stop_text = open('stop_list.txt', 'r')
# stop_word = []
# for line in stop_text:
#     stop_word.append(line.strip())
TaggededDocument = gensim.models.doc2vec.TaggedDocument
with open("stop_list.txt", 'r', encoding='utf-8') as r:
    stop_list = r.readlines()
def get_corpus():

    with open("data/corpus_seg.txt", 'r',encoding='utf-8') as doc:
        docs = doc.readlines()
    train_docs = []
    for i, text in enumerate(docs):
        # word_list = text.split(' ')
        word_list_tmp = jieba.lcut(text)
        word_list = [e for e in word_list_tmp if e not in stop_list]
        length = len(word_list)
        word_list[length - 1] = word_list[length - 1].strip()
        document = TaggededDocument(word_list, tags=[i])
        train_docs.append(document)
    return train_docs

def train(x_train, size=200, epoch_num=1):
    model_dm = Doc2Vec(x_train, min_count=1, window=3, vector_size=size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=700)
    model_dm.save('model_doc2vec')
    return model_dm

def test():
    model_dm = Doc2Vec.load("model_doc2vec")
    text_test = u'在时代下,信息管理与信息系统的应用越发受到人们重视。当下,信息资源炙手可热,尤其是各行各业正在大力发展的情况下,有必要完善信息管理与信息系统建设,创新企业管理模式,实现资源的优化配置和利用。笔者主要对时代下的信息管理与信息系统管理进行了分析。'
    text_raw = jieba.lcut(text_test)
    text_raw = [e for e in text_raw if e not in stop_list]
    inferred_vector_dm = model_dm.infer_vector(text_raw)
    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=10)

    return sims


if __name__ == '__main__':
    x_train = get_corpus()
    model_dm = train(x_train)
    sims = test()
    for count, sim in sims:
        sentence = x_train[count]
        words = ''

        for word in sentence[0]:
            words = words + word
        print(words, sim,count)