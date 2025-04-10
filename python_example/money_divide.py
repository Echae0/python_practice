money = int(input("얼마를 가지고 있습니까?: "))
people = int(input("몇 명이서 나눠 가지겠습니까?: "))
money_div = money // people
change = money % people
print("각자 {}원을 받고 {}원이 남습니다.".format(money_div, change))