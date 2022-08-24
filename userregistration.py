#email=str(input())
#print("enter your email id:",email)
import re
#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+.[A-Za-z]\b'
regex = r'\b[a-z.]+[0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
  if(re.match(regex,email)):
    return True
  else:
    return False


def ValidatePassword(password):
  SpecialSym =['~','!','@', '#','$','%','^','&','*','_','-']
  val = True
  if len(password) < 6:
    print('length should be at least 6')
    val = False
          
  if len(password) > 16:
    print('length should be not be greater than 16')
    val = False
          
  if not any(char.isdigit() for char in password):
    print('Password should have at least one number')
    val = False
          
  if not any(char.isupper() for char in password):
    print('Password should have at least one uppercase letter')
    val = False
          
  if not any(char.islower() for char in password):
    print('Password should have at least one lowercase letter')
    val = False
          
  if not any(char in SpecialSym for char in password):
    print('Password should have at least one of the symbols ~!@#$%^&*_-')
    val = False
  return val

import csv
f=open('user_details.csv','w')
obj=csv.writer(f)
obj.writerow(["UserName","Password"])
f.close()

def Savefile(email,password):
  data=[email,password]
  f=open('user_details.csv','a')
  obj=csv.writer(f)
  obj.writerow(data)
  f.close()
  
def Checkfile_from_csv(email):
  f1=open('user_details.csv','r')
  obj1=csv.reader(f1)
  for user in obj1:
   #print(user)
   if email==user[0]:
    #print('This email available in csv file ')
    return True
   
  #print('This email not available in csv file')
  return False
  f1.close()
  
def Check_both_empwd(email,password):
  data=[email,password]
  checklist=[]
  f2=open('user_details.csv','r')
  obj2=csv.reader(f2)
  for user in obj2:
   checklist.append(user)
  if data in checklist:
   #print('email and pwd exist')
   return True
  else:
   #print('email and pwd mot exists')
   return False
  f2.close()
  
def check_forgotten_pwd(email):
  f3=open('user_details.csv','r')
  obj3=csv.reader(f3)
  for user in obj3:
    #print(user[1])
    if email==user[0]:
      return user[1]
   
  return ''
  f3.close()
  
  def login_checking(email,password):
  if Check_both_empwd(email,password):
    print('you are succesfully login')
  else:
    print('pls enter vaild details')
    Login()

def GetEmail():
  print("enter your email id:")
  email=str(input())
  return email

def GetPassword():
  print("enter your password:")
  password=str(input())
  return password
 
def Registration():
  email=GetEmail()
  if check(email):
    print('your email is valid')
  else:
    print('your email is not valid .. try again')
    Registration() 

  if Checkfile_from_csv(email):
    print('This mailid is already register,you can try another id')
    Registration()
  else:
   password=GetPassword()  
  if ValidatePassword(password): 
     print('password is valid')
     Savefile(email,password)
     print('your mailid id successfully register')
  else:
      print('password is invalid')
      Registration()


def Login():
  email=GetEmail() 
  if Checkfile_from_csv(email): 
   password=GetPassword()  
   login_checking(email,password)
   #print('you are successfully login')
  else:
   print('pls register your details')
   Registration()

  #if not there in file print('please register your details')

def ForgotPassword():
   email=GetEmail()
   print(check_forgotten_pwd(email))

print('please select your choice  \r\n Press no:1 for Registration  \r\n Press no:2 for Login \r\n  Press no:3 for Forgot Password ')

choice=int(input())

if(choice==1):
  Registration()
elif(choice==2):
  Login()
elif(choice==3):
  ForgotPassword()
