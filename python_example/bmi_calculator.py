weight = float(input("체중을 입력하세요(kg): "))
height = float(input("키를 입력하세요 (cm): "))
BMI = weight / ((height/100) ** 2)
print("체중(kg): ", round(weight,0))
print("키(cm): ", round(height,0))
print("BMI: ", round(BMI, 1))