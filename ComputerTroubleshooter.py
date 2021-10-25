#import sys to access varibales used or maintained by the interpreter
import sys

#function definition
def initial_prompt():
    print('Please answer all the following questions by typing \'yes\' or \'no\'.\n')

    #take string as input and store in response
    response = str(input('You are here because your computer is running too slow or is crashing too often, correct? '))
    if response == 'yes':
        question_programs()
    elif response == 'no':
        print('Well, then why did you come here?')
        question_again()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.\n')
        initial_prompt()

def question_programs():
    response = str(input('Are you running a lot of programs at once? '))
    if response == 'yes':
        close_program()
    elif response == 'no':
        question_defragment()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.\n')
        initial_prompt()

def close_program():
    response = str(input('Try closing the ones that you are not using. You can do this in Task Manager. Open Task Manager? '))
    if response == 'yes':
        import TaskManager
        del sys.modules['TaskManager']
    elif response == 'no':
        question_browser()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        close_program()

def question_defragment():
    response = str(input('Have you defragmented your computer? '))
    if response == 'yes':
        hardware_issue()
    elif response == 'no':
        how_about_now()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_defragment()

def how_about_now():
    response = str(input('Please run a full system defragment and restart your computer. Proceed with defragmentation? '))
    if response == 'yes':
        import Defragment
        del sys.modules['Defragment']
    elif response == 'no':
        hardware_issue()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        how_about_now()

def question_browser():
    response = str(input('Are you currently running a browser? '))
    if response == 'yes':
        question_howmanytabs()
    elif response == 'no':
        hardware_issue()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_browser()

def question_howmanytabs():
    response = str(input('Are you running a lot of tabs at once in your browser? '))
    if response == 'yes':
        close_tabs()
    elif response == 'no':
        question_defragment()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_howmanytabs()

def close_tabs():
    response = str(input('Try closing the tabs that you are not using, or closing the browser altogether. Did that help? '))
    if response == 'yes':
        exit()
    elif response == 'no':
        hardware_issue()
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        close_tabs()

def hardware_issue():
    response =str(input('This might be a hardware issue.  If your computer has a processor speed of less than 2.0 GHz and/or less than 2GB of RAM, or if it is just older than 5 years, you should consider an upgrade. In the meantime, you should check your CPU Temperature. \n Check Temperature and Fan Speed? '))
    if response == 'yes':
        import TemperaturePowerFanspeed
        del sys.modules['TemperaturePowerFanspeed']
    question_again()


def question_again():
    response = str(input('Would you run this again? to try again? '))
    if response == 'yes':
        initial_prompt()
    elif response == 'no':
        print('I hope this helped, but if it didn\'t, i would suggest you contact your computer company\'s customer service department and ask them to help you, or browse forums for a fix to your issue. You can exit now.')
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_again()

initial_prompt()
