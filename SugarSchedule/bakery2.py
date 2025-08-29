import customtkinter as ctk
from tkinter import messagebox
import datetime

# Class for orders
class Order:
    def __init__(self, name, email, item, quantity, deadline):
        self.name = name 
        self.email = email
        self.item = item
        self.quantity = quantity
        self.deadline = deadline
        self.done = False

# List to store all orders
all_orders = []

# Class for inventory items
class InventoryItem:
    def __init__(self, name, current_stock, min_stock, unit):
        self.name = name
        self.current_stock = current_stock
        self.min_stock = min_stock
        self.unit = unit
        
    def is_low_stock(self):
        return self.current_stock <= self.min_stock

# List to store inventory
inventory = [
    InventoryItem("Flour", 50, 10, "kg"),
    InventoryItem("Sugar", 30, 5, "kg"), 
    InventoryItem("Butter", 20, 3, "kg"),
    InventoryItem("Eggs", 100, 20, "pieces"),
    InventoryItem("Vanilla Extract", 5, 1, "bottles"),
    InventoryItem("Chocolate Chips", 15, 3, "bags"),
    InventoryItem("Strawberries", 8, 2, "kg"),
    InventoryItem("Cream", 12, 2, "liters")
]

# Color Palette
PINK = "#FFB6C1"
LIGHT_PINK = "#FFCCCB"
HOT_PINK = "#FF69B4"
WHITE = "#FFFFFF"
CREAM = "#FFF8DC"
LAVENDER = "#E6E6FA"
SOFT_PURPLE = "#DDA0DD"

# Main app setup
app = ctk.CTk()
app.title("🎀 SugarSchedule 🎀")
app.geometry("1400x800")
app.configure(fg_color=LIGHT_PINK)

# Current page state
current_page = "home"

# Main container frame
main_frame = ctk.CTkFrame(app, fg_color=LIGHT_PINK)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Header frame (always visible)
header_frame = ctk.CTkFrame(main_frame, height=120, fg_color=HOT_PINK, corner_radius=20)
header_frame.pack(fill="x", padx=10, pady=(10, 20))
header_frame.pack_propagate(False)

# Title
title_label = ctk.CTkLabel(
    header_frame, 
    text="🎀 SugarSchedule Bakery 🎀\n", 
    font=("Comic Sans MS", 32, "bold"), 
    text_color=WHITE
)
title_label.pack(pady=20)

# Navigation frame
nav_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
nav_frame.pack(pady=(0, 10))

