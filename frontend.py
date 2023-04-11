from functools import partial
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root', #your username
    password='Rachit_0033', #your password
    database='Grading_Man_Sys'
)

window = Tk()
window.update()
window.configure(bg='#292841')
window.title("GRADING MANAGEMENT SYSTEM")
mycursor = db.cursor() 

def result1(txt1,txt2):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL viewSGrades('"+txt1+"','"+txt2+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    


def viewSgradesscreen():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="View Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl2 = Label(window, text="Student ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5)) 

    lbl1 = Label(window, text="Course ID",font=("Arial", 13))
    lbl1.configure(bg='#292841',fg='white')
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5)) 

    def submit1():
        str1=txt1.get()
        str2=txt2.get()
        for widget in window.winfo_children():
            widget.destroy()
        result1(str1,str2)
        
    btn = Button(window, text="Submit", command=submit1)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))


def result2(txt1):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL viewSCourses('"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def viewScourses():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="View courses",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Student ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5)) 

    def submit2():
        str1=txt1.get()
        for widget in window.winfo_children():
            widget.destroy()
        result2(str1)
        
    btn = Button(window, text="Submit", command=submit2)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result3(txt1):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL viewStudPerf('"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def viewCourperformance(): 
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="View Course Performance",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Student ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5))
    def submit3():
        str1=txt1.get()
        for widget in window.winfo_children():
            widget.destroy()
        result3(str1)
        
    btn = Button(window, text="Submit", command=submit3)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result4(txt1,txt2,txt3):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL UpdateStud('"+txt1+"','"+txt2+"','"+txt3+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop()  
    


def updatedetails():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Update Details",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Student ID(Existing)",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5)) 
    lbl2 = Label(window, text="Name",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=30)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="System Password",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=30)
    txt3.pack(pady=(2, 5)) 

    def submit4():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        for widget in window.winfo_children():
            widget.destroy()
        result4(str1,str2,str3)
        
    btn = Button(window, text="Submit", command=submit4)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        studenthomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result5(txt1,txt2):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))
    
    
    mycursor.execute("CALL viewTGrades('"+txt2+"','"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop()  
    

def viewTgradesscreen():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="View Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5)) 

    def submit5():
        str1=txt1.get()
        str2=txt2.get()
        for widget in window.winfo_children():
            widget.destroy()
        result5(str1,str2)
        
    btn = Button(window, text="Submit", command=submit5)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result6(txt1):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL viewTCourses('"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    


def viewTcourses():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="View courses",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))

    def submit6():
        str1=txt1.get()
        for widget in window.winfo_children():
            widget.destroy()
        result6(str1)
        
    btn = Button(window, text="Submit", command=submit6)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result7(txt1,txt2,txt3,txt4):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL addGradeAS1('"+txt2+"','"+txt3+"','"+txt1+"','"+txt4+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def addAS1gradescreen():
    window.geometry("700x500")
    window.resizable(False, False)
    lbl = Label(window, text="Add Assignment-1 Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Student ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=4)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Grade in Assignment-1",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit7():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        str4=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result7(str1,str2,str3,str4)
        
    btn = Button(window, text="Submit", command=submit7)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result8(txt1,txt2,txt3,txt4):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL addGradeAS2('"+txt2+"','"+txt3+"','"+txt1+"','"+txt4+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop()
    

def addAS2gradescreen():
    window.geometry("700x500")
    window.resizable(False, False)
    lbl = Label(window, text="Add Assignment-2 Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Student ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=4)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Grade in Assignment-2",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit8():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        str4=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result8(str1,str2,str3,str4)
        
    btn = Button(window, text="Submit", command=submit8)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result9(txt1,txt2,txt3,txt4):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL addGradeMS('"+txt2+"','"+txt3+"','"+txt1+"','"+txt4+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop()
    


def addMSgradescreen():
    window.geometry("700x500")
    window.resizable(False, False)
    lbl = Label(window, text="Add Midsem Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Student ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=4)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Grade in Midsem",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit9():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        str4=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result9(str1,str2,str3,str4)
        
    btn = Button(window, text="Submit", command=submit9)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result10(txt1,txt2,txt3,txt4):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL addGradeES('"+txt2+"','"+txt3+"','"+txt1+"','"+txt4+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def addESgradescreen():
    window.geometry("700x500")
    window.resizable(False, False)
    lbl = Label(window, text="Add Endsem Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Student ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=4)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Grade in Endsem",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit10():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        str4=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result10(str1,str2,str3,str4)
        
    btn = Button(window, text="Submit", command=submit10)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result11(txt1,txt2,txt3,txt4):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL addGradeFG('"+txt2+"','"+txt3+"','"+txt1+"','"+txt4+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop()
    

def addFinalgradescreen():
    window.geometry("700x500")
    window.resizable(False, False)
    lbl = Label(window, text="Add Final Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()  

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5))
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Student ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=4)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Final Grade",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit11():
        str1=txt1.get()
        str2=txt2.get()
        str3=txt3.get()
        str4=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result11(str1,str2,str3,str4)
        
    btn = Button(window, text="Submit", command=submit11)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result12(txt1,txt2):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL PerformanceRep('"+txt1+"','"+txt2+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def viewperformance():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Performance Reports",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Student ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5)) 
    lbl2 = Label(window, text="Course ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5)) 

    def submit12():
        str1=txt1.get()
        str2=txt2.get()
        for widget in window.winfo_children():
            widget.destroy()
        result12(str1,str2)
        
    btn = Button(window, text="Submit", command=submit12)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result13(txt1,txt2):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL RemoveTeac('"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    


def delprofile():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Profile Delete",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack() 

    lbl = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack(pady=(2, 5)) 

    def submit13():
        str1=txt1.get()
        for widget in window.winfo_children():
            widget.destroy()
        result13(str1)
        
    btn = Button(window, text="Submit", command=submit13)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result14(txt1,txt2,txt3):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL ListStudent('"+txt2+"','"+txt1+"','"+txt3+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    
    

def comparegrades():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Compare Grades",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl2 = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Course ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=3)
    txt3.pack(pady=(2, 5))
    lbl4 = Label(window, text="Comparing Grade",font=("Arial", 13))
    lbl4.configure(bg='#292841',fg='white')
    lbl4.config(anchor=CENTER)
    lbl4.pack()
    txt4 = Entry(window, width=1)
    txt4.pack(pady=(2, 5)) 

    def submit14():
        str1=txt2.get()
        str2=txt3.get()
        str3=txt4.get()
        for widget in window.winfo_children():
            widget.destroy()
        result14(str1,str2,str3)
        
    btn = Button(window, text="Submit", command=submit14)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def result15(txt1,txt2):
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Result",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Home", command=back)
    btn.pack(pady=(10, 0))

    
    mycursor.execute("CALL LowestGrade('"+txt2+"','"+txt1+"')")
    myresult = mycursor.fetchall() 
    result_label = Label(window, text = myresult) 
    result_label.pack()
    window.mainloop() 
    

def lowestgrade():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Lowest Grade in Course",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl2 = Label(window, text="Teacher ID",font=("Arial", 13))
    lbl2.configure(bg='#292841',fg='white')
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    txt2 = Entry(window, width=3)
    txt2.pack(pady=(2, 5))
    lbl3 = Label(window, text="Course ID",font=("Arial", 13))
    lbl3.configure(bg='#292841',fg='white')
    lbl3.config(anchor=CENTER)
    lbl3.pack()
    txt3 = Entry(window, width=3)
    txt3.pack(pady=(2, 5)) 

    def submit15():
        str1=txt2.get()
        str2=txt3.get()
        for widget in window.winfo_children():
            widget.destroy()
        result15(str1,str2)
        
    btn = Button(window, text="Submit", command=submit15)
    btn.pack(pady=(10, 0))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="Back", command=back)
    btn.pack(pady=(10, 0))

def teacherhomepagescreen():
    window.geometry("800x600")
    window.resizable(False, False)
    lbl = Label(window, text="Welcome Teacher",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def viewcourses():
        for widget in window.winfo_children():
                widget.destroy()
        viewTcourses() 
    
    def viewgrades():
        for widget in window.winfo_children():
                widget.destroy()
        viewTgradesscreen()
    
    def addgrade1(): 
        for widget in window.winfo_children():
                widget.destroy()
        addAS1gradescreen() 

    def addgrade2(): 
        for widget in window.winfo_children():
                widget.destroy()
        addAS2gradescreen()

    def addgrade3(): 
        for widget in window.winfo_children():
                widget.destroy()
        addMSgradescreen() 

    def addgrade4(): 
        for widget in window.winfo_children():
                widget.destroy()
        addESgradescreen() 

    def addgrade5(): 
        for widget in window.winfo_children():
                widget.destroy()
        addFinalgradescreen() 

    def viewstudperformance():
        for widget in window.winfo_children():
                widget.destroy()
        viewperformance() 

    def deleteprofile(): 
        for widget in window.winfo_children():
                widget.destroy()
        delprofile() 

    def compgrades(): 
        for widget in window.winfo_children():
                widget.destroy()
        comparegrades() 

    def lowgrade(): 
        for widget in window.winfo_children():
                widget.destroy()
        lowestgrade()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        Launch()
    
    btn = Button(window, text="View Courses",command = viewcourses)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="View Grades in a Course", command= viewgrades)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="Add Grade for Assignment-1",command=addgrade1)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="Add Grade for Assignment-2",command=addgrade2)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="Add Grade for Midsem",command=addgrade3)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)  
    btn = Button(window, text="Add Grade for Endsem",command=addgrade4)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5) 
    btn = Button(window, text="Add Final Grade",command=addgrade5)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)  
    btn = Button(window, text="View Student Performance", command = viewstudperformance)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5) 
    btn = Button(window, text="Delete Profile",command=deleteprofile)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="Compare Grades of a Course", command=compgrades)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5) 
    btn = Button(window, text="Lowest Grade for a course",command=lowgrade)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="LOGOUT", command= back)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)


