import sqlite3 
from cgitb import reset
from flask import Flask, render_template, request, redirect
import csv
from os.path import exists
import os

def saveDetails():  
    msg = "msg"  
    print("=====Inserting=====")

    with open('pizza.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        orderlist=[]
        amountlist=[]
        pricelist=[]
        list0=[[],[],[]]
        orderNo=0
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

            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name,price,profit))
            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name1,price1,profit1))
            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name2,price2,profit2))
            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name3,price3,profit3))
            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name4,price4,profit4))
            # cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name5,price5,profit5))

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

saveDetails()