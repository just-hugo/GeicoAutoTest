from selenium import webdriver
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains as action
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from AutoGeicoTestClass import Auto_Geico_Test
import sys


#Precondition methods used to get initial conditions for a test case.
def preconditionA(anObject):
    #these are the steps from test case(s) A in order in order to do test case B01
    anObject.zip_input_0()
    anObject.customer_intent_1()
    anObject.next_button_0()
    return

    #these are the steps from test cases A and B in order to do test case C01
def preconditionB(anObject):
    preconditionA(anObject)
    anObject.first_name_input_0()
    anObject.last_name_input_0()
    anObject.next_button_1()
    return

    #these are the steps from test cases A, B, and C in order to do test case D01
def preconditionC(anObject):
    preconditionA(anObject)
    preconditionB(anObject)
    anObject.apt_input_0()
    anObject.zip_input_1()
    anObject.next_button_3()
    return

#GEICO HELP TEST CASES
#TC_A01
try:
    Test_A01 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A01.zip_input_0()
    Test_A01.customer_intent_0()
    Test_A01.next_button_0()
except Exception as err:
    print('Test A01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A01:")
    print(err.__module__)


#TC_A02
try:
    Test_A02 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A02.zip_input_0()
    Test_A02.customer_intent_1()
    Test_A02.next_button_0()
except Exception as err:
    print('Test A02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A02:")
    print(err.__module__)


#TC A03
try:
    Test_A03 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A03.zip_input_0()
    Test_A03.customer_intent_2()
    Test_A03.next_button_0()
except Exception as err:
    print('Test A03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A03:")
    print(err.__module__)

#TC_A04
try:
    Test_A04 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A04.zip_input_0()
    Test_A04.customer_intent_3()
    Test_A04.next_button_0()
except Exception as err:
    print('Test A04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A04:")
    print(err.__module__)


#TC_A05
try:
    Test_A05 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A05.zip_input_0()
    Test_A05.customer_intent_4()
    Test_A05.next_button_0()
except Exception as err:
    print('Test A05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A05:")
    print(err.__module__)


#TC A06
try:
    Test_A06 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A06.zip_input_0()
    Test_A06.customer_intent_5()
    Test_A06.next_button_0()
except Exception as err:
    print('Test A06' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A06:")
    print(err.__module__)

#
#TC_B01 - WHAT IS YOUR NAME
try:
    Test_B01 = Auto_Geico_Test() #creating Test case object
    preconditionA(Test_B01) #does initial setup for test B01

    Test_B01.first_name_input_0()
    Test_B01.last_name_input_0()
    Test_B01.next_button_1()
except Exception as err:
    print('Test B01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test B01:")
    print(err.__module__)



























































'''
#TC B01
zip input()
customer intent
enter first name
enter last name
select next
#
'''







