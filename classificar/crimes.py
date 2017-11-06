import numpy as np
import matplotlib.pyplot as plt
from util.Util import size_mb
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from util.Train import benchmark

from util.BaseDadosCriminosos import get_data
from util.BaseDadosCriminosos import get_target_names
from util.BaseDadosCriminosos import get_target
from util.BaseDadosCriminosos import get_text_list
from util.BaseDadosCriminosos import crimes
from random import randrange

data_train = get_data(type="train")

data_test = get_data(type="test")

target_names = get_target_names()

y_train, y_test = get_target(data_train), get_target(data_test)

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)

crimes_train = get_text_list(data_train)
crimes_test = get_text_list(data_test)

X_train = vectorizer.fit_transform(crimes_train)

X_test = vectorizer.transform(crimes_test)

results = []

clf = Perceptron(max_iter=50)

print('=' * 80)


results.append(benchmark(clf, target_names, X_train, y_train, X_test, y_test, False, False))
print(results)

crime = "Pedofilia, Propina, Corrupção Ativa, Atear fogo em pessoas, Estupro"
print("Testando crime: "+crime)
v_crime = []
v_crime.append(crime)

X_beta_test = vectorizer.transform(v_crime)

pred = clf.predict(X_beta_test)

print(pred)


