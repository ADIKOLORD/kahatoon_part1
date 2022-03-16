"""
# Problem 1
all_sum = 0
for i in range(1, 1000):
    if i % 3 or i % 5:
        all_sum += i
print(all_sum)  # > 466335


# Problem 2
a = 333
b = 555
a, b = b, a


# Problem 3
str_number = '4729461084'
str_sum = 0
for i in str_number:
    str_sum += int(i)
print(str_sum)  # > 45


# Problem 4
user_time = input('Введите дату в формате: "2020-10-24 18:30" >>> ').split()
only_data = user_time[0].split('-')
only_time = user_time[1].split(':')
date = {
    'year': only_data[0],
    'month': only_data[1],
    'day': only_data[2],
    'hour': only_time[0],
    'minute': only_time[1],
}
print(date)


# Problem 5
# Слово на анг. string, а string это все что внутри кавычки, '1' - так это тоже строка!
word = '1'
get_int_in_str = 0
for i in range(5):
    get_int_in_str += int(word)
get_int_in_str2 = int(word) * 7


# Problem 6
# mkdir -p nofile/newfile


# Problem 7
# с командой pwd



########################################
# Part 2

# Problem 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i > 5:
        print(i)



# Problem 2
digits = (113, 118, -5, 1, 135, 137, 0, 142, 144, 17, 154, 0, 155, 2, 159, 172)
for i in digits:
    print(i / 9)


# Problem 3
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
spisok2 = []
for i in spisok_2:
    if i not in spisok_1:
        spisok2.append(i)
print(spisok2)



########################################
# Part 3

# Problem 1
l_numbers = [i for i in range(301)]
for j in l_numbers:
    if j == 237:
        break
    elif j % 2 == 0:
        print(j)


# Problem 2

while True:
    user = input('Text a sentence >>> ').split()
    if len(user) < 6:
        continue
    else:
        break
if len(user) % 2 == 0:
    main_list = user[int(len(user) / 2):] + user[:int(len(user) / 2)]
else:
    main_list = user[int(len(user) / 2) + 1:] + user[:int(len(user) / 2) + 1]
print(main_list)


# Problem 3
numbers = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]
count_ch = 0
count_nech = 0

for i in numbers:
    if i % 2 == 0:
        count_ch += 1
    else:
        count_nech += 1
print(f'Чётные = {count_ch}\nНе чётные = {count_nech}')


# Problem 4
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
one_zero_list = []
for i in numbers:
    if i > 0:
        i = 1
        one_zero_list.append(i)
    elif i < 0:
        i = -1
        one_zero_list.append(i)
    else:
        one_zero_list.append(i)
print(one_zero_list)


# Problem 5
my_list = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11, 13, 17]
for i in range(0, len(my_list), 2):
    a = my_list[i]
    print(f'my_list[{my_list.index(a)}] --> {my_list[i]}')


# Problem 6
numbers = [1, 0, -2, 4, 3, 6, 6, 3, 5, 8, 4, 2]
count = 0
for i in range(len(numbers)):
    if count > 0:
        if numbers[i] > numbers[i - 1]:
            print(numbers[i])
    count += 1

"""



