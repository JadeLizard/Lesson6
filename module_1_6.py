my_dict = {'каждый':'красный', 'охотник':'ораньжевый','таро':72} #словарь не может быть изменен, поэтому без списков
print(my_dict)
print(my_dict['каждый'])
print(my_dict.get('знать'))
my_dict.update({'Мару':'cat',
                'МАУС':'книга'})
a = my_dict.pop('охотник')
print(a)
print(my_dict)

my_set = {1, 2, 3, 4, 'привет', (122), 3, 2, 1}
print(my_set)
my_set.add(5)
my_set.add((7,8,'лимон'))
print(my_set)


