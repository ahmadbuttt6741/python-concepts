# # with open('practice.txt','w') as f:
# #   f.write('hallo this is our file input practice \n')
# #   f.write('using Java \ni like programming in Java.\n')

# with open('practice.txt','r') as f:
#   data = f.read()

# newdata = data.replace("Java", "Python")

# with open('practice.txt','w') as f:
#   f.write(newdata)

# with open('practice.txt','r') as f:
#   data = f.read()
#   if(data.find('practice') != -1 ):
#     print("Found")
#   else:
#     print("not Found")



# def check_for_line():
#   word = "practice"
#   data = True
#   line_no = 1
#   with open('practice.txt', 'r') as f:
#     while data:
#       data = f.readline()
#       if(word in data):
#         print(line_no)
#         return
#       line_no += 1
#   return -1

# check_for_line()
# array = [1,2,3,4,5,5,23,62,23]
# with open('practice.txt','w') as f :
#   f.write(str(array))
count = 0
with open('practice.txt','r') as f :
  data = (f.read())
  print((data))
  print(type(data))

  nums = data.split(',')
  print((nums))

  for val in nums:
    if (int(val) % 2 == 0): 
      count += 1
print(count)



