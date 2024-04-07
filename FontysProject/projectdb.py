import sqlite3
from tkinter import INSERT  

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

con = sqlite3.connect("project.db")  
print("Database opened successfully") 


con.execute("CREATE TABLE Menu ( item_name	TEXT NOT NULL UNIQUE, price	NUMERIC NOT NULL, profit NUMERIC NOT NULL, PRIMARY KEY(item_name));")  
print("Table Menu created successfully")  

con.execute("CREATE TABLE Orders ( order_no	NUMERIC NOT NULL, item_name	TEXT NOT NULL, quantity	NUMERIC NOT NULL, FOREIGN KEY(item_name) REFERENCES Menu(item_name), PRIMARY KEY(order_no,item_name));")  
print("Table Order created successfully")  

con.execute("CREATE TABLE Cashier ( customer_no	NUMERIC NOT NULL, amount NUMERIC NOT NULL, profit	NUMERIC NOT NULL, FOREIGN KEY(customer_no) REFERENCES Orders(order_no), PRIMARY KEY(customer_no));")  
print("Table Cashier created successfully")  

con.execute("CREATE TABLE KitchenScreen ( order_no	NUMERIC NOT NULL, pizza	TEXT NOT NULL, quantity	NUMERIC NOT NULL, status TEXT NOT NULL, FOREIGN KEY(pizza) REFERENCES Orders(item_name), FOREIGN KEY(order_no) REFERENCES Orders(order_no), PRIMARY KEY(order_no,pizza));")  
print("Table KitchenScreen created successfully")  

con.execute("CREATE TABLE CustomerScreen ( token_no	NUMERIC NOT NULL, status	TEXT NOT NULL, FOREIGN KEY(token_no) REFERENCES KitchenScreen(order_no), PRIMARY KEY(token_no));")  
print("Table CustomerScreen created successfully")



with sqlite3.connect("project.db") as con:  
    cur = con.cursor()   

    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name,price,profit))
    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name1,price1,profit1))
    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name2,price2,profit2))
    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name3,price3,profit3))
    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name4,price4,profit4))
    cur.execute("INSERT into Menu (item_name, price, profit) values (?,?,?)",(item_name5,price5,profit5))

con.close()