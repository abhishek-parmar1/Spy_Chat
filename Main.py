###########IMPORT FILES AND VARIABLES AND BASIC FUNCTION################

#for creating files and folders
import os

#for storing data about spy
from All_Spy_Dictionary import spy_dictionary

#for displaying chat history for spy
from All_Spy_Dictionary import chat_history

#for guest user
from Default_Spy_Details import default_spy_details

#for displaying history of guest user
from Default_Spy_Details import chat_history_default

#for encoding and decoding message inside the image
from steganography.steganography import Steganography

#for date and time
from datetime import datetime

#default status list
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

#class to update the status and change status list of spy
class Status:
    #constructor
    def __init__(self,spy_name):
        self.spy_name=spy_name
    #function to change status
    def change_status(self):
        spy_choice = input_func("Do you  want to \n1> choose from the older status updates  \n2> create a new status update \nSelect :",0)
        if(spy_choice == 1):
            #change status of spy
            if (self.spy_name != "Demo"):
                #display current status
                print "Your current Status is " + spy_dictionary[spy_name]['Status']
                print "Select Status : "
                #display default status list
                index = 1
                for name in status_list:
                    print str(index) + "> " + name
                    index += 1
                spy_status = raw_input("Enter status : ")
                #change status
                spy_dictionary[spy_name]['Status'] = spy_status
                #display new status
                print "Your new status is : " + spy_dictionary[spy_name]['Status']
            # change status of guest
            else:
                # display current status
                print "Your Current Status is " + default_spy_details['Demo']['Status']
                print "Select Status : "
                # display default status list
                index = 1
                for name in status_list:
                    print str(index) + "> " + name
                    index += 1
                spy_status = raw_input("Enter status : ")
                # change status
                default_spy_details['Demo']['Status'] = spy_status
                # display new status
                print "Your new status is : " + default_spy_details['Demo']['Status']
        elif(spy_choice == 2):
            # change status of spy
            if(self.spy_name != "Demo"):
                # display current status
                print "Your current Status is " + spy_dictionary[spy_name]['Status']
                spy_status = raw_input("Enter status : ")
                # check if status already in default list, if yes only update status
                if(spy_status in status_list):
                    spy_dictionary[spy_name]['Status'] = spy_status
                # if no append status to default list
                else:
                    spy_dictionary[spy_name]['Status'] = spy_status
                    status_list.append(spy_status)
                # display new status
                print "Your new status is : " + spy_dictionary[spy_name]['Status']
            # change status of guest
            else:
                # display current status
                print "Your Current Status is " + default_spy_details['Demo']['Status']
                spy_status = raw_input("Enter status : ")
                # check if status already in default list, if yes only update status
                if (spy_status in status_list):
                    default_spy_details['Demo']['Status'] = spy_status
                # if no append status to default list
                else:
                    default_spy_details['Demo']['Status'] = spy_status
                    status_list.append(spy_status)
                # display new status
                print "Your new status is : " + default_spy_details['Demo']['Status']

#class to add a friend
class Friend:
    #constructor
    def __init__(self,spy_name):
        self.spy_name=spy_name
    # function to add friend to spy friend list
    def add_friend(self):
        #for spy
        if (self.spy_name != "Demo"):
            friend_name = input_func("Enter your friend name : ",1)
            #if empty friend name inputed
            if (len(friend_name) <= 0):
                print "Invalid Friend Name"
            #if friend actually not exist
            if (friend_name not in (spy_dictionary.keys())):
                print friend_name + " not Exist"
            else:
                friend_age =  input_func("Enter your friend age : ",0)
                #if friend age is not enough
                if (friend_age <= 12):
                    print friend_name + " is underaged (less than or equal to 12)"
                else:
                    friend_rating = input_func("Enter your friend rating : ", 2)
                    #if friend rating is not enough
                    if (spy_dictionary[self.spy_name]['Rating'] > friend_rating):
                        print friend_name + " has low rating than you"
                    else:
                        #match the detail of friend from the actual spy, if yes add friend
                        if (friend_rating == spy_dictionary[friend_name]['Rating'] and friend_age ==
                            spy_dictionary[friend_name]['Age']):
                            spy_dictionary[self.spy_name]['Friend'].update({
                                friend_name: {
                                    'Age': friend_age,
                                    'Rating': friend_rating
                                }
                            })
                            print "Your Friend added"
                        else:
                            print " Entered details not matched the original details of your friend"
            #return length of friend list of spy
            return len(spy_dictionary[self.spy_name]['Friend'].keys())
        else:
            #for guest spy
            friend_name = input_func("Enter your friend name : ", 1)
            # if empty friend name inputed
            if (len(friend_name) <= 0):
                print "Invalid Friend Name"
            # if friend actually not exist
            if (friend_name not in (spy_dictionary.keys())):
                print friend_name + " not Exist"
            else:
                friend_age = input_func("Enter your friend age : ", 0)
                # if friend age is not enough
                if (friend_age <= 12):
                    print friend_name + " is underaged (less than or equal to 12)"
                else:
                    friend_rating = input_func("Enter your friend rating : ", 2)
                    # if friend rating is not enough
                    if (default_spy_details['Demo']['Rating'] > friend_rating):
                        print friend_name + " has low rating than you"
                    else:
                        # match the detail of friend from the actual spy, if yes add friend
                        if (friend_rating == spy_dictionary[friend_name]['Rating'] and friend_age ==
                            spy_dictionary[friend_name]['Age']):
                            default_spy_details['Demo']['Friend'].update({
                                friend_name: {
                                    'Age': friend_age,
                                    'Rating': friend_rating
                                }
                            })
                            print "Your Friend added"
                        else:
                            print " Entered details not matched the original details of your friend"
            # return length of friend list of spy
            return len(default_spy_details['Demo']['Friend'].keys())

