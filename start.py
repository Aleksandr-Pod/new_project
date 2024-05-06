# a = "my friend"
# b = a
# print(b)

# объекты не копируются, как и в JS копируется ссілка на память, где хранится объект
# a = ["say", "hello"]
# b = a
# a[1] = "stop"
# print("a: " , a)
# print("b: ", b)

# a = "Hello, "
# b = "Bro"
# print(a + b*2) # Только для текстовых элементов
# print("Hi," + "I am " + "happy "*20)

# print('''
# Hey!
# What?
# What are you doing?
# ''')

# сепаратор можно использовать для переноса строк
# print('туториал', 'по', 'функции', 'print()', sep='\n * ')

# по умолчанию end="\n" что переводит каждый раз на новую строку.
# str1 = 'туториал по'
# str2 = 'функции print()'
# print(str1, end=" ")
# print(str2)

# print и работа с файлами: 
# sourceFile = open('log.txt', 'a+')
# print("hello", file=sourceFile)


# Все типы анных порождены метаклассом type !!!
# print(type(3)) # <class 'int'>
# class NewClass:
#   pass
# print(type(NewClass)) # <class 'type'>
# print(type(int)) # <class 'type'>
# print(type([1, 2])) # <class 'list'>
# print(type((1, 2, 3))) # <class 'tuple'>


# print()
# print("12*34=")
# sys_p= "408"

# user_pass = input("введите ответ...:")

# if user_pass==sys_p:
#   print("Да, это правда")
# else:
#   print("нет, САМОУНИЧТОЖЕНИЕ через 3сек")


print(type("b"))