import time


def USER_CHOICE():
    print("\n")
    print(" ******* If you have another number to check write y ******* ")
    UserDecision = input("  Enter yor choise >>>>>  ")
    if UserDecision == "y":
        EN()
    else:
        print("\n")
        print(" <><><><><><><> Thank you for using this program :) <><><><><><><> ")
        time.sleep(5)
        quit()

def EN():
    try:
        PHone = input(" \n Enter phone number :  ")
        lst = [int(i) for i in str(PHone)]
    except:
        print(" ****** You must enter numbers not letters ******")
        EN()
    else:
        if len(lst) == 11:
            def KNOW_I(lst1):
               
                if lst[0] == 0:
                    if lst[1] == 1:
                        if lst[2] == 1:
                            print("  Company :     Etisalat  ")
                            time.sleep(5)
                            USER_CHOICE()

                        elif lst[2] == 0:
                            print("  Company :     Vodafone  ")
                            time.sleep(5)
                            USER_CHOICE()

                        elif lst[2] == 4:
                            print("  Company :     WE  ")
                            time.sleep(5)
                            USER_CHOICE()

                        elif lst[2] == 5:
                            print("  Company :     Orange  ")
                            time.sleep(5)
                            USER_CHOICE()
                        else:
                            print("<<<< This is a new company >>>> ")
                            time.sleep(5)
                            USER_CHOICE()
                    else:
                        print("  @@@@ This is not a mobile number ")
                        time.sleep(5)
                        USER_CHOICE()
                else:
                    print("  @@@@ This is not a mobile number ")
                    time.sleep(5)
                    USER_CHOICE()
                return
            KNOW_I(lst1=lst)
        else:
            print("  @@@@ This is not a mobile number ")
            time.sleep(5)
            USER_CHOICE()
    return
EN()
