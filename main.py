# from tkinter import *
#
# def button_clicked():
#     print("Bingo")
#     new_text=input.get()
#     label.config(text=new_text)
#
# window=Tk()
# window.title("One Piece")
# window.minsize(width=500,height=300)
# window.config(padx=20,pady=20)
#
#
# #label
# label=Label(text="I'm gonna be the king of the pirates",font=("Arial",14,"bold"))
# label["text"]="New text"
# # label.config(text="new txt")
# # label.pack()
# # label.place(x=100,y=200)
# label.grid(column=0,row=0)
# label.config(padx=10,pady=10)
#
#
# #button
# button = Button(text="Click Me",command=button_clicked)
# # button.pack()
# button.grid(column=1,row=1)
#
# button1 = Button(text="Flick me")
# # button.pack()
# button1.grid(column=2,row=0)
#
#
# #Entry
# input=Entry(width=30)
# input.insert(END,"Some text to begin with")
# # input.pack()
# input.grid(column=3,row=2)

# #text
# text=Text(height=5,width=30)
# text.focus()
# text.insert(END,"Examples of Multiline text entry")
# text.pack()
#
# #spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()
#
# #Scale
# def scale_used(value):
#     print(value)
# scale=Scale(from_=0,to=100,command=scale_used)
# scale.pack()
#
# #checkbutton
# def checkbutton_used():
#     print(checked_state.get())
# checked_state=IntVar()
# checkbutton=Checkbutton(text="Is On?",variable=checked_state,command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #RadioButton
# def radio_used():
#     print(radio_state.get())
#
# radio_state=IntVar()
# radiobutton1=Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
# radiobutton2=Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #listbox
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
# listbox=Listbox(height=4)
# fruits=["Apple","Banana","Pear","Orange"]
# for item in fruits:
#     listbox.insert(fruits.index(item),item)
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()









window.mainloop()
