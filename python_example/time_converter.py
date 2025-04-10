time = int(input("시간을 입력하세요 (초): "))
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print("{}초는 {}시간 {}분 {}초입니다.".format(time, hour, minute, second))
