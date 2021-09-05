"""
Whatsapp automation using Python

Source code to send a message to a person.
"""
#import the webdriver from selenium package
from selenium import webdriver

#import the keys class from selenium package
from selenium.webdriver.common.keys import Keys

#initialize the web driver variable
#give the path of the web driver in the string
driver=webdriver.Chrome(executable_path=r"C:\Users\AKANDE\Documents\chrome driver\chromedriver.exe")

#browse to a whatsapp web
driver.get(r"https://web.whatsapp.com")

#give the list of contact names in the below list
names=["Kate","Chris","Bob"]

#give the path of the bill for each user in the below list
bills=[r"C:\Users\AKANDE\Desktop\AUTOMATION\bill1.png",
       r"C:\Users\AKANDE\Desktop\AUTOMATION\bill2.jpg",
       r"C:\Users\AKANDE\Desktop\AUTOMATION\bill3.jpg"]

#iterate over the names list
for i in range(3):
    name=names[i]
    path=bills[i]

    #generate the message
    msg1="Hi {0}".format(name)
    msg2="Thanks for purchasing. Your bill is attached."
    msg3="Have a nice day"
    
    #control the search contact text box
    search=driver.find_elements_by_class_name(r"_13NKt")

    #type the contact name and press enter    
    search[0].send_keys(name+Keys.ENTER)
    
    #type the messages and press enter
    search=driver.find_elements_by_class_name(r"_13NKt")    
    search[1].send_keys(msg1+Keys.ENTER)
    search[1].send_keys(msg2+Keys.ENTER)
    search[1].send_keys(msg3+Keys.ENTER)
    
    #control the attach button
    attach=driver.find_element_by_xpath(r'//*[@title="Attach"]')
    #click the attach button
    attach.click()
    
    #contol the open dialog
    dialog=driver.find_element_by_tag_name(r"input")
    #send the bill 
    dialog.send_keys(path)
    
    #add delay to wait till the upload is completed
    import time 
    time.sleep(2)
    
    #control the send button
    button=driver.find_element_by_class_name(r"_165_h")
    #click the send button
    button.click()
    
    #wait for some time before opening next chat
    time.sleep(2)



