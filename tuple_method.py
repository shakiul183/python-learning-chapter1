a = (1,48,56869,5258,45,45555,False,"Rohan",45,"Shivam")
b = (1,565,545465,454654,54,54454,"shakiul","karim")

print(a)
print(type(a))
no = a.count(45)
print(no)
i = a.index(45555)
print(i)

concatenated = a+b
print(a+b)

print("shakiul" in a)
print("shakiul" in b)

print(a*3)