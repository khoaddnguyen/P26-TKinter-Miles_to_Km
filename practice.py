from tkinter import *
# Types of common widgets in TKinter: label, button, entry, text, spinbox, scale, checkbutton, radiobutton, listbox
# See widgetdemo for references

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# add padding
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# import turtle
#
# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 80, "bold"))
#my_label.pack()


# Button
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#New Button
new_button = Button(text="Don't Click Me", command=button_clicked)
#button.pack()
new_button.grid(column=2, row=0)

# Entry
# input = Entry(width=10)
# print(input.get())
#input.pack()


entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()
