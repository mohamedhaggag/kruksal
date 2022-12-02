def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4

myGen = myGenerator()

print(next(myGen), end=" ")
print("Hello From Python")
print(next(myGen), end=" ")

for number in myGen:
  print(number)