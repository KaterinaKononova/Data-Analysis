import matplotlib.pyplot as plt
import csv
from functools import reduce

file = open("russian_demography.csv", 'r', encoding="utf-8")

reader = csv.reader(file)

year_Russia = []           #год
region = []                #наименование субъекта Российской Федерации
npg = []                   #естественный прирост населения на 1000 человек
birth_rate = []            #рождаемость на 1000 человек
death_rate = []            #смертность на 1000 человек
gdw = []                   #общий демографический вес (сколько людей нетрудоспособного возраста приходится
                           #                                             на 100 человек трудоспособного возраста)
urbanization = []          #процент городского населения

for line in reader:
   year_Russia.append(line[0])
   region.append(line[1])
   npg.append(line[2])
   birth_rate.append(line[3])
   death_rate.append(line[4])
   gdw.append(line[5])
   urbanization.append(line[6])


def death_birth_grapth():  #функция для графиков, которые отражают смертность и рождаемость по России с 1990-2017
   death = list(zip(year_Russia, death_rate))
   year = list(dict.fromkeys(year_Russia))
   year = year[1:]

   death = death[1:]
   birth = list(zip(year_Russia, birth_rate))
   birth = birth[1:]
   d = {x: 0 for x, _ in death}
   for name, num in death:
      if num != '':
         d[name] += float(num) / 85  # 85, так как 85 субъектов РФ

   birth_result = list(map(tuple, d.items()))

   t = {x: 0 for x, _ in death}
   for name, num in birth:
      if num != '':
         t[name] += float(num) / 85  # 85, так как 85 субъектов РФ

   death_result = list(map(tuple, t.items()))

   death = []
   birth = []
   for i in range(len(death_result)):
      if i != '':
         death.append(death_result[i][1])

   for j in range(len(birth_result)):
      if i != '':
         birth.append(birth_result[j][1])

   plt.style.use('ggplot')

   plt.subplot(2, 1, 1)
   plt.plot(year, death)
   plt.title("Birth rate in Russia", fontsize=10, fontweight="bold")

   plt.subplot(2, 1, 2)
   plt.plot(year, birth)
   plt.title("Death rate in Russia", fontsize=10, fontweight="bold")
   plt.show()


def gdw_diagram():    #функция для графика отношения нетрудоспособного населения к трудоспособному по стране
   gdw_data = list(zip(year_Russia, gdw))
   year = list(dict.fromkeys(year_Russia))
   year = year[1:]

   d = {x: 0 for x, _ in gdw_data}
   for name, num in gdw_data:
      if num != "gdw" and num != '':
         d[name] += float(num) / 85  # 85, так как 85 субъектов РФ

   gdw_level = list(map(tuple, d.items()))
   gdw_level = gdw_level[1:]
   level = []
   for i in range(len(gdw_level)):
      level.append(gdw_level[i][1])

   x = year
   y = level

   fig, ax = plt.subplots()

   ax.bar(x, y)

   fig.set_figwidth(22)  # ширина Figure
   fig.set_figheight(12)  # высота Figure

   plt.show()


def urbanization_NN_grapthic():   #функция графика, отражающего % городского населения в Нижегородской области
   urbaniz = list(zip(region, year_Russia, urbanization))
   year = list(dict.fromkeys(year_Russia))
   year = year[1:]
   urbaniz.sort(key=lambda x: (x[0], x[1]))
   NN_urb = urbaniz[1036:1064]
   urb_level = []
   for i in range(len(NN_urb)):
      urb_level.append(NN_urb[i][2])

   plt.style.use('ggplot')
   plt.xlabel("year")
   plt.ylabel("% urbanization")
   plt.plot(year, urb_level, color='indigo')
   plt.title("% of ubran population in Nizhny Novgorod oblast", fontsize=10, fontweight="bold")

   plt.show()


def urbanization_diagram():    #функция графика, отражающего % городского населения в среднем по стране
   urb_data = list(zip(year_Russia, urbanization))
   year = list(dict.fromkeys(year_Russia))
   year = year[1:]

   d = {x: 0 for x, _ in urb_data}
   for name, num in urb_data:
      if num != "urbanization" and num != '':
         d[name] += float(num) / 85  # 85, так как 85 субъектов РФ

   urb_level = list(map(tuple, d.items()))
   urb_level = urb_level[1:]
   level = []
   for i in range(len(urb_level)):
      level.append(urb_level[i][1])

   x = year
   y = level

   fig, ax = plt.subplots()

   ax.bar(x, y)

   fig.set_figwidth(22)  # ширина Figure
   fig.set_figheight(12)  # высота Figure

   plt.show()


def NN_graphic():  #функция которая стоит 2 графика (уровень рождаемости и уровень смертности по Нижегородсткой области с 1990 по 2017)
   example = list(zip(region, year_Russia, death_rate, birth_rate))
   year = list(dict.fromkeys(year_Russia))
   year = year[1:]
   example.sort(key=lambda x: (x[0], x[1]))
   NN = example[1036:1064]

   death_r = []
   birth_r = []
   for i in range(len(NN)):
      if i != "death_rate" and i != 'birth_rate' and i != '':
         death_r.append(float(NN[i][2]))
         birth_r.append(float(NN[i][3]))

   plt.style.use('ggplot')

   plt.subplot(2, 1, 1)
   plt.plot(year, death_r)
   plt.title("Death rate in Nizhny Novgorod oblast", fontsize=10, fontweight="bold")

   plt.subplot(2, 1, 2)
   plt.plot(year, birth_r)
   plt.title("Birth rate in Nizhny Novgorod oblast", fontsize=10, fontweight="bold")
   plt.show()


