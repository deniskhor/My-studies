# Задание: Напиши систему учета инвестиционного портфеля.
# Создай класс IndexFund.Добавь переменную уровня класса total_funds_in_portfolio = 0.  
# В методе __init__ принимай ticker (например, 'SBMX' или 'SBGB') и allocation (доля в портфеле, например 80).  
# Внутри конструктора делай так, чтобы при создании каждого нового фонда переменная total_funds_in_portfolio увеличивалась на 1. 
# Создай два объекта фонда. 
# Выведи их тикеры и проверь, чему равна общая переменная IndexFund.total_funds_in_portfolio.  

# РЕШЕНИЕ

# class IndexFund:
    
#     total_funds_in_portfolio = 0
    
#     def __init__(self, ticker, allocation):
#         self.ticker = ticker
#         self.allocation = allocation
    
#         IndexFund.total_funds_in_portfolio += 1
    
# numb1 = IndexFund('SBMX', 80)
# numb2 = IndexFund('SBGB', 20)

# print(numb1.ticker)
# print(numb1.allocation)
# print(IndexFund.total_funds_in_portfolio)





# Твоя задача — описать систему продуктов для плана питания:
# Создай базовый класс FoodItem с параметрами name и is_allowed (True/False — например, для исключения хлеба или сладкого) в __init__.
# Напиши в нем метод info(), который выводит базовую строку: разрешен этот продукт или нет (используй тернарный оператор if-else в f-строке, как мы разбирали!).
# Создай класс-наследник Meat, который наследует FoodItem и добавляет уникальный параметр protein_grams (количество белка).
# В __init__ класса Meat обязательно используй super().__init__ для передачи name и is_allowed родителю.
# Переопредели метод info() в Meat: сначала напечатай строку с количеством белка, а на следующей строчке вызови super().info(), чтобы допечатать базовый статус.
# Создай объект куриных бедер (название 'Chicken Thighs', разрешено True, белок 19) и вызови его метод info().

# РЕШЕНИЕ

# class FoodTeam:
#     def __init__(self, name,  is_allowed):
#         self.name = name 
#         self.is_allowed = is_allowed
        
#     def info(self):
#         print(f'{self.name} | {"разрешен" if self.is_allowed else "не разрешен"}')
#         # print(f'It is {self.color} and {"filled" if self.filled else "not filled"}')
        
# class Meat(FoodTeam):
#     def __init__(self, name, is_allowed, protein_grams):
#         super().__init__(name, is_allowed)
#         self.protein_grams = protein_grams
        
#     def info(self):
#         print(f'{self.protein_grams} граммов')
#         super().info()

# object1 = Meat(name = 'Chicken Thighs', is_allowed = True, protein_grams = 19)

# object1.info()





# # Импортируй класс ABC и декоратор abstractmethod из модуля abc.
# # Создай абстрактный класс MLModel с двумя абстрактными методами: train() и predict(). Внутри этих методов просто напиши pass.
# # Попробуй создать объект model = MLModel() и запусти код. Убедись, что Python выдаст ошибку TypeError (после проверки можешь закомментировать эту строчку, чтобы она не ломала программу).
# # Создай класс-наследник LinearRegression, который наследует MLModel.
# # Напиши в нем реализацию обязательных методов:
# # В train() пусть выводится сообщение (например: Обучение линейной регрессии на данных о недвижимости...).
# # В predict() пусть выводится сообщение (например: Возврат массива предсказанных цен...).
# # Создай объект линейной регрессии и по очереди вызови эти два метода.


# from abc import ABC, abstractmethod

# class MLModel(ABC):
    
#     @abstractmethod
#     def train(self):
#         pass
    
#     @abstractmethod
#     def predict(self):
#         pass
    
    
# # model = MLModel()

# class LinearRegression(MLModel):
    
#     def train(self):
#         print('Обучение линейной регрессии на данных о недвижимости...')
        
#     def predict(self):
#         print('Возврат массива предсказанных цен...')
        
# object_LinearRegression = LinearRegression()

# object_LinearRegression.train()
# object_LinearRegression.predict()



# Система автоматической реструктуризации инвестиционного портфеля
# Контекст:
# Нам нужно разработать ядро для приложения брокера, которое помогает пользователям автоматически ребалансировать портфель.
# Бизнес-требования:
# Система работает с финансовыми активами. Любой актив в системе обязан иметь базовый функционал: возможность покупки и продажи. Программа не должна позволять создавать активы без этих функций.
# У пользователя есть текущие позиции (например, фонды TMOS и BSPB), у которых зафиксирована цена покупки и текущая рыночная цена.
# Реализовать функцию продажи: актив можно продать только в том случае, если текущая рыночная цена равна или превышает цену покупки (выход в ноль или плюс). При успешной продаже средства зачисляются на свободный баланс.
# Реализовать функцию распределения баланса: свободные средства должны распределяться между новыми целевыми активами (например, SBMX и SBGB) в строгой пропорции 80 на 20.
# Написать скрипт, который прогоняет этот сценарий: проверяет два текущих актива, продает подходящие и покупает новые по заданному сплиту.

from abc import ABC, abstractmethod

class Basic_functionality(ABC):
    
    def __init__(self, purchase, market_price):
        self.purchase = purchase
        self.market_price = market_price
    
    @abstractmethod
    def buy(self):
        pass
    
    @abstractmethod
    def sale(self):
        pass
    
    
class Investment_portfolio(Basic_functionality):
    
    balance = 0
    
    def __init__(self, name, purchase, market_price):
        self.name = name
        super().__init__(purchase, market_price)
        
    def buy():
        pass    
    
    def sale(self):
        if self.market_price >= self.purchase:
            Investment_portfolio.balance += self.market_price
        else:
            print('Продажа не будем нам в плюс. Отказано.')
            
    def distributions(self):
        pass