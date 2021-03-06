import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import PIL
from PIL import ImageTk, Image
import webbrowser
import string
from datetime import date
import time
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

url = 'try.html'
acc = "    Login/Signup"
userid = -1
nextcase = 0
casecounter = -1
canvacloser = 0
def home(root):
    objhome = home_page(root)
class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style = "Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
    def _add_placeholder(self,e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

def stAr(arr):
    arrx = arr.split(',')
    return arrx
#string comparison
def comp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
#complaint form
class complaint_form:
    def __init__(self, root):
        self.rootcf = root

        self.rootcf.title("Lodge Complaint")
        self.rootcf.geometry("1450x900+0+0")

        self.bg_icon = tk.PhotoImage(file=r"images/check_bg.png")
        self.user_icon = tk.PhotoImage(file=r"images/logo.png")
        self.name_icon = tk.PhotoImage(file=r"images/useracc.png")
        self.passw_icon = tk.PhotoImage(file=r"images/pswd.png")
        lb_bg = tk.Label(self.rootcf, image=self.bg_icon )
        lb_bg.place(x=0, y=0, relwidth=1, relheight=1)
        frame2=tk.Frame(self.rootcf,bg="white")
        frame2.place(x=100,y=50)
        #self.phone = tk.PhotoImage(file=r"C:\Users\HP\Downloads\phone.png")
        #self.place = tk.PhotoImage(file=r"C:\Users\HP\Downloads\icons8-location-24.png")
        self.mobile_no = tk.StringVar()
        self.uname = tk.StringVar()
        self.state = tk.StringVar()
        self.district = tk.StringVar()
        self.pc = tk.StringVar()
        self.cat = tk.StringVar()
        self.relation = tk.StringVar()
        self.incdet=tk.StringVar()
        self.incident=tk.StringVar()

        tk.Label(frame2, text="Name:",  bg="white",
              font=("times new roman", 15, "bold")).grid(row=1, column=0, )
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.uname, font=("", 15)).grid(row=1, column=1)
        tk.Label(frame2, text="Mobile no",  bg="white",
              font=("times new roman", 15, "bold")).grid(row=2, column=0,padx=10)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.mobile_no, font=("", 15)).grid(row=2, column=1,
                                                                                            padx=10)
        tk.Label(frame2, text="State:", bg="white",
              font=("times new roman", 15, "bold")).grid(row=3, column=0)
        self.state = tk.StringVar()
        choose_state = ttk.Combobox(frame2, text="**state**", textvariable=self.state, font=("times new roman", 15, "bold"))

        choose_state['values'] = (
        '**select state**', 'Andra Pradesh', 'Hyderabad', 'Amaravati', 'Arunachal Pradesh', 'Itangar', 'Assam',
        'Dispur', 'Bihar', 'Patna', 'Chhattisgarh', 'Raipur', 'Goa', 'Panaji', 'Gujarat', 'Gandhinagar', 'Haryana',
        'Chandigarh', 'Himachal Pradesh', 'Shimla', 'Jammu and Kashmir', 'Srinagar and Jammu', 'Jharkhand', 'Ranchi',
        'Karnataka', 'Bangalore', 'Kerala', 'Thiruvananthapuram', 'Madya Pradesh', 'Bhopal', 'Maharashtra', 'Mumbai',
        'Manipur', 'Imphal', 'Meghalaya', 'Shillong', 'Mizoraz', 'Aizawi', 'Nagaland', 'Kohima', 'Orissa',
        'Bhubaneshwar', 'Punjab', 'Chandigarh', 'Rajasthan', 'Jaipur', 'Sikkim', 'Gangtok', 'Tamil Nadu', 'Chennai',
        'Telagana', 'Hyderabad', 'Tripura', 'Agartala', 'Uttaranchal', 'Dehradun', 'Uttar Pradesh', 'Lucknow',
        'West Bengal', 'Kolkata')
        choose_state.grid(row=3, column=1, padx=40, pady=10)
        choose_state.current(0)

        l1 = tk.Label(frame2, text="District:",  bg="white", font=("times of roman", 15, "bold"))
        l1.grid(row=4,column=0,padx=40,pady=10)
        tk.Entry(frame2, textvariable=self.district,bd=5, relief=tk.GROOVE,font=("times new roman",15,"bold") ).grid(row=4, column=1, padx=20)
        lpc = tk.Label(frame2, text="Pincode:",  bg="white", font=("times of roman", 15, "bold"))
        lpc.grid(row=5,column=0,padx=40,pady=10)
        tk.Entry(frame2, textvariable=self.pc,bd=5, relief=tk.GROOVE,font=("times new roman",15,"bold") ).grid(row=5, column=1, padx=20)
        tk.Label(frame2, text="Category:", bg="white",
              font=("times new roman", 15, "bold")).grid(row=6, column=0, padx=40, pady=20)
        choose_state = ttk.Combobox(frame2, text="**state**", textvariable=self.cat, font=("times new roman", 15, "bold"))

        choose_state['values'] = (
        '**select category**', 'Property Crimes', 'Substance abuse', 'Violent Crime', 'Disorderly Conduct', 'Fraud', 'Theft',
        'Monetary Crime', 'Offense to family', 'Rape/Assault', 'Other')
        choose_state.grid(row=6, column=1, padx=20)
        choose_state.current(0)
        l3 = tk.Label(frame2, text="Relationship with the victim", bg="white",font=("times of roman", 15, "bold"))
        l3.grid(row=7, column=0, padx=40, pady=20)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.relation,font=("times new roman", 15, "bold")).grid(row=7, column=1)
        l4 = tk.Label(frame2, text="please provide any additional information about the incident: ", bg="white", font=("times of roman", 15, "bold"))
        l4.grid(row=8, column=0, padx=40, pady=20)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.incident, font=("times new roman", 15, "bold")).grid(row=8,
                                                                                                                  column=1)
        self.uname = tk.StringVar()
        self.pas = tk.StringVar()
        self.cat = tk.StringVar()
        self.time = tk.StringVar()
        self.place = tk.StringVar()
        tk.Label(frame2,text="Incident details:",font=("times new roman", 15, "bold"),
                         bg="blue",fg="white").grid(row=9, column=0)

        username = tk.Label(frame2, text="approximate timing and date of incident/recieving/viewing of content *",
                         bg="white",
                         font=("times new roman", 15, "bold"))
        username.grid(row=10, column=0)
        txtuser = tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.incdet, font=("", 15))
        txtuser.grid(row=10, column=1)
        userpass = tk.Label(frame2, text="where did the incident occur?", bg="white",
                         font=("times new roman", 15, "bold"))
        userpass.grid(row=11, column=0)
        txtpass = tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.place, font=("", 15))
        txtpass.grid(row=11, column=1, padx=10)
        place=tk.Label(frame2,text="Place",bg="white",font=("times new roman",15,"bold"))
        place.grid(row=12,column=0)
        ent = tk.Entry(frame2, bd=3, relief=tk.GROOVE, textvariable=self.place, font=("", 15))
        ent.grid(row=12, column=1)

        self.susname = tk.StringVar()
        self.cat = tk.StringVar()
        self.susdet = tk.StringVar()
        self.place = tk.StringVar()
        sus=tk.Label(frame2, text="Please share the details of the suspect.Any information will be kept confidential amd may help during investigation", font=("times new roman", 15, "bold"),
                         bg="light blue")
        sus.grid(row=13, column=0)
        category = tk.Label(frame2, text="suspect_name", font=("times new roman", 15, "bold"),
                         bg="white")
        category.grid(row=14, column=0)
        catent = tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.susname, font=("", 15))
        catent.grid(row=14, column=1)
        username = tk.Label(frame2, text="suspect details:",
                         bg="white",
                         font=("times new roman", 15, "bold"))
        username.grid(row=15, column=0)
        txtuser = tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.susdet, font=("", 15))
        txtuser.grid(row=15, column=1)
        Btn=tk.Button(frame2,text="submit",bg="blue",font=("times new roman",20,"bold"),fg="white", command=lambda : self.lodge())
        Btn.grid(row=16,columnspan=2)
    def lodge(self):
        self.status  ="pending"
        dist = self.district.get()
        self.name = self.uname.get()
        self.contact = self.mobile_no.get()
        self.sus_name = self.susname.get()
        self.pc_db = self.pc.get()
        self.loc = self.place.get()
        self.inc_det = self.incdet.get()
        self.sus_det = self.susdet.get()
        self.category = self.cat.get()
        self.stt = self.state.get()
        self.rel = self.relation.get()
        global userid
        self.time = time.localtime()
        self.date = date.today()
        self.pid = -1
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dreamers29",
        database="crime_report")
        self.curs = self.mydb.cursor()  
        self.check2 = "SHOW TABLES LIKE 'complaints'"  
        self.curs.execute(self.check2)
        self.result1 = self.curs.fetchone()
        if self.result1:
            print("table for contact exists")
        else:
            print("table doesn't exist")      
            self.curs.execute("CREATE TABLE complaints (id int AUTO_INCREMENT PRIMARY KEY, userid int, name VARCHAR(255), contact VARCHAR(255), city VARCHAR(255), district VARCHAR(255), pincode VARCHAR(66), state VARCHAR(255), category VARCHAR(255), location VARCHAR(255), time TIME, date DATE, suspect_name VARCHAR(255), inc_des VARCHAR(255), sus_des VARCHAR(255), stat VARCHAR(66), relvictim VARCHAR(255), pid INT)")
        jd=""
        self.num = -1
        self.jdbool = False
        self.curs.execute("SELECT * FROM stations")
        self.res = self.curs.fetchall()
        n = len(self.res)
        for i in range(0, n):
            (result) =self.res[i]
            jd = stAr(result[7])
            for c in jd:
                if comp(dist, c):
                    num = i
                    print(num)
                    self.jdbool = True
                    print("found")
                    break

        if self.jdbool:
            (psttn) = self.res[num]
            self.pid = psttn[0]
            self.inst= """INSERT INTO complaints (userid, name, contact, city, district, pincode, state, category, location, time, date, suspect_name, inc_des, sus_des, stat, relvictim, pid) 
                           VALUES 
                           (%(userid)s,%(name)s, %(contact)s, %(dist)s, %(dist)s, %(pc_db)s, %(stt)s, %(category)s, %(loc)s, %(time)s, %(date)s, %(sus_name)s, %(inc_det)s, %(sus_det)s, %(status)s, %(rel)s, %(pid)s) """
            self.curs.execute(self.inst, {'userid':userid,'name':self.name, 'contact': self.contact, 'dist':dist, 'pc_db':self.pc_db, 'stt':self.stt, 'category':self.category, 'loc':self.loc, 'time':self.time, 'date': self.date, 'sus_name':self.sus_name, 'inc_det':self.inc_det, 'sus_det':self.sus_det, 'status':self.status, 'rel':self.rel, 'pid': self.pid})
            self.mydb.commit()
            self.curs.execute("SELECT * FROM complaints WHERE userid=%(userid)s AND time=%(time)s", {'userid':userid, 'time':self.time})
            self.resagain = self.curs.fetchone()
            self.complaint_id = str(self.resagain[0])
            messagebox.showinfo("Submitted",  f"Note your complaint id {self.complaint_id}")
            self.backhome = home_page(self.rootcf)
        else:
            self.inst= """INSERT INTO complaints (userid, name, contact, city, district, pincode, state, category, location, time, date, suspect_name, inc_des, sus_des, relvictim, pid) 
                           VALUES 
                           (%(userid)s,%(uname)s, %(mobile_no)s, %(district)s, %(district)s, %(pc)s, %(state)s, %(cat)s, %(place)s, %(time)s, %(date)s, %(susname)s, %(incdet)s, %(susdet)s, %(relation)s) """
            self.curs.execute(self.inst, {'userid':userid,'uname':self.uname, 'mobile_no': self.mobile_no, 'district':self.district, 'pc':self.pc, 'state':self.state, 'cat':self.cat, 'place':self.place, 'time':self.time, 'date': self.date, 'susname':self.susname, 'incdet':self.incdet, 'susdet':self.susdet, 'relation':self.relation})
            self.mydb.commit()




