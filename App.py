import customtkinter
import tkinter as tk
from tkcalendar import Calendar
from Bot import register
from datetime import datetime


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x450")


frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 60, pady = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(frame, text="AUTO REGISTER", font=("Helvetica", 20))
label.place(x= 55, y= 30)

calender = Calendar(frame, showweeknumbers = False, showothermonthdays = False)
calender.place(x = 510, y=55, width = 300, height = 300)

location = customtkinter.CTkOptionMenu(frame, values=["Richcraft", "Cardel", "Nepean"])
category = customtkinter.CTkOptionMenu(frame, values=["Badminton doubles - adult", "Badminton doubles - all ages", 
                                                      "Badminton - Family", "Open gym", "Open gym - Family", "Open gym - youth", 
                                                      "Badminton - 16+", "Badminton"],
                                                      width = 220)
location.place(x= 30, y = 85)
category.place(x = 30, y = 135)

phone = customtkinter.CTkEntry(frame, width = 190,placeholder_text="Phone Number")
phone.place(x = 30, y = 185)    

name = customtkinter.CTkEntry(frame, width = 190,placeholder_text="Name")
name.place(x = 30, y = 235)    

hour = customtkinter.CTkEntry(frame, width = 50,placeholder_text="Hour")
hour.place(x = 423, y = 300)

minute = customtkinter.CTkEntry(frame, width = 65,placeholder_text="Minute")
minute.place(x = 488, y = 300)

ap = customtkinter.CTkEntry(frame, width = 65,placeholder_text="AM/PM")
ap.place(x = 565, y = 300)

spots = customtkinter.CTkEntry(frame, width = 65, placeholder_text="Spots")
spots.place(x=30, y= 285)
def popup(message):
    popup = customtkinter.CTkToplevel(root)
    label = customtkinter.CTkLabel(popup, text=message)
    label.pack(padx=20, pady=20)
    popup.wm_transient(root)

def getDate():
    date = calender.get_date()
    formatted_date = datetime.strptime(date, "%m/%d/%y").strftime("%B %d, %Y") 
    selected_datetime = datetime.strptime(date, "%m/%d/%y")
    day_of_week = selected_datetime.strftime("%A")
    return day_of_week + " " +formatted_date

def getLocationLink():
    loc = location.get()
    print(loc)
    if loc == "Richcraft":
        return "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
    elif loc == "Cardel":
        return "https://reservation.frontdesksuite.ca/rcfs/cardelrec/Home/Index?Culture=en&PageId=a10d1358-60a7-46b6-b5e9-5b990594b108&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
    else:
        return "https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
def initiate():
    entryLocation = getLocationLink()
    entryName = name.get()
    entryPhone = phone.get()
    entryTime = hour.get() + ":" + minute.get() + " " + ap.get().upper()
    entrySpots = spots.get()
    entryProgram = category.get()
    entryDate = getDate()
    result=register(entryName, entryPhone, entryDate, entryTime, entryProgram, entrySpots, entryLocation)
    popup(result)


submit = customtkinter.CTkButton(frame, text="Submit", command=initiate)
submit.place(x = 60, y=335)

root.mainloop()
