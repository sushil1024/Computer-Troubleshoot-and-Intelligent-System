#importing os which is used for interaction with the operating system
import os

#choice to whether or not restart the computer
restart = input("Are you sure ? (yes / no): ")

if restart == 'yes':

    #restart the computer
    os.system("shutdown /r /t 1")
elif restart == 'no':
    print("Cancelled")

else:
    print("Enter valid choice!")
