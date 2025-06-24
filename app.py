import customtkinter

app = customtkinter.CTk()
app.title("SugarSchedule")
app.geometry("1000x600")


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=4)
app.grid_rowconfigure(0, weight=1)



app.mainloop()