#search sttn 
class srch_sttn:
    def __init__(self, root):
        self.roots = tk.Toplevel(root)
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dreamers29",
        database="crime_report")
        self.curs = self.mydb.cursor()
        self.search_var = tk.StringVar()

        self.roots.geometry("400x400")
        self.roots.configure(bg="#ddebc5")
        self.style = ttk.Style(self.roots)
        self.roots.title("Online Crime Branch")
        self.roots.iconbitmap('images/justice_logo.ico')
        self.crs_menu = tk.Menu(self.roots)
        self.roots.config(menu=self.crs_menu)
        self.file_menu = tk.Menu(self.crs_menu)
        self.crs_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.roots.quit)

        self.image2 = Image.open('bg.jpg')
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.w = self.image1.width()
        self.h = self.image1.height()
        self.roots.geometry('%dx%d+0+0' % (self.w,self.h))
        self.logophoto = ImageTk.PhotoImage(Image.open('images/logo.png')) 
        self.labelText = tk.StringVar()


        self.label1 = tk.Label(self.roots, text="Know Your Police Station",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

        self.label1.place(x=555, y=18)
        self.logolbl = tk.Label(self.roots, image=self.logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
        self.logolbl.place(x=460, y=000)
        self.frame_srch = tk.Frame(self.roots, bg="#a86d32", height=600, width=800)
        self.frame_srch.place(x=300, y=150)
        self.searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
        self.locphoto = ImageTk.PhotoImage(Image.open('images/pin.png'))
        self.style.configure("Placeholder.TEntry", foreground="#8b8b8c")
        self.srch_in = PlaceholderEntry(self.frame_srch, "Enter your location", textvariable=self.search_var)
        self.srch_in.place(x=230, y=20, height=35, width=250)
        self.res_dict = {
            "pid": -1,
            "sttn_name":"",
            "dist":"",
            "city":"",
            "state":"",
            "pc":"",
            "des":"",
            "contact": "",
            "email":""}
        #logic

        self.found = ""

        self.jdbool = False
        self.search_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda: self.searchSttn())
        self.search_btn.place(x=490, y=20)
        self.search_btn.config(image=self.searchphoto,compound=tk.LEFT, width=30, height=30)
        #self.loc_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
        #self.loc_btn.place(x=540, y=20)
        #self.loc_btn.config(image=self.locphoto,compound=tk.LEFT, width=30, height=30)
    def searchSttn(self):
        jd=""
        num = -1
        self.loc_db = self.search_var.get()
        print(self.loc_db)
        self.curs.execute("SELECT * FROM stations")
        self.res = self.curs.fetchall()
        n = len(self.res)
        for i in range(0, n):
            (result) =self.res[i]
            jd = stAr(result[7])
            for c in jd:
                print(c, self.loc_db)
                if comp(self.loc_db, c):
                    num = i
                    print(num)
                    self.jdbool = True
                    print("found")
                    break
        if self.jdbool:
            (result) = self.res[num]
            self.res_dict["pid"] = result[0]
            self.res_dict["sttn_name"] = result[2]
            self.res_dict["dist"]  = result[3]
            self.res_dict["city"] = result[4]
            self.res_dict["state"] = result[5]
            self.res_dict["pc"] = result[6]
            self.curs.execute("SELECT * FROM sttn_contact WHERE pid=%(pid)s",{'pid':self.res_dict["pid"]})
            res_ctt = self.curs.fetchone()
            (res_x) = res_ctt
            print(res_x)
            self.res_dict["des"] = res_x[3]
            self.res_dict["contact"] = res_x[2]
            self.res_dict["email"] = res_x[4]
            self.address = self.res_dict["dist"] + ", " + self.res_dict["city"] + ", " + self.res_dict["state"] 
            self.frame_res = tk.Frame(self.roots, bg="#ede779", height=300, width=450)
            self.frame_res.place(x=480, y=300)
            self.ps = tk.Label(self.frame_res, text=self.res_dict["sttn_name"], bg="#ede779", font=("Times New Roman", 14, "bold"))
            self.ps.place(x=20, y=45)
            self.add = tk.Label(self.frame_res, text=self.address, bg="#ede779", font=("Times New Roman", 12) )
            self.add.place(x=20, y=80)
            self.containeract = tk.Label(self.frame_res, text=self.res_dict["contact"], bg="#ede779", font=("Times New Roman", 12))
            self.containeract.place(x=20, y=105)
            self.email = tk.Label(self.frame_res, text=self.res_dict["email"], bg="#ede779", font=("Times New Roman", 12) )
            self.email.place(x=20, y=130)
            self.designation  = tk.Label(self.frame_res, text=self.res_dict["des"], bg="#ede779", font=("Times New Roman", 12))
            self.designation.place(x=20, y=155)
        else:
            self.found = "No nearby police station found!"
            self.frame_res = tk.Frame(self.roots, bg="#ede779", height=300, width=450)
            self.frame_res.place(x=480, y=300)
            self.nf = tk.Label(self.frame_res, text=self.found, bg="#ede779", font=("Times New Roman", 14))
            self.nf.place(x=20, y=45)
class pol_prof:
    def __init__(self, root):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dreamers29",
            database ="crime_report")
        self.curs = self.mydb.cursor()
        self.check1 = "SHOW TABLES LIKE 'stations'"
        self.curs.execute(self.check1)
        self.result = self.curs.fetchone()
        if self.result:
            print("table exist")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE stations (id int AUTO_INCREMENT PRIMARY KEY, userid int, sttn_name VARCHAR(255), district VARCHAR(255), city VARCHAR(255), state VARCHAR(255), pincode VARCHAR(66), jurisdication VARCHAR(255))")
            messagebox.showerror("error","Profile doesn't exist!")

        self.check2 = "SHOW TABLES LIKE 'sttn_contact'"  
        self.curs.execute(self.check2)
        self.result1 = self.curs.fetchone()
        if self.result1:
            print("table for contact exists")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE sttn_contact (id int AUTO_INCREMENT PRIMARY KEY, pid int NOT NULL, designation VARCHAR(255), contact VARCHAR(66), email VARCHAR(66))")

        self.res_dict = {
            "pid": -1,
            "sttn_name":"",
            "dist":"",
            "city":"",
            "state":"",
            "pc":"",
            "jd":"",
            "des":"",
            "contact": "",
            "email":""}
        global userid
        self.curs.execute("SELECT * FROM stations WHERE userid=%(userid)s",{'userid':userid})
        resp = self.curs.fetchone()
        if resp:
            (p) = resp
            self.res_dict["pid"] = p[0]
            self.res_dict["sttn_name"]=p[2]
            self.res_dict["dist"] = p[3]
            self.res_dict["city"] = p[4]
            self.res_dict["state"] = p[5]
            self.res_dict["pc"] = p[6]
            self.res_dict["jd"] = p[7]
            self.curs.execute("SELECT * FROM sttn_contact WHERE pid=%(pid)s",{'pid':self.res_dict["pid"]})
            respc = self.curs.fetchone()
            if respc:
                (pcontact) = respc
                self.res_dict["des"] = pcontact[3]
                self.res_dict["contact"] = pcontact[2]
                self.res_dict["email"] = pcontact[4]
        else:
            messagebox.showerror("error","Profile doesn't exist!")


        self.address = self.res_dict["dist"] + ", " + self.res_dict["city"] + ", "  + self.res_dict["pc"]
        self.rootp = tk.Toplevel(root)
        self.rootp.title("Branch Status")
        self.rootp.geometry('1350x1000+0+0')
        self.rootp.iconbitmap('images/justice_logo.ico')

        #self.rootp.configure(background = "grey")
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.rootp,image=self.bg_icon,)
        self.lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.label3=tk.Label(self.rootp,text="Check Your Branch",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=450,y=0)
        self.container = tk.Frame(self.rootp, bg="white", height=460, width=1000)
        self.container.place(x=200, y=200)
        self.p =   ImageTk.PhotoImage(Image.open('images/police_badge.png')) 
        self.plabel = tk.Label(self.container, image=self.p, compound=tk.LEFT)
        self.plabel.place(x=-2, y=-2)
        self.pname = tk.Label(self.container, text=self.res_dict["sttn_name"], font=("times new roman",20), bg="white")
        self.pname.place(x=635, y=10)
        self.add = tk.Label(self.container, text="Address: ", font=("times new roman",15, "bold"), bg="white")
        self.add.place(x=515, y=100)
        self.padd = tk.Label(self.container, text=self.address, font=("times new roman",15), bg="white")
        self.padd.place(x=600, y=100)
        self.state = tk.Label(self.container, text="State: ", font=("times new roman",15, "bold"), bg="white")
        self.state.place(x=515, y=160)
        self.pstate = tk.Label(self.container, text=self.res_dict["state"], font=("times new roman",15), bg="white")
        self.pstate.place(x=580, y=160)
        self.jd = tk.Label(self.container, text="Jurisdiction: ", font=("times new roman",15, "bold"), bg="white")
        self.jd.place(x=515, y=210)
        self.pjd = tk.Label(self.container, text=self.res_dict["jd"], font=("times new roman",12), bg="white")
        self.pjd.place(x=625, y=213)
        self.des = tk.Label(self.container, text="Designation : ", font=("times new roman",15, "bold"), bg="white")
        self.des.place(x=515, y=270)
        self.pdes = tk.Label(self.container, text=self.res_dict["des"], font=("times new roman",15), bg="white")
        self.pdes.place(x=650, y=270)
        self.ctt = tk.Label(self.container, text="Contact : ", font=("times new roman",15, "bold"), bg="white")
        self.ctt.place(x=515, y=330)
        self.pctt = tk.Label(self.container, text=self.res_dict["contact"], font=("times new roman",15), bg="white")
        self.pctt.place(x=610, y=330)
        self.em = tk.Label(self.container, text="Email Id : ", font=("times new roman",15, "bold"), bg="white")
        self.em.place(x=515, y=390)
        self.pem = tk.Label(self.container, text=self.res_dict["email"], font=("times new roman",15), bg="white")
        self.pem.place(x=610, y=390)
        self.vcrime = tk.Button(self.container, text="View FIRs", bg="yellow", command = lambda: self.vc(self.rootp,self.res_dict["pid"]))
        self.vcrime.place(x=900, y=390)
    def vc(self, root, pid):
        root.destroy()
        global nextcase
        self.vcobj = viewCrimes(root, nextcase, pid)
