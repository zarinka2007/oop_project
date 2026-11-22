import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Загрузка данных
df_time = pd.read_csv('Проблема нехватки времени.csv')
df_ing = pd.read_csv("Проблема 'нечего готовить.csv")
df_eq = pd.read_csv('Проблема отсутствия техники.csv')
df_diff = pd.read_csv('Проблема сложности для новичков.csv')
df_survey = pd.read_csv('Проблема глазами людей.csv')

print(df_time.head())
print(df_time.shape, df_time.dtypes)
print(df_time.isna().sum())   # проверка пропусков

# график 1- Столбчатая диаграмма, быстрые и долгие рецепты
quick_counts = df_time['is_quick'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(quick_counts.index, quick_counts.values, color=['green', 'red'])
plt.title('Доля быстрых (до 20 мин) и долгих рецептов')
plt.xlabel('Быстрый рецепт (до 20 минут)')
plt.ylabel('Количество рецептов')
plt.grid(axis='y')
plt.show()

#среднее время по категориям
avg_time = df_time.groupby('category')['cook_time_min'].mean()
print(avg_time)

plt.figure(figsize=(8, 5))
plt.bar(avg_time.index, avg_time.values, color='orange')
plt.title('Среднее время приготовления по категориям блюд')
plt.xlabel('Категория')
plt.ylabel('Среднее время, мин')
plt.grid(axis='y')
plt.show()

#график 2 - Распределение количества ингредиентов

ing_counts = df_ing['ingredient_count'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(ing_counts.index, ing_counts.values, color='steelblue')
plt.title('Распределение рецептов по количеству ингредиентов')
plt.xlabel('Количество ингредиентов в рецепте')
plt.ylabel('Количество рецептов')
plt.grid(axis='y')
plt.show()

# график 3 - Круговая диаграмма, техника
eq_counts = df_eq['required_equipment'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(eq_counts.values, labels=eq_counts.index, autopct='%1.0f%%')
plt.title('Какое оборудование требуется для рецептов')
plt.show()

#график 4 - Столбчатая диаграмма, сложность рецептов

diff_counts = df_diff['difficulty'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(diff_counts.index, diff_counts.values, color='purple')
plt.title('Распределение рецептов по уровню сложности')
plt.xlabel('Уровень сложности')
plt.ylabel('Количество рецептов')
plt.grid(axis='y')
plt.show()

#график 5 - Точечная диаграмма, возраст, время выбора рецепта

students = df_survey[df_survey['status'] == 'Студент']
workers = df_survey[df_survey['status'] == 'Работающий']

plt.figure(figsize=(9, 6))
plt.scatter(students['age_group'], students['time_spent_choosing_min'],
            color='red', label='Студенты', alpha=0.6)
plt.scatter(workers['age_group'], workers['time_spent_choosing_min'],
            color='blue', label='Работающие', alpha=0.6)
plt.title('Время, затрачиваемое на выбор рецепта')
plt.xlabel('Возрастная группа')
plt.ylabel('Время на выбор рецепта, мин')
plt.legend()
plt.grid()
plt.show()

#численные выводы

n_time = len(df_time)
quick_n = (df_time['is_quick'] == 'да').sum()
quick_percent = int(quick_n / n_time * 100)

print('ВЫВОДЫ')
print(f'1. Быстрых рецептов (до 20 мин): {quick_n} из {n_time} ({quick_percent}%)')
print(f'Среднее время готовки: {np.mean(df_time["cook_time_min"])} мин')
print(f'Медиана времени готовки: {np.median(df_time["cook_time_min"])} мин')

mean_ing = np.mean(df_ing['ingredient_count'])  # среднее число ингредиентов
few_ing = (df_ing['ingredient_count'] <= 4).sum()  # количество рецептов с 4 и менее ингредиентами
few_percent = int(few_ing / len(df_ing) * 100)  # их доля в процентах
print(f'2.Среднее число ингредиентов: {mean_ing}')
print(f'Рецептов с 4 и менее ингредиентами: {few_ing} из {len(df_ing)} ({few_percent}%)')

stove_n = (df_eq['required_equipment'] == 'Плита').sum()  # сколько рецептов требуют плиту
micro_n = (df_eq['required_equipment'] == 'Микроволновка').sum()  # сколько готовятся в микроволновке
no_cook_n = (df_eq['required_equipment'] == 'Без готовки').sum()  # сколько не требуют готовки вообще
stove_percent = int(stove_n / len(df_eq) * 100)  # доля рецептов с плитой, %
available_percent = int((micro_n + no_cook_n) / len(df_eq) * 100)  # доля доступных без плиты, %
print(f'3.Требуют плиту: {stove_percent}%')
print(f'Доступно без плиты (микроволновка + без готовки): {available_percent}%')

easy_n = (df_diff['difficulty'] == 'Легко').sum()  # количество простых рецептов
easy_percent = int(easy_n / len(df_diff) * 100)  # их доля в процентах
print(f'4.Простых рецептов: {easy_n} из {len(df_diff)} ({easy_percent}%)')

problem_counts = df_survey['main_problem'].value_counts()  # подсчёт каждой жалобы
main_problem_n = problem_counts.iloc[0]  # число людей с самой частой жалобой
main_percent = int(main_problem_n / len(df_survey) * 100)  # их доля в процентах
delivery_n = (df_survey['orders_delivery_if_cant_choose'] == 'да').sum()  # сколько заказывают доставку
delivery_percent = int(delivery_n / len(df_survey) * 100)  # их доля в процентах

students = df_survey[df_survey['status'] == 'Студент']  # только студенты
workers = df_survey[df_survey['status'] == 'Работающий']  # только работающие
avg_students = np.mean(students['time_spent_choosing_min'])  # среднее время выбора у студентов
avg_workers = np.mean(workers['time_spent_choosing_min'])  # среднее время выбора у работающих

print(f'5.Главная жалоба "{problem_counts.index[0]}": {main_problem_n} из {len(df_survey)} человек ({main_percent}%)')
print(f'Среднее время на выбор рецепта: студенты {avg_students} мин, работающие {avg_workers} мин')
print(f'Заказывают доставку при затруднении: {delivery_percent}%')