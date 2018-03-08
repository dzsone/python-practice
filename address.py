#address
import easygui
name = easygui.enterbox("What is your name?")
address = easygui.enterbox("What's your home's street?")
city = easygui.enterbox("What is your city that you live in ?")
state = easygui.enterbox("What is your state or province?")
code = easygui.enterbox("What is your postal code?")

whole_add = name + "\n"+ address + "\n" + city + "\n" + state + "\n" + code
easygui.msgbox(whole_add,"Here is your address!")