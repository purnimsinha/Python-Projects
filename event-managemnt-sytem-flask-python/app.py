from flask import Flask, render_template,request,session
import pymysql
#from flask_ngrok import run_with_ngrok


app = Flask(__name__)
#run_with_ngrok(app)
app.secret_key = "super secret key"

#displaying all webpages starting
@app.route("/signup")
def signup():
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor=db.cursor()
   query="""select * from department"""
   cursor.execute(query)
   data=cursor.fetchall()
   for row in data:
      print(row)
    
   return render_template("student/signup.html", result=data)
#---------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
@app.route("/stusignin")
def stusignin():
   return render_template("student/signin.html")

def rgtdevt():
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor=db.cursor()
   qry="""SELECT students.stuname,students.fathername,students.email,events.eventname,registration.regstudent,registration.eventname FROM registration inner join students on registration.regstudent=students.stuid INNER join events on registration.eventname=events.eventid where students.stuid='{}'""".format(session['sid'])
   cursor.execute(qry)
   result=cursor.fetchall()
   return result

@app.route("/stuevtrgtd")
def stuevtrgtd():
   return render_template("student/stuevtrgtd.html",monu=rgtdevt())


@app.route("/stuevtrgt")
def stuevtrgt():
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor=db.cursor()
   query="""select * from events"""
   cursor.execute(query)
   data=cursor.fetchall()
   return render_template("student/stuevtrgt.html",puru=data)


def stuprofile(sessid):
   session['sid']=sessid
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   qry="""SELECT students.stuname, students.fathername,students.email,department.depname FROM students INNER JOIN department ON department.depid=students.studep WHERE students.stuid='{}'""".format(sessid)
   cursor.execute(qry)
   result = cursor.fetchone()
   print(result)
   return result
   
   


@app.route("/stuprofile")
def stuprofilecaller():
   row=stuprofile(session['sid'])
   return render_template("student/index.html",result=row)


#------------------------------------------------------------------------------------------------------

#displaying all webpages ending
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#student operations starting

@app.route("/register", methods=['POST','GET'])
def register():
   studentname = request.form['sname']
   fathername = request.form['fname']
   emailid = request.form['semail']
   departmentid = request.form['sdepartment']
   pwd = request.form['pass']
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   query = """insert into students(stuname,fathername,email,studep,password) values('{}','{}','{}','{}','{}') """.format(studentname,fathername,emailid,departmentid,pwd)
   cursor.execute(query)
   db.commit()
   db.close()
   return render_template("student/thankyou.html")

@app.route('/studelevt/<stuid>/<evtid>')
def studelevt(stuid,evtid):
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   qry="""delete from registration where regstudent={} and eventname={}""".format(stuid,evtid)
   print(qry)
   cursor.execute(qry)
   db.commit()
   db.close()
   return render_template("student/stuevtrgtd.html",monu=rgtdevt())


@app.route('/stu_insert_event',methods=['POST'])
def stu_insert_event():
   eventname=request.form['evt']
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   query="""INSERT INTO registration (regid, regstudent, studentdepartment, eventname) VALUES (NULL, '{}', NULL, '{}');""".format(session['sid'],eventname)
   cursor.execute(query)
   db.commit()
   db.close()
   return render_template("student/stuevtrgtd.html",monu=rgtdevt())
   
#-------------------------------------------------------------------------------------------------------
@app.route("/login",methods=['POST','GET'])
def login():
   emailid = request.form['email']
   password = request.form['pass']
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   query = """select stuid from students where email='{}' and password='{}' """.format(emailid,password)
   cursor.execute(query)
   data = cursor.fetchone()
   if data==None:
      return "i got no such user please register first"
   else:
      result=stuprofile(data[0])
      return render_template("student/index.html",result=result)
      
   
@app.route("/logout",methods=['POST','GET'])
def logout():
   session.pop('sid', None)
   session.pop('admid', None)
   return render_template("/index.html")


#----------------------------admin code starting-------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

#signin----------------------------------------------------------------------------------------------------------------
@app.route('/admin')
def admin():
    return render_template('/adminnavbar/admin.html')

@app.route('/disp_signin')
def disp_signin():
    return render_template('/adminnavbar/signin.html')



@app.route('/signin',methods=['POST','GET'])
def signin():
    adminemail=request.form['emailid']
    pwd=request.form['pwd']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query="""select admid from tbadmin where admuserid='{}' and admpassword='{}'""".format(adminemail,pwd)
    cursor.execute(query)
    data=cursor.fetchone()
    if data==None:
      return render_template('/adminnavbar/nouser.html') 
    else:
       session['admid']=data[0]
    return render_template('/adminnavbar/admin.html')
       
    
    
   
    
#route department
#-----------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def dispdep():
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query="select * from department"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return data
    
@app.route('/department')
def department():    
    return render_template('/adminnavbar/department.html',result=dispdep())

@app.route('/insert_department', methods=['POST','GET'])
def insert_department():
    departname=request.form['depname']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query=""" insert into department(depname) VALUES('{}')""".format(departname)
    cursor.execute(query)
    db.commit()
    query="select * from department"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return render_template('/adminnavbar/department.html',result=data)

