# import the necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

# create object
bot = ChatBot("Roboz")

# create conversations
convo = [
 'hello',
 'hi there!',
 'what is your name?',
 'My name is Roboz, I am created by Shaona Kundu',
 'how are you?',
 'I am fine',
 'thank you',
 'Where do you live?',
 'I live in Kolkata, WB',
 'In which language do you speak?',
 'I mostly talk in English'
 ]

trainer = ListTrainer(bot)

# train the bot with help of trainer
trainer.train(convo)

# print("Talk to bot")
# while True:
#  query = input()
#  if query == 'exit':
#   break
# ans = bot.get_response(query)
# print("bot : ", ans)
main = Tk()
main.geometry("500x650")

main.title("My Chat Bot")
img = PhotoImage(file="bot1.png")
photoL = Label(main, image=img)

photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    textF.delete(0, END)



frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

main.mainloop()
