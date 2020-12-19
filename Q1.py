import csv as CSV
import numpy as np

# ------------------------------------------------------------------

# Класс программы по сортировке работы
class Job_Search:

    # ---------------------------------------------------

    # Чтение вакансий из CSV
    def FileRead(self, File_Name):
        Tab = []
        with open(File_Name, newline='') as File:
            Read = CSV.reader(File)
            for Line in Read: Tab.append(Line[0].split(';'))
        return Tab

    # ---------------------------------------------------

    # Вывод списка 
    def ListWork(self): return self.Work_List

    # ---------------------------------------------------

    # Замена пузырьком
    def Replacement(self, Arr, X, Y):
        self.Bubble = Arr[X]
        Arr[X] = Arr[Y]
        Arr[Y] = self.Bubble
        return Arr

    # ---------------------------------------------------

    # Сортировка по фирме
    def SortWork(self, Disc = "Компания"): # Должность;

        # Получили данные
        Tab = self.Work_List

        # Ищем конкретный столбец
        N, L, Lm = 0, len(Tab[0]), len(Tab)
        for Pos in range(L): 
            if(Tab[0][Pos] ==  Disc): N = Pos
       
        # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(2, len(Tab)):
            Item_to_Insert = Tab[i]
            j = i - 1                                       # Сохраняем ссылку на индекс предыдущего элемента
            while j >= 0 and Tab[j] > Item_to_Insert:       # Элементы отсортированного сегмента перемещаем вперёд,
                Tab[j + 1] = Tab[j]                         # если они больше элемента для вставки
                j -= 1
    
            Tab[j + 1] = Item_to_Insert                     # Вставляем элемент
    
        # Возвращаем отсортированную таблицу
        return Tab
    # ---------------------------------------------------

    # Сортировка по возрастанию зарплаты
    def SortAscendingSalary(self):

        # Получили данные
        Tab = self.Work_List

        # Ищем столбец с зарплатой 
        N, L, Lm = 0, len(Tab[0]), len(Tab)
        for Pos in range(L): 
            if(Tab[0][Pos] == "Средняя зарплата" ): N = Pos
           
        # Сортировка
        for x in range(1,Lm):
            for y in range(1,Lm):
                if(y > x):
                    if(Tab[x][N] > Tab[y][N]):
                        Tab = self.Replacement(Tab,x,y)

        # Возвращаем отсортированную таблицу
        return Tab
    
    # Сортировка по возрастанию зарплаты
    def SortExperience(self):

        # Получили данные
        Tab = self.Work_List

        # Ищем столбец с зарплатой 
        N, L, Lm = 0, len(Tab[0]), len(Tab)
        for Pos in range(L): 
            if(Tab[0][Pos] == "Стаж" ): N = Pos
           
        # Сортировка
        for x in range(1,Lm):
            for y in range(1,Lm):
                if(y > x):
                    if(Tab[x][N] > Tab[y][N]):
                        Tab = self.Replacement(Tab,x,y)

        # Возвращаем отсортированную таблицу
        return Tab
    
    # ---------------------------------------------------

    # Конструктор
    def __init__(self,File_Name = "Work.csv"):

        # Прочли файл
        self.Work_List = self.FileRead(File_Name)
        
        # Получили заголовки
        self.Categor = self.Work_List

# ------------------------------------------------------------------


# Обратились к файлу
Work = Job_Search("Work.csv")

# РАССКОМЕНТИРУЙ СТРОКУ ДЛЯ ВЫВОДА ДАННЫХ В КОНСОЛЬ
# ЛУЧШЕ СМОТРЕТЬ ПО ОЧЕРЕДНО, ИНАЧЕ КАША

# Вывести все из файла на экран
#for Line in Work.ListWork(): print(Line)

# Сортировка по возрастанию зарплаты
#for Line in Work.SortAscendingSalary(): print(Line)

# Сортировка по возрастанию стажа
#for Line in Work.SortExperience(): print(Line)

# Сортировка вставками
#for Line in Work.SortWork("Компания"): print(Line)


# ------------------------------------------------------------------