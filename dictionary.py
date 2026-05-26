dic = {
  "Name": "Ahmad",
  "Age" :21,
  "Course" : "CS"
  }
print(dic)
print(dic["Name"])
print(dic["Age"])
print(dic["Course"])
print(dic.get("Course2"))
print(dic.keys())
print(dic.values())

for i in dic:
  print(dic[i])

dic2 = {
    "Name1": "Ahmad",
  "Age1" :21,
  "Course1" : "CS",
  "dic3" :
  {
      "Name2": "Ahmad",
  "Age2" :21,
  "Course2" : "CS"  ,
  "Name3": "Ahmad",
  "Age3" :21,
  "Course3" : "CS"
  }
}
# print(dic2)
print(dic2.items())
