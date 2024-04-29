# найти количество отдельно мужчин отдельно женщин по каждому классу обслуживания
male= {'1': 0, '2': 0, '3': 0}
female= {'1': 0, '2': 0, '3': 0}

with open('data.csv.csv') as file:
    for line in file:
        data = line.split(',')
        if data[0] == 'PassengerId':
            continue
        pclass = data[2]
        sex = data[5]
        if sex == 'male':
            male[pclass] += 1
        if sex == 'female':
            female[pclass] += 1
    print(male, female)
