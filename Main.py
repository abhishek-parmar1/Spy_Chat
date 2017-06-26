###########IMPORT FILES AND VARIABLES AND BASIC FUNCTION################

from All_Spy_Dictionary import spy_dictionary

from Default_Spy_Details import default_spy_details

from steganography.steganography import Steganography

status_list = ['Online','Offline','Available','Unavailable','Busy','At the movie','At work','In a meeting','At the gym']

# function to take input
def input_func(string,x):
    #for input in integer
    if(x==0):
        return int(raw_input(string))
    #for input in string
    elif(x==1):
        return raw_input(string)
    #for input in float
    elif(x==2):
        return float(raw_input(string))

####################CLASS###############################################

class Status:
    def __init__(self,spy_name):
        self.spy_name=spy_name
    def change_status(self):
        spy_choice = input_func("Do you  want to \n1> choose from the older status updates  \n2> create a new status update \nSelect :",0)
        if(spy_choice == 1):
            if (self.spy_name != "Demo"):
                print "Your current Status is " + spy_dictionary[spy_name]['Status']
                print "Select Status : "
                index = 1
                for name in status_list:
                    print str(index) + "> " + name
                    index += 1
                spy_status = raw_input("Enter status : ")
                spy_dictionary[spy_name]['Status'] = spy_status
                print "Your new status is : " + spy_dictionary[spy_name]['Status']
            else:
                print "Your Current Status is " + default_spy_details['Demo']['Status']
                print "Select Status : "
                index = 1
                for name in status_list:
                    print str(index) + "> " + name
                    index += 1
                spy_status = raw_input("Enter status : ")
                default_spy_details['Demo']['Status'] = spy_status
                print "Your new status is : " + default_spy_details['Demo']['Status']
        elif(spy_choice == 2):
            if(self.spy_name != "Demo"):
                print "Your current Status is " + spy_dictionary[spy_name]['Status']
                spy_status = raw_input("Enter status : ")
                if(spy_status in status_list):
                    spy_dictionary[spy_name]['Status'] = spy_status
                else:
                    spy_dictionary[spy_name]['Status'] = spy_status
                    status_list.append(spy_status)
                print "Your new status is : " + spy_dictionary[spy_name]['Status']
            else:
                print "Your Current Status is " + default_spy_details['Demo']['Status']
                spy_status = raw_input("Enter status : ")
                if (spy_status in status_list):
                    default_spy_details['Demo']['Status'] = spy_status
                else:
                    default_spy_details['Demo']['Status'] = spy_status
                    status_list.append(spy_status)
                print "Your new status is : " + default_spy_details['Demo']['Status']

class Friend:
    def __init__(self,spy_name):
        self.spy_name=spy_name
    def add_friend(self):
        if (self.spy_name != "Demo"):
            friend_name = input_func("Enter your friend name : ",1)
            friend_age =  input_func("Enter your friend age : ",0)
            friend_rating = input_func("Enter your friend rating : ", 2)
            if(len(friend_name) <= 0):
                print "Invalid Friend Name"
            elif(friend_name not in (spy_dictionary.keys())):
                print friend_name + " not Exist"
            elif(friend_age <= 12):
                print friend_name + " is underaged (less than or equal to 12)"
            elif(spy_dictionary[self.spy_name]['Rating'] > friend_rating):
                print friend_name + " has low rating than you"
            elif( len(friend_name) > 0 and friend_name in (spy_dictionary.keys()) and friend_age > 12 and spy_dictionary[self.spy_name]['Rating'] <= friend_rating):
                if(friend_rating == spy_dictionary[friend_name]['Rating'] and friend_age == spy_dictionary[friend_name]['Age']):
                    spy_dictionary[self.spy_name]['Friend'].update({
                        friend_name: {
                            'Age': friend_age,
                            'Rating': friend_rating,
                        }
                    })
                else:
                    print " Entered details not matched the original details of your friend"
            else:
                print "INVALID DETAILS"
            return len(spy_dictionary[self.spy_name]['Friend'].keys())
        else:
            friend_name = input_func("Enter your friend name : ", 1)
            friend_age = input_func("Enter your friend age : ", 0)
            friend_rating = input_func("Enter your friend rating : ", 2)
            if (len(friend_name) <= 0):
                print "Invalid Friend Name"
            elif (friend_name not in (spy_dictionary.keys())):
                print friend_name + " not Exist"
            elif (friend_age <= 12):
                print friend_name + " is underaged (less than or equal to 12)"
            elif (default_spy_details['Demo']['Rating'] > friend_rating):
                print friend_name + " has low rating than you"
            elif (len(friend_name) > 0 and friend_name in (spy_dictionary.keys()) and friend_age > 12 and default_spy_details['Demo']['Rating'] <= friend_rating):
                if (friend_rating == spy_dictionary[friend_name]['Rating'] and friend_age == spy_dictionary[friend_name]['Age']):
                    default_spy_details['Demo']['Friend'].update({
                        friend_name: {
                            'Age': friend_age,
                            'Rating': friend_rating,
                        }
                    })
                else:
                    print " Entered details not matched the original details of your friend"
            else:
                print "INVALID DETAILS"
            return len(default_spy_details['Demo']['Friend'].keys())

