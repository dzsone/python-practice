# -*- coding: utf-8 -*-
import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
choices = ['Vanilla','Chocolate','Strawberry'])
#buttonbox和choicebox变更，效果不同。一个是按钮选择，一个是选择框。
#enterbox为输入框，需要去除choices部分的代码。添加默认值为default='xx',替换choices部分。
easygui.msgbox("Your picked " + flavor)