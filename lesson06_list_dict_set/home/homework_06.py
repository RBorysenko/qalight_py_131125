# task 1. Знайдіть всі унікальні елементи в списку small_list
print("\ntask 1")
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements = list(set(small_list))
print("\nВсі унікальні елементи в списку small_list -", unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("\ntask 2")
average = sum(small_list) / len(small_list)
print("\nСереднє арифметичне всіх елементів у списку small_list -", average)

# task 3. Перевірте, чи є в списку big_list дублікати
print("\ntask 3")
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
duplicates = len(big_list) != len(set(big_list))
print("\nВ списку big_list дублікати -", duplicates)

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("\ntask 4")
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key = max(add_dict, key=add_dict.get)
print("\nКлюч з максимальним значенням у словнику add_dict -", max_key)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
print("\ntask 5")
reversed_dict = {value: key for key, value in base_dict.items()}
print("\nНовий словник, в якому ключі та значення base_dict будуть замінені місцями -", reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("\ntask 6")
sum_dict = {}
for key, value in base_dict.items():
    sum_dict[key] = value
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print("\nДва словника base_dict та add_dict в новий словник sum_dict -", sum_dict)

# task 7.
print("\ntask 7")
line = "Створіть множину всіх символів, які входять у заданий рядок"
char_set = set(line)
print("\nМножина всіх символів, які входять у заданий рядок -", char_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("\ntask 8")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_elements = set_1 ^ set_2
total_sum = sum(unique_elements)
print("Сума елементів двох множин, які не є спільними -", total_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("\ntask 9")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
unique_elements = set1 ^ set2
print("\nДва списки та обробіть їх так, щоб отримати сет, який містить всі елементи\
з обох списків,  які зустрічаються тільки один раз. -", unique_elements)

#----------------------------------------------------------------------------------------
print("\ntask 10")
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_dict = {}
for name, age in person_list:
    lower = (age // 10) * 10
    upper = lower + 9
    age_range = f"{lower}-{upper}"
    # Додаємо ім'я до відповідного діапазону
    if age_range not in age_dict:
        age_dict[age_range] = []
    age_dict[age_range].append(name)
print("Обробіть список кортежів person_list, що містять ім'я та вік людей,\
так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),\
а значення - списки імен людей, які потрапляють в кожен діапазон -", age_dict)