def studenthomepagescreen():
    window.geometry("500x300")
    window.resizable(False, False)
    lbl = Label(window, text="Welcome Student",font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    def viewgrades():
        for widget in window.winfo_children():
                widget.destroy()
        viewSgradesscreen() 

    def viewcourses(): 
        for widget in window.winfo_children():
                widget.destroy()
        viewScourses() 

    def viewperformance(): 
        for widget in window.winfo_children():
                widget.destroy()
        viewCourperformance() 

    def updatedet():
        for widget in window.winfo_children():
                widget.destroy()
        updatedetails() 

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        Launch()

    btn = Button(window, text="View Courses",command= viewcourses)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="View Grades in a Course",command=viewgrades)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="View Performance in Courses",command = viewperformance)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="Update Personal Details", command = updatedet)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    btn = Button(window, text="LOGOUT", command = back)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)

def signUp(userType):
    window.geometry("300x250")
    window.resizable(False, False)
    lbl = Label(window, text="Sign up as "+userType,font=("Arial", 13))
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl = Label(window, text="Teacher/Student ID")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=4)
    txt1.pack(pady=(2, 5))

    lbl = Label(window, text="Name")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt3 = Entry(window, width=30)
    txt3.pack(pady=(2, 5))

    lb2 = Label(window, text="Password")
    lb2.configure(bg='#292841',fg='white')
    lb2.config(anchor=CENTER)
    lb2.pack()
    txt = Entry(window, width=30, show="*")
    txt.pack(pady=(2, 5))
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.configure(bg='#292841', fg='white')
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    txt2 = Entry(window, width=30, show="*")
    txt2.pack(pady=(2, 5))

    def signup():
        # check if user exists
        # rest cases
        if(len(txt1.get())==0 and len(txt.get())==0):
            messagebox.showerror("Error", "Username and Password cannot be empty")
        elif(txt.get()!=txt2.get()):
            messagebox.showerror("Error", "Passwords don't match")
        elif(txt.get()==txt2.get()):
            # createAccount(txt1.get(),txt.get())
            messagebox.showinfo("Success", "Account created")
            for widget in window.winfo_children():
                widget.destroy()
            if(userType=="TEACHER"): 
                
                mycursor.execute("CALL NewTeacher('"+txt1+"','"+txt3+"','"+txt2+"')")
                teacherlogin()
            else:
                
                mycursor.execute("CALL NewStudent('"+txt1+"','"+txt3+"','"+txt2+"')")
                studentlogin()


    btn = Button(window, text="Create Account",command=signup)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=(1, 9))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        Launch()

    btn = Button(window, text="BACK")
    btn.configure(bg="#308B3B", fg='white',command=back)
    btn.pack(side=BOTTOM)

