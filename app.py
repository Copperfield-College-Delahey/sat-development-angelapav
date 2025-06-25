import  customtkinter as ctk

app = ctk.CTk()
app.title("SugarSchedule")
app.geometry("900x500")

#app window grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

#top frame
topFrame= ctk.CTkFrame(app, border_width=2)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)
titleLabel = ctk.CTkLabel(topFrame, text= "SugarSchedule", font= ("Helvetica", 40))
titleLabel.grid(row=0, column=0, sticky="nsew")






app.mainloop()