# Content frame (changes based on page)
content_frame = ctk.CTkFrame(main_frame, fg_color=CREAM, corner_radius=20)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Global form variables
name_entry = None
email_entry = None
item_entry = None
quantity_entry = None
deadline_entry = None
#from ai
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_home_page():
    global current_page
    current_page = "home"
    clear_content()
    
    # Welcome message
    welcome_frame = ctk.CTkFrame(content_frame, fg_color=WHITE, corner_radius=15)
    welcome_frame.pack(fill="x", padx=30, pady=30)
    
    welcome_text = ctk.CTkLabel(
        welcome_frame,
        text="🌸 Welcome to SugarSchedule! 🌸\n",
        font=("Comic Sans MS", 24, "bold"),
        text_color=HOT_PINK
    )
    welcome_text.pack(pady=30)
    
    # Quick stats
    stats_frame = ctk.CTkFrame(content_frame, fg_color=LAVENDER, corner_radius=15)
    stats_frame.pack(fill="x", padx=30, pady=20)
    
    pending_orders = len([o for o in all_orders if not o.done])
    completed_orders = len([o for o in all_orders if o.done])
    
    stats_text = ctk.CTkLabel(
        stats_frame,
        text=f"🧁 Total Orders: {len(all_orders)} | 📝 Pending: {pending_orders} | ✅ Completed: {completed_orders} 🧁",
        font=("Comic Sans MS", 18),
        text_color="purple"
    )
    stats_text.pack(pady=20)
    
    # Action buttons grid
    buttons_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    buttons_frame.pack(expand=True, fill="both", padx=30, pady=20)
    
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_rowconfigure(0, weight=1)
    buttons_frame.grid_rowconfigure(1, weight=1)
    
    # Add Order Button
    add_btn = ctk.CTkButton(
        buttons_frame,
        text="🍰 Add New Order 🍰\n✨ Create Sweet Magic ✨",
        font=("Comic Sans MS", 20, "bold"),
        fg_color=HOT_PINK,
        hover_color=SOFT_PURPLE,
        height=150,
        corner_radius=20,
        command=show_add_order_page
    )
    add_btn.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # View Orders Button
    view_btn = ctk.CTkButton(
        buttons_frame,
        text="📋 View All Orders 📋\n🎂 Sweet Creations List 🎂",
        font=("Comic Sans MS", 20, "bold"),
        fg_color="#9370DB",
        hover_color="#8A2BE2",
        height=150,
        corner_radius=20,
        command=show_orders_page
    )
    view_btn.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    
    # Calendar Button
    calendar_btn = ctk.CTkButton(
        buttons_frame,
        text="📅 Check Calendar 📅\n⏰ Urgent Deadlines ⏰",
        font=("Comic Sans MS", 20, "bold"),
        fg_color="#FF1493",
        hover_color="#DC143C",
        height=150,
        corner_radius=20,
        command=show_calendar
    )
    calendar_btn.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    
    # Inventory Button
    inventory_btn = ctk.CTkButton(
        buttons_frame,
        text="🥄 Sweet Inventory 🥄\n📦 Track Ingredients 📦",
        font=("Comic Sans MS", 20, "bold"),
        fg_color="#DA70D6",
        hover_color="#BA55D3",
        height=150,
        corner_radius=20,
        command=show_inventory_page
    )
    inventory_btn.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

def show_add_order_page():
    global current_page, name_entry, email_entry, item_entry, quantity_entry, deadline_entry
    current_page = "add_order"
    clear_content()
    
    # Home button for this page
    home_page_btn = ctk.CTkButton(
        content_frame,
        text="🏠",
        font=("Comic Sans MS", 16, "bold"),
        fg_color=HOT_PINK,
        hover_color=SOFT_PURPLE,
        corner_radius=20,
        command=show_home_page
    )
    home_page_btn.pack(pady=10, padx=20, anchor="w")
    
    # Page title
    title = ctk.CTkLabel(
        content_frame,
        text="🍰 Add New Sweet Order 🍰",
        font=("Comic Sans MS", 28, "bold"),
        text_color=HOT_PINK
    )
    title.pack(pady=20)
    
    # Form frame
    form_frame = ctk.CTkFrame(content_frame, fg_color=WHITE, corner_radius=15)
    form_frame.pack(fill="both", expand=True, padx=40, pady=20)
    
    # Create form in a scrollable frame
    scroll_frame = ctk.CTkScrollableFrame(form_frame, fg_color="transparent")
    scroll_frame.pack(fill="both", expand=True, padx=30, pady=30)
    
    # Customer Name
    ctk.CTkLabel(scroll_frame, text="👤 Customer Name:", font=("Comic Sans MS", 16, "bold"), text_color=HOT_PINK).pack(anchor='w', pady=(10, 5))
    name_entry = ctk.CTkEntry(scroll_frame, placeholder_text="Enter customer name ✨", font=("Comic Sans MS", 12), height=35)
    name_entry.pack(fill="x", pady=(0, 15))
    
    # Email
    ctk.CTkLabel(scroll_frame, text="📧 Email:", font=("Comic Sans MS", 16, "bold"), text_color=HOT_PINK).pack(anchor='w', pady=(0, 5))
    email_entry = ctk.CTkEntry(scroll_frame, placeholder_text="sweetcustomer@email.com 💌", font=("Comic Sans MS", 12), height=35)
    email_entry.pack(fill="x", pady=(0, 15))
    
    # Item
    ctk.CTkLabel(scroll_frame, text="🧁 Sweet Item:", font=("Comic Sans MS", 16, "bold"), text_color=HOT_PINK).pack(anchor='w', pady=(0, 5))
    item_entry = ctk.CTkEntry(scroll_frame, placeholder_text="Describe the magical creation 🎂", font=("Comic Sans MS", 12), height=35)
    item_entry.pack(fill="x", pady=(0, 15))
    
    # Quantity
    ctk.CTkLabel(scroll_frame, text="🔢 Quantity:", font=("Comic Sans MS", 16, "bold"), text_color=HOT_PINK).pack(anchor='w', pady=(0, 5))
    quantity_entry = ctk.CTkEntry(scroll_frame, placeholder_text="How many sweet treats? 🍪", font=("Comic Sans MS", 12), height=35)
    quantity_entry.pack(fill="x", pady=(0, 15))
    
    # Deadline
    ctk.CTkLabel(scroll_frame, text="📅 Sweet Deadline (DD-MM-YYYY):", font=("Comic Sans MS", 16, "bold"), text_color=HOT_PINK).pack(anchor='w', pady=(0, 5))
    deadline_entry = ctk.CTkEntry(scroll_frame, placeholder_text="25-12-2024 🎄", font=("Comic Sans MS", 12), height=35)
    deadline_entry.pack(fill="x", pady=(0, 20))
    

    # Save button
    save_btn = ctk.CTkButton(
        scroll_frame,
        text="💖 Save Order 💖",
        font=("Comic Sans MS", 18, "bold"),
        fg_color="#32CD32",
        hover_color="#228B22",
        height=50,
        corner_radius=25,
        command=save_order
    )
    save_btn.pack(pady=20)