class Send_Message:
    def __init__(self,spy_name):
        self.spy_name=spy_name
    def select_friend(self):
        if(self.spy_name != "Demo"):
            print "Select your friend to send message : "
            index =1
            for name in (spy_dictionary[self.spy_name]['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name : ",1)
        else:
            print "Select your friend to send message : "
            index = 1
            for name in (default_spy_details['Demo']['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name :", 1)
    def send_message(self):
        chat_friend = Send_Message.select_friend()

#####################ADVANCE FUNCTIONS#######################################

# function for spy menu
def spy_menu(spy_name):
    while(True):
        print "1> Add Status Update"
        print "2> Add a Friend"
        print "3> Send an Encoded Message"
        print "4> Read Message"
        print "5> Read Previous History"
        print "6> Close Application"
        spy_choice = input_func("select : ",0)
        if(spy_choice == 1):
            obj = Status(spy_name)
            obj.change_status()
        elif(spy_choice == 2):
            obj = Friend(spy_name)
            print spy_name + " has " + str(obj.add_friend()) + " friends."
        elif(spy_choice == 3):
            obj = Send_Message(spy_name)
            obj.send_a_message()

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
                    if(spy_age <= 12):
                        print "Mr." + spy_name + " you are underaged (less than or equal to 12), SORRY. "
                        break
                    elif(spy_age >= 50):
                        print "Mr." + spy_name + " you are overaged (greater than or equal to 50), SORRY. "
                        break
                    else:
                        spy_rating = input_func("Please enter your Rating (out of 5.0) : ",2)
                        spy_dictionary.update({
                            spy_name : {
                                'Gender' : spy_gender,
                                'Age'    : spy_age,
                                'Rating' : spy_rating,
                                'Status' : 'Online',
                                'Friend' : {
                                }
                            }
                        })
                        print "Your Details are : \nName = Mr. " + spy_name + "\nGender = " + str(
                            spy_dictionary[spy_name]['Gender']) + "\nAge = " + str(
                            spy_dictionary[spy_name]['Age']) + "\nStatus = " + str(
                            spy_dictionary[spy_name]['Status']) + "\nRating = " + str(
                            spy_dictionary[spy_name]['Rating'])
                        spy_menu(spy_name)
                        break
                if (spy_gender == "Female"):
                    spy_age = input_func("Please enter your Age Mrs. " + spy_name + " : ", 0)
                    if (spy_age <= 12):
                        print "Mrs." + spy_name + " you are underaged (less than or equal to 12), SORRY. "
                        break
                    elif (spy_age >= 50):
                        print "Mrs." + spy_name + " you are overaged (greater than or equal to 50), SORRY. "
                        break
                    else:
                        spy_rating = input_func("Please enter your Rating (out of 5.0) : ", 2)
                        spy_dictionary.update({
                            spy_name: {
                                'Gender': spy_gender,
                                'Age': spy_age,
                                'Rating': spy_rating,
                                'Status': 'Online',
                                'Friend': {
                                }
                            }
                        })
                        print "Your Details are : \nName = Mrs. " + spy_name + "\nGender = " + str(
                            spy_dictionary[spy_name]['Gender']) + "\nAge = " + str(
                            spy_dictionary[spy_name]['Age']) + "\nStatus = " + str(
                            spy_dictionary[spy_name]['Status']) + "\nRating = " + str(
                            spy_dictionary[spy_name]['Rating'])
                        spy_menu(spy_name)
                        break
            else:
                print "Your name is INVALID "
                break
exit()