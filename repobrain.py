#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
import keyboard
from python_imagesearch.imagesearch import imagesearch
from datetime import datetime
import selenium
from selenium import webdriver
import os
from requests import post
import pyautogui
import webbrowser
import time
from time import sleep
from random import randint
from os import system
from PyQt5 import QtWidgets,QtGui
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
username = "NRB"
password = randint(10000000,100000000000000)
while True:
    if os.path.exists("password.txt") == True:
        kullanıcı_adı = pyautogui.prompt(text='Kullanıcı adınızı girin', title='NRB SECURİTY', default='')
        sifre = pyautogui.password(text='Şifrenizi giriniz.', title='NRB SECURİTY', mask="*")
        read_path = open("password.txt", "r")
        if read_path.read() == sifre and kullanıcı_adı == username:
            pyautogui.alert(text='Giriş Başarılı ...', title='NRB SECURİTY', button="Tamam")
            read_path.close()
            break
        else:
            pyautogui.alert(text='Giriş Başarısız (Şifrenizi admin den alabilirsiniz.)', title='NRB SECURİTY',
                            button="Tamam")
            exit()
    elif os.path.exists("password.txt") == False:
        key_sc = randint(10,1000)
        quer = pyautogui.confirm(
            text='İlk girişler için belirli bir ücret karşılığında adminden kendine özel bir şifre alman gerekiyor',
            title='NRB', buttons=["Şifre al", "Daha sonra"])
        if str(quer) == "Şifre al":
            password = randint(10000000, 100000000000000)
            pyautogui.alert(text='KEY_SC: {} kodunu şifre satın alma sürecince bir yere not edin'.format(key_sc), title='NRB SECURİTY',
                            button="Tamam")
            post("https://api.telegram.org/bot5051736797:AAEw9X9SWyJKoAsgJhbq49i70nqZfHp8F5w/sendMessage",
                 data={"chat_id": "1107031296", "text": "KEY: {}-{}".format(password,key_sc)})
            write_path = open("password.txt","w")
            write_path.write(str(password))
            write_path.close()
        elif str(quer) == "Daha sonra":
            exit()


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("NRB")
        self.buton = QtWidgets.QPushButton("Start")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.show()

    def click(self):
        browser = webdriver.Firefox()

        time.sleep(10)
        browser.close()
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
