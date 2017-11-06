import numpy as np
import matplotlib.pyplot as plt
from util.Util import size_mb
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from util.Train import benchmark

categories = [
        'alt.atheism',
        'talk.religion.misc',
        'comp.graphics',
        'sci.space',
    ]

remove = ()

data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42,
                                remove=remove)


data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42,
                               remove=remove)


print("Dados carregados")

target_names = data_train.target_names

print("Categorias>")
print(target_names)

print("%d documents - %0.3fMB (training set)" % (len(data_train.data), size_mb(data_train)))
print("%d documents - %0.3fMB (test set)" % (len(data_test.data), size_mb(data_test)))

#Extraindo y do conjunto de treinamento e de teste
y_train, y_test = data_train.target, data_test.target

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')

X_train = vectorizer.fit_transform(data_train.data)

X_test = vectorizer.transform(data_test.data)

# mapping from integer feature name to original token string
feature_names = vectorizer.get_feature_names()


results = []

clf = Perceptron(max_iter=50)

print('=' * 80)


results.append(benchmark(clf, target_names, X_train, y_train, X_test, y_test, True, True))

print(results)