class viewCrimes:
    def __init__(self, root,nc, pid):
        global nextcase
        global casecounter
        t = time.localtime()
        today = date.today()
        stat = "pending"
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="Dreamers29",database="crime_report")
        self.curs = self.mydb.cursor()
        arr = []
        temparr = []
        crimes = {"id": -1,"name":"","address":"","category":"","location":"","time":t,"date":today,"contact": "","inc_des":"","sus_name":"","sus_des":"","rel":""}
        self.curs.execute("SELECT * FROM complaints WHERE stat=%(stat)s and pid=%(pid)s", {"stat":stat, "pid":pid})
        self.res = self.curs.fetchall()
        rows = len(self.res)
        casecounter = rows
        
        for counter in range(0,rows):
            temparr.append("")
            (cr) = self.res[counter]
            crimes["id"] = cr[0]
            crimes["name"]= cr[2]
            crimes["address"]= cr[5] + ", " + cr[4] + ", " + cr[7] + ", " + cr[6]
            crimes["category"] = cr[8]
            crimes["location"] = cr[9]
            crimes["time"] = cr[10]
            crimes["date"] = cr[11]
            crimes["contact"] = cr[3]
            crimes["inc_des"] = cr[13]
            crimes["rel"] = cr[16]
            crimes["sus_name"] = cr[12]
            crimes["sus_des"] = cr[14]
            temparr[counter] = crimes.copy()
            arr.append(temparr[counter])  

        self.rootv = tk.Toplevel()
        self.rootv.title("View Crimes")
        self.rootv.geometry('1350x1350+0+0')
        self.rootv.iconbitmap('images/justice_logo.ico')

        #self.rootv.configure(background = "grey")
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.rootv,image=self.bg_icon,)
        self.lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.label3=tk.Label(self.rootv,text="View Pending FIRs",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=500,y=0)
        self.container = tk.Frame(self.rootv, bg="white", height=485, width=1200)
        self.container.place(x=170, y=200)
        self.p =   ImageTk.PhotoImage(Image.open('images/police_badge.png')) 
        self.plabel = tk.Label(self.container, image=self.p, compound=tk.LEFT)
        self.plabel.place(x=0, y=0)
        self.cid = tk.Label(self.container, text=arr[nc]["id"], font=("times new roman",15), bg="white")
        self.cid.place(x=775, y=10)
        print(nc, "nextcase")
        self.cname= tk.Label(self.container, text="Petitioner's Name: ", font=("times new roman",14, "bold"), bg="white")
        self.cname.place(x=435, y=50)
        self.cn = tk.Label(self.container, text=arr[nc]["name"], font=("times new roman",14), bg="white")
        self.cn.place(x=590, y=50)
        self.cctt = tk.Label(self.container, text="Contact: ", font=("times new roman",14, "bold"), bg="white")
        self.cctt.place(x=435, y=90)
        self.cc = tk.Label(self.container, text=arr[nc]["contact"], font=("times new roman",14), bg="white")
        self.cc.place(x=515, y=90)
        self.cadd = tk.Label(self.container, text="Address: ", font=("times new roman",14, "bold"), bg="white")
        self.cadd.place(x=435, y=130)
        self.ca = tk.Label(self.container, text=arr[nc]["address"], font=("times new roman",14), bg="white")
        self.ca.place(x=515, y=130)
        
        self.jd = tk.Label(self.container, text="Category of Crime: ", font=("times new roman",14, "bold"), bg="white")
        self.jd.place(x=435, y=170)
        self.pjd = tk.Label(self.container, text=arr[nc]["category"], font=("times new roman",14), bg="white")
        self.pjd.place(x=600, y=170)
        self.cdt = tk.Label(self.container, text="Date & Time: ", font=("times new roman",14, "bold"), bg="white")
        self.cdt.place(x=435, y=210)
        self.cd = tk.Label(self.container, text=arr[nc]["date"], font=("times new roman",14), bg="white")
        self.cd.place(x=555, y=210)
        self.ct = tk.Label(self.container, text=arr[nc]["time"], font=("times new roman",13), bg="white")
        self.ct.place(x=645, y=210)
        self.cloc = tk.Label(self.container, text="Location of Crime : ", font=("times new roman",14, "bold"), bg="white")
        self.cloc.place(x=435, y=250)
        self.cl = tk.Label(self.container, text=arr[nc]["location"], font=("times new roman",14), bg="white")
        self.cl.place(x=600, y=250)
        self.cincdet = tk.Label(self.container, text="Incident details : ", font=("times new roman",14, "bold"), bg="white")
        self.cincdet.place(x=435, y=290)
        self.cinc = tk.Label(self.container, text=arr[nc]["inc_des"], font=("times new roman",12), bg="white", wraplength=550, justify=tk.LEFT)
        self.cinc.place(x=580, y=291)
        self.crel= tk.Label(self.container, text="Relation with the victim : ", font=("times new roman",14, "bold"), bg="white")
        self.crel.place(x=435, y=350)
        self.crv = tk.Label(self.container, text=arr[nc]["rel"], font=("times new roman",14), bg="white")
        self.crv.place(x=630, y=350)
        self.csusn= tk.Label(self.container, text="Suspect Name : ", font=("times new roman",14, "bold"), bg="white")
        self.csusn.place(x=435, y=390)
        self.csn = tk.Label(self.container, text=arr[nc]["sus_name"], font=("times new roman",14), bg="white")
        self.csn.place(x=590, y=390)
        self.csusdes = tk.Label(self.container, text="Suspect Description : ", font=("times new roman",14, "bold"), bg="white")
        self.csusdes.place(x=435, y=420)
        self.csd = tk.Label(self.container, text=arr[nc]["sus_des"], font=("times new roman",14), bg="white", wraplength=550, justify=tk.LEFT)
        self.csd.place(x=610, y=420)
        self.vcrime = tk.Button(self.container, text="<< Previous", bg="yellow", command=lambda: self.prevCase(self.rootv, pid))
        self.vcrime.place(x=900, y=430)
        self.vcrime = tk.Button(self.container, text="Mark as completed", bg="yellow", command=lambda: self.mark(arr))
        self.vcrime.place(x=980, y=430)
        self.vcrime = tk.Button(self.container, text="Next >>", bg="yellow", command =lambda: self.nextCase(self.rootv, pid))
        self.vcrime.place(x=1100, y=430)
        self.vc = root
        container = tk.Frame(self.vc, bg="white", height=660, width=1000)
        container.place(x=200, y=100)
    def nextCase(self,root, pid):
        global nextcase
        print(nextcase)
        if nextcase<casecounter:
            root.destroy()
            nextcase = nextcase + 1
            self.rootv.destroy
            self.vcobj = viewCrimes(root, nextcase, pid)
        else:
            messagebox.showerror("error","No more cases!")
    def prevCase(self, root, pid):
        global nextcase 
        if nextcase!=0:
            root.destroy()
            nextcase = nextcase - 1
            self.prevc = viewCrimes(root, nextcase, pid)
        else:
            messagebox.showerror("error","No more cases!")


        
    def mark(self, arr):
        global nextcase
        status = "completed"
        casid = arr[nextcase]["id"] 
        print(casid)
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="Dreamers29",database="crime_report")
        self.curs = self.mydb.cursor()
        caseinsert = """UPDATE complaints SET stat=%(status)s WHERE id=%(casid)s"""
        self.curs.execute(caseinsert, {'status':status, 'casid': casid})
        self.mydb.commit()

