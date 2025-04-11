idnum = "901212-1234567"

birth = idnum[:6]
number = idnum[7]

if number in ['1', '2']:
    year = "19" + birth[:2]
elif number in ['3', '4']:
    year = "20" + birth[:2]
else:
    print("잘못된 형식입니다.")

month = birth[2:4]
day = birth[4:6]

print(f"{year}년 {month}월 {day}일")
