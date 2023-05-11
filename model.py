import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics  


df = pd.read_csv('C:/Users/User/JupyterLab/Projects/Drug/drug200.csv')

sex = LabelEncoder()
bp = LabelEncoder()
chol = LabelEncoder()
drug = LabelEncoder()

sex.fit(df['Sex'])
bp.fit(df['BP'])
chol.fit(df['Cholesterol'])
drug.fit(df['Drug'])

df['Sex'] = sex.transform(df['Sex'])
df['BP'] = bp.transform(df['BP'])
df['Cholesterol'] = bp.transform(df['Cholesterol'])
df['Drug'] = drug.transform(df['Drug'])
        
x, y = df.drop(columns=['Drug']), df['Drug']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

clf = RandomForestClassifier(max_depth=10, random_state=1)
clf.fit(x_train, y_train)

y_predict = clf.predict(x_test).reshape(-1, 1)
acc = metrics.accuracy_score(y_test, y_predict)

def show_prediction_score():
    print(acc)

def encode_input(data, cat):
    if cat == 'Sex':
        return sex.transform(data)
    if cat == 'BP':
        return bp.transform(data)
    if cat == 'Cholesterol':
        return chol.transform(data)

def reverse_output(datas):

    def predict(datas):
        return clf.predict(datas)
    
    return drug.inverse_transform(predict(datas))

x = reverse_output([[40, 0, 2, 1, 22.000]])
print(x[0])