class status:
    def __init__(self, root):
        self.rootstat = tk.Toplevel(root)
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dreamers29",
        database="crime_report")
        self.curs = self.mydb.cursor()
        self.search_var = tk.StringVar()
        self.rootstat.geometry("700x700")
        self.rootstat.configure(bg="#ddebc5")
        self.style = ttk.Style(self.rootstat)
        self.rootstat.title("Online Crime Branch")
        self.rootstat.iconbitmap('images/justice_logo.ico')
        self.crs_menu = tk.Menu(self.rootstat)
        self.rootstat.config(menu=self.crs_menu)
        self.file_menu = tk.Menu(self.crs_menu)
        self.crs_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.rootstat.quit)

        self.image2 = Image.open('bg.jpg')
        self.image1 = ImageTk.PhotoImage(self.image2)
        
        self.logophoto = ImageTk.PhotoImage(Image.open('images/logo.png')) 
        self.labelText = tk.StringVar()


        self.label1 = tk.Label(self.rootstat, text="Check Complaint Status",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

        self.label1.place(x=185, y=18)
        self.logolbl = tk.Label(self.rootstat, image=self.logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
        self.logolbl.place(x=80, y=000)
        self.frame_srch = tk.Frame(self.rootstat, bg="#a86d32", height=300, width=600)
        self.frame_srch.place(x=40, y=150)
        self.searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
        self.locphoto = ImageTk.PhotoImage(Image.open('images/pin.png'))
        self.style.configure("Placeholder.TEntry", foreground="#8b8b8c")
        self.srch_in = PlaceholderEntry(self.frame_srch, "Enter complaint number", textvariable=self.search_var)
        self.srch_in.place(x=150, y=20, height=35, width=250)
        self.status = ''
        #logic
        self.search_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda: self.searchSttn())
        self.search_btn.place(x=405, y=20)
        self.search_btn.config(image=self.searchphoto,compound=tk.LEFT, width=30, height=30)
        #self.loc_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
        #self.loc_btn.place(x=540, y=20)
        #self.loc_btn.config(image=self.locphoto,compound=tk.LEFT, width=30, height=30)
    def searchSttn(self):
        cid = self.search_var.get()
        self.curs.execute("SELECT stat FROM complaints WHERE id=%(cid)s", {"cid":cid})
        self.res = self.curs.fetchone()
        if self.res:
            (st) = self.res
            self.status = st[0]

            self.frame_res = tk.Frame(self.rootstat, bg="#ede779", height=100, width=450)
            self.frame_res.place(x=90, y=260)
            self.ps = tk.Label(self.frame_res, text=self.status, bg="#ede779", font=("Times New Roman", 14, "bold"))
            self.ps.place(x=20, y=30)
        else:
            self.found = "No complaint found!"
            self.frame_res = tk.Frame(self.rootstat, bg="#ede779", height=300, width=350)
            self.frame_res.place(x=90, y=260)
            self.nf = tk.Label(self.frame_res, text=self.found, bg="#ede779", font=("Times New Roman", 14))
            self.nf.place(x=20, y=45)
#police branch registeration

class reg_police:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title('Register your branch')
        try:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dreamers29",
            database ="crime_report")
            self.curs = self.mydb.cursor()
        except: 
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dreamers29")
            self.curs = self.mydb.cursor()
            self.curs.execute("CREATE DATABASE crime_report")
        self.check1 = "SHOW TABLES LIKE 'stations'"
        self.curs.execute(self.check1)
        self.result = self.curs.fetchone()
        if self.result:
            print("table exist")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE stations (id int AUTO_INCREMENT PRIMARY KEY, userid int, sttn_name VARCHAR(255), district VARCHAR(255), city VARCHAR(255), state VARCHAR(255), pincode VARCHAR(66), jurisdication VARCHAR(255))")
        self.check2 = "SHOW TABLES LIKE 'sttn_contact'"  
        self.curs.execute(self.check2)
        self.result1 = self.curs.fetchone()
        if self.result1:
            print("table for contact exists")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE sttn_contact (id int AUTO_INCREMENT PRIMARY KEY, pid int NOT NULL, designation VARCHAR(255), contact VARCHAR(66), email VARCHAR(66))")
        self.name_var = tk.StringVar()
        self.dist_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.state_var = tk.StringVar()
        self.pc_var = tk.StringVar()
        self.jd_var = tk.StringVar()
        self.ot_var = tk.StringVar()
        self.ct_var = tk.StringVar()
        self.des_var = tk.StringVar()
        self.ctt_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.window.geometry('1350x1000+0+0')
        #self.window.configure(background = "grey")
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.window,image=self.bg_icon,)
        self.lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.label3=tk.Label(self.window,text="REGISTERATION PAGE",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=356,y=0)
        self.container = tk.Frame(self.window, bg="white", height=400, width=800)
        self.container.place(x=400, y=200)

        self.name = tk.Label(self.container,text = "Name of Police Station", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.name.grid(row = 0,column = 0, padx=40,pady=10)
        self.district = tk.Label(self.container ,text = "District", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.district.grid(row = 1,column = 0, padx=40,pady=10)
        self.city = tk.Label(self.container ,text = "City", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.city.grid(row = 2,column = 0, padx=40,pady=10)
        self.state = tk.Label(self.container ,text = "State", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.state.grid(row = 3,column = 0, padx=40,pady=10)
        self.pc = tk.Label(self.container ,text = "Pincode", compound=tk.LEFT,bg="white",font=("times new roman",16,))
        self.pc.grid(row = 4,column = 0, padx=40,pady=10)
        self.jd = tk.Label(self.container,text = "Jurisdiction", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.jd.grid(row = 5,column = 0, padx=40,pady=10)

        self.containeract = tk.Label(self.container, text="Phone no.", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.containeract.grid(row= 8, column = 0, padx=40,pady=10)
        self.des = tk.Label(self.container, text="Designation: ", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.des.grid(row=9, column=0, padx=40,pady=10)
        self.email = tk.Label(self.container, text="Email id", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.email.grid(row=10, column=0, padx=40,pady=10)



        self.name_in = tk.Entry(self.container, textvariable=self.name_var, bd=5, relief=tk.GROOVE,)
        self.name_in.grid(row = 0,column = 1,padx=20)
        self.district_in = tk.Entry(self.container, textvariable=self.dist_var, bd=5, relief=tk.GROOVE,)
        self.district_in.grid(row = 1,column = 1, padx=20)
        self.city_in = tk.Entry(self.container, textvariable=self.city_var, bd=5, relief=tk.GROOVE,)
        self.city_in.grid(row = 2,column = 1, padx=20)
        self.state_in=ttk.Combobox(self.container,textvariable=self.state_var,font=("times new roman",13))

        self.state_in['values']=('Select state','Andra Pradesh','Hyderabad', 'Amaravati','Arunachal Pradesh','Itangar','Assam','Dispur','Bihar','Patna','Chhattisgarh','Raipur','Goa','Panaji','Gujarat','Gandhinagar','Haryana','Chandigarh','Himachal Pradesh','Shimla','Jammu and Kashmir','Srinagar and Jammu','Jharkhand','Ranchi','Karnataka','Bangalore','Kerala','Thiruvananthapuram','Madya Pradesh','Bhopal','Maharashtra','Mumbai','Manipur','Imphal','Meghalaya','Shillong','Mizoraz','Aizawi','Nagaland','Kohima','Orissa','Bhubaneshwar','Punjab','Chandigarh','Rajasthan','Jaipur','Sikkim','Gangtok','Tamil Nadu','Chennai','Telagana','Hyderabad','Tripura','Agartala','Uttaranchal','Dehradun','Uttar Pradesh','Lucknow','West Bengal','Kolkata')
        self.state_in.grid(row=3, column=1, padx=20)
        self.state_in.current(0)
        self.pc_in = tk.Entry(self.container, textvariable=self.pc_var, bd=5, relief=tk.GROOVE,)
        self.pc_in.grid(row = 4,column = 1, padx=20)
        self.jd_in = tk.Entry(self.container, textvariable=self.jd_var, bd=5, relief=tk.GROOVE,)
        self.jd_in.grid(row = 5,column = 1, padx=20)

        self.des_in = tk.Entry(self.container, textvariable=self.des_var, bd=5, relief=tk.GROOVE,)
        self.des_in.grid(row = 8,column = 1,padx=20)
        self.ctt_in = tk.Entry(self.container, textvariable=self.ctt_var, bd=5, relief=tk.GROOVE,)
        self.ctt_in.grid(row = 9,column = 1, padx=20)
        self.email_in = tk.Entry(self.container, textvariable=self.email_var, bd=5, relief=tk.GROOVE,)
        self.email_in.grid(row = 10,column = 1, padx=20)
        self.btn = tk.Button(self.container ,text="Submit", bg="white",fg="blue",font=("times new roman",14,"bold"), command=lambda:self.onSubmit())
        self.btn.grid(row=11,column=1, pady=20)

    #function
    def onSubmit(self):
        self.name_db=self.name_var.get() 
        self.dist_db =self.dist_var.get() 
        self.city_db = self.city_var.get()
        self.state_db = self.state_var.get()
        self.pc_db = self.pc_var.get()
        self.jd_db = self.jd_var.get()
        self.des_db = self.des_var.get()
        self.ctt_db = self.ctt_var.get()
        self.email_db = self.email_var.get()
        self.pid = 0
        global userid
        self.inst= """INSERT INTO stations (userid, sttn_name, district, city, state, pincode, jurisdication ) 
                           VALUES 
                           (%(userid)s,%(name_db)s, %(dist_db)s, %(city_db)s, %(state_db)s, %(pc_db)s, %(jd_db)s) """
        self.curs.execute(self.inst, {
            'userid':userid,
            'name_db':self.name_db,
            'dist_db':self.dist_db,
            'city_db':self.city_db,
            'state_db':self.state_db,
            'pc_db':self.pc_db,
            'jd_db':self.jd_db })
        self.mydb.commit()
        self.curs.execute("SELECT id FROM stations WHERE sttn_name=%(name_db)s AND district=%(dist_db)s", {'name_db':self.name_db, 'dist_db': self.dist_db})
        self.res = self.curs.fetchone()
        x = 0
        (x) = self.res
        self.pid = x[0]
        #pid = int(res['id'])
        print(self.pid)   
    
        self.instctt = """INSERT INTO sttn_contact (pid, designation, contact, email) 
                           VALUES 
                           (%(pid)s, %(des_db)s, %(ctt_db)s, %(email_db)s) """
        self.curs.execute(self.instctt, {
            'pid':self.pid,
            'des_db':self.des_db,
            'ctt_db':self.ctt_db,
            'email_db':self.email_db
        })
        self.mydb.commit()
        self.polobj = pol_prof(self.window)
        



    




#user/plice
class chose:
    def __init__(self, root):
        self.rootc = root
        self.rootc.title('User Type')
        self.rootc.geometry("1250x700+0+0")
        self.rootc.iconbitmap('images/justice_logo.ico')
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.rootc,image=self.bg_icon,)
        self.lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.frame2=tk.Frame(self.rootc,bg="white")
        self.frame2.place(x=420,y=150)
        self.label3=tk.Label(self.rootc,text="REGISTERATION PAGE",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=320,y=0)
        self.container = tk.Frame(self.rootc, bg="white", height=300, width=800)
        self.container.place(x=260, y=250)
        self.userbtn = tk.Button(self.container, text="Register as a User", height=2, width=30, bg="#f56042", font=("Times New Roman", 13, "bold"), command=lambda: self.userClicked(self.rootc) )
        self.userbtn.place(x=250, y=80)
        self.branch = tk.Button(self.container, text="Register your branch", height=2, width=30, bg="#f56042", font=("Times New Roman", 13, "bold"), command=lambda: self.polClicked(self.rootc) )
        self.branch.place(x=250, y=150)
    def userClicked(self, root):
        
        global acc
        acc = "   Logout"
        self.home_again = home_page(root)
    def polClicked(self, root):
        
        self.ref_pol = reg_police(root)



#login page
class login_page:
    def __init__(self,root):
        self.root1 = root
        self.root1 =root
        self.root1.title("Login Page")
        self.root1.geometry("1350x700+0+0")

        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.user_icon=tk.PhotoImage(file=r"images/logo.png")
        self.name_icon=tk.PhotoImage(file=r"images/useracc.png")
        self.passw_icon=tk.PhotoImage(file=r"images/pswd.png")
        lb_bg=tk.Label(self.root1,image=self.bg_icon,)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        label=tk.Label(self.root1,text="Login System",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        label.place(x=500,y=0)
        logoframe=tk.Frame(self.root1,bg="white")
        logoframe.place(x=400,y=150)
        self.uname = tk.StringVar()
        self.pas = tk.StringVar()
        userlabel=tk.Label(logoframe,image=self.user_icon)
        userlabel.grid(row=0,columnspan=2,pady=20)
        username=tk.Label(logoframe,text="Username:",image=self.name_icon,compound=tk.LEFT,bg="white",font=("times new roman",20,"bold"))
        username.grid(row=1,column=0,padx=40,pady=20)
        txtuser = tk.Entry(logoframe, bd=5, relief=tk.GROOVE,textvariable=self.uname, font=("", 15))
        txtuser.grid(row=1, column=1, padx=20)
        userpass=tk.Label(logoframe,text="password",image=self.passw_icon,compound=tk.LEFT,bg="white",font=("times new roman",20,"bold"))
        userpass.grid(row=2,column=0,padx=40,pady=20)
        txtpass = tk.Entry(logoframe, bd=5, relief=tk.GROOVE,textvariable=self.pas, font=("", 15), show="*")
        txtpass.grid(row=2, column=1, padx=20)
        btn1=tk.Button(logoframe,text="Login",bg="blue",fg="white",font=("times new roman",20,"bold"),command=self.login)
        btn1.grid(row=3,columnspan=2,pady=20)
        btn2=tk.Button(logoframe,text="Click here for new user",bg="white",fg="blue",font=("times new roman",20,"bold"),command=self.register)
        btn2.grid(row=4,columnspan=2,pady=20)
    def regClicked(self, root):
        un = self.uname.get()
        pwd = self.password.get()
        dist = self.district.get()
        stt = self.state.get()
        mno = self.mobile_no.get()
        em = self.email.get()
        if un=="" or pwd=="":
            messagebox.showerror("error","Please fill username and password!")
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Dreamers29",
                    database="crime_report")
                curs = mydb.cursor()
            except:
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dreamers29")
                curs = mydb.cursor()
                curs.execute("CREATE DATABASE crime_report")
            check1 = "SHOW TABLES LIKE 'users'"
            curs.execute(check1)
            result = curs.fetchone()
            if result:
                print("table exists")
            else:
                print("table doesn't exist")
                curs.execute("CREATE TABLE users(id int AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), district VARCHAR(66), state VARCHAR(66), contact VARCHAR(66), email VARCHAR(66))")
            inst= """INSERT INTO users(username, password, district, state, contact, email ) 
                           VALUES 
                           (%(un)s, %(pwd)s, %(dist)s, %(stt)s, %(mno)s, %(email)s) """
            curs.execute(inst, {
                'un':un,
                'pwd':pwd,
                'dist':dist,
                'stt':stt,
                'mno':mno,
                'email':em
            })

            mydb.commit()
            messagebox.showinfo("Registered", "You have been registered with us!")
            curs.execute("SELECT id FROM users WHERE username=%(un)s", {'un':un})
            self.resu = curs.fetchone()
            z = 0
            (z) = self.resu
            global userid
            userid = z[0]
            print(userid)
           
            self.choseobj = chose(root)


        


    def register(self):
        self.root2=tk.Toplevel(self.root1)
        self.root2.title("sign up")
        self.root2.geometry("1350x700+0+0")
        self.bg=tk.PhotoImage(file=r"images/check_bg.png")
        self.label1=tk.Label(self.root2,image=self.bg)
        self.label1.place(x=0,y=0,relwidth=1,relheight=1)
        frame2=tk.Frame(self.root2,bg="white")
        frame2.place(x=400,y=150)
        label3=tk.Label(self.root2,text="REGISTERATION PAGE",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        label3.place(x=400,y=0)
        #self.police_station = tk.StringVar()
        self.mobile_no=tk.StringVar()
        self.username=tk.StringVar()
        self.state=tk.StringVar()
        self.district = tk.StringVar()
        self.password = tk.StringVar()
        self.email = tk.StringVar()
        #self.ploice_station = tk.StringVar()
        #self.where_the_incident_occur = tk.StringVar()

        self.phone=tk.PhotoImage(file=r"images/pin.png")
        self.place = tk.PhotoImage(file=r"images/pin.png")

        tk.Label(frame2, text="Name:", compound=tk.LEFT, bg="white",
                         font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=40, pady=20)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.uname, font=("", 15)).grid(row=1, column=1,
                                                                                                     padx=20)
        tk.Label(frame2, text="Mobile no", compound=tk.LEFT, bg="white",
                         font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=40, pady=20)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.mobile_no, font=("", 15)).grid(row=2, column=1,
                                                                                                   padx=20)
        tk.Label(frame2, text="Email ID", compound=tk.LEFT, bg="white", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=40, pady=20)
        tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.email, font=("", 15)).grid(row=3, column=1,
                                                                                                   padx=20)
        tk.Label(frame2,text="SELECT STATE:", compound=tk.LEFT,bg="white",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=40,pady=20)
        state=tk.StringVar()
        choose_state=ttk.Combobox(frame2,text="**state**",textvariable=state,font=("times new roman",15,"bold"))

        choose_state['values']=('**select select**','Andra Pradesh','Hyderabad', 'Amaravati','Arunachal Pradesh','Itangar','Assam','Dispur','Bihar','Patna','Chhattisgarh','Raipur','Goa','Panaji','Gujarat','Gandhinagar','Haryana','Chandigarh','Himachal Pradesh','Shimla','Jammu and Kashmir','Srinagar and Jammu','Jharkhand','Ranchi','Karnataka','Bangalore','Kerala','Thiruvananthapuram','Madya Pradesh','Bhopal','Maharashtra','Mumbai','Manipur','Imphal','Meghalaya','Shillong','Mizoraz','Aizawi','Nagaland','Kohima','Orissa','Bhubaneshwar','Punjab','Chandigarh','Rajasthan','Jaipur','Sikkim','Gangtok','Tamil Nadu','Chennai','Telagana','Hyderabad','Tripura','Agartala','Uttaranchal','Dehradun','Uttar Pradesh','Lucknow','West Bengal','Kolkata')
        choose_state.grid(row=4, column=1, padx=40,pady=40)
        choose_state.current(0)

        l1=tk.Label(frame2,text="DISTRICT:",compound=tk.LEFT,bg="white", font=("times of roman",16,"bold"))
        l1.grid(row=5,column=0,padx=40,pady=20)
        txt_district=tk.Entry(frame2, bd=5, textvariable=self.district, font=("", 15))
        txt_district.grid(row=5, column=1, padx=20)
        regpass = tk.Label(frame2, text="Password", compound =tk.LEFT, bg="white", font=("times of roman",16,"bold"))
        regpass.grid(row=6, column=0, padx=40, pady=20)
        txtpass = tk.Entry(frame2, bd=5, relief=tk.GROOVE,textvariable=self.password, font=("", 15), show="*")
        txtpass.grid(row=6, column=1, padx=20)

        #l2=tk.Label(frame2, text="Police_station:", compound=tk.LEFT, bg="white", font=("times of roman", 20, "bold"))
        #l2.grid(row=3,column=0,padx=40,pady=20)
        #text_ploice=tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.police_station, font=("times new roman", 20,"bold"))
        #text_ploice.grid(row=5, column=1, padx=20)
        #l3=tk.Label(frame2, text="where did the incident occur:", compound=tk.LEFT, bg="white", font=("times of roman", 20, "bold"))
        #3.grid(row=6, column=0, padx=40, pady=20)
        #text_incident=tk.Entry(frame2, bd=5, relief=tk.GROOVE, textvariable=self.where_the_incident_occur, font=("times new roman", 20,"bold"))
        #text_incident.grid(row=6, column=1,padx=20)
        
        but=tk.Button(frame2,text="Sign Up",bg="blue",fg="white", command=lambda: self.regClicked(self.root2))
        but.grid(row=7,columnspan=2,pady=20)



    def login(self):
        global userid
        logbool = False
        if self.uname.get()=="" or self.pas.get()=="":
            messagebox.showerror("error","All field required")
        #creating db connection 
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dreamers29",
            database="crime_report")
            curs = mydb.cursor()
        except:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dreamers29")
            curs = mydb.cursor()
            curs.execute("CREATE DATABASE crime_report")
        check1 = "SHOW TABLES LIKE 'users'"
        curs.execute(check1)
        result = curs.fetchone()
        if result:
            print("table exists")
        else:
            print("table doesn't exist")
            curs.execute("CREATE TABLE users(id int AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), district VARCHAR(66), state VARCHAR(66), contact VARCHAR(66), email VARCHAR(66))")
        curs.execute("SELECT * FROM users")
        res = curs.fetchall()
        n = len(res)
        for i in range(0,n):
            (res_user) = res[i]
            cmpid = res_user[0]
            cmpuser = res_user[1]
            cmppass = res_user[2]
            if self.uname.get()==cmpuser and self.pas.get()==cmppass:
                logbool = True
                messagebox.showinfo("Successful", f"welcome {self.uname.get()}")
                curs.execute("SELECT * FROM stations WHERE userid=%(cmpid)s",{"cmpid":cmpid})
                uop = curs.fetchone()
                if uop:
                    userid = cmpid
                    self.polobj = pol_prof(self.root1)
                    
                else:
                    userid = cmpid
                    global acc
                    acc = "   Logout"
                    
                    self.userobj = home_page(self.root1)


        if logbool==False:
            messagebox.showerror("invalid","invalide Username or Password")


def OpenUrl(url):
    webbrowser.open_new(url)
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 5
        y = y + cy + self.widget.winfo_rooty() +7
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "10", "normal"))
        label.place(x=0,y=0)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
class home_page:
    def __init__(self,root):
        self.root =tk.Toplevel(root)
        self.root.geometry("400x400")
        self.root.configure(bg="#ddebc5")
        self.root.title("Online Crime Branch")
        self.root.iconbitmap('images/justice_logo.ico')
        self.crs_menu = tk.Menu(self.root)
        self.root.config(menu=self.crs_menu)
        self.file_menu = tk.Menu(self.crs_menu)
        self.crs_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="Go Back to Home", command=lambda: home(self.root))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.root.quit)

        self.image2 = Image.open('bg.jpg')
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.w = self.image1.width()
        self.h = self.image1.height()
        self.root.geometry('%dx%d+0+0' % (self.w,self.h))
        self.logophoto = ImageTk.PhotoImage(Image.open('images/logo.png')) 
        self.labelText = tk.StringVar()


        self.label1 = tk.Label(self.root, text="Online Crime Branch India",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

        self.label1.place(x=555, y=18)
        self.logolbl = tk.Label(self.root, image=self.logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
        self.logolbl.place(x=460, y=000)
        self.frame_btn = tk.Frame(self.root, bg="#a86d32", height=400, width=500)
        self.frame_btn.place(x=140, y=200)
        self.frame_map = tk.Frame(self.root, bg="#a86d32", height=550, width=550)
        self.frame_map.place(x=850, y=150)
        self.searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
        self.reportphoto = ImageTk.PhotoImage(Image.open('images/report.png')) 
        self.accphoto =   ImageTk.PhotoImage(Image.open('images/acc.png')) 
        self.hlphoto =   ImageTk.PhotoImage(Image.open('images/hl.png')) 

        self.reportbtn = tk.Button(self.frame_btn,text="   Report Crime", height=2, width=30,bg="#ede779", font=("Times New Roman",11, "bold"), command=lambda: self.compform(self.root))
        self.reportbtn.place(x=40, y=80)
        self.reportbtn.config(image=self.reportphoto,compound=tk.LEFT, width=400, height=30)


        self.reportbtn = tk.Button(self.frame_btn,text="  View FIR Status", height=2, width=30,bg="#ede779", font=("Times New Roman",11, "bold"), command=lambda: self.crimeReport(self.root))
        self.reportbtn.place(x=40, y=140)
        self.reportbtn.config(image=self.reportphoto,compound=tk.LEFT, width=400, height=30)

        self.acc_btn = tk.Button(self.frame_btn, text=acc, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda : self.openAcc(self.root))
        self.acc_btn.place(x=40, y=200)
        self.acc_btn.config(image=self.accphoto,compound=tk.LEFT, width=400, height=30)

        self.search_btn = tk.Button(self.frame_btn, text="  Find Nearest Branch", height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda : self.openSrch(self.root))
        self.search_btn.place(x=40, y=260)
        self.search_btn.config(image=self.searchphoto,compound=tk.LEFT, width=400, height=30)

        self.crime_stats = tk.Label(self.frame_map, text="Crime Stats Of India", justify=tk.CENTER, fg="white", bg="#a86d32", font=("Times New Roman", 14, "bold"))
        self.crime_stats.place(x=195, y=15)
        self.map_img = ImageTk.PhotoImage(Image.open("images/map_crime.jpg"))
        self.map_button = tk.Button(self.frame_map, image=self.map_img, compound='center', borderwidth=0, bg="#ede779", fg="#ede779", command=lambda: self.plot(self.root))
        self.map_lbl = tk.Label(self.frame_map, image=self.map_img,justify = tk.CENTER, width=400, compound='center', bg="#ede779", fg="#ede779")
        self.map_button.place(x=50,y=40)
        CreateToolTip(self.map_button, text = 'Click to view detailed \n'' crime rate statistics of \n''India..')
        self.hover = tk.Label(self.frame_map, text="Click the map to view detailed statistics...", justify=tk.CENTER, fg="white", bg="#a86d32", font=("Times New Roman", 11))
        self.hover.place(x=275, y=505)
    def plot(self, root):
        self.stats = root
        self.stats.geometry("400x400")
        self.stats.title("Crime Statistics Statewise")
        global canvacloser
        canvacloser = canvacloser + 1
       
        states = ['Assam', 'Bihar','Delhi',  'Gujarat', 'Himachal Pradesh',  'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Odhisha', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Uttar Pradesh', 'West Bengal'] 
  
        data = [ 14590, 34277, 18765, 8623, 9922, 8514, 17868, 11490, 23593, 32574, 13990, 4938, 16439, 12692,  41889, 27798] 
  
  
        explode = (0.1, 0.0, 0.2, 0.3, 0.0,  0.2, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3) 
        colors = ( "orange", "cyan", "brown", 
          "grey", "indigo", "beige") 
        wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
        fig, ax = plt.subplots(figsize =(10, 7)) 
        wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: self.func(pct, data), 
                                  explode = explode,  
                                  labels = states, 
                                  shadow = True, 
                                  colors = colors, 
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = None) 
        plt.setp(autotexts, size = 6)
        canvas = FigureCanvasTkAgg(fig, master = self.stats)  
        canvas.draw() 
        canvas.get_tk_widget().pack() 
        toolbar = NavigationToolbar2Tk(canvas,self.stats) 
        toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack()
    def openAcc(self, root):
        self.useracc = login_page(root)

    def openSrch(self, root):
        self.usersrch = srch_sttn(root)
    def crimeReport(self, root):
        self.crimeobj = status(root)
    def func(self, pct, allvalues): 

        absolute = int(pct / 100.*np.sum(allvalues)) 
        return "{:.1f}%\n({:d})".format(pct, absolute)
    def compform(self, root):
        if userid==-1:
            messagebox.showerror("error","Please First Login!")
        else:
            self.cform = complaint_form(root)


        
    







root=tk.Tk()
obj_home = home_page(root)
#obj=login_page(root)

root.mainloop()
