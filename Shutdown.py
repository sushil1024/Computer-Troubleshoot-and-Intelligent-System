#importing os to perform operating system related functions
import os

#take choice as input as to whether or not shut down the computer
shutdown = input("Are you sure you want to shut down? (yes/no): ")

if shutdown=='yes':

    #shut down the computer
    os.system("shutdown /s /t 1")
elif shutdown=='no':
    print("Cancelled!")
else:
    print("Enter valid choice!")