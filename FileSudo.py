import os
print(os.getcwd())
os.remove("hello")
fo=open("hello.txt","w+")
fo.write("Hello Python")
fo.close()

