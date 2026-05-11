import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Запуск ML пайплайна...")

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Параметры модели
hyperparameters = {"n_estimators": 100, "random_state": 42}

# Разделение на train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Обучение модели
model = RandomForestClassifier(**hyperparameters)
model.fit(X_train, y_train)

# Оценка качества
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Точность модели (accuracy): {accuracy:.4f}')
print(f'Пайплайн выполнен успешно!')
