import  customtkinter as ctk

app = ctk.CTk()
app.title("SugarSchedule")
app.geometry("800x500")

#app window grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

#top frame
topFrame= ctk.CTkFrame(app, border_width=1)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)
titleLabel = ctk.CTkLabel(topFrame, text= "SugarSchedule", font= ("Helvetica", 30))
titleLabel.grid(row=0, column=0, sticky="nsew")
homeButtonFrame = ctk.CTkFrame(topFrame)
homeButtonFrame.grid(row=0, column=1, sticky="e", padx=5, pady=5)

#left frame
leftFrame= ctk.CTkFrame(app, border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
leftFrame.grid_rowconfigure(0, weight=1)
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight=1)
leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.grid_columnconfigure(1, weight=1)




#right frame
rightFrame= ctk.CTk(app, border_width=4)
rightFrame.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
rightFrame.grid_rowconfigure(0, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_rowconfigure(2, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_columnconfigure(1, weight=1)




app.mainloop()
