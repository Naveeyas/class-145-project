from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("Driving License")
root.configure(bg="Turquoise")


labelHeading=Label(root,text="Driving License", bg="red")
labelID=Label(root, bg="red")
labelName=Label(root, bg="red")
labelDOB=Label(root, bg="red")
labelAdress=Label(root, bg="red")


def card():
    Name="Naveeyas Das"
    DOB="twenty-fourth March two thousand and eleven"
    ID="1982375"
    Adress="Purva Fountain Square, Marathahalli, Banglore"
    labelName['text']="Name: "+ Name
    labelID['text']="ID "+ ID
    labelDOB['text']="Date of Birth: "+ DOB
    labelAdress['text']="Adress: "+ Adress
    
Details=Button(root,text="Show Details",bg="green", command=card)

Details.place(relx=0.5, rely=0.9, anchor=CENTER)
labelHeading.place(relx=0.5, rely=0.4, anchor=CENTER)
labelName.place(relx=0.5, rely=0.5, anchor=CENTER)
labelID.place(relx=0.5, rely=0.6, anchor=CENTER)
labelAdress.place(relx=0.5, rely=0.7, anchor=CENTER)
labelDOB.place(relx=0.5, rely=0.8, anchor=CENTER)



root.mainloop()