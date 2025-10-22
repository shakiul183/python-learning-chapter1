marks = {
"shakiul karim": 100,
"majed khan": 90,
"zohurul pir":99,
0: "pervez",
1: "ibrahim"


}  # dictonary method 

print(type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shakiul karim":99,"Renuka": 100})
print(marks)
print(marks.get("shakiul karim"))
print(marks.get("ibrahim2"))  # print none but not error
# print(marks["majed khan2"]) # print error .. but both are not same