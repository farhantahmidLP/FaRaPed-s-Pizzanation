from cgitb import reset
from flask import Flask, render_template, request, redirect
import csv
from os.path import exists
import os
import sqlite3 
from cgitb import reset


app = Flask(__name__)

orderlist =[]
orderNo=0
###############
kitchenorderno = 1
dictionary={}
###dashboard###
user = []
passw = []
loggedin = False

#######################################################
###################Home-Screen#########################
#######################################################

@app.route('/')
def index():
    if not exists("order.csv"):
        with open("order.csv", "a", newline="") as c:
            write = csv.writer(c)
            row = ["Order"]
            write.writerow(row)
    return render_template("index.html")

@app.route('/index')
def ind():
    return render_template("index.html")


#######################################################
######################Menu#############################
#######################################################

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template("menu.html")

if not exists("pizza.csv"):
    with open("pizza.csv", "a", newline="") as c:
        write = csv.writer(c)
        row = ["Orders", "Amount", "Price"]
        write.writerow(row)


@app.route('/menu1', methods=['POST'])
def cart():
    order = request.form['pizza']
    amount = request.form['number']
    price=0

    if(order=="Pepperoni"):
        price=int(amount)*3
    elif(order=="Margherita"):
        price=int(amount)*2
    elif(order=="Meatlovers"):
        price=int(amount)*6
    elif(order=="BBQchicken"):
        price=int(amount)*5
    elif(order=="Salami"):
        price=int(amount)*5
    elif(order=="Vegan"):
        price=int(amount)*4

    with open("pizza.csv", "a", newline="") as c:
        writer = csv.writer(c)
        row = [order, amount, price]
        writer.writerow(row)

    return render_template('menu.html', order=order, amount=amount)

#######################################################
###################Cart################################
#######################################################

