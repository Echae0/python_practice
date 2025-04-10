weight = float(input("체중을 입력하세요(kg): "))
height = float(input("키를 입력하세요 (cm): "))
BMI = weight / (height ** 2)
print("체중(kg): ", weight, \n
      "키(cm): ", height, \n
      "BMI: ", BMI)