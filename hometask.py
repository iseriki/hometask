names = ['Ann', 'Bob', 'Suzan', 'Radonir', 'Fill', 'Sam', 'Al']
ages = [12, 33, 56, 87, 4, 18, 21]
text_a = "Special cases aren't special enough to break the rules."
text_b = "In the face of ambiguity, refuse the temptation to guess."

#  Задание:
#  1. Посчитать количество элементов в списке names
len(names)
#  2. Посчитать количество элементов в списке ages
len(ages)
#  3. Посчитать количество элементов в строке text_a
len(text_a)
#  4. Посчитать количество элементов в строке text_b
len(text_b)
#  5. Посчитать сумму элементов списка ages
sum(ages)
#  6. Вывести максимальный элемент списка ages
max(ages)
#  7. Вывести минимальный элемент списка ages
min(ages)
#  8. Найти самое короткое слово d text_a
print min(text_a.split(),key=len)
#  9. Найти самое длинное слово в text_b
#  10. Вывести слово special из text_a
#  11. Вывести слово refuse из text_b
#  12. В names и ages имена соответствуют возрасту,
#      используя print вывести имя и возраст, например
#      Sergey is 19 yesrs old
#      то есть Sergey и 19 взяты из списков