def show_orders_page():
    global current_page
    current_page = "orders"
    clear_content()
    
    # Home button for this page
    home_page_btn = ctk.CTkButton(
        content_frame,
        text="🏠",
        font=("Comic Sans MS", 16, "bold"),
        fg_color=HOT_PINK,
        hover_color=SOFT_PURPLE,
        corner_radius=20,
        command=show_home_page
    )
    home_page_btn.pack(pady=10, padx=20, anchor="w")
    
    # Page title
    title = ctk.CTkLabel(
        content_frame,
        text="📋 All Sweet Orders 📋",
        font=("Comic Sans MS", 28, "bold"),
        text_color=HOT_PINK
    )
    title.pack(pady=20)
    
    # Orders container
    orders_container = ctk.CTkScrollableFrame(content_frame, fg_color=WHITE, corner_radius=15)
    orders_container.pack(fill="both", expand=True, padx=20, pady=20)
    
    if not all_orders:
        no_orders = ctk.CTkLabel(
            orders_container,
            text=" No orders yet! \n",
            font=("Comic Sans MS", 20),
            text_color=SOFT_PURPLE
        )
        no_orders.pack(pady=50)
        return
    
    for i, order in enumerate(all_orders):
        # Order card
        order_card = ctk.CTkFrame(orders_container, fg_color=LAVENDER, corner_radius=15)
        order_card.pack(fill="x", padx=10, pady=10)
        
        # Order info
        info_frame = ctk.CTkFrame(order_card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=20, pady=15)
        
        customer_label = ctk.CTkLabel(info_frame, text=f"👤 {order.name}", font=("Comic Sans MS", 16, "bold"), text_color="purple")
        customer_label.pack(anchor="w")
        
        details = f"📧 {order.email}\n {order.item}\n Quantity: {order.quantity}\n📅 Due: {order.deadline}"
        details_label = ctk.CTkLabel(info_frame, text=details, font=("Comic Sans MS", 12), text_color="darkblue", justify="left")
        details_label.pack(anchor="w", pady=(5, 0))
        
        # Buttons
        btn_frame = ctk.CTkFrame(order_card, fg_color="transparent")
        btn_frame.pack(side="right", padx=20, pady=15)
        
        status_color = '#32CD32' if order.done else '#FF8C00'
        status_text = '✅ Complete!' if order.done else '⏳ Pending'
        status_emoji = '🎉' if order.done else '👩‍🍳'
        
        status_btn = ctk.CTkButton(
            btn_frame,
            text=f"{status_emoji} {status_text}",
            fg_color=status_color,
            font=("Comic Sans MS", 12, "bold"),
            width=120,
            height=35,
            command=lambda idx=i: toggle_order_status(idx)
        )
        status_btn.pack(pady=2)
        
        delete_btn = ctk.CTkButton(
            btn_frame,
            text="🗑️ Delete",
            fg_color='#DC143C',
            font=("Comic Sans MS", 12, "bold"),
            width=120,
            height=35,
            command=lambda idx=i: delete_order(idx)
        )
        delete_btn.pack(pady=2)

