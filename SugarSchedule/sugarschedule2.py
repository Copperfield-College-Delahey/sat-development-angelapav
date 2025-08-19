import customtkinter as ctk
from tkinter import messagebox
import datetime

#Class for orders
class Order:
    def __init__(self, name, email, item, quantity, deadline):
        self.name = name 
        self.email = email
        self.item = item
        self.quantity = quantity
        self.deadline = deadline
        self.done= False

#List to store all orders
all_orders = []

#main app setup
app = ctk.CTk()
app.title("SugarSchedule")
app.geometry("1200x700")

#window grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

#top frame
topFrame = ctk.CTkFrame(app, border_width=5, border_color='brown')
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)

titleLabel = ctk.CTkLabel(topFrame, text="🌸 Sugar Schedule 🌸", text_color='black', font=("Helvetica", 30))
titleLabel.grid(row=0, column=0, sticky="nsew")

#nav buttons frame
navFrame = ctk.CTkFrame(topFrame)
navFrame.grid(row=0, column=1, sticky="e", padx=5, pady=5)

homeButton = ctk.CTkButton(navFrame, text="Home", command=lambda:show_home())
homeButton.pack(side='left', padx=5)

homeButton = ctk.CTkButton(navFrame, text="🏠 Home", command=lambda: show_home())
homeButton.pack(side='left', padx=5)

addButtion = ctk.CTkButton(navFrame,text="Add Order", command=lambda:show_add_order())
addButtion.pack(side='left', padx=5)

calendarButton =ctk.CTkButton(navFrame, text='Calendar', command=lambda:show_calendar())

#left frame -orders display
leftFrame= ctk.CTkFrame(app, border_width=4, border_color="brown")
leftFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
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

#form frame
formFrame = ctk.CTkFrame(rightFrame)
formFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

#entry widgets for form
name_entry = None
email_entry = None
item_entry = None
quantity_entry = None
deadline_entry = None

#form elements
def create_form():
    global name_entry, email_entry, item_entry, quantity_entry, deadline_entry
#got from AI 96-97 line
    for widgets in formFrame.winfo_children():
        widget.destroy()

#Name
ctk.CTkLabel(formFrame, text="Customer Name:", font=("Helvetica",14)).pack(anchor='w',padx=10,pady=(10,5))
name_entry = ctk.CTkEntry(formFrame, placeholder_text="Enter customer name")
name_entry.pack(fill="x", padx=10, pady=(0,10))

ctk.CTkLabel(formFrame, text="Email:", font=("Helvetica",14)).pack(anchor='w',padx=10,pady=(0,5))
email_entry = ctk.CTkEntry(formFrame, placeholder_text="Enter email:")
email_entry.pack(fill="x", padx=10, pady=(0,10))

ctk.CTkLabel(formFrame, text="Item:", font=("Helvetica",14)).pack(anchor='w',padx=10,pady=(0,5))
item_entry = ctk.CTkEntry(formFrame, placeholder_text="Enter description:")
item_entry.pack(fill="x", padx=10, pady=(0,10))

ctk.CTkLabel(formFrame, text="Quantity:", font=("Helvetica",14)).pack(anchor='w',padx=10,pady=(0,5))
quantity_entry = ctk.CTkEntry(formFrame, placeholder_text="Enter quantity:")
quantity_entry.pack(fill="x", padx=10, pady=(0,10))

ctk.CTkLabel(formFrame, text="Deadline, (DD-MM-YYYY):", font=("Helvetica",14)).pack(anchor='w',padx=10,pady=(0,5))
deadline_entry = ctk.CTkEntry(formFrame, placeholder_text="12-3-24")
deadline_entry.pack(fill="x", padx=10, pady=(0,10))

#save button
save_button = ctk.CTkButton(formFrame, text = "Save Order", fg_color='green', command=save_order)
save_button.pack(pady=20)

#Frame colouring
topFrame.configure(fg_color='pink')
leftFrame.configure(fg_color='white')
rightFrame.configure(fg_color='white')

#functions
def show_home():
    refresh_orders_display()
    create_form()

def show_add_order():
    create_form()

def refresh_form():
    if name_entry:
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        item_entry.delete(0, 'end')
        quantity_entry.delete(0, 'end')
        deadline_entry.delete(0, 'end')
