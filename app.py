import  customtkinter as ctk

app = ctk.CTk()
app.title("SugarSchedule")
app.geometry("1000x600")

#app window grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

#top frame
topFrame= ctk.CTkFrame(app, border_width=5, border_color='brown')
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)
titleLabel = ctk.CTkLabel(topFrame, text= "Sweet Orders", text_color='black', font= ("Helvetica", 30))
titleLabel.grid(row=0, column=0, sticky="nsew")
homeButtonFrame = ctk.CTkFrame(topFrame)
homeButtonFrame.grid(row=0, column=1, sticky="e", padx=5, pady=5)
cupcakeButtonFrame = ctk.CTkFrame(topFrame)
cupcakeButtonFrame.grid(row=0, column=0, sticky='w')
#left frame
leftFrame= ctk.CTkFrame(app, border_width=4, border_color="brown")
leftFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
leftFrame.grid_rowconfigure(0, weight=1)
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight=1)
leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.grid_columnconfigure(1, weight=1)
ordersLabel = ctk.CTkLabel(leftFrame, text= "Orders", text_color='black', font= ("Helvetica", 30))
ordersLabel.grid(row=0, column=0, sticky="nw")
saveButtonFrame = ctk.CTkFrame(leftFrame)
saveButtonFrame.grid(row=2, column=0, sticky="e", padx=5, pady=5)

#right frame
rightFrame= ctk.CTkFrame(app, border_width=2, border_color="brown")
rightFrame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
rightFrame.grid_rowconfigure(0, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_rowconfigure(2, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_columnconfigure(1, weight=1)
newOrderLabel = ctk.CTkLabel(rightFrame, text= "New Order", text_color='black', font= ("Helvetica",30))
newOrderLabel.grid(row=0, column=0, sticky="nw")


#frame colouring
topFrame.configure(fg_color='pink')
leftFrame.configure(fg_color='white')
rightFrame.configure(fg_color='white')







app.mainloop()