def show_inventory_page():
    global current_page
    current_page = "inventory"
    clear_content()
    
    # Home button for this page
    home_page_btn = ctk.CTkButton(
        content_frame,
        text="🏠",
        font=("Comic Sans MS", 16, "bold"),
        fg_color=HOT_PINK,
        hover_color=SOFT_PURPLE,
        corner_radius=20,
        command=show_home_page
    )
    home_page_btn.pack(pady=10, padx=20, anchor="w")
    
    # Page title
    title = ctk.CTkLabel(
        content_frame,
        text="🥄 Inventory Tracker 🥄",
        font=("Comic Sans MS", 28, "bold"),
        text_color=HOT_PINK
    )
    title.pack(pady=20)
    
    # Quick stats
    low_stock_count = len([item for item in inventory if item.is_low_stock()])
    stats_frame = ctk.CTkFrame(content_frame, fg_color=LAVENDER, corner_radius=15)
    stats_frame.pack(fill="x", padx=30, pady=10)
    
    stats_text = ctk.CTkLabel(
        stats_frame,
        text=f"📦 Total Items: {len(inventory)} | ⚠️ Low Stock Alerts: {low_stock_count} 📦",
        font=("Comic Sans MS", 16, "bold"),
        text_color="purple"
    )
    stats_text.pack(pady=15)
    
    # Add new item button
    add_item_btn = ctk.CTkButton(
        content_frame,
        text="➕ Add New Ingredient ➕",
        font=("Comic Sans MS", 14, "bold"),
        fg_color="#32CD32",
        hover_color="#228B22",
        corner_radius=15,
        command=show_add_inventory_form
    )
    add_item_btn.pack(pady=10)
    
    # Inventory list
    inventory_container = ctk.CTkScrollableFrame(content_frame, fg_color=WHITE, corner_radius=15)
    inventory_container.pack(fill="both", expand=True, padx=20, pady=20)
    
    if not inventory:
        no_items = ctk.CTkLabel(
            inventory_container,
            text="📦 No ingredients yet! \n✨ Time to stock up on sweet supplies! ✨",
            font=("Comic Sans MS", 18),
            text_color=SOFT_PURPLE
        )
        no_items.pack(pady=50)
        return
    #sister help 
    for i, item in enumerate(inventory):
        # Item card
        card_color = "#FFE4E1" if item.is_low_stock() else LAVENDER
        item_card = ctk.CTkFrame(inventory_container, fg_color=card_color, corner_radius=15)
        item_card.pack(fill="x", padx=10, pady=8)
        
        # Item info
        info_frame = ctk.CTkFrame(item_card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=20, pady=15)
        
        # Item name with low stock warning
        name_text = f"🥄 {item.name}"
        if item.is_low_stock():
            name_text += " ⚠️ LOW STOCK!"
        
        name_label = ctk.CTkLabel(info_frame, text=name_text, font=("Comic Sans MS", 16, "bold"), text_color="purple")
        name_label.pack(anchor="w")
        
        details = f"Current: {item.current_stock} {item.unit}\n📉 Minimum: {item.min_stock} {item.unit}"
        details_label = ctk.CTkLabel(info_frame, text=details, font=("Comic Sans MS", 12), text_color="darkblue", justify="left")
        details_label.pack(anchor="w", pady=(5, 0))
        
        # Buttons
        btn_frame = ctk.CTkFrame(item_card, fg_color="transparent")
        btn_frame.pack(side="right", padx=20, pady=15)
        
        # Update stock buttons
        update_frame = ctk.CTkFrame(btn_frame, fg_color="transparent")
        update_frame.pack()
        
        minus_btn = ctk.CTkButton(
            update_frame,
            text="➖",
            width=40,
            height=30,
            fg_color="#FF6347",
            font=("Comic Sans MS", 14, "bold"),
            command=lambda idx=i: update_stock(idx, -1)
        )
        minus_btn.pack(side="left", padx=2)
        
        plus_btn = ctk.CTkButton(
            update_frame,
            text="➕",
            width=40,
            height=30,
            fg_color="#32CD32",
            font=("Comic Sans MS", 14, "bold"),
            command=lambda idx=i: update_stock(idx, 1)
        )
        plus_btn.pack(side="left", padx=2)
        
        # Edit button
        edit_btn = ctk.CTkButton(
            btn_frame,
            text="✏️ Edit",
            width=80,
            height=30,
            fg_color="#4169E1",
            font=("Comic Sans MS", 10, "bold"),
            command=lambda idx=i: edit_inventory_item(idx)
        )
        edit_btn.pack(pady=(5, 0))
        
        # Delete button
        delete_btn = ctk.CTkButton(
            btn_frame,
            text="🗑️ Delete",
            width=80,
            height=30,
            fg_color='#DC143C',
            font=("Comic Sans MS", 10, "bold"),
            command=lambda idx=i: delete_inventory_item(idx)
        )
        delete_btn.pack(pady=2)

