revenue = int(input("прибыль"))
costs = int(input("издержки"))
if revenue > costs:
    print("прибыль больше")
    rent = revenue / (revenue - costs)
    staff = int(input("введите кол-во сотрудников"))
    print(rent / staff)
else:
    print("издержки больше")