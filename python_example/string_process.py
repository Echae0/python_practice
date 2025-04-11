# "Hello"와 "World"를 연결하여 "Hello World"를 출력하세요.
hello = "Hello"
world = "World"
print(hello + " " + world)
#  대문자로 변환하세요.
print((hello + " " + world).upper())
# "Hello World"에서 "World"만 슬라이싱하여 출력하세요.
sentence = "Hello World"
print(sentence[6:])
#  "Python is fun"에서 공백을 기준으로 문자열을 분리하세요.
sentence2 = "Python is fun"
print(sentence2.split())
#  "abcdef"에서 짝수 인덱스(0, 2, 4)의 문자들만 출력하세요.
text = "abcdef"
print(text[::2])
# "Hello"를 3번 반복하여 출력하세요.
print(hello * 3)