# Navigation functions
def show_calendar():
    today = datetime.date.today()
    urgent_orders = []
    #breakpoint() -This breakpoit was used to test if once the check calendar button was pressed there was messagebox popup for any orders. Successful.
    for order in all_orders:
        if not order.done:
            try:
                day, month, year = order.deadline.split('-')
                deadline_date = datetime.date(int(year), int(month), int(day))
                days_left = (deadline_date - today).days
                if days_left <= 3:
                    urgent_orders.append((order, days_left))
            except (ValueError, AttributeError):
                continue

    if urgent_orders:
        urgent_text = "🚨 Urgent Sweet Orders! 🚨\n\n"
        for order, days in urgent_orders:
            if days < 0:
                urgent_text += f"💥 OVERDUE: {order.item} for {order.name} 💥\n"
            elif days == 0:
                urgent_text += f"⏰ DUE TODAY: {order.item} for {order.name} ⏰\n"
            else:
                urgent_text += f"⚡ DUE IN {days} DAY(S): {order.item} for {order.name} ⚡\n"
        messagebox.showwarning("🎀 Deadline Alert! 🎀", urgent_text)
    else:
        messagebox.showinfo('📅 Calendar Check 📅', '🌸 No urgent deadlines! Everything is sweet! 🌸')

def toggle_order_status(index):
    if 0 <= index < len(all_orders):
        all_orders[index].done = not all_orders[index].done
        if current_page == "orders":
            show_orders_page()
#breakpoint() - used to test if the breakpoint() would still run- didn't and fixed this error through pressing n to continue to the next line of code.

def delete_order(index):
    if 0 <= index < len(all_orders):
        order = all_orders[index]
        if messagebox.askyesno("🗑️ Confirm Delete 🗑️", f"Delete sweet order for {order.name}?"):
            all_orders.pop(index)
            if current_page == "orders":
                show_orders_page()

def validate_deadline(deadline_str):
    try:
        day, month, year = deadline_str.split('-')
        datetime.date(int(year), int(month), int(day))
        return True
    except (ValueError, AttributeError):
        return False


def save_order():
    if not all([name_entry, email_entry, item_entry, quantity_entry, deadline_entry]):
        messagebox.showerror("💔 Error", "Form not ready! Try again! 💔")
        return
    
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    item = item_entry.get().strip()
    quantity = quantity_entry.get().strip()
    deadline = deadline_entry.get().strip()

    if not all([name, email, item, quantity, deadline]):
        messagebox.showerror('💔 Oopsie!', "Please fill in all the sweet fields! 🌸")
        return
    
    if not validate_deadline(deadline):
        messagebox.showerror('📅 Date Error!', "Invalid deadline format! Please use DD-MM-YYYY format! ✨")
        return

    new_order = Order(name, email, item, quantity, deadline)
    all_orders.append(new_order)

    messagebox.showinfo("🎉 Success! 🎉", f"Sweet order for {name} saved! 💖")

    send_receipt = messagebox.askyesno("💌 Receipt", "Send a sweet receipt? 🎀")
    if send_receipt:
        messagebox.showinfo("📧 Email", "Sweet receipt sent to {email}! ✨".format(email=email))

    # Clear form
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end') 
    item_entry.delete(0, 'end')
    quantity_entry.delete(0, 'end')
    deadline_entry.delete(0, 'end')

