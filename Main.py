###########IMPORT FILES AND VARIABLES################################

from All_Spy_Dictionary import spy_dictionary

from Default_Spy_Details import default_spy_details

status_list = ['Online','Offline','Available','Unavailable','Busy','At the movie','At work','In a meeting','At the gym']
####################CLASS############################

class status:
    def __init__(self,spy_name):
        self.spy_name=spy_name
    def change_status(self):
        if(self.spy_name != "Demo"):
            print "Your current Status is " + spy_dictionary[spy_name]['Status']
            print "Select Status or Add your own Status : "
            index = 1
            for name in status_list:
                print str(index) + "> " + name
                index += 1
            spy_status = raw_input("Select status : ")
            if(spy_status in status_list):
                spy_dictionary[spy_name]['Status'] = spy_status
            else:
                spy_dictionary[spy_name]['Status'] = spy_status
                status_list.append(spy_status)
            print status_list
        else:
            print "Your Previous Status is Demo"
            print "Select Status or Add your own Status : "
            index = 1
            for name in status_list:
                print str(index) + "> " + name
                index += 1
            spy_status = raw_input("Enter status : ")
            default_spy_details['Demo']['Status'] = spy_status
            print status_list

class friend:
    def __init__(self,spy_name):
        self.spy_name=spy_name
    def add_friend(self):
        print ""


#####################FUNCTIONS#######################

# function to take input
def input_func(string,x):
    #for input in integer
    if(x==0):
        return int(raw_input(string))
    #for input in string
    if(x==1):
        return raw_input(string)

# function for spy menu
def spy_menu(spy_name):
    while(True):
        print "1> Add Status"
        print "2> Add a friend"
        print "3> Send an encoded message"
        print "4> Read message"
        print "5> Read Previous History"
        print "6> To Exit"
        spy_choice = input_func("select : ",0)
        if(spy_choice == 1):
            obj = status(spy_name)
            obj.change_status()
        elif(spy_choice == 2):
            obj = friend(spy_name)
            obj.add_friend()
        elif(spy_choice == 3):
            print ""
        elif(spy_choice == 4):
            print ""
        elif(spy_choice == 5):
            print ""
        elif(spy_choice == 6):
            break

###########PROGRAM START###############################
print "Welcome Spy"

spy_choice = input_func("Do you want to use \n1> default user details  \n2> create your own user \n: ",0)
if(spy_choice == 1):
    print "Your Details are : \nName = Demo \nGender = " + str(default_spy_details['Demo']['Gender']) + "\nAge = " + str(default_spy_details['Demo']['Age']) + "\nStatus = " + str(default_spy_details['Demo']['Status']) + "\nRating = " + str(default_spy_details['Demo']['Rating'])
    spy_menu("Demo")
    exit()
elif(spy_choice == 2):
    while(True):
        spy_name = input_func("Enter your SPY name : ", 1)
        if(spy_name in (spy_dictionary.keys())):
            print "Aleady Present"
            spy_menu(spy_name)
            break
        else:
            if(len(spy_name)>0):
                spy_gender = input_func("Please select your Gender : \n1> Male \n2> Female \n: ",1)
                if(spy_gender == "Male"):
                    spy_age = input_func("Please enter your Age Mr. " + spy_name + " : ",0)
                    if(spy_age<12):
                        print "Mr." + spy_name + " you are underaged, SORRY. "
                        break
                    elif(spy_age>50):
                        print "Mr." + spy_name + " you are overaged, SORRY. "
                        break
                    else:
                        spy_rating = input_func("Please enter your Rating (out of 5) : ",0)
                        spy_dictionary.update({
                            spy_name : {
                                'Gender' : spy_gender,
                                'Age'    : spy_age,
                                'Rating' : spy_rating,
                                'Status': 'Online'
                            }
                        })
                        print spy_dictionary
                        spy_menu(spy_name)
                        break
                if (spy_gender == "Female"):
                    spy_age = input_func("Please enter your Age Mrs. " + spy_name + " : ", 0)
                    if (spy_age < 12):
                        print "Mrs." + spy_name + " you are underaged, SORRY. "
                        break
                    elif (spy_age > 50):
                        print "Mrs." + spy_name + " you are overaged, SORRY. "
                        break
                    else:
                        spy_rating = input_func("Please enter your Rating (out of 5) : ", 0)
                        spy_dictionary.update({
                            spy_name: {
                                'Gender': spy_gender,
                                'Age': spy_age,
                                'Rating': spy_rating,
                                'Status': 'Online'
                            }
                        })
                        print spy_dictionary
                        spy_menu(spy_name)
                        break
            else:
                print "Your name is INVALID "