import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch("Outlook.Application")
outlook_ns = outlook.GetNamespace("MAPI")

myfolder = outlook_ns.Folders['mckenna_preston1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items

messagecount = 0
'''
for message in messages:
    if message.UnRead:
        print(message.sender)
        print(message.subject)

        if 'absence' in message.subject:
            print("Found message with absence")

            Msg = outlook.CreateItem(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject  + ' email'
            Msg.HTMLBody = 'Hi' + message.sender + "\n" + "sorry you are not well"

            Msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
            Msg.ReadReceiptRequested = True

            Msg.Send()
'''
for message in messages:
    