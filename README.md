# DLS_project (продвинутый поток)
Выпускной проект по курсу DLS MIPT


В моей задаче необходимо при помощи нейронной сети научиться осуществлять активную фазировку многоканальной системы. 
На данный момент у меня есть некоторые наработки по сбору данных для обучения и концепция разработки сети. 

1. Это новая технология в физической системе, но есть прикладные к ней, 
на основе которых строится датасет.

2. Данные - будут использоваться численные алгоритмы для наработки данных. Данные представляют собой матрицу интенсивностей поля с неким разбиением. 

3. Концептуально хочется разработать 2 сетки. Сверточную и полносвязную, провести эксперименты над гиперпараметрами,
выбрать лучшую, обосновать результаты. Сеть должна быть простой и легкой, потому что в реальном эксперименте важна быстрота фазировки. Именно для этой задачи сверточная, кажется, подойдет больше всего, ее можно будет "наворачивать" и расширять функционал, 
но опять же выбор архитектуры будет в пользу быстродействия работы системы. 

4. Целевой метрикой будет являться физическая величина, показывающая сфазированность системы после применения сетки к матрице интенсивностей. 
Так же для более полного понимания решаемой задачи предоставляю блок схему проекта


![image](https://github.com/sammorozov/DLS_project/assets/109150200/cdd4d4be-4e02-40ad-b267-1bd459bd4fd9)

План реализации: 

1. Моделирование многоканального лазерного излучения в ближней и дальней зонах
2. Создание обучающей выборки для нейронной сети 
3. Разработка полносвязной нейронной сети 
4. Анализ результатов 
5. Разработка сверточной нейронной сети 
6. Эксперименты с гиперпараметрами лучшей модели

# Моделирование многоканального лазерного излучения в ближней зоне.

![image](https://github.com/sammorozov/DLS_project/assets/109150200/a858d1f5-a3f7-4e34-95ba-5a98210f8b53)

![image](https://github.com/sammorozov/DLS_project/assets/109150200/aaf934dc-76e8-469a-8900-507d9136d9ba)


# Моделирование многоканального лазерного излучения в дальней зоне.

![image](https://github.com/sammorozov/DLS_project/assets/109150200/58dd8903-b8f4-437e-b0bb-d2b064a0f53e)


![image](https://github.com/sammorozov/DLS_project/assets/109150200/133932c6-d9e6-4de5-b1c8-30759b4546a4)


# Создание обучающей выборки 

Принцип формирования одной пары данных:

Имеется отрезок  [0, 2π] для возможных значений одной из четырех фаз лазерного канала.
Выбирая разбиение 2π/16 для каждой фазы численно получен полный перебор фаз, зная которые получены распределения интенсивностей.

![image](https://github.com/sammorozov/DLS_project/assets/109150200/d58d774a-bed3-4160-89c6-f356a56540fe)

![image](https://github.com/sammorozov/DLS_project/assets/109150200/df7b43e9-1a54-447d-ac7f-76b2684464cc)


# Разработка полносвязной нейронной сети

Архитектура:

![image](https://github.com/sammorozov/DLS_project/assets/109150200/9f6c93bf-ca13-447c-be1f-8b2b5c1d4dca)

Алгоритм обучения:

![image](https://github.com/sammorozov/DLS_project/assets/109150200/4d624bac-c07f-4adb-9921-070af91f4e41)

Лосс:

![image](https://github.com/sammorozov/DLS_project/assets/109150200/37f549aa-27fd-462a-bf6f-835ffcf7c213)


# Анализ результатов

Единичный случай
![image](https://github.com/sammorozov/DLS_project/assets/109150200/2a4a0edf-8d62-40fa-838e-b3d6f8df300f)

Слева матрица на случайно сгенерированных фазах

Справа матрица после применения "нейрофазировки"

![image](https://github.com/sammorozov/DLS_project/assets/109150200/d4b5fa4a-42b2-48eb-8795-cba086d3b13e)

Общий случай

![image](https://github.com/sammorozov/DLS_project/assets/109150200/bdc2a411-2d5b-44b1-b4ae-f9e60fa11026)

# Разработка полносвязной нейронной сети

Архитектура. За базовую модель была взята LeNet5, однако была изменена для решения задачи регрессии, 
а так же претерпели изменения размерности слоев, сдвиг и размер свертки, слои пулинга работали жадно для такой задачи,
в итоге после многочисленных экспериментов с гиперпараметрами была выбрана следующая архитектура, которая дала 
наиулучшие результаты.

![image](https://github.com/sammorozov/DLS_project/assets/109150200/864bddad-871f-492a-bd46-ad8d08e0334b)
![image](https://github.com/sammorozov/DLS_project/assets/109150200/c0246bb7-9f98-41ba-9d09-45c70ab9fb39)



# Анализ результатов сверточной нейронной сети.

![image](https://github.com/sammorozov/DLS_project/assets/109150200/9eada714-fa30-44bf-8b1f-4c367e346702)

Далее, посчитаем на сколько в среднем увеличивается число Штреля при такой конфигурации, которая на данный момент является лучшей по результатам графиков. В среднем после прохода любого набора данных через сверточную нейросеть число Штреля увеличивается на 0.42, через полносвязную на 0.37. Очевидно, что будет использоваться сверточная нейронная сеть для фазировки, поскольку она дает лучшее качество и количество сфазированных случаев. Из начального распределения среднее число Штреля составляет: 0.25, что означает при сложении будет в среднем получаться 0.69, что недотягивает до фазировки на несколько пунктов, но уже является хорошим результатом. 

# Выводы

Сверточная сеть показала лучший результат для максимального количества сфазированных случаев, однако, не исключен тот факт, что полносвязную сеть можно было улучшить таким образом, чтобы результат был похожим на итоговый результат для сверточной сети. В этом предположении и дальнейших рассуждениях я утверждаю, что сверточная сеть является более гибкой в настройке гиперпараметров, поэтому для больших разбиений дальней зоны именно сверточная сеть будет быстрее давать хорошие результаты, поскольку количество экспериментов на сверточных нейросетях не ограничивается только лишь перебором количеством нейронов в скрытых слоях, можно добавлять различные слои, и проводить еще больше различных экспериментов в различных конфигурациях. 

