#importing sys to de-import modules to repeating calls
import sys

#infinite while loop until selected 'Exit'
while True:

    #menu
    print("\n\t-------M E N U-------\n")
    print("\t1. Show computer specifications")
    print("\t2. Open Control Panel")
    print("\t3. Open Device Manager")
    print("\t4. Shutdown the computer")
    print("\t5. Restart the computer")
    print("\t6. Show Temperature, Power & Fan Speed")
    print("\t7. Troubleshoot")
    print("\t8. Exit")
    print("\tEnter your choice: ")
    
    #taking choice as input (1-8)
    choice = int(input("\t"))
    if choice==1:
        print("The specifications of your system are:")

        #import python file in the same directory
        import Specifications

        #de-import python file so that it can be called back again on next iteration
        del sys.modules['Specifications']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==2:
        print("Opening Control Panel!!!")
        import ControlPanel
        del sys.modules['ControlPanel']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==3:
        print("Opening Device Manager")
        import DeviceManager
        del sys.modules['DeviceManager']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==4:
        import Shutdown
        del sys.modules['Shutdown']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==5:
        import Restart
        del sys.modules['Restart']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==6:
        print("Opening Software!!!")
        import TemperaturePowerFanspeed
        del sys.modules['TemperaturePowerFanspeed']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==7:
        import ComputerTroubleshooter
        del sys.modules['ComputerTroubleshooter']
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
    elif choice==8:

        #exits the infinite while loop
        exit()
    
    #if user enter values which are not in range (1-8), this will display and the loop will run again
    else:
        print("Enter a valid choice!")
        print("\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
