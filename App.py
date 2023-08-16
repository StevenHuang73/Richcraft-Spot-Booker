import customtkinter
import tkinter as tk
from tkcalendar import Calendar
from Bot import register
from datetime import datetime


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x400")


frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 60, pady = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(frame, text="AUTO REGISTER", font=("Helvetica", 20))
label.place(x= 55, y= 30)

calender = Calendar(frame, showweeknumbers = False, showothermonthdays = False)
calender.place(x = 510, y=55, width = 300, height = 300)

category = customtkinter.CTkOptionMenu(frame, values=["Badminton doubles - adult", "Badminton doubles - all ages", 
                                                      "Badminton - Family", "Open gym", "Open gym - Family", "Open gym - youth", "Cardio 50+"],
                                                      width = 220)
category.place(x = 30, y = 85)

phone = customtkinter.CTkEntry(frame, width = 190,placeholder_text="Phone Number")
phone.place(x = 30, y = 135)    

name = customtkinter.CTkEntry(frame, width = 190,placeholder_text="Name")
name.place(x = 30, y = 185)    

hour = customtkinter.CTkEntry(frame, width = 50,placeholder_text="Hour")
hour.place(x = 423, y = 300)

minute = customtkinter.CTkEntry(frame, width = 65,placeholder_text="Minute")
minute.place(x = 488, y = 300)

ap = customtkinter.CTkEntry(frame, width = 65,placeholder_text="AM/PM")
ap.place(x = 565, y = 300)

spots = customtkinter.CTkEntry(frame, width = 65, placeholder_text="Spots")
spots.place(x=30, y= 235)
def popup(message):
    popup = tk.Toplevel(root)
    label = tk.Label(popup, text=message)
    label.pack(padx=20, pady=20)
    
def initiate():
    entryName = name.get()
    entryPhone = phone.get()
    time1 = hour.get() + ":" + minute.get() + " " + ap.get().upper()
    entrySpots = spots.get()
    program1 = category.get()
    date = calender.get_date()
    formatted_date = datetime.strptime(date, "%m/%d/%y").strftime("%B %d, %Y") 
    selected_datetime = datetime.strptime(date, "%m/%d/%y")
    day_of_week = selected_datetime.strftime("%A")
    final_date = day_of_week + " " +formatted_date
    result=register(entryName, entryPhone, final_date, time1, program1, entrySpots)
    popup(result)

submit = customtkinter.CTkButton(frame, text="Submit", command=initiate)
submit.place(x = 60, y=285)

root.mainloop()