@app.route('/deldep/<depid>')
def deldep(depid):
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   qry="""delete from department where depid={}""".format(depid)
   print(qry)
   cursor.execute(qry)
   db.commit()
   db.close()
   return render_template('/adminnavbar/department.html',result=dispdep())

@app.route('/disp_editdep/<depid>')
def disp_editdep(depid):
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""select * from department where depid={}""".format(depid)
    cursor.execute(qry)
    data=cursor.fetchone()
    db.close()
    return render_template('/adminnavbar/updatedep.html',result=data)

@app.route('/update_dep/<depid>',methods=['POST','GET'])
def update_dep(depid):
    depname=request.form['editdepname']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""update department set depname='{}' where depid={}""".format(depname,depid)
    cursor.execute(qry)
    db.commit()
    db.close()
    return render_template('/adminnavbar/department.html',result=dispdep())
    

#---------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
def evtdisplay():
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query="select * from events"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return data
    
@app.route('/event')
def event():
    return render_template('/adminnavbar/event.html',puru=evtdisplay())


@app.route('/insert_event', methods=['POST','GET'])
def insert_event():
    evtname=request.form['evtname']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query=""" insert into events(eventname) VALUES('{}')""".format(evtname)
    cursor.execute(query)
    db.commit()
    query="select * from events"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return render_template('/adminnavbar/event.html',puru=data)

@app.route('/delevt/<eventid>')
def delevt(eventid):
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   qry="""delete from events where eventid={}""".format(eventid)
   print(qry)
   cursor.execute(qry)
   db.commit()
   db.close()
   return render_template('/adminnavbar/event.html',puru=evtdisplay())


@app.route('/disp_editevt/<eventid>')
def disp_editevt(eventid):
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""select * from events where eventid={}""".format(eventid)
    print(qry)
    cursor.execute(qry)
    data=cursor.fetchone()
    db.close()
    return render_template('/adminnavbar/updateevt.html',result=data)

@app.route('/update_evt/<eventid>',methods=['POST','GET'])
def update_evt(eventid):
    evtname=request.form['editevtname']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""update events set eventname='{}' where eventid={}""".format(evtname,eventid)
    cursor.execute(qry)
    db.commit()
    db.close()
    return render_template('/adminnavbar/event.html',puru=evtdisplay())



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
def admdisplay():
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query="select * from tbadmin"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return data

@app.route('/adduser')
def adduser():
    return render_template('/adminnavbar/adduser.html',monu=admdisplay())

@app.route('/insert_adduser', methods=['POST','GET'])
def insert_adduser():
    username=request.form['username']
    userpwd=request.form['password']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    query=""" insert into tbadmin(admuserid,admpassword) VALUES('{}','{}')""".format(username,userpwd)
    cursor.execute(query)
    db.commit()
    query="select * from tbadmin"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
         print(row)
    db.close()
    return render_template('/adminnavbar/adduser.html',monu=data)

@app.route('/deluser/<admid>')
def deluser(admid):
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor = db.cursor()
   qry="""delete from tbadmin where admid={}""".format(admid)
   print(qry)
   cursor.execute(qry)
   db.commit()
   db.close()
   return render_template('/adminnavbar/adduser.html',monu=admdisplay())

@app.route('/disp_editadm/<admid>')
def disp_editadm(admid):
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""select * from tbadmin where admid={}""".format(admid)
    print(qry)
    cursor.execute(qry)
    data=cursor.fetchone()
    db.close()
    return render_template('/adminnavbar/updateadm.html',result=data)

@app.route('/update_adm/<admid>',methods=['POST','GET'])
def update_adm(admid):
    admname=request.form['username']
    admpassword=request.form['password']
    db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
    cursor=db.cursor()
    qry="""update tbadmin set admuserid='{}',admpassword='{}' where admid={}""".format(admname,admpassword,admid)
    cursor.execute(qry)
    db.commit()
    db.close()
    return render_template('/adminnavbar/adduser.html',monu=admdisplay())


#------------------------------------------------------------------------------------------------------------------------------------
    
@app.route('/admlogin')
def admlogin():
     return render_template('/admin/index.html')


def admrgtdevt():
   db=pymysql.connect("remotemysql.com","SzRUvhv8iO","EgCKdXmZw1","SzRUvhv8iO")
   cursor=db.cursor()
   qry="""SELECT students.stuname,students.fathername,students.email,events.eventname,registration.regstudent,registration.eventname FROM registration inner join students on registration.regstudent=students.stuid INNER join events on registration.eventname=events.eventid"""
   cursor.execute(qry)
   result=cursor.fetchall()
   return result
   
@app.route('/dispevtrgtd')
def dispevtrgtd():
     return render_template('/adminnavbar/dispevtrgtd.html',result=admrgtdevt())




#---------------------------------------------------------------------------------------------------------------------------------------
#----------------------------- code for anonymous user-----------------------
#----------------------------------------------------------------------------

@app.route('/')
def index():
     return render_template('/index.html')



#student operations ending
if __name__ == '__main__':
   app.run(debug=True)