def teacherlogin():
    window.resizable(False, False)
    window.geometry("300x200")
    lbl = Label(window, text="LOGIN as Teacher")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    lbl = Label(window, text="Teacher ID")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=3)
    txt1.pack()
    lb2 = Label(window, text="Password")
    lb2.configure(bg='#292841',fg='white')
    lb2.config(anchor=CENTER)
    lb2.pack()
    txt = Entry(window, width=30, show="*")
    txt.pack()
    txt.focus()
    def teacherhomepage():
        for widget in window.winfo_children():
            widget.destroy()
        teacherhomepagescreen()
    btn = Button(window, text="LOGIN",command=teacherhomepage )
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    def signUpTEACHER():
        for widget in window.winfo_children():
            widget.destroy()
        signUp("TEACHER")
    button4=Button(window, text="New User?",command=signUpTEACHER)
    button4.configure(bg="#308B3B", fg='white')
    button4.pack(side=RIGHT) 


def studentlogin():
    window.resizable(False, False)
    window.geometry("300x200")
    lbl = Label(window, text="LOGIN as Student")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    lbl = Label(window, text="Username")
    lbl.configure(bg='#292841',fg='white')
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt1 = Entry(window, width=20)
    txt1.pack()
    lb2 = Label(window, text="Password")
    lb2.configure(bg='#292841',fg='white')
    lb2.config(anchor=CENTER)
    lb2.pack()
    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()
    def studenthomepage():
        str1=txt.get()
        str2=txt1.get()
        for widget in window.winfo_children():
            widget.destroy() 
        studenthomepagescreen()
    btn = Button(window, text="LOGIN",command=studenthomepage )
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=5)
    def signUpSTUDENT():
        for widget in window.winfo_children():
            widget.destroy()
        signUp("STUDENT")
    button4=Button(window, text="New User?",command=signUpSTUDENT)
    button4.configure(bg="#308B3B", fg='white')
    button4.pack(side=RIGHT)

    
def Launch():
        
    window.geometry("300x200")
    window.resizable(False, False)
    
    def tlogin():
        for widget in window.winfo_children():
                widget.destroy()
        teacherlogin()

    def stlogin():
        for widget in window.winfo_children():
                widget.destroy()
        studentlogin()
    

    btn = Button(window, text="TEACHER SPACE", command=tlogin)
    btn.configure(bg="#308B3B", fg='white')
    btn.place(relx=0.5, rely=0.3, anchor='center')
    # btn.place(x=100, y=400)

    # btn.pack(pady=10,side=)

    btn = Button(window, text="STUDENT SPACE", command=stlogin)
    btn.configure(bg="#308B3B", fg='white')
    btn.pack(pady=7)
    btn.place(relx=0.5, rely=0.7, anchor='center')

Launch()
window.mainloop()
