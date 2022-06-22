#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
import os
from datetime import datetime
from requests import post
import time
from python_imagesearch.imagesearch import imagesearch
id = str(input("Telegram id:"))
time_x = 0
analys_text = open("analiz{}_{}_{}_{}.txt".format(datetime.now().day,datetime.now().hour,datetime.now().minute,datetime.now().second),"w")
try:
    while True:
        if imagesearch(image="active.PNG")[0] != -1:
            time_x = 0
            analys_text.write("Giriş yapıldı: {}:{}\n".format(datetime.now().hour, datetime.now().minute))
            post("https://api.telegram.org/bot5051736797:AAEw9X9SWyJKoAsgJhbq49i70nqZfHp8F5w/sendMessage",
                 data={"chat_id": id, "text": "WhatsApp-Giriş yapıldı. BO1"})
            while True:
                if imagesearch(image="active.PNG")[0] != -1:
                    print("Online - {}".format(time_x))
                    time_x += 1
                    time.sleep(1)
                else:
                    analys_text.write("Aktif kalındı: {} dk {} sn\n".format(time_x // 60, time_x - (time_x // 60) * 60))
                    analys_text.write("Çıkış yapıldı: {}:{}\n".format(datetime.now().hour, datetime.now().minute))
                    post("https://api.telegram.org/bot5051736797:AAEw9X9SWyJKoAsgJhbq49i70nqZfHp8F5w/sendMessage",
                         data={"chat_id": id,
                               "text": "{} dk {} sn boyunca whatsapp'ta aktif kaldı ve çıkış yaptı. BO2".format(
                                   time_x // 60, time_x - (time_x // 60) * 60)})
                    time_x = 0
                    break
        elif imagesearch(image="active.PNG")[0] == -1:
            time.sleep(1)
            time_x += 1
            print("Offline - {}".format(time_x))

except:
    post("https://api.telegram.org/bot5051736797:AAEw9X9SWyJKoAsgJhbq49i70nqZfHp8F5w/sendMessage",
         data={"chat_id": id, "text": "Bir hata oluştu ! BO3"})
finally:
    analys_text.close()
    post("https://api.telegram.org/bot5051736797:AAEw9X9SWyJKoAsgJhbq49i70nqZfHp8F5w/sendMessage",
         data={"chat_id": id, "text": "Txt log dosyası kaydedildi mevcut konuma: {}".format(os.getcwd())})