def find_average_death():    #функция подсчёта средней смертности за все годы в России по регионам
   death_table = list(zip(region, death_rate))
   d = {x: 0 for x, _ in death_table}
   for name, num in death_table:
      if num != "death_rate" and num != '':
         d[name] += float(num)

   Result = list(map(tuple, d.items()))
   number = []
   names = []
   for i in range(len(Result)):
      number.append(float(Result[i][1]))
      names.append(Result[i][0])

   average_num = list(map(lambda x: x / 28, number))  #реднённые значения
   average_death = list(zip(names, average_num))      #средние значения с названиями регионов
   return average_death


def find_average_birth():    #функция подсчёта средней рождаемости за все годы в России по регионам
   death_table = list(zip(region, birth_rate))
   d = {x: 0 for x, _ in death_table}
   for name, num in death_table:
      if num != "birth_rate" and num != '':
         d[name] += float(num)

   Result = list(map(tuple, d.items()))
   number = []
   names = []
   for i in range(len(Result)):
      number.append(float(Result[i][1]))
      names.append(Result[i][0])

   average_num = list(map(lambda x: x / 28, number))  #реднённые значения
   average_death = list(zip(names, average_num))      #средние значения с названиями регионов
   return average_death


def max_avr_birth():    #функция поиск региона с максимальной средней рождаемостью по стране
   avr_birth = find_average_birth()
   number = []
   for i in range(len(avr_birth)):
      number.append(float(avr_birth[i][1]))

   max_birth = reduce(lambda a, b: a if (a > b) else b, number)
   max_birth_region = "m"
   for j in range(len(avr_birth)):
      if avr_birth[j][1] == max_birth:
         max_birth_region = avr_birth[j][0]

   return max_birth_region


def min_avr_death():    #функция поиск региона с максимальной средней рождаемостью по стране
   avr_death = find_average_death()
   number = []
   for i in range(1, len(avr_death)):
      number.append(float(avr_death[i][1]))

   min_death = reduce(lambda a, b: a if (a < b) else b, number)
   min_death_region = ""
   for j in range(len(avr_death)):
      if avr_death[j][1] == min_death:
         min_death_region = avr_death[j][0]

   return min_death_region


def region_death_birth():      #функция для вычисления и сравнения средней смертности и рождаемости по регионам
   statistic = list(zip(region, npg))       #функция подсчитывает и выводит все области в которых смертность превышает (рождаемость)
   d = {x: 0 for x, _ in statistic}
   for name, num in statistic:
      if num != "npg" and num != '':
         d[name] += float(num) / 28

   Result = list(map(tuple, d.items()))

   number = []
   names = []
   for i in range(len(Result)):
      number.append(float(Result[i][1]))
      names.append(Result[i][0])

   avr_data = list(zip(names, number))
   return avr_data


my_file = open("Data_file.txt", "w")

avr_death = find_average_death()
avr_birth = find_average_birth()

my_file.write("Средняя смертность и рождаемость по регионам России \n")

my_file.write("Название региона" + "                        " + "Средняя смертность" + "                    " + "Средняя рождаемость" + "\n")

for i in range(1, len(avr_birth)):
   my_file.write(avr_birth[i][0]+"                        " + str(avr_death[i][1]) + "                      " + str(avr_birth[i][1]) + "\n")

my_file.write("\n")
my_file.write("\n")
my_file.write("\n")
region_death = min_avr_death()
region_birth = max_avr_birth()
my_file.write("Регион с самой низкой смертностью          " + region_death + "\n")
my_file.write("\n")
my_file.write("Регион с самой высокой рождаемостью          " + region_birth + "\n")

avr_data = region_death_birth()
death_list = []
birth_list = []
counter_birth = 0
counter_death = 0
for j in range(len(avr_data)):
   if avr_data[j][1] < 0:
      counter_death = counter_death + 1
      death_list.append(avr_data[j][0])
   if avr_data[j][1] > 0:
      counter_birth = counter_birth + 1
      birth_list.append(avr_data[j][0])


my_file.write("\n")
my_file.write("\n")
my_file.write("\n")
my_file.write("Регионы, где рождаемость превышает смертность       \n")
my_file.write("Таких регионов            " + str(counter_birth) + "\n")
for i in range(len(birth_list)):
   my_file.write(birth_list[i]+"   ||   ")

my_file.write("\n")
my_file.write("\n")
my_file.write("\n")
my_file.write("Регионы, где смертность превышает рождаемость          \n")
my_file.write("Таких регионов            " + str(counter_death) + "\n")
for i in range(len(death_list)):
   my_file.write(death_list[i]+"   ||   ")


death_birth_grapth()
urbanization_NN_grapthic()
gdw_diagram()
urbanization_diagram()
NN_graphic()

