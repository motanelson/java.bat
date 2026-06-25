import os
import copy
compilers="javac --release 8 "
decompilers="javap -c -private "
print("\033c\033[47;31m\ngive me file to jbat: ? \n")
a=input().strip()
#a="Hello.java"
b=a.replace(".java","")
os.system(compilers + a)
os.system(decompilers + b+".class > "+b +".jbat")