#from ai
    def refresh_orders_display():
        #clear existing order displays
        for widget in orderScrollFrame.winfo_children():
            widget.destroy()

        if not all_orders:
            no_order_label = ctk.CTkLabel(ordersScrollFrame, text="No order yet!", font=("Helvetica", 16))
            no_orders_label.pack(pady=20)
            return
        for i, order in enumerate(all_orders):
            order_frame = ctk.CTkFrame(ordersScrollFrame)
            order_frame.pack(fill="x",padx=5, pady=5)

            #order info - have to do

            #status and buttons
            button_frame = ctk.CTkFrame(order_frame)
            button_frame.pack(side="right", padx=10,pady=10)

            status_color = 'green' if order.done else 'orange'
            status_text = 'Completed' if order.done else 'Pending'

            status_button = ctk.CTkButton(button_frame, text=status_text, fg_color = status_color, command=lambda idx=i: toggle_order_status(idx))

            status_button.pack(pady=2)

            delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color='red', command=lambda idx:i: delete_order(idx))
            delete_button.pack(pady=2)
    
    
    def toggle_order_status(index):
        if 0 < index < len(all_orders):
            all_orders[index].done = not all_orders[index].done
            refresh_orders_display()

    def delete_order(index):
        if 0 < index < len(all_orders):
            order = all_orders[index]
            if messagebox.askyesno("Confirm Delete", f"Delete order for {order.name}?"):
                all_orders.pop(index)
                refresh_orders_display()

    #save new order
    def save_order():
        if not all([name_entry, email_entry, item_entry, quantity_entry, deadline_entry]):
            messagebox.showerror("Error", "Form not completed!")
            return
        
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        item= item_entry.get().strip()
        quantity = quantity_entry.get().strip()
        deadline = deadline_entry.get().strip()

        #check if all fields are filled out
        if not all([name, email,item,quantity,deadline]):
            messagebox.showerror('Error', "Please fill in all fields!")
            return
        
        #validate deadline format..-need to do

        #create new order and add to list
        new_order = Order(name, email, item, quantity, deadline)
        all_orders.append(new_order)

        messagebox.showinfo("Success", f"Order for {name} saved!")

        #send receipt?
        send_receipt = messagebox.askyesno("Receipt", "Do you want to send a receipt?")
        if send_receipt:
            messagebox.showinfo("Email", f"Receipt would be sent to {email}!")

        #clear form and refresh display
        refresh_form()
        refresh_orders_display()

        #calendar to organise
    def show_calender():
        today = datetime.date.today()
        urgent_orders = []

        for order in all_orders:
            if not order.done:
                day, month, year = order.deadline.split('-')
                deadline_date = datetime.date(int(year), int(month), int(day))
                days_left = (deadline_date-today).days
                if days_left < 3:
                    urgent_orders.append((order, days_left))
                    (ValueError, AttributeError):
            continue

            if urgent_orders:
                urgent_text = "Urgent Orders"
                for order, days in urgent_orders:
                    if days < 0:
                        urgent_text += f"OVEERDUE: {order.item} for {order.name}\n"
                    elif days ==0:
                        urgent_text += f"DUE TODAY: {order.item} for {order.name}\n"
                    else:
                        urgent_text += f"DUE IN {days}DAYS: {order.item} for {order.name}\n"
                        messagebox.showwarning("Deadline Alert!", urgent_text)
                else:
                    messagebox.showinfo('Calendar', 'No urgent deadlines!')
            def check_deadline_on_start():
                today = datetime.date.today()
                urgent_count = 0

                for order in all_orders:
                    if not order.done:
                        try:
                            day, month, year = order.deadline.split('-')
                            deadline_date = datetime.date(int(date),int(month)int(year))
                            days_left = (deadline_date - today).days

                            if days_left <1:
                                urgent_count +=1
                        except (ValueError, AttributeError):
                            continue
                    
                    if urgent_count > 0:
                        messagebox.showinfo("Startup Alert", f"You have {urgent_count} urgent orders(s) that need attention!")


                create_form()
                refresh_orders_display()
                check_deadline_on_start()



    app.mainloop()


            



