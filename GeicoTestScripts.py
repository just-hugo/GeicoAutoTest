
from AutoGeicoTestClass import Auto_Geico_Test
import sys

gvt = Auto_Geico_Test()

#Precondition methods used to get initial conditions for a test case.
def preconditionA(testCaseObject):
    #these are the steps from test case(s) A in order in order to do test case B01
    testCaseObject.zip_input_0()
    testCaseObject.skip_help_page_0()
    testCaseObject.next_button_0()
    return

    #these are the steps from test cases A and B in order to do test case C01
def preconditionB(testCaseObject):
    preconditionA(testCaseObject)
    testCaseObject.first_name_input_0()
    testCaseObject.last_name_input_0()
    testCaseObject.next_button_1()
    return

    #these are the steps from test cases A, B, and C in order to do test case D01
def preconditionC(testCaseObject):
    preconditionB(testCaseObject)
    testCaseObject.month_dob_0()
    testCaseObject.day_dob_0()
    testCaseObject.year_dob_0()
    testCaseObject.next_button_2()
    return

    #these are the steps from test cases A, B, C and D in order to do test case E01
def preconditionD(testCaseObject):
    preconditionC(testCaseObject)
    testCaseObject.street_input_0()
    testCaseObject.zip_input_1()
    testCaseObject.next_button_3()
    try:
        testCaseObject.verify_address_0()
        testCaseObject.next_button_4()
    except:
        print("unable to locate verify address")
    return

def preconditionE():
    preconditionD(gvt)
    gvt.select_vehicles_unlisted()
    gvt.select_specific_body_style_unlisted(1)  # doesnt always run
    gvt.select_specific_new_costs(2)  # doesnt always run
    gvt.select_antilock_brakes(0)  # doesnt always run
    gvt.select_specific_antitheft_device_unlisted(0)  # doesnt always run
    gvt.select_ownership_unlisted(1)
    gvt.go_next()
    gvt.select_primary_use_unlisted(2)
    gvt.go_next()
    gvt.select_annual_mileage_unlisted(2)
    gvt.go_next()
    gvt.go_next()

#TC_E01 - DRIVER INFORMATION - SELECT GENDER
try:
    Test_E01 = Auto_Geico_Test()
    # preconditionX(Test_E01)

    Test_E01.gender_select_0()
    Test_E01.close_browser()
    print("test E01 ran successfully")

except Exception as err:
    print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E01:")
    print(err.__module__)
    print(str(err))

#GEICO HELP TEST CASES
#TC_A01 - I NEED INSURANCE RIGHT AWAY
try:
    Test_A01 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A01.zip_input_0()
    Test_A01.customer_intent_0()
    Test_A01.next_button_0()
    print("test case A01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A01:")
    print(err.__module__)


#TC_A02 - I'M BUYING OR JUST BOUGHT A CAR
try:
    Test_A02 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A02.zip_input_0()
    Test_A02.customer_intent_1()
    Test_A02.next_button_0()
    print("test case A02 ran successfully")
    Test_A02.close_browser()