def update_stock(index, change):
    if 0 <= index < len(inventory):
        inventory[index].current_stock += change
        if inventory[index].current_stock < 0:
            inventory[index].current_stock = 0
        if current_page == "inventory":
            show_inventory_page()

def delete_inventory_item(index):
    if 0 <= index < len(inventory):
        item = inventory[index]
        if messagebox.askyesno("🗑️ Confirm Delete 🗑️", f"Delete {item.name} from inventory? "):
            inventory.pop(index)
            if current_page == "inventory":
                show_inventory_page()

def edit_inventory_item(index):
    if 0 <= index < len(inventory):
        item = inventory[index]
        # Simple edit - just update stock amount
        new_stock = ctk.CTkInputDialog(
            text=f" Update stock for {item.name}\nCurrent: {item.current_stock} {item.unit}",
            title="✏️ Edit Ingredient"
        ).get_input()
        
        if new_stock:
            try:
                inventory[index].current_stock = int(float(new_stock))
                messagebox.showinfo("✅ Updated!", f"Stock updated for {item.name}! 🎉")
                if current_page == "inventory":
                    show_inventory_page()
            except ValueError:
                messagebox.showerror("💔 Error", "Please enter a valid number! 🔢")

def show_add_inventory_form():
    # Create popup window for adding new inventory item
    popup = ctk.CTkToplevel(app)
    popup.title("➕ Add Sweet Ingredient")
    popup.geometry("400x500")
    popup.configure(fg_color=LIGHT_PINK)
    
    # Center the popup
    popup.transient(app)
    popup.grab_set()
    
    title = ctk.CTkLabel(popup, text="🥄 Add New Ingredient 🥄", font=("Comic Sans MS", 20, "bold"), text_color=HOT_PINK)
    title.pack(pady=20)
    
    form_frame = ctk.CTkFrame(popup, fg_color=WHITE, corner_radius=15)
    form_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Name
    ctk.CTkLabel(form_frame, text="🏷️ Ingredient Name:", font=("Comic Sans MS", 14, "bold"), text_color=HOT_PINK).pack(anchor='w', padx=20, pady=(20, 5))
    name_input = ctk.CTkEntry(form_frame, placeholder_text="e.g., Rainbow Sprinkles ✨", font=("Comic Sans MS", 12))
    name_input.pack(fill="x", padx=20, pady=(0, 10))
    
    # Current Stock
    ctk.CTkLabel(form_frame, text="📊 Current Stock:", font=("Comic Sans MS", 14, "bold"), text_color=HOT_PINK).pack(anchor='w', padx=20, pady=(0, 5))
    stock_input = ctk.CTkEntry(form_frame, placeholder_text="How much do you have? 🔢", font=("Comic Sans MS", 12))
    stock_input.pack(fill="x", padx=20, pady=(0, 10))
    
    # Minimum Stock
    ctk.CTkLabel(form_frame, text="📉 Minimum Stock Alert:", font=("Comic Sans MS", 14, "bold"), text_color=HOT_PINK).pack(anchor='w', padx=20, pady=(0, 5))
    min_input = ctk.CTkEntry(form_frame, placeholder_text="Alert when below this amount ⚠️", font=("Comic Sans MS", 12))
    min_input.pack(fill="x", padx=20, pady=(0, 10))
    
    # Unit
    ctk.CTkLabel(form_frame, text="📏 Unit:", font=("Comic Sans MS", 14, "bold"), text_color=HOT_PINK).pack(anchor='w', padx=20, pady=(0, 5))
    unit_input = ctk.CTkEntry(form_frame, placeholder_text="kg, liters, pieces, bags... 📦", font=("Comic Sans MS", 12))
    unit_input.pack(fill="x", padx=20, pady=(0, 20))
    
    def save_new_item():
        name = name_input.get().strip()
        current = stock_input.get().strip()
        minimum = min_input.get().strip()
        unit = unit_input.get().strip()
        
        if not all([name, current, minimum, unit]):
            messagebox.showerror("💔 Oopsie!", "Please fill all fields! 🌸")
            return
            
        try:
            current_stock = int(float(current))
            min_stock = int(float(minimum))
            new_item = InventoryItem(name, current_stock, min_stock, unit)
            inventory.append(new_item)
            messagebox.showinfo("🎉 Success!", f"Added {name} to inventory! 💖")
            popup.destroy()
            if current_page == "inventory":
                show_inventory_page()
        except ValueError:
            messagebox.showerror(" Number Error!", "Stock amounts must be numbers! ✨")
    
    # Save button
    save_btn = ctk.CTkButton(
        form_frame,
        text="💖 Add to Inventory 💖",
        font=("Comic Sans MS", 16, "bold"),
        fg_color="#32CD32",
        hover_color="#228B22",
        height=45,
        corner_radius=20,
        command=save_new_item
    )
    save_btn.pack(pady=20)
    
    # Cancel button
    cancel_btn = ctk.CTkButton(
        form_frame,
        text="❌ Cancel",
        font=("Comic Sans MS", 14, "bold"),
        fg_color="#DC143C",
        hover_color="#B22222",
        height=35,
        corner_radius=15,
        command=popup.destroy
    )
    cancel_btn.pack(pady=(0, 20))

