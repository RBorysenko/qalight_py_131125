# -*- coding: utf-8 -*-
# Самостійне вивчення - Поглиблені задачі
# Виконайте завдання та збережіть результати у вказаних змінних

print("=== ПОГЛИБЛЕНІ ЗАДАЧІ ===")

# Task 1. Створіть список з парних чисел від 2 до 20
even_numbers = list(range(2, 21, 2))  # Ваш код тут
print(even_numbers)
# Task 2. Відфільтруйте з списку тільки числа більше 10
numbers_list = [5, 12, 8, 15, 3, 18, 7, 20]
filtered_numbers = [num for num in numbers_list if num > 10] # Ваш код тут

# Task 3. Створіть список квадратів непарних чисел від 1 до 9
odd_squares = [x**2 for x in range(10) if x % 2 ==1]
print(odd_squares)  # Ваш код тут: [1, 9, 25, 49, 81]

# Task 4. Об'єднайте два списки без дублікатів
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_unique = list(set(list1 + list2))  # Ваш код тут
print(merged_unique)

# Task 5. Створіть кортеж з координатами точок
points = ((0, 0), (1, 1), (2, 2))  # Ваш код тут: ((0,0), (1,1), (2,2))
print(points)

# Task 6. Розпакуйте кортеж координат
coordinates = (10, 20, 30)
x, y, z = coordinates # Ваш код тут
print("Координати", x,y,z)

# Task 7. Створіть множину голосних літер
vowels = {'a', 'e', 'i', 'o', 'u'}  # Ваш код тут: {'a', 'e', 'i', 'o', 'u'}

# Task 8. Знайдіть унікальні символи у рядку
text = "programming"
unique_chars = set(text)  # Ваш код тут
print(unique_chars)

# Task 9. Створіть множину чисел, які діляться на 3 від 1 до 15
divisible_by_3 = {n for n in range(1, 16) if n % 3 == 0}  # Ваш код тут
print(divisible_by_3)

# Task 10. Знайдіть симетричну різницю двох множин
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1 ^ set2  # Ваш код тут
print(symmetric_diff)

# Task 11. Створіть словник з кількістю символів у кожному слові
words = ["cat", "dog", "elephant", "bee"]
word_lengths = {word: len(word) for word in words}  # Ваш код тут: {"cat": 3, "dog": 3, ...}
print(word_lengths)

# Task 12. Створіть словник з квадратами та кубами чисел
numbers = [2, 3, 4, 5]
powers_dict = {n: {"square": n**2, "cube": n**3} for n in numbers} # Ваш код тут: {2: {"square": 4, "cube": 8}, ...}
print(powers_dict)

# Task 13. Згрупуйте слова за їх довжиною
word_list = ["apple", "cat", "dog", "banana", "car", "elephant"]
grouped_by_length = {}  # Ваш код тут
for word in word_list:
    length = len(word)
    if length not in grouped_by_length:
        grouped_by_length[length] = []
    grouped_by_length[length].append(word)

print(grouped_by_length)

# Task 14. Створіть словник частоти символів у рядку
sentence = "hello world"
char_frequency = {}  # Ваш код тут
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)

# Task 15. Об'єднайте декілька словників
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
combined_dict = {}  # Ваш код тут
for d in (dict1, dict2, dict3):
    combined_dict.update(d)
print(combined_dict)

# Task 16. Інвертуйте словник (ключі стають значеннями)
original = {"name": "John", "age": 25, "city": "Kyiv"}
inverted = {value: key for key, value in original.items()}  # Ваш код тут
print(inverted)

# Task 17. Створіть список кортежів з словника
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
score_tuples = [tuple(item) for item in scores.items()]  # Ваш код тут: [("Alice", 95), ...]
print(score_tuples)

# Task 18. Знайдіть спільні ключі у двох словниках
dict_a = {"x": 1, "y": 2, "z": 3}
dict_b = {"y": 5, "z": 6, "w": 7}
common_keys = set(dict_a.keys()) & set(dict_b.keys())  # Ваш код тут
print(common_keys)

# Task 19. Створіть вкладений словник з інформацією про студентів
# Ваш код тут: {"student1": {"name": ..., "grades": [...]}, ...}
students_info = {"student1": {"name": "Alice","grades": [95, 88, 92]},
                 "student2": {"name": "Bob","grades": [78, 85, 80]},
                 "student3": {"name": "Charlie","grades": [90, 91, 89]}}
print(students_info)

# Task 20. Сплюсніть всі списки у словнику
data = {"list1": [1, 2], "list2": [3, 4], "list3": [5, 6]}
# Ваш код тут: [1, 2, 3, 4, 5, 6]
flattened = [item for sublist in data.values() for item in sublist]
print(flattened)

if __name__ == "__main__":
    print("\n=== ЗАВЕРШЕННЯ ===")
    print("Поглиблені завдання виконано! Запустіть test_selflearning.py для перевірки.")