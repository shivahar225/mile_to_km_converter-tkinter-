from tkinter import *

window = Tk()
window.title("my program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# label
my_label = Label(text="i am a label", font=("arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "new text"
my_label.config(text="new text")


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print(new_text)


button = Button(text="click here", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="new button", command=button_clicked)
button_2.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

mainloop()
