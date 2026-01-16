import matplotlib.pyplot as plr
import mysql.connector as ms
from datetime import datetime
from tabulate import tabulate

con=ms.connect(host='localhost',user='root',port='3306',password='123',database='flight_reservation_system')
cur=con.cursor()
if con.is_connected():
    print('successfully connected')

print()
print('************************************')
print()
print()
print("FLIGHT RESERVATION SYSTEM, EMIRATES AIRLINES.")
print()
print()
print('************************************')
print()

def create_login():
    
    cur.execute('create table if not exists login(name varchar(35),phone varchar(15),email_id varchar(35),password varchar(35))')
create_login()
 
L=[]
def entername():
    while True:
        name=input("ENTER FULL NAME:").strip()
        if not name:
            print("Name is required!")
        else:
            print('')
            L.append(name)
            break
    
        
def enterphone():
    while True:
        phone=input("ENTER PHONE NUMBER(10 DIGITS):")
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number. Please enter a 10-digit phone number.")
        else:
            print('')
            L.append(phone)
            break


def enteremailid():
    while True:
        email_id=input("ENTER EMAIL ID: ").strip()
        if not email_id:
            print("Email id is required!")
        elif '@' not in email_id or email_id.count('@') > 1:
            print("Invalid email id! '@' symbol is required and it should appear only once.")
        elif email_id.startswith('@') or email_id.endswith('@'):
            print("Invalid email id! '@' should not be at the beginning or end.")
        elif '.' not in email_id.split('@')[1]:
            print("Invalid email id! The domain part must contain a dot ('.').")
        else:
            print('')
            L.append(email_id)
            break

def enterpass():
    while True:
        password=input("ENTER PASSWORD: ")
        if len(password) < 6:
            print("Password must be at least 6 characters.")
        else:
            print('')
            L.append(password)
            break
    
    

def createacc():
    print('Create your new account:')
    cur=con.cursor()
    entername()
    enterphone()
    enteremailid()
    enterpass()
    log=(L)
    sql=('insert into login(name,phone,email_id,password) values(%s,%s,%s,%s)')
    
    cur.execute(sql, log)
    con.commit() 
    print("\nNew account created and saved successfully!")
        



def Showpassengerlist():
    cur.execute("select * from passenger")
    c1=cur.fetchall()
    columns1 = [desc[0] for desc in cur.description]
    print(tabulate(c1, headers=columns1, tablefmt="grid"))
    print()
    
def Showflights():
    cur.execute("select * from flights")
    c2=cur.fetchall()
    columns2 = [desc[0] for desc in cur.description]
    print(tabulate(c2, headers=columns2, tablefmt="grid"))
    print()


def Showfoodpiechart():
    part=[20,18,20,15,10,12,20,11,8,6,6,7,20]
    mylabels=('Hash brown+Salad','Meatballs+Spaghetti','Chicken biriyani','Club sandwich','Cup noodles','Ramen noodles','Caesar salad','Green salad','Samosa chat','Chocolate pudding','cut fruits','pastries(1 pc)','brownies(2 pc)')
    mycolours=['r','g','b','y','r','g','b','c','y','r','g','b','c']
    plr.pie(part, labels=mylabels, colors=mycolours)
    plr.title(label='Price range')
    plr.show()

def Showavfoodmenu():
    print('All food items available')
    cur.execute("select * from food")
    c1=cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    print(tabulate(c1, headers=columns, tablefmt="grid"))
    print()

def Showticketprices():
    print("1. ECONOMY CLASS AED 2500 PER PERSON")
    print("2. BUSINESS CLASS AED 4067 PER PERSON")
    print("3. FIRST CLASS AED 5960 PER PERSON")

def ViewRecords():
    opt=""
    print()
    print('1.Show passenger arrival and departure list' )
    print('2.Show available flights')
    print('3.Show available food menu')

    print('4.Show permissible weights for first class')
    print('5.Show permissible weights for business class')
    print('6.Show permissible weights for economy class')
    print('7.Show ticket prices')
    print("************************************")

    opt=int(input("enter your choice (SELECT NUMBER): "))
    if opt==1:
        Showpassengerlist()
     
        
    elif opt==2:
        Showflights()
        
        
    elif opt==3:
        Showavfoodmenu()
        
        
        
    elif opt==4:
        print('Permissible weight for first class: 40kg')
        print()
        
        
    elif opt==5:
        print('Permissible weight for business class: 35kg')
        print()
       
        
    elif opt==6:
        print('Permissible weight for economy class: 30kg')
        print()
    
    
    elif opt==7:
        Showticketprices()


    else:
        print('INVALID OPTION')
        ViewRecords()
    op=int(input('Do you want to continue? 1-Yes , 2-No :'))
    if op==1:
        ViewRecords()
    else:
        print('Going back to start menu...')
        start()
        
L1=[]
PD=[]     
def passid():
    while True:
        pid=input('Enter passenger id')
        if not pid.isdigit():
            print("Invalid passenger ID. PLease enter a numeric value.")
        else:
            print('')
            L1.append(pid)
            PD.append(pid)
            break


def passname():
    while True:
        name=input("ENTER FULL NAME:").strip()
        if not name:
            print("Name is required!")
        else:
            print('')
            L1.append(name)
            PD.append(name)
            break

def departdate():
    while True:
        dateofdep1 = input('ENTER DATE OF DEPARTURE (yyyy-mm-dd): ')
        try:
            dateofdep = datetime.strptime(dateofdep1, "%Y-%m-%d")
            L1.append(dateofdep)
            print('Date of Departure:', dateofdep)
            break
        except ValueError:
            print('Invalid date. Please enter a valid date in the format YYYY-MM-DD.')


def deparloc():
    while True:
        departloc=input("ENTER DEPARTURE LOCATION:").strip()
        if not departloc:
            print("Departure location is required!")
        else:
            print('')
            L1.append(departloc)
            break
        
def arrloc():
    while True:
        arrloc=input("ENTER ARRIVAL LOCATION:").strip()
        if not arrloc:
            print("Arrival location is required!")
        else:
            print('')
            L1.append(arrloc)
            break
def flightno():
    while True:
        flightno=input("ENTER FLIGHT SERIAL NUMBER:").strip()
        if not flightno.isdigit():
            print("flight serial number is required!")
        else:
            print('')
            L1.append(flightno)
            break


def dob():
    while True:
        dob1=input("ENTER DATE OF BIRTH (yyyy-mm-dd):")
        try:
           # Validate the date format   
           dob = datetime.strptime(dob1, "%Y-%m-%d")
           PD.append(dob)
           break
        except ValueError:
           print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")

def passemail():
    while True:
        emailid=input('Enter email id:').strip()
        if not emailid:
            print("Email id is required!")
        elif '@' not in emailid or emailid.count('@') > 1:
            print("Invalid email id! '@' symbol is required and it should appear only once.")
        elif emailid.startswith('@') or emailid.endswith('@'):
            print("Invalid email id! '@' should not be at the beginning or end.")
        elif '.' not in emailid.split('@')[1]:
            print("Invalid email id! The domain part must contain a dot ('.').")
        else:
            print('')
            PD.append(emailid)
            break

def passphno():
    while True:
        phoneno=input('Enter phone number(05XXXXXXXX)')
        if not phoneno.isdigit() or len(phoneno) != 10:
            print("Invalid phone number. Please enter a 10-digit phone number.")
        else:
            print('')
            PD.append(phoneno)
            break

def passaddress():
    while True:
        address=input('Enter address:').strip()
        if not address:
            print("address is required!")
        else:
            print('')
            PD.append(address)
            break

def tclassprice():
    while True:
        tclass=input("ENTER TICKET CLASS TYPE('Ec' for Economy class /'Bc' for Business class / 'Fc' for First class):").strip().lower()
        tprice=0
        if tclass in ['ec','economy','economy class']:
            tprice=tprice+2500
            PD.append(tclass)
            PD.append(tprice)
            break
        elif tclass in ['bc','business','business class']:
            tprice=tprice+4067
            PD.append(tclass)
            PD.append(tprice)
            break
        elif tclass in ['fc','first','first class']:
            tprice=tprice+5960
            PD.append(tclass)
            PD.append(tprice)
            break
        else:
            print('Enter valid input!')

def foodord():
    while True:
        foodord=input('ENTER FOOD ID IF ORDERED(0 if not ordered):')
        if not foodord.isdigit():
            print("Invalid input!.")
        else:
            print('')
            PD.append(foodord)
            break
        
lpass=(L1)
pdpass=(PD)
def add_passenger():
    passid()
    passname()
    departdate()
    deparloc()
    arrloc()
    flightno()
    dob()
    passemail()
    passphno()
    passaddress()
    tclassprice()
    foodord()

    
    sql1=('insert into passenger(P_ID,name,dateofdeparture,departurelocation,arrivallocation,flight_sno) values (%s,%s,%s,%s,%s,%s)')
    cur.execute(sql1,lpass)
    
    sql2=("insert into passenger_details(P_ID,name,dateofbirth,email_id,phone_no,address,ticket_class,total_ticket_price,food_ordered_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cur.execute(sql2,pdpass)
    
    con.commit()
    print('RECORD OF PASSENGER INSERTED')



def add_food():
    c1=con.cursor()
    L=[]
    sno=input("ENTER SERIAL NO:")
    cur.execute('select * from food where sno={}'.format(sno))
    data = cur.fetchone()
    if data!=None:
                print('Serial no aldready exists!')
                add_food()
    else:
        print()
    itemname=input("ENTER NAME OF FOOD:")
    price=float(input('ENTER FOOD ITEM PRICE:'))
    quantity=input("ENTER QUANTITY:")
    
    L.append(sno)
    L.append(itemname)
    L.append(quantity)
    L.append(price)
    f=(L)
    try:
        sql=("insert into food(sno,itemname,quantity,FPRICE) values(%s,%s,%s,%s)")
        c1.execute(sql,f)
        con.commit()
        print('FOOD RECORD INSERTED')
    except Exception as e:
        print(e,'error occured')
        
    
    
    
def delete_food():
    cur.execute("select * from food")
    c1=cur.fetchall()
    columns1 = [desc[0] for desc in cur.description]
    print(tabulate(c1, headers=columns1, tablefmt="grid"))
    print()
    print()
    d=input(" DELETE FOOD?(YES/NO): ")
    if(d=='y' or d=='yes' or d=='Y' or d=='YES'):
        fid = int(input('Enter S.no of food item to be deleted: '))
        cur.execute("delete from food where Sno={}".format(fid))
        print("FOOD ENTRY DELETED")
        cur.execute("select * from food")
        c2=cur.fetchall()
        columns2 = [desc[0] for desc in cur.description]
        print(tabulate(c2, headers=columns2, tablefmt="grid"))
        con.commit()
    elif(d=='n' or d=='no' or d=='N' or d=='NO'):
        print("NO ITEM DELETED.")
    else:
        print('INVALID ENTRY')
        delete_food()


def luggagebill():
    x=input("ADDITIONAL WEIGHT REQUIRED?(YES/NO): ").strip().lower()
    if x in ['y', 'yes']:
        pid=int(input('Enter passenger ID:'))
        cur.execute('select * from passenger_details where P_ID={}'.format(pid))
        data = cur.fetchone()
        if data==None:
            print('Invalid passenger ID ')
            luggagebill()
        print("1) For 5 KG - 150AED")
        print("2) For 10 KG - 300AED")
        print("3) For 15 KG - 500AED")
        ch=int(input("ADD IN FLIGHT BAGGAGE(ENTER NUMBER): "))
        addw=0
        addp=0
        print("ADDITIONAL WEIGHT ADDED")
        if ch==1:
            addw=5
            addp=150
        elif ch==2:
            addw=10
            addp=300
        elif ch==3:
            addw=15
            addp=500
    
    elif x in ['n','no']:
        print("NO ADDITIONAL WEIGHT ADDED")
           
    else:
        print('INVALID ENTRY')
        luggagebill()
        
    cur.execute('UPDATE passenger_details SET additional_weight={} and total_ticket_price=total_ticket_price+{} WHERE P_ID={}'.format(addw,addp,pid))                   
           
        
    

            
def EditRecords():
    opt=""
    print()
    print('1.Add new passenger' )
    print('2.Add extra luggage for a passenger')
    print('3.Add a food item to food menu')
    print('4.Delete a food item from food menu')
    print("************************************")

    opt=int(input("enter your choice (SELECT NUMBER): "))
    if opt==1:
        add_passenger()
     
        
    elif opt==2:
        luggagebill()
        
        
    elif opt==3:
        add_food()
        
        
    elif opt==4:
        delete_food()
        
    
    else:
        print('INVALID OPTION')
        EditRecords()
    op=int(input('Do you want to continue? 1-Yes , 2-No :'))
    if op==1:
        EditRecords()
    else:
        print('Going back to start menu...')
        start()
        




#-----------------------------------------------------------------------------

def start():
    print()
    print('************************************')
    print()
    print("FLIGHT MANAGEMENT SYSTEM PROJECT".center(50))
    option=int(input('\nWelcome! '
                     '\n1.View records.  2.Edit records 3.Quit'
                     '\nEnter required option number to continue:'))
    if option==1:
        ViewRecords()
    elif option==2:
        EditRecords()
    elif option==3:
        print('Quitting..')
    else:
        print('Enter approprtiate number')
        
def login():
    while True:
        global cur
        acc = input("\nDO YOU HAVE AN ACCOUNT (Y/N)").strip().lower()
        if acc in ['y', 'yes']:
            email = input("\nENTER YOUR EMAIL ID:-").strip()
            pas = input("\nENTER YOUR PASSWORD:-")
            if not email or not pas:
                print("\nBoth email and password are required!")
                return
            
            cur.execute('select * from login where email_id="{}" and password="{}"'.format(email,pas))
            data = cur.fetchone()
            if data==None:
                print('Invalid username or password')
                login()
            else:
                print('\n-------LOGIN SUCCESSFUL ----------')
                start()
        elif acc in ['n', 'no']:
            createacc()
            login()
        else:
            print('Enter valid input!')

        
login()