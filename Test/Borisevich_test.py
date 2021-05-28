# Импорт библиотек
import os
import pandas as pd
import numpy as np
from flask import Flask, url_for


# Создаем 2 датафрейма с одним столбцом и 100 строчками, заполненными рандомными числами
random_numbers_1 = pd.DataFrame(np.random.randint(0,100,size=(100, 1)), columns=(['Первый набор чисел']))
random_numbers_2 = pd.DataFrame(np.random.randint(0,100,size=(100, 1)), columns=(['Второй набор чисел']))

# Сохраняем датафреймы в формате csv в папку static
try:
    direc = os.mkdir('static')
except: pass

random_numbers_1.to_csv('static/random_numbers_1.csv', index=False)
random_numbers_2.to_csv('static/random_numbers_2.csv', index=False)

 
app = Flask(__name__)
 
@app.route('/')
def home():

    return '''
    <!doctype html>
    <title>Расчет корреляции</title>
        <h1>
    <a href="/correlation">Расчет корреляции для двух наборов чисел</a>
    <h1>
    '''
 
 # Расчет корреляции
@app.route('/correlation')
def correlation():
    url_for('static', filename='random_numbers_1.csv')
    url_for('static', filename='random_numbers_2.csv')
    with open("static/random_numbers_1.csv") as f_1:
        with open("static/random_numbers_2.csv") as f_2:
            numbers_1 = pd.read_csv(f_1)
            numbers_2 = pd.read_csv(f_2)
            df = pd.concat([numbers_1, numbers_2], axis=1)
            corr_matrix = df.corr()
            corr = corr_matrix.iloc[0][1]
            return f'Корреляция между двумя наборами чисел составляет {corr}'         
  
if __name__ == '__main__':
    app.run()


