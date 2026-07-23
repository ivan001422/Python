import numpy as np
import matplotlib.pyplot as plt

'-----------------Создание места хранения для графиков---------------'
container = plt.figure() # Создание 'контейнера' для хранения графиков

# строки столбцы позиция
chart_1 = container.add_subplot(1, 2, 1) # Создание пустого графика с осями
chart_2 = container.add_subplot(1, 2, 2) # 1 - высота графика относительно всего контейнера
                                           # 2 - ширина графика относительно всего контейнера
                                           # 1 = местоположение графика в контейнере (отсчет с 1)

plt.subplots_adjust(left=0.02, bottom=0.05, top=0.95, right=0.98, wspace=0.1, hspace=0.1) # Отступы от краев экрана для container

'-------------------------Подпись информации--------------------------'
plt.suptitle('suptitle')

chart_1.set_title('set_title')
chart_2.set_title('set_title')

chart_1.set_xlabel('set_xlabel')
chart_1.set_ylabel('set_ylabel')

chart_2.set_xlabel('set_xlabel')
chart_2.set_ylabel('set_ylabel')

'-----------------------Настройка меток графиков-------------------------'
# major - основные метки
x_0, x_1, c = 0, 10, 1
chart_1.set_xticks(np.arange(x_0, x_1, c)) # (x_0, x_1, c): начало метки, конец метки, шаг
chart_1.set_yticks(np.arange(x_0, x_1, c)) # (x_0, x_1, c): начало метки, конец метки, шаг

chart_2.set_xticks(np.arange(x_0, x_1, c)) # (x_0, x_1, c): начало метки, конец метки, шаг
chart_2.set_yticks(np.arange(x_0, x_1, c)) # (x_0, x_1, c): начало метки, конец метки, шаг

# minor - вспомогательные метки
x_0, x_1, c = 0.5, 10, 1
chart_1.set_xticks(np.arange(x_0, x_1, c), minor=True) # (x_0, x_1, c): начало метки, конец метки, шаг
chart_1.set_yticks(np.arange(x_0, x_1, c), minor=True) # (x_0, x_1, c): начало метки, конец метки, шаг

'----------------------Внешний вид меток графиков----------------------'
chart_1.tick_params(axis='both', which='major',
                    length=6,
                    width=1,
                    color='black',
                    labelsize=10,
                    labelcolor='black',
                    direction='inout')

chart_2.tick_params(axis='both', which='major',
                    length=6,
                    width=1,
                    color='black',
                    labelsize=10,
                    labelcolor='black',
                    direction='out')

chart_1.tick_params(axis='both', which='minor',
                    length=4,
                    width=0.8,
                    color='gray',
                    labelsize=8,
                    labelcolor='gray',
                    direction='inout')

'---------------------Создание и настройка сетки----------------'
chart_1.grid(True, which='major',
             axis='both',
             color='black',
             linestyle='--',
             linewidth=0.2,
             alpha=0.7)

chart_1.grid(True, which='minor',
             axis='both',
             color='grey',
             linestyle='--',
             linewidth=0.2,
             alpha=0.5)

chart_2.grid(True, which='major',
             axis='both',
             color='black',
             linestyle='--',
             linewidth=0.2,
             alpha=0.8)

'---------------------------Создание разных видов графиков-----------------'
x = np.arange(10)
y = np.arange(10)

chart_1.plot(x, y,
             linewidth=1,
             color='red',
             linestyle='-',
             alpha=1,
             label='label_1')

x = np.arange(10)
y = np.arange(10) + 1

chart_1.plot(x, y,
             linewidth=1,
             color='blue',
             linestyle='-',
             alpha=1,
             label='label_2')

matrix = 2 * np.random.rand(10, 10) - 1
heatmap = chart_2.imshow(matrix, # Создаем тепловую карту на chart_2, записываем ссылку на нее в heatmap
    cmap='viridis', # Цветовая карта: 'viridis', 'plasma', 'hot', 'cool', 'RdYlBu'
    interpolation='nearest', # Интерполяция: 'nearest', 'bilinear', 'bicubic'
    aspect='auto', # Соотношение сторон: 'auto', 'equal'
    vmin=-1, # Минимальное значение для цветовой шкалы
    vmax=1, # Максимальное значение для цветовой шкалы
    alpha=0.8                # Прозрачность
)

# тип шкалы | для какого графика | с какой стороны расположить
cbar = plt.colorbar(heatmap, ax=chart_2, location='left') # для тепловой карты делаем шкалу значений
cbar.set_label('Значения') # подписываем шкалу

chart_1.legend()
plt.show()
