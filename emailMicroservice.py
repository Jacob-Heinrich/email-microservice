#!/usr/bin/env python

import pika,sys,os
import ssl
from tkinter import *
from tkinter import ttk
import smtplib
from email.message import EmailMessage


def communication():
        openEmail = ""

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='email')

        def callback(ch,method,properties,body):
            openEmail = body
            if(str(body) == "b'yes'"):
                email()


        channel.basic_consume(queue='email',on_message_callback=callback,auto_ack = True)

        channel.start_consuming()


def email():
        root = Tk()

        # Set the size of the window
        root.geometry("900x450")

        # Frame
        frame = Frame(root, height = 200, width = 900)
        frame.pack()


        def display_text():
            global entry
            string = entry.get()
            bodyString = emailBody.config(1.0, END)
            msg = EmailMessage()
            msg.set_content(bodyString)
            msg['Subject'] = string
            msg['From'] = "heinrija@oregonstate.edu"
            msg['To'] = "jacob.heinrich09@gmail.com"

            s = smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('CS361SoftwareEngineering@gmail.com','yoevauamcinrcxvs')
            s.sendmail('CS361SoftwareEngineering','jacob.heinrich09@gmail.com',msg.as_string())
            s.quit()




        # Email subject section
        emailSubject = Label(frame,text = "Subject")
        emailSubject.pack()


        emailMessage = Label(frame)
        emailMessage.pack()



        entry = Entry(frame, width = 50)
        entry.focus_set()
        entry.pack()

        # Email body section
        emailBody = Text(root, width = 60, height = 20,bg = "lightgray")
        emailBody.pack()


        button_frame = Frame(root)
        button_frame.pack()


        submitButton = Button(
                    root,
                    text="Send Email",
                    command = display_text,
                    fg="black")


        submitButton.pack( side = BOTTOM )
        root.mainloop()

while True:
    email()