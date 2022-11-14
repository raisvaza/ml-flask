import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv('./data/prostate_cancer.csv')

X = df[["radius", "texture", "perimeter", "area", "smoothness", "compactness", "symmetry", "fractal_dimension"]]
y = df[["diagnosis_result"]]

y['diagnosis_result'].unique()

diagnosis_mapping_dict = {}

for i in range(len(y['diagnosis_result'].unique())):
    diagnosis_mapping_dict[y['diagnosis_result'].unique()[i]] = i

y.loc[y['diagnosis_result'] == 'M', 'diagnosis_result'] = 0
y.loc[y['diagnosis_result'] == 'B', 'diagnosis_result'] = 1

y=y.astype('float')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 8), random_state=1)

clf.fit(X_train,y_train)

predict = clf.predict(X_test)
print(classification_report(y_test, predict))