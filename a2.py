num = {1,2,3,4}
item = {"Eggs", "Coffee" , "Chocolate", "Bread"}
zipper = list(zip(num ,item))
print(zipper)

num2 = [5,4,3,2,1]
num3 = [50,40,30,20,10]
ans = list(zip(num2 , num3[::-1] ))
for x , y in ans:
    print(x,y)

for i in range(10):
    if i == 6:
    #  print(exit)
     break
    #  exit()
    print(i)

print("Hello")
