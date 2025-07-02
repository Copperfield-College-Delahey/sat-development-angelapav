import  customtkinter as ctk

#testing different pages
from cupcakeButton import CupcakePage
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
cupcakeButton = ctk.CTkFrame(topFrame)
cupcakeButton.grid(row=0, column=0, sticky='w')
#test
cupcakeButton.pack(side=ctk.LEFT, padx=10)

#frame for changing pages TEST
pageContainer = ctk.CTkFrame(app)
pageContainer.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
pageContainer.grid_rowconfigure(0, weight=1) #single row
pageContainer.grid_columnconfigure(0, weight=1) #single column

#Load CupcakePage class
CupcakePage = page(pageContainer)
CupcakePage.grid(row=0, column=0, sticky="nesw")

#Page-switching function
def show_frame(page_name):
    frames[page_name].tkraise()

    




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
saveButton = ctk.CTkFrame(leftFrame)
saveButton.grid(row=2, column=2, sticky= "e", padx=5, pady=5)


#right frame
rightFrame= ctk.CTkFrame(app, border_width=4, border_color="brown")
rightFrame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
rightFrame.grid_rowconfigure(0, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_rowconfigure(2, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_columnconfigure(1, weight=1)
newOrderLabel = ctk.CTkLabel(rightFrame, text= "New Order", text_color='black', font= ("Helvetica",30))
newOrderLabel.grid(row=0, column=0, sticky="nw")
addButton = ctk.CTkFrame(rightFrame)
addButton.grid(row=2, column=1, sticky="e", padx=5, pady=5)

#frame colouring
topFrame.configure(fg_color='pink')
leftFrame.configure(fg_color='white')
rightFrame.configure(fg_color='white')







app.mainloop()