def check_deadline_on_start():
    today = datetime.date.today()
    urgent_count = 0

    for order in all_orders:
        if not order.done:
            try:
                day, month, year = order.deadline.split('-')
                deadline_date = datetime.date(int(year), int(month), int(day))
                days_left = (deadline_date - today).days
                if days_left <= 1:
                    urgent_count += 1
            except (ValueError, AttributeError):
                continue
    
    if urgent_count > 0:
        messagebox.showinfo(" Alert! ", f"You have {urgent_count} urgent sweet order(s)! Time to get baking! 🧁")

# Create navigation buttons
home_btn = ctk.CTkButton(
    nav_frame,
    text="🏠",
    font=("Comic Sans MS", 14, "bold"),
    fg_color=WHITE,
    text_color=HOT_PINK,
    hover_color=LIGHT_PINK,
    corner_radius=20,
    command=show_home_page
)
home_btn.pack(side='left', padx=10)

add_btn = ctk.CTkButton(
    nav_frame,
    text="🍰 Add Order",
    font=("Comic Sans MS", 14, "bold"),
    fg_color=WHITE,
    text_color=HOT_PINK,
    hover_color=LIGHT_PINK,
    corner_radius=20,
    command=show_add_order_page
)
add_btn.pack(side='left', padx=10)

orders_btn = ctk.CTkButton(
    nav_frame,
    text="📋 View Orders",
    font=("Comic Sans MS", 14, "bold"),
    fg_color=WHITE,
    text_color=HOT_PINK,
    hover_color=LIGHT_PINK,
    corner_radius=20,
    command=show_orders_page
)
orders_btn.pack(side='left', padx=10)

inventory_btn = ctk.CTkButton(
    nav_frame,
    text="🥄 Inventory",
    font=("Comic Sans MS", 14, "bold"),
    fg_color=WHITE,
    text_color=HOT_PINK,
    hover_color=LIGHT_PINK,
    corner_radius=20,
    command=show_inventory_page
)
inventory_btn.pack(side='left', padx=10)

calendar_btn = ctk.CTkButton(
    nav_frame,
    text="📅 Calendar",
    font=("Comic Sans MS", 14, "bold"),
    fg_color=WHITE,
    text_color=HOT_PINK,
    hover_color=LIGHT_PINK,
    corner_radius=20,
    command=show_calendar
)
calendar_btn.pack(side='left', padx=10)


check_deadline_on_start()
show_home_page()

# Start the app
app.mainloop()