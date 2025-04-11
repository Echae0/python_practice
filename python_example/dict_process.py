# {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
john = {"name": "John", "age": 30} 
print("나이: ", john["age"])

# {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
subject = {"math": 90, "science": 85, "history": 78}
print("과목들: ", list(subject.keys()))

# 딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.
fruit = {'apple': 3, 'banana': 5}
fruit['apple'] += 2
print(fruit)