import customtkinter as ctk
from tkinter import messagebox
import datetime

#main app setup
app = ctk.CTk()
app.title("SugarSchedule")
app.geometry("100x600")

# App window grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

# Top frame
topFrame = ctk.CTkFrame(app, border_width=5, border_color='brown')
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)

titleLabel = ctk.CTkLabel(topFrame, text="🌸 Sugar Schedule 🌸", text_color='black', font=("Helvetica", 30))
titleLabel.grid(row=0, column=0, sticky="nsew")

#Navigation buttons frame
navFrame = ctk.CTkFrame(topFrame)
navFrame.grid(row=0, column=1, sticky="e", padx=5, pady=5)
homeButton = ctk.CTkButton(navFrame, text="Home", command=lambda:show_home())
homeButton.pack(side='left', padx=5)

homeButton = ctk.CTkButton(navFrame, text="🏠 Home", command=lambda: show_home())
homeButton.pack(side='left', padx=5)

addButtion = ctk.CTkButton(navFrame,text="Add Order", command=lambda:show_add_order())
addButtion.pack(side='left', padx=5)

calendarButton =ctk.CTkButtion(navFrame, text='Calendar', command=lambda:show_calendar())


#Left frame

leftFrame= ctk.CTkFrame(app, border_width=4, border_color="brown")
leftFrame.grid(row=1, column=0, sticky"nsew", padx=5, pady=5)
leftFrame.grid_rowconfigure(0, weight=1)
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight=1)
leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.grid_columnconfigure(1, weight=1)

ordersLabel = ctk.CTkLabel(leftFrame, text= "Current Orders", text_color='black', font=("Helvetica, 24"))
ordersLabel.grid(row=0, column=0, columnspan=2,sticky="nw", padx=10, pady=10)

#scroll frame for orders
ordersScrollFrame = ctk.CTkScrollableFrame(leftFrame)
ordersScrollFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

#Right frame- new order form
rightFrame = ctk.CTkFrame(app, border_width=4, border_color="brown")
rightFrame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
rightFrame.grid_rowconfigure(0, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_rowconfigure(2, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_columnconfigure(1, weight=1)

newOrderLabel = ctk.CTkLabel(rightFrame, text= "Add New Order", text_color='black', font=("Helvetica", 24))
newOrderLabel.grid(row=0, column=0, columnspan=2, sticky="nw", padx=10, pady=10)

#Form Frame
formFrame = ctk.CTkFrame(rightFrame)
formFrame.grid(row=1, column=0, columnspan=2, sticky="nsew" padx=10, pady=10)

#entry widgets for the form
name_entry = None
email_entry = None
item_entry = None
quantity_entry = None
deadline_entry = None

#Frame colouring
topFrame.configure(fg_color='pink')
leftFrame.configure(fg_color='white')
rightFrame.configure(fg_color='white')

def show_home():
    refresh_orders_display()
    refresh_form()


#Class for orders
class Order:
    def_init_(self, name, email, item, quantity, deadline):
    self.name = name 
    self.email = email
    self.item = item
    self.quantity = quantity
    self.deadline = deadline
    self.done= False


#save button
save_button = ctk.CTkButton(formFrame, text = "Save Order", fg_color='green', command=save_order)
save_button.pack(pady=20)


#save new order
def save_order():
    name = name_entry.get()
    email = email_entry.get()
    item= item_entry.get()
    quantity = quantity_entry.get()
    deadline = deadline_entry.get()

#to check if all fields are filled out
if not name or not email or not item or not quantity or not deadline:
    messagebox.showerror('Error,' "Please fill in all fields!")
    return

#Create new order and add to list
new_order = Order(name, email, item, quantity, deadline)
all_orders.append(new_order)

messagebox.showinfo("Success", f"Order for {name} saved!")

"Send receipt?"
send_receipt = messagebox.askyesorno("Receipt", "Do you want to send a receipt to the client?")
if send_receipt:
    messagebox.showinfo("Email",f"Receipt would be sent to {email}!")


    