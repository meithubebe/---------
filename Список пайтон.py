# my_list_1 = []
# print(type(my_list_1))

# my_list_2 = list()
# print(type(my_list_2))

# my_list = ["hello", 23, 2.6, ("2", "2")]
# print(my_list)

my_list_1 = [2, 5, 2, 1, 5, 124, 252, 250]
my_list_2 = ["Salam", "Kruto", "Kak dela?"]

# print(my_list_2[0])  


# print(len(my_list_2))

# print(my_list_2[:])

my_list_2.append("Pokakat")
# print(my_list_2) 

my_list_2.insert(1, "Sratjestko")
# print(my_list_2)

my_list_2.pop(-2)
# print(my_list_2)

list2 = ["Syest", "Kfafs", "sfasf"]
my_list_2.extend(list2)
# print(my_list_2)

a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
# print(c)

x = ["Hello"] + ["Maria"] + [2512]
# print(x)

# print(my_list_2)
my_list_2.remove("Syest")
# print(my_list_2)

my_list_2_copy = my_list_2.copy()
# print(my_list_2_copy)

# print(my_list_2.count("Syest"))


# print(my_list_2)
# print(my_list_2.index("Pokakat"))

# print(my_list_2)
# my_list_2.sort()
# print(my_list_2)

n_list = [5, 1, 2, 4, 3, 6, 7, 9, 10, 8]
n_list.sort()
# print(n_list)

n_list.reverse()
# print(n_list)

# print(n_list)
# print(min(n_list))
# print(max(n_list))

words_list = ["s", "toboy", "ploho"]

my_str = " ".join(words_list)
# print(my_str)


print(words_list)
words_list.clear()
print(words_list)