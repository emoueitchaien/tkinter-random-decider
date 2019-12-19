import tkinter as tk
import random

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter = random.randint(1,4)
    label.config(text=str(counter),font = "Times 300 underline",padx=80,pady=1)
    label.after(5, count)
  count()

root = tk.Tk()
root.geometry('1366x768+-10+-5')
root.configure(background='yellow')
root.title("Lets Decide!!")

logo = tk.PhotoImage(file="C:/Users/Weirdo!/Pictures/KOXOBiN2.gif")
label = tk.Label(root, compound=tk.LEFT, fg='red', bg='yellow',image=logo)
label.pack()

counter_label(label)

button = tk.Button(root, text='STOP!!', fg='Blue', bg='#00ff22',highlightthickness=1,
			font = ("comic sans ms", 30,'bold'), width=10, borderwidth=3, command=root.destroy)
button.pack()

label2 = tk.Label(root, text="Let's Decide, Now Press The Button Above!!",
			fg='Blue', bg='Yellow' ,font = ("comic sans ms", 35),padx=80, pady=40 )
label2.pack()

root.mainloop()

root = tk.Tk()
root.geometry('1366x768+-10+-5')
root.configure(background='yellow')
root.title("Lets Decide!!")

logo = tk.PhotoImage(file="C:/Users/Weirdo!/Pictures/KOXOBiN.gif")
label = tk.Label(root, 
            compound=tk.LEFT, text=str(counter),font = "Times 300 underline",
            padx=80, fg='red', bg='yellow',image=logo)
label.pack()

place={1:'Okhaldhunga\'s Chop Center!',2:'The Bakery!!',
	 			3:'Hotel Glass: The Black!!!',4:'Explore New One Today!!!!'}
label2 = tk.Label(root, text="We Are Going To... {}".format(place[counter]),
			fg='Blue', bg='Yellow' ,font = ("comic sans ms", 35),padx=10, pady=30 )
label2.pack()

button = tk.Button(root, text='Let\'s Go!!', fg='Blue', bg='#00ff22', highlightthickness=1,
			font = ("comic sans ms", 30, 'bold'), width=10, borderwidth=3,command=root.destroy)
button.pack()

root.mainloop()
