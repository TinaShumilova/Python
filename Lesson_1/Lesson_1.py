# типы данных, переменные 
# int, float, boolean, str, list, None

# int
#a = 123
#print(a)
# float
#b = 1.23
#print(b)
# None
#value = None
#value = 1234
#print(value)
#str
#text = 'hello \'world\''
#print(text)

#print(a, b, text)                       
#print(a, '-', b, '-', text)                
#print('{1} - {2} - {0}'.format(a,b,text))   
# print(f'{a} - {b} - {text}')  

# boolean
#s = True
#print(s)
#list
#list_1 = []
#list_2 = [1, 2, 3]
#list_3 = ['1', '2', '3', 'hello']
#list_4 = ['1', '2', '3', 'hello', 1.5248, True]
#print(list_1)
#print(list_2)
#print(list_3)
#print(list_4)


# Ввод и выод данных
#print('введите a')
#a = int(input())
#print('введите b')
#b = int(input())
#print(type(a), b)
#print(a, '+', b, '=', a+b)

#Арифметические операции
#a = 1.3123548
#b = 3
#c = round(a * b, 6)
#print(c)

#Логические операции

#f = [1, 2, 3, 4]
#print(2 in f)

#is_odd = not f[0]%2
#print(is_odd)

# if-else
#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

# if-elif-else
#username = input('Введите имя: ')
#if username == 'Маша':
# print('Ура, это же МАША!')
#elif username == 'Марина':
# print('Я так ждала Вас, Марина!')
#elif username == 'Ильнар':
# print('Ильнар - топ)')
#else:
# print('Привет, ', username)

#while
#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#print(inverted)

#while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else: 
    print('Пожалуй')
    print('хватит )')
print(inverted)