except Exception as err:
    print('Test A02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A02:")
    print(err.__module__)


#TC A03 - i'M LOOKING FOR A BETTER PRICE
try:
    Test_A03 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A03.zip_input_0()
    Test_A03.customer_intent_2()
    Test_A03.next_button_0()
    print("test case A03 ran successfully")
    Test_A03.close_browser()

except Exception as err:
    print('Test A03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A03:")
    print(err.__module__)

#TC_A04 - I'M COMPARING RATES FOR DIFFERENT CARS
try:
    Test_A04 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A04.zip_input_0()
    Test_A04.customer_intent_3()
    Test_A04.next_button_0()
    print("test case A04 ran successfully")
    Test_A04.close_browser()

except Exception as err:
    print('Test A04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A04:")
    print(err.__module__)


#TC_A05 - I'M JUST SHOPPING TODAY
try:
    Test_A05 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A05.zip_input_0()
    Test_A05.customer_intent_4()
    Test_A05.next_button_0()
    print("test case A05 ran successfully")
    Test_A05.close_browser()

except Exception as err:
    print('Test A05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A05:")
    print(err.__module__)


#TC A06 - SKIP
try:
    Test_A06 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A06.zip_input_0()
    Test_A06.customer_intent_5()
    Test_A06.next_button_0()
    print("test case A06 ran successfully")
    Test_A06.close_browser()

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
    print("test case B01 ran successfully")
    Test_B01.close_browser()

except Exception as err:
    print('Test B01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test B01:")
    print(err.__module__)

#TC_C01 - WHEN WERE YOU BORN
try:
    Test_C01 = Auto_Geico_Test()
    preconditionB(Test_C01)

    Test_C01.month_dob_0()
    Test_C01.day_dob_0()
    Test_C01.year_dob_0()
    Test_C01.next_button_2()
    print("test case C01 ran successfully")
    Test_C01.close_browser()

except Exception as err:
    print('Test C01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test C01:")
    print(err.__module__)

#TC_D01 - WHAT'S YOUR ADDRESS,APARTMENT, ZIP CODE
#TODO look back at this and make sure it is accurate, we haven't fleshed this out entirely
try:
    Test_D01 = Auto_Geico_Test()
    preconditionC(Test_D01)

    Test_D01.street_input_0()
    Test_D01.zip_input_1()
    Test_D01.next_button_3()
    print("test D01 ran successfully")
    Test_D01.close_browser()
except Exception as err:
    print('Test D01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test D01:")
    print(err.__module__)

#TODO need to add preconditions to E01 - E5.11 lots of work to do here
#TC_E01 - DRIVER INFORMATION - SELECT GENDER
try:
    Test_E01 = Auto_Geico_Test()

    Test_E01.gender_select_0()
    Test_E01.next_button_x()
    print("test E01 ran successfully")
    Test_E01.close_browser()

except Exception as err:
    print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E01:")
    print(err.__module__)
    print(str(err))

#TC_E02 - DRIVER INFORMATION - MARITAL STATUS AND SOCIAL SECURITY NUMBER
try:
    Test_E02 = Auto_Geico_Test()

    Test_E02.marital_status_0()
    Test_E02.social_security_number_0()
    Test_E02.next_button_x()
    Test_E02.social_security_number_2()
    Test_E02.next_button_x()
    Test_E02.social_security_number_1()
    Test_E02.next_button_x()
    print("test E02 ran successfully")
    Test_E02.close_browser()

except Exception as err:
    print('Test E02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E02:")
    print(err.__module__)
    print(str(err))

#TC_E03 - DRIVER INFORMATION - HOME INFORMATION
try:
    Test_E03 = Auto_Geico_Test()

    Test_E03.home_ownership_0()
    Test_E03.next_button_x()
    print("test E03 ran successfully")
    Test_E03.close_browser()

except Exception as err:
    print('Test E03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E03:")
    print(err.__module__)
    print(str(err))

#TC_E04.1 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "YES"
try:
    Test_E04o1 = Auto_Geico_Test()

    Test_E04o1.current_insured_status_1()
    Test_E04o1.next_button_x()
    Test_E04o1.current_insurance_disclosure_0()
    Test_E04o1.current_insurance_disclosure_1()
    Test_E04o1.next_button_x()
    Test_E04o1.driving_history_1()
    Test_E04o1.next_button_x()
    print("test E04o1 ran successfully")
    Test_E04o1.close_browser()

except Exception as err:
    print('Test E04o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o1:")
    print(err.__module__)
    print(str(err))

#TC_E04.2 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I HAVEN'T NEEDED INSURANCE"
try:
    Test_E04o2 = Auto_Geico_Test()

    Test_E04o2.current_insured_status_2()
    Test_E04o2.next_button_x()
    Test_E04o2.driving_history_1()
    Test_E04o2.next_button_x()
    print("test E04o2 ran successfully")
    Test_E04o2.close_browser()

except Exception as err:
    print('Test E04o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o2:")
    print(err.__module__)
    print(str(err))

#TC_E04.3 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, MY INSUARANCE RAN OUT"
try:
    Test_E04o3 = Auto_Geico_Test()

    Test_E04o3.current_insured_status_3()
    Test_E04o3.next_button_x()
    Test_E04o3.previous_insurance_disclosure_0()
    Test_E04o3.previous_insurance_disclosure_1()
    Test_E04o3.previous_insurance_disclosure_3()
    Test_E04o3.next_button_x()
    Test_E04o3.driving_history_1()
    Test_E04o3.next_button_x()
    print("test E04o3 ran successfully")
    Test_E04o3.close_browser()

except Exception as err:
    print('Test E04o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o3:")
    print(err.__module__)
    print(str(err))

#TC_E04.4 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I WAS DEPLOYED"
try:
    Test_E04o4 = Auto_Geico_Test()

    Test_E04o4.current_insured_status_4()
    Test_E04o4.next_button_x()
    print("test E04o4 ran successfully")
    Test_E04o4.close_browser()

except Exception as err:
    print('Test E04o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o4:")
    print(err.__module__)
    print(str(err))

#TODO these need to be added to our list of test cases in the master spreadsheet, and assigned a test case id
#TC_XX01 - DRIVER INFORMATION - EDUCATION
try:
    Test_XX01 = Auto_Geico_Test()

    Test_XX01.education_level_0()
    Test_XX01.next_button_x()
    print("test E04o4 ran successfully")

except Exception as err:
    print('Test XX01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test XX01:")
    print(err.__module__)
    print(str(err))

#TC_E05o1 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
try:
    Test_E05o1 = Auto_Geico_Test()

    Test_E05o1.employment_status_0()
    Test_E05o1.next_button_x()
    Test_E05o1.current_occupation_0()
    Test_E05o1.current_occupation_1()
    Test_E05o1.next_button_x()
    print("test E05o1 ran successfully")

except Exception as err:
    print('Test E05o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o1:")
    print(err.__module__)
    print(str(err))

#TC_E05o2 - DRIVER INFORMATION - EMPLOYMENT STATUS - "ACTIVE MILITARY DUTY"
try:
    Test_E05o2 = Auto_Geico_Test()

    Test_E05o2.employment_status_0()
    Test_E05o2.employment_status_1()
    Test_E05o2.employment_status_2()
    Test_E05o2.next_button_x()
    print("test E05o2 ran successfully")

except Exception as err:
    print('Test E05o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o2:")
    print(err.__module__)
    print(str(err))

#TC_E05o3 - DRIVER INFORMATION - EMPLOYMENT STATUS - "FEDERAL GOVERNMENT AND POSTAL SERVICE"
try:
    Test_E05o3 = Auto_Geico_Test()

    Test_E05o3.employment_status_0()
    Test_E05o3.employment_status_3()
    Test_E05o3.next_button_x()
    print("test E05o3 ran successfully")

except Exception as err:
    print('Test E05o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o3:")
    print(err.__module__)
    print(str(err))

#TC_E05o4 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A STAE/LOCAL/MUNICIPAL GOVERNMENT"
try:
    Test_E05o4 = Auto_Geico_Test()

    Test_E05o4.employment_status_0()
    Test_E05o4.next_button_x()
    Test_E05o4.current_occupation_0()
    Test_E05o4.current_occupation_1()
    Test_E05o4.next_button_x()
    print("test E05o4 ran successfully")

except Exception as err:
    print('Test E05o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o4:")
    print(err.__module__)
    print(str(err))

#TC_E05o5 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM A FULL TIME STUDENT"
try:
    Test_E05o5 = Auto_Geico_Test()

    Test_E05o5.employment_status_0()
    Test_E05o5.type_of_student_0()
    Test_E05o5.next_button_x()
    print("test E05o4 ran successfully")

except Exception as err:
    print('Test E05o5' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o5:")
    print(err.__module__)
    print(str(err))

#TC_E05o6 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM CURRENTLY A HOMEMAKER"
try:
    Test_E05o6 = Auto_Geico_Test()

    Test_E05o6.employment_status_0()
    Test_E05o6.next_button_x()
    print("test E05o6 ran successfully")

except Exception as err:
    print('Test E05o6' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o6:")
    print(err.__module__)
    print(str(err))

#TC_E05o7 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM NOT CURRENTLY EMPLOYED"
try:
    Test_E05o7 = Auto_Geico_Test()

    Test_E05o7.employment_status_0()
    Test_E05o7.next_button_x()
    print("test E05o7 ran successfully")

except Exception as err:
    print('Test E05o7' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05O7:")
    print(err.__module__)
    print(str(err))

#TC_E05o8 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
try:
    Test_E05o7 = Auto_Geico_Test()

    Test_E05o7.employment_status_0()
    Test_E05o7.next_button_x()
    Test_E05o7.retirement_occupation_0()
    Test_E05o7.retirement_occupation_1()
    Test_E05o7.next_button_x()
    print("test E05o7 ran successfully")

except Exception as err:
    print('Test E05o7' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05O7:")
    print(err.__module__)
    print(str(err))

#TC_E05o9 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED MILITARY"
try:
    Test_E05o9 = Auto_Geico_Test()

    Test_E05o9.employment_status_0()
    Test_E05o9.employment_status_1()
    Test_E05o9.employment_status_2()
    Test_E05o9.next_button_x()
    print("test E05o9 ran successfully")

except Exception as err:
    print('Test E05o9' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o9:")
    print(err.__module__)
    print(str(err))

#TC_E05o10 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED FEDERAL GOVERNMENT AND POSTAL SERVICE"
try:
    Test_E05o10 = Auto_Geico_Test()

    Test_E05o10.employment_status_0()
    Test_E05o10.employment_status_3()
    Test_E05o10.next_button_x()
    print("test E05o10 ran successfully")

except Exception as err:
    print('Test E05o10' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o10:")
    print(err.__module__)
    print(str(err))

#TC_E05o11 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED STATE/LOCAL/MUNICIPAL GOVERNMENT"
try:
    Test_E05o11 = Auto_Geico_Test()

    Test_E05o11.employment_status_0()
    Test_E05o11.retirement_occupation_0()
    Test_E05o11.retirement_occupation_1()
    Test_E05o11.next_button_x()
    print("test E05o11 ran successfully")

except Exception as err:
    print('Test E05o11' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o10:")
    print(err.__module__)
    print(str(err))

#TC_W01 - MILITARY AFFILIATION 1
try:
    Test_W01 = Auto_Geico_Test()

    Test_W01.military_affiliation_0()
    Test_W01.military_affiliation_1()
    Test_W01.military_affiliation_2()
    Test_W01.next_button_x()
    print("test W01 ran successfully")

except Exception as err:
    print('Test W01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test W01:")
    print(err.__module__)
    print(str(err))

#TC_W02 - MILITARY AFFILIATION 2
try:
    Test_W02 = Auto_Geico_Test()

    Test_W02.military_affiliation_0()
    Test_W02.military_affiliation_1()
    Test_W02.military_affiliation_2()
    Test_W02.next_button_x()
    print("test W02 ran successfully")

except Exception as err:
    print('Test W02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test W02:")
    print(err.__module__)
    print(str(err))

#TC_W03 - MILITARY AFFILIATION 3
try:
    Test_W03 = Auto_Geico_Test()

    Test_W03.military_affiliation_0()
    Test_W03.military_affiliation_1()
    Test_W03.military_affiliation_2()
    Test_W03.next_button_x()
    print("test W03 ran successfully")

except Exception as err:
    print('Test W03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test W03:")
    print(err.__module__)
    print(str(err))

#TC_W04 - MILITARY AFFILIATION 4
try:
    Test_W04 = Auto_Geico_Test()

    Test_W04.military_affiliation_0()
    Test_W04.military_affiliation_1()
    Test_W04.military_affiliation_2()
    Test_W04.next_button_x()
    print("test W04 ran successfully")

except Exception as err:
    print('Test W04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test W04:")
    print(err.__module__)
    print(str(err))

#TC_W05 - MILITARY AFFILIATION 5
try:
    Test_W05 = Auto_Geico_Test()

    Test_W05.military_affiliation_0()
    Test_W05.military_affiliation_1()
    Test_W05.military_affiliation_2()
    Test_W05.next_button_x()
    print("test W05 ran successfully")

except Exception as err:
    print('Test W05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test W05:")
    print(err.__module__)
    print(str(err))

#TC_X01 - GOVERNMENT AFFILIATION 1
try:
    Test_X01 = Auto_Geico_Test()

    Test_X01.government_affiliation_0()
    Test_X01.government_affiliation_1()
    Test_X01.next_button_x()
    print("test X01 ran successfully")

except Exception as err:
    print('Test X01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test X01:")
    print(err.__module__)
    print(str(err))

#TC_X02 - GOVERNMENT AFFILIATION 2
try:
    Test_X02 = Auto_Geico_Test()

    Test_X02.government_affiliation_0()
    Test_X02.government_affiliation_1()
    Test_X02.next_button_x()
    print("test X02 ran successfully")

except Exception as err:
    print('Test X02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test X02:")
    print(err.__module__)
    print(str(err))

#TC_X03 - GOVERNMENT AFFILIATION 3
try:
    Test_X03 = Auto_Geico_Test()

    Test_X03.government_affiliation_0()
    Test_X03.government_affiliation_1()
    Test_X03.next_button_x()
    print("test X03 ran successfully")

except Exception as err:
    print('Test X03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test X03:")
    print(err.__module__)
    print(str(err))

#TC_Z01 - ADD DRIVER
try:
    Test_Z01 = Auto_Geico_Test()

    Test_Z01.next_button_x()
    print("test Z01 ran successfully")

except Exception as err:
    print('Test Z01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test Z01:")
    print(err.__module__)
    print(str(err))

#TC_Z02 - SAVED DRIVERS SCREEN
try:
    Test_Z02 = Auto_Geico_Test()

    Test_Z02.next_button_x()
    print("test Z02 ran successfully")

except Exception as err:
    print('Test Z02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test Z02:")
    print(err.__module__)
    print(str(err))

#TC_AA01 - INCIDENT LANDING PAGE 1
try:
    Test_AA01 = Auto_Geico_Test()

    Test_AA01.next_button_x()
    print("test AA01 ran successfully")

except Exception as err:
    print('Test AA01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AA01:")
    print(err.__module__)
    print(str(err))

#TC_AA02 - INCIDENT LANDING PAGE 2
try:
    Test_AA02 = Auto_Geico_Test()

    Test_AA02.add_incident()
    print("test AA02 ran successfully")

except Exception as err:
    print('Test AA02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AA02:")
    print(err.__module__)
    print(str(err))

#TC_AB01 - INCIDENT TYPE 1
try:
    Test_AB01 = Auto_Geico_Test()

    Test_AB01.add_incident()
    Test_AB01.incident_type()
    print("test AB01 ran successfully")

except Exception as err:
    print('Test AB01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AB01:")
    print(err.__module__)
    print(str(err))

#TC_AB02 - INCIDENT TYPE 2
try:
    Test_AB02 = Auto_Geico_Test()

    Test_AB02.add_incident()
    Test_AB02.incident_type()
    Test_AB02.next_button_x()
    print("test AB02 ran successfully")

except Exception as err:
    print('Test AB01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AB01:")
    print(err.__module__)
    print(str(err))

#TC_AB03 - INCIDENT TYPE 3
try:
    Test_AB03 = Auto_Geico_Test()

    Test_AB03.add_incident()
    Test_AB03.incident_type()
    Test_AB03.next_button_x()
    print("test AB03 ran successfully")

except Exception as err:
    print('Test AB03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AB03:")
    print(err.__module__)
    print(str(err))

#TC_AB04 - INCIDENT TYPE 4
try:
    Test_AB04 = Auto_Geico_Test()

    Test_AB04.add_incident()
    Test_AB04.incident_type()
    Test_AB04.next_button_x()
    print("test AB04 ran successfully")

except Exception as err:
    print('Test AB04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AB04:")
    print(err.__module__)
    print(str(err))

#TC_AB05 - INCIDENT TYPE 5
try:
    Test_AB05 = Auto_Geico_Test()

    Test_AB05.add_incident()
    Test_AB05.incident_type()
    Test_AB05.next_button_x()
    print("test AB05 ran successfully")

except Exception as err:
    print('Test AB05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AB05:")
    print(err.__module__)
    print(str(err))

#TC_AC01 - ACCIDENT RESPONSIBILITY 1
try:
    Test_AC01 = Auto_Geico_Test()

    Test_AC01.accident_flow_2()
    Test_AC01.accident_flow_4()
    Test_AC01.next_button_x()
    print("test AC01 ran successfully")

except Exception as err:
    print('Test AC01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AC01:")
    print(err.__module__)
    print(str(err))

#TC_AC02 - ACCIDENT RESPONSIBILITY 2
try:
    Test_AC02 = Auto_Geico_Test()

    Test_AC02.accident_flow_3()
    Test_AC02.accident_flow_6()
    Test_AC02.next_button_x()
    print("test AC02 ran successfully")

except Exception as err:
    print('Test AC02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AC02:")
    print(err.__module__)
    print(str(err))

#TC_AD01 - CONVICTION DETAILS 1
try:
    Test_AD01 = Auto_Geico_Test()

    Test_AD01.conviction_flow_0()
    Test_AD01.next_button_x()
    print("test AD01 ran successfully")

except Exception as err:
    print('Test AD01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AD01:")
    print(err.__module__)
    print(str(err))

#TC_AD02 - CONVICTION DETAILS 2
try:
    Test_AD02 = Auto_Geico_Test()

    Test_AD02.conviction_flow_0()
    Test_AD02.next_button_x()
    print("test AD02 ran successfully")

except Exception as err:
    print('Test AD02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AD02:")
    print(err.__module__)
    print(str(err))

#TC_ADO3 - CONVICTION/INCIDENT LENGTH OF TIME 1
try:
    Test_AD03 = Auto_Geico_Test()

    Test_AD03.conviction_flow_1()
    Test_AD03.next_button_x()
    print("test AD03 ran successfully")

except Exception as err:
    print('Test AD03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AD03:")
    print(err.__module__)
    print(str(err))

#TC_AD04 - CONVICTION/INCIDENT LENGTH OF TIME 2
try:
    Test_AD04 = Auto_Geico_Test()

    Test_AD04.conviction_flow_2()
    Test_AD04.next_button_x()
    print("test AD04 ran successfully")

except Exception as err:
    print('Test AD04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AD04:")
    print(err.__module__)
    print(str(err))

#TC_AE01 - SUSPENSION DETAILS 1
try:
    Test_AE01 = Auto_Geico_Test()

    Test_AE01.suspension_flow_0()
    Test_AE01.next_button_x()
    print("test AE01 ran successfully")

except Exception as err:
    print('Test AE01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE01:")
    print(err.__module__)
    print(str(err))

#TC_AE02 - SUSPENSION DETAILS 2
try:
    Test_AE02 = Auto_Geico_Test()

    Test_AE02.suspension_flow_0()
    Test_AE02.next_button_x()
    print("test AE02 ran successfully")

except Exception as err:
    print('Test AE02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE02:")
    print(err.__module__)
    print(str(err))

#TC_AE03 - SUSPENSION/HOW LONG AGO 1
try:
    Test_AE03 = Auto_Geico_Test()

    Test_AE03.suspension_flow_1()
    Test_AE03.next_button_x()
    print("test AE03 ran successfully")

except Exception as err:
    print('Test AE03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE03:")
    print(err.__module__)
    print(str(err))

#TC_AE04 - SUSPENSION/HOW LONG AGO 2
try:
    Test_AE04 = Auto_Geico_Test()

    Test_AE04.suspension_flow_1()
    Test_AE04.next_button_x()
    print("test AE04 ran successfully")

except Exception as err:
    print('Test AE04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE04:")
    print(err.__module__)
    print(str(err))

#TC_AE05 - LENGTH OF SUSPENSION 1
try:
    Test_AE05 = Auto_Geico_Test()

    Test_AE05.suspension_flow_2()
    Test_AE05.next_button_x()
    print("test AE05 ran successfully")

except Exception as err:
    print('Test AE05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE05:")
    print(err.__module__)
    print(str(err))

#TC_AE06 - LENGTH OF SUSPENSION 2
try:
    Test_AE06 = Auto_Geico_Test()

    Test_AE06.suspension_flow_2()
    Test_AE06.next_button_x()
    print("test AE06 ran successfully")

except Exception as err:
    print('Test AE06' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AE06:")
    print(err.__module__)
    print(str(err))

#TC_F01 - DISCOUNTS AND CONTACTS - GROUP CATEGORY SELECTION
try:
    Test_F01 = Auto_Geico_Test()

    Test_F01.discounts_1()
    Test_F01.discounts_5()
    Test_F01.next_button_x()
    print("test F01 ran successfully")

except Exception as err:
    print('Test F01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test F01:")
    print(err.__module__)
    print(str(err))

#TC_F02 - DISCOUNTS AND CONTACTS - SPECIFIC GROUP SELECTION
try:
    Test_F02 = Auto_Geico_Test()

    Test_F02.discounts_9()
    Test_F02.next_button_x()
    print("test F02 ran successfully")

except Exception as err:
    print('Test F02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test F02:")
    print(err.__module__)
    print(str(err))

#TC_F03 - DISCOUNTS AND CONTACTS - CONTACT INFORMATION
try:
    Test_F03 = Auto_Geico_Test()

    Test_F03.contact_information_0()
    Test_F03.next_button_x()
    print("test FO3 ran successfully")

except Exception as err:
    print('Test F03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test AF03:")
    print(err.__module__)
    print(str(err))