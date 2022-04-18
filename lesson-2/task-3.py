months = {
1: {"name": "Январь", "season": 1},
2: {"name": "Февраль", "season": 1},
3: {"name": "Март", "season": 2},
4: {"name": "Апрель", "season": 2},
5: {"name": "Май", "season": 2},
6: {"name": "Июнь", "season": 3},
7: {"name": "Июль", "season": 3},
8: {"name": "Август", "season": 3},
9: {"name": "Сентябрь", "season": 4},
10: {"name": "Октябрь", "season": 4},
11: {"name": "Ноябрь", "season": 4},
12: {"name": "Декабрь", "season": 1},
}
seasons = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
getMonth = int(input("Номер месяца"))
getObjectMonth = months.get(getMonth)
getSeason = getObjectMonth.get("season")
print(seasons.get(getSeason))