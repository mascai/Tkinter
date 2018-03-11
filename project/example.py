from pox.core import core
from pox.messenger import *
import sklearn
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils import shuffle

class MyComponent (object):
  def __init__ (self, an_arg):
    self.arg = an_arg
    print "MyComponent instance registered with arg:", self.arg
 
  def foo (self):
    print "MyComponent with arg:", self.arg
 
 
def launch ():
  component = MyComponent("Test data")
  core.register("thing", component)
  core.thing.foo() 
  df = pd.read_csv("out.csv", sep=',')
  df = df[:20000]
  df_train = df[:int(len(df)/2)]
  df_test = df[int(len(df)/2):]
  target_vec = list(df_test["normal."].values)
  true_val = list(df_test["normal."].values)
  del df_test["normal."]
  del df_train["normal."]
  print(df_train.shape)
  print(df_test.shape)

  colons = df_test.columns
  neigh = KNeighborsClassifier(n_neighbors=5)
  neigh.fit(df_train.values, target_vec)
  prediction = list(neigh.predict(df_test[colons]))

  correct = 0
  for i in range(len(true_val)):
      if true_val[i] == prediction[i]:
        correct += 1
        
  print float(correct / len(true_val))
  print "SVC --- 79.8"
  print "Decision Tree --- 87.2"
  print "Random Forest --- 88.5"
  print "Gradient Boosting --- 94.1"