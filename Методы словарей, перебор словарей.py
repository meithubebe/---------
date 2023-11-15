# my_dict1 = {}
# my_dict2 = dict()

# print(type(my_dict1))
# print(type(my_dict2))

my_dict = {
    "user": "Thomas Shelby",
    "nickname": "Neo",
    "team": ["Morpasf", "TRint"],
    # [1, 2, 3]: "HEllo"
    1: "Martrix",
    "has": "you",
    (1, 2 ,3): "hello"

}
# print(my_dict)
# print(my_dict["user"])
# print(my_dict[1])
# print(my_dict[(1, 2 , 3)])

months = {1: "April", 2: "February"}
# print(months[2])

person = {"имя": "Виктор", "возраст": 28, "рост": 180}
# print(person["рост"])

# print(person)
person["down"] = 92
person["up"] = 24
# print(person)

person["down"] = 195
# print(person)

# del person["up"] 
# print(person)

person["car"] = "Mercedes"

# for k, v in person.items():
#     print(f"{k}>>>{v}")

# for key in person:
#     print(key)

# print("-" * 20)

# for key in person.keys():
#     print(key)

# if "crabs" in person:
#     print("Yes its rotate")
# else:
#     print("NEtu sorry")

# for value in person.values():
#     print(value)


# print(person)

person = {
    'имя': 'Виктор',
    'возраст': 28,
    'рост': 180,
    'down': 195,
    'up': 24,
    'car': 'Mercedes',
    'airsoft':  'T90', 
    'Wife': 'Unkown',
    'Daddy': ['two stepdaddyes', 'three downbreakers', 'five mothers'],
    
}

# for values in person['Daddy']: 
#     print(values)

persons = {
    "Alex": {
      "Level": 20,
      "Hight": 184,
      "Rost": 197,
      "car": 'Toyota camry', 

    },  
    "Olga": { 
      "Level": 29,
      "Hight": 46,
      "Rost": 165,
      "car": 'Toyota Mark II',
    },
}

# for username, userinfo in persons.items():
#     print(f"Имя пользователя: {username}")
#     age = userinfo["Level"]
#     car = userinfo["car"]

#     print(f"Возраст пользователя {username} : {age} лет.")
#     print(f"Авто пользователя {username} : {car}\n")


print(person)
# print(person.get("им", "wtf man?"))

# print(person.setdefault(5))
# print(person)

# person_copy = person.copy()
# print(person_copy)

# person.update({"Проффесия": "Программист"})
# print(person)


