'''
import random
secret = random.randint(1,100)
guess = 0
tries = 0

print("AHOY! I'm the Dread Pirate Roberts, and I have secrect!")
print("It is a number from 1 to 99. I'll give you 6 tries.")

while guess != secret and tries < 6:
    guess = input("What's yer guess?")
    if int(guess) < secret:
        print("Too low, ye scurvy dog!")
    elif int(guess) > secret :
        print("Too high, landlubber!")
    tries = tries + 1
    if int(guess) == secret :
        print("Avast! Ye got it! Found my secret, ye did!")
    elif guess != secret and tries == 6 :
        print("No more guesses! Better luck next time, matey!")
        print("The secret number was",secret)
'''        

#图形界面的游戏
# -*- coding: utf-8 -*-
import random, easygui
secret = random.randint(1,100)
guess = 0
tries = 0

easygui.msgbox("""这里有一个猜数字游戏，欢迎大家尝试！
猜数范围在1到99之间。 你有6次机会""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("朋友，你猜测的数字是什么?")
    if not guess:break
    if guess < secret:
        easygui.msgbox(str(guess) + " 太小了，大胸弟！")
    elif guess > secret :
        easygui.msgbox(str(guess) + " 太高了，老铁！")
    tries = tries + 1
    if guess == secret :
        easygui.msgbox("屌炸天了，恭喜你朋友！你猜对了！")
    elif guess != secret and tries == 6 :
        easygui.msgbox("""可惜了，朋友。 欢迎你下次再有机会来参加此游戏。
        本次的猜数游戏答案是 """ + str(secret))