#class to send message
class Send_Message:
    #constructor
    def __init__(self,spy_name):
        self.spy_name=spy_name
    #function to select a friend to send message
    def select_friend(self):
        #for spy
        if(self.spy_name != "Demo"):
            print "Select your friend to send message : "
            #display friend list
            index =1
            for name in (spy_dictionary[self.spy_name]['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name : ",1)
        #for guest
        else:
            print "Select your friend to send message : "
            # display friend list
            index = 1
            for name in (default_spy_details['Demo']['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name :", 1)
    #function to send message
    def send_a_message(self):
        #for spy
        if (self.spy_name != "Demo"):
            chat_friend = Send_Message.select_friend(self)
            #cannot send message to guest
            if(chat_friend =="Demo"):
                print "Sorry you can't send message to demo"
                return
            #take details of message
            image_path = input_func("Enter the name of the image in which you want to encode the message : ",1)
            secret_message = input_func("Enter the secret message you want to send : ",1)
            output_image = input_func("Enter the name of the output image (.PNG): ",1)
            #create folder of friend
            if((os.path.isdir(chat_friend)) == False):
                os.mkdir(chat_friend)
            #create folder of spy inside friend folder
            if((os.path.isdir(chat_friend + "/" + self.spy_name)) == False):
                os.mkdir(chat_friend + "/" + self.spy_name)
            #generate path for output image
            output_image_with_path = chat_friend + "/" + self.spy_name + "/" + output_image
            #encode image
            Steganography.encode(image_path, output_image_with_path, secret_message)
            print "Message encrypted and sent "
            #store record of chat history
            if(chat_friend in chat_history.keys()):
                chat_history[chat_friend].update({
                    datetime.today().strftime("%d/%m/%y  %H:%M:%S"): {
                        'Message': secret_message,
                        'Flag': True
                    }
                })
            else:
                chat_history.update({
                    chat_friend : {
                        datetime.today().strftime("%d/%m/%y  %H:%M:%S"): {
                            'Message': secret_message,
                            'Flag': True
                        }
                    }
                })
        #for guest
        else:
            chat_friend = Send_Message.select_friend(self)
            # take details of message
            image_path = input_func("Enter the name of the image in which you want to encode the message : ", 1)
            secret_message = input_func("Enter the secret message you want to send : ", 1)
            output_image = input_func("Enter the name of the output image (.PNG): ", 1)
            # create folder of friend
            if ((os.path.isdir(chat_friend)) == False):
                os.mkdir(chat_friend)
            # create folder of guest inside friend folder
            if ((os.path.isdir(chat_friend + "/Demo")) == False):
                os.mkdir(chat_friend + "/Demo")
            # generate path for output image
            output_image_with_path = chat_friend + "/Demo" + "/" + output_image
            # encode image
            Steganography.encode(image_path, output_image_with_path, secret_message)
            print "Message encrypted and sent"
            # store record of chat history
            if (chat_friend in chat_history_default.keys()):
                chat_history_default[chat_friend].update({
                    datetime.today().strftime("%d/%m/%y  %H:%M:%S"): {
                        'Message': secret_message,
                        'Flag': True
                    }
                })
            else:
                chat_history_default.update({
                    chat_friend: {
                        datetime.today().strftime("%d/%m/%y  %H:%M:%S"): {
                            'Message': secret_message,
                            'Flag': True
                        }
                    }
                })

#class to read message for spy
class Read_Message:
    #constructor
    def __init__(self,spy_name):
        self.spy_name = spy_name
     #function to select a friend to read message
    def select_a_friend(self):
        #for spy select friend
        if(self.spy_name != "Demo"):
            print "Select your friend to read message : "
            #display friend list of spy
            index =1
            for name in (spy_dictionary[self.spy_name]['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            #display demo friend
            print str(index) + "> Demo"
            #display name other user who sended message
            index += 1
            unknown_list = os.listdir(self.spy_name)
            if (len(unknown_list) > 0):
                print "Messages from other Users : "
                for name in unknown_list:
                    print str(index) + "> " + name
                    index += 1
            return input_func("Enter friend name : ",1)
    #function to read message
    def read_a_message(self):
        #for spy
        if (self.spy_name != "Demo"):
            chat_friend = Read_Message.select_a_friend(self)
            #check if spy actually recived a message
            if ((os.path.isdir(self.spy_name)) == True):
                #check if friend actually send message
                if ((os.path.isdir(self.spy_name + "/" + chat_friend)) == True):
                    #display message list form friend
                    message_list = os.listdir(self.spy_name + "/" + chat_friend)
                    index = 1
                    if (len(message_list) > 0):
                        print "Messages from : " + chat_friend
                        for name in message_list:
                            print str(index) + "> " + name
                            index += 1
                        #take image details
                        image_name = input_func("Enter the name of the image which you want to dencode the message : ",1)
                        #generate image path
                        output_image_with_path = self.spy_name + "/" + chat_friend + "/" + image_name
                        #decode image and print message
                        secret_text = Steganography.decode(output_image_with_path)
                        print "secret message is : " + secret_text
                    else:
                        print "You have messages from " + chat_friend
                else:
                    print "You have no new messages from " + chat_friend
            else:
                print "You have no new messages"
        #guest cannot read message
        else:
            print "You are demo user, you can't read messages "

#class to print chat history
class History:
    #constructor
    def __init__(self,spy_name):
        self.spy_name = spy_name
    #function to select a friend to read chat history
    def select_a_friend(self):
        #for spy
        if (self.spy_name != "Demo"):
            print "Select your friend to read chat : "
            #display friend list
            index = 1
            for name in (spy_dictionary[self.spy_name]['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name : ", 1)
        #for guest
        else:
            print "Select your friend to read chat : "
            # display friend list
            index = 1
            for name in (default_spy_details['Demo']['Friend'].keys()):
                print str(index) + "> " + name
                index += 1
            return input_func("Enter friend name :", 1)
    #function to display chat history
    def read_chat(self):
        newdate = datetime.today()
        #for spy
        if (self.spy_name != "Demo"):
            chat_friend = History.select_a_friend(self)
            if (chat_friend in chat_history.keys()):
                for newdate in chat_history[chat_friend]:
                    print str(newdate) + " " + str(chat_history[chat_friend][newdate])
            else:
                print " no chat history with " + chat_friend
        #for guest
        else:
            chat_friend = History.select_a_friend(self)
            if (chat_friend in chat_history_default.keys()):
                for newdate in chat_history_default[chat_friend]:
                    print str(newdate) + " " + str(chat_history_default[chat_friend][newdate])
            else:
                print " no chat history with" +chat_friend

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
        #input choice of spy and call the function
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
            obj = Read_Message(spy_name)
            obj.read_a_message()
        elif(spy_choice == 5):
            obj = History(spy_name)
            obj.read_chat()
        elif(spy_choice == 6):
            break

###########PROGRAM START###############################
print "Welcome Spy"

spy_choice = input_func("Do you want to use \n1> default user details  \n2> create your own user \n: ",0)
#for guest
if(spy_choice == 1):
    print "Your Details are : \nName = Demo \nGender = " + str(default_spy_details['Demo']['Gender']) + "\nAge = " + str(default_spy_details['Demo']['Age']) + "\nStatus = " + str(default_spy_details['Demo']['Status']) + "\nRating = " + str(default_spy_details['Demo']['Rating'])
    spy_menu("Demo")
    exit()
#for spy
elif(spy_choice == 2):
    while(True):
        spy_name = input_func("Enter your SPY name : ", 1)
        #for already created spy
        if(spy_name in (spy_dictionary.keys())):
            print "Aleady Present"
            spy_menu(spy_name)
            break
        #for creation of new spy
        else:
            #for valid name
            if(len(spy_name)>0):
                spy_gender = input_func("Please select your Gender : \n1> Male \n2> Female \n: ",1)
                if(spy_gender == "Male"):
                    spy_age = input_func("Please enter your Age Mr. " + spy_name + " : ",0)
                    #for valid age
                    if(spy_age <= 12):
                        print "Mr." + spy_name + " you are underaged (less than or equal to 12), SORRY. "
                        break
                    elif(spy_age >= 50):
                        print "Mr." + spy_name + " you are overaged (greater than or equal to 50), SORRY. "
                        break
                    #add spy
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
                    #for valid age
                    if (spy_age <= 12):
                        print "Mrs." + spy_name + " you are underaged (less than or equal to 12), SORRY. "
                        break
                    elif (spy_age >= 50):
                        print "Mrs." + spy_name + " you are overaged (greater than or equal to 50), SORRY. "
                        break
                    #add spy
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