@app.route('/cart')
def cart3():
    with open('pizza.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        orderlist=[]
        amountlist=[]
        pricelist=[]
        total=0
        list0=[[],[],[]]
        msg=""
        for row in reader:
            orderlist.append(row['Orders'])
            amountlist.append(row['Amount'])
            pricelist.append(row['Price'])
            list0[0].append(orderlist[-1])
            list0[1].append(amountlist[-1])
            list0[2].append(pricelist[-1])

        for x in list0[2]:
            total=total+int(x)
            
        pName1=""
        pName2=""
        pName3=""
        pName4=""
        pName5=""
        pName6=""
        pName7=""
        pName8=""
        pName9=""
        pName10=""

        pVal1=""
        pVal2=0
        pVal3=0
        pVal4=""
        pVal5=0
        pVal6=0
        pVal7=""
        pVal8=0
        pVal9=0
        pVal10=""
        pVal11=0
        pVal12=0
        pVal13=""
        pVal14=0
        pVal15=0
        pVal16=""
        pVal17=0
        pVal18=0
        pVal19=""
        pVal20=0
        pVal21=0
        pVal22=""
        pVal23=0
        pVal24=0
        pVal25=""
        pVal26=0
        pVal27=0
        pVal28=""
        pVal29=0
        pVal30=0

        prnt=""
        list1 = [list(a) for a in zip(list0[0], list0[1], list0[2])]
        if len(list1)>=10:
            msg="=== Cannot add 10 items at once!!! ==="
            os.remove('pizza.csv')
            with open("pizza.csv", "a", newline="") as c:
                write = csv.writer(c)
                row = ["Orders", "Amount", "Price"]
                write.writerow(row)
            return render_template('cart.html', msg=msg, dictionary=dictionary)

        for i in range(len(list1)):
            prnt = ( '  '.join(str(v) for v in list1[i]))
            if(i==0):
                pName1=prnt
                x = pName1.split()
                pVal1=x[0]
                pVal2=x[1]
                pVal3=x[2]
            elif(i==1):
                pName2=prnt
                x = pName2.split()
                pVal4=x[0]
                pVal5=x[1]
                pVal6=x[2]
            elif(i==2):
                pName3=prnt
                x = pName3.split()
                pVal7=x[0]
                pVal8=x[1]
                pVal9=x[2]
            elif(i==3):
                pName4=prnt
                x = pName4.split()
                pVal10=x[0]
                pVal11=x[1]
                pVal12=x[2]
            elif(i==4):
                pName5=prnt
                x = pName5.split()
                pVal13=x[0]
                pVal14=x[1]
                pVal15=x[2]
            elif(i==5):
                pName6=prnt
                x = pName6.split()
                pVal16=x[0]
                pVal17=x[1]
                pVal18=x[2]
            elif(i==6):
                pName7=prnt
                x = pName7.split()
                pVal19=x[0]
                pVal20=x[1]
                pVal21=x[2]
            elif(i==7):
                pName8=prnt
                x = pName8.split()
                pVal22=x[0]
                pVal23=x[1]
                pVal24=x[2]
            elif(i==8):
                pName9=prnt
                x = pName9.split()
                pVal25=x[0]
                pVal26=x[1]
                pVal27=x[2]
            elif(i==9):
                pName10=prnt
                x = pName10.split()
                pVal28=x[0]
                pVal29=x[1]
                pVal30=x[2]
        dictionary["pName1"]=pName1
        dictionary["pName2"]=pName2
        dictionary["pName3"]=pName3
        dictionary["pName4"]=pName4
        dictionary["pName5"]=pName5
        dictionary["pName6"]=pName6
        dictionary["pName7"]=pName7
        dictionary["pName8"]=pName8
        dictionary["pName9"]=pName9
        dictionary["pName10"]=pName10

    return render_template('cart.html', dictionary=dictionary, pVal1=pVal1, pVal2=pVal2, pVal3=pVal3, pVal4=pVal4, pVal5=pVal5, pVal6=pVal6, pVal7=pVal7, pVal8=pVal8, pVal9=pVal9, pVal10=pVal10, pVal11=pVal11, pVal12=pVal12, pVal13=pVal13, pVal14=pVal14, pVal15=pVal15, pVal16=pVal16, pVal17=pVal17, pVal18=pVal18, pVal19=pVal19, pVal20=pVal20, pVal21=pVal21, pVal22=pVal22, pVal23=pVal23, pVal24=pVal24, pVal25=pVal25, pVal26=pVal26, pVal27=pVal27, pVal28=pVal28, pVal29=pVal29, pVal30=pVal30, total=total)

@app.route('/final', methods=['GET', 'POST'])
def saveDetails():  
    global orderNo
    msg = "msg"  
    print("=====Inserting=====")

    with open('pizza.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        orderlist=[]
        amountlist=[]
        pricelist=[]
        list0=[[],[],[]]
        
        amount=0
        msg=""
        for row in reader:
            orderlist.append(row['Orders'])
            amountlist.append(row['Amount'])
            pricelist.append(row['Price'])
            list0[0].append(orderlist[-1])
            list0[1].append(amountlist[-1])
            list0[2].append(pricelist[-1])

    list1 = [list(a) for a in zip(list0[0], list0[1], list0[2])]

    try: 

        item_name = "Pepperoni"
        price = 3.0
        profit =   1
        item_name1 = "Margherita"
        price1 = 2.00
        profit1 =   1
        item_name2 = "Meatlovers"
        price2 = 6
        profit2 =   1.00
        item_name3 = "BBQchicken"
        price3 = 5
        profit3 =   1.00
        item_name4 = "Salami"
        price4 = 5
        profit4 =   1.00
        item_name5 = "Vegan"
        price5 = 4
        profit5 =   1.00
        
        print(list1)

        with sqlite3.connect("project.db") as con:  
            cur = con.cursor()   

            orderNo=orderNo+1

            for items in list1:
                cur.execute("INSERT into Orders (order_no, item_name, quantity) values (?,?,?)",(orderNo,items[0],items[1]))
                amount=amount+int(items[2])
            cur.execute("INSERT into Cashier (customer_no, amount, profit) values (?,?,?)",(orderNo,amount,items[1]))
            for items in list1:
                cur.execute("INSERT into KitchenScreen (order_no, pizza, quantity, status) values (?,?,?,?)",(orderNo,items[0],items[1],"red"))
            cur.execute("INSERT into CustomerScreen (token_no, status) values (?,?)",(orderNo,"red"))

            con.commit()  
            print("=====Everything successfully Added=====")
    except:  
        con.rollback()  
        print("=====Not Added=====") 
    finally:
        print("=====Done=====")  
        con.close()

    os.remove('pizza.csv')
    with open("pizza.csv", "a", newline="") as c:
        write = csv.writer(c)
        row = ["Orders", "Amount", "Price"]
        write.writerow(row)

    return render_template('thanks.html', orderNo=orderNo)

@app.route('/delete', methods=['GET', 'POST'])
def delete():  
    os.remove('pizza.csv')
    with open("pizza.csv", "a", newline="") as c:
        write = csv.writer(c)
        row = ["Orders", "Amount", "Price"]
        write.writerow(row)

    return redirect('/')

#######################################################
###################Kitchen-Screen######################
#######################################################
@app.route('/kitchenscreen', methods=['POST', 'GET'])
def kitchenscreen():
    global kitchenorderno
    con = sqlite3.connect("project.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select KitchenScreen.pizza, KitchenScreen.quantity from KitchenScreen where KitchenScreen.order_no=(?)", (str(kitchenorderno)))   
    rows = cur.fetchall()  
    with open("order.csv", "a", newline="") as c:
        write = csv.writer(c)
        row=[kitchenorderno]
        write.writerow(row)
    return render_template('kitchenscreen.html', rows=rows)

@app.route('/kitchen2', methods=['POST', 'GET'])
def kitchen2():
    global kitchenorderno
    kitchenorderno = kitchenorderno + 1
    return redirect('/kitchenscreen')

#######################################################
###################Customer-Screen#####################
#######################################################

@app.route('/customerscreen', methods=['POST', 'GET'])
def customerscreen():
    con = sqlite3.connect("project.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select CustomerScreen.token_no, CustomerScreen.status from CustomerScreen")   
    rows = cur.fetchall()  
    return render_template('customerscreen.html', rows=rows)



#######################################################
####################Dashboard##########################
#######################################################


@app.route('/login', methods=['POST', 'GET'])
def login():
    global user, passw
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            user.append(row['username'])
            passw.append(row['passw'])

    return render_template('login.html')

@app.route('/autheticate', methods=['POST', 'GET'])
def autheticate():
    global user, passw, loggedin

    loggedin = False

    username = request.form['username']
    password = request.form['password']

    if username == user[0] and password == passw[0]:
        loggedin = True
        return redirect('/dashboard')


    return render_template('login.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    global loggedin
    con = sqlite3.connect("project.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select sum(Cashier.amount) as Earned, sum(Cashier.profit) as Profit from Cashier")   
    rows = cur.fetchall()  
    if loggedin == True:
        loggedin = False
        return render_template('dashboard.html', rows=rows)
    else:
        return redirect('/login')

@app.errorhandler(405)
def pageNotFound(e):
    return render_template('menu.html'),405


# app.run(host="145.93.57.14",port=8000, debug=True)
app.run()
