from CustomPymata4 import *
from os.path import exists
import time
import sqlite3 
from cgitb import reset
import csv

# board = CustomPymata4(com_port="COM5", baud_rate=57600)
board = CustomPymata4(com_port="/dev/cu.usbserial-1420", baud_rate=57600)

# light, buzzer and buttons
board.set_pin_mode_digital_output(4)
board.set_pin_mode_digital_output(5)
board.set_pin_mode_digital_output(3)
board.set_pin_mode_digital_output(7)
board.set_pin_mode_digital_input_pullup(9)
orderNo=[]

while True:
    time.sleep(1)
    board.digital_write(7,1)
    if board.digital_read(9)[0] == 0:
        t = 5
        try: 
            with open('order.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row)
                    orderNo.append(row['Order'])



            with sqlite3.connect("project.db") as con:  
                cur = con.cursor()
                print(orderNo[-1])
                cur.execute("UPDATE KitchenScreen SET status='yellow' WHERE order_no=(?)",(orderNo[-1]))
                cur.execute("UPDATE CustomerScreen SET status='yellow' WHERE token_no=(?)",(orderNo[-1]))
                # cur.execute("UPDATE KitchenScreen SET status='green' WHERE KitchenScreen.order_no=(?)",(int(orderNo[-1])))
                # cur.execute("UPDATE CustomerScreen SET status='green' WHERE CustomerScreen.token_no=(?)",(int(orderNo[-1])))
                con.commit()  
                print("=====Updated=====")
        except:  
            con.rollback()  
            print("=====Not updated=====") 
        finally:
            print("=====Done arduino=====")  
            con.close()
        board.digital_write(7,0)
        board.digital_write(4,1)
        while t > -1:
            mins, secs = divmod(t, 60)
            timer = '{:02d}.{:02d}'.format(mins, secs)
            board.displayShow(timer)
            time.sleep(1)
            t -= 1
        count = 20
        try:
            with sqlite3.connect("project.db") as conn:  
                curr = conn.cursor()
                # cur.execute("UPDATE KitchenScreen SET status='yellow' WHERE order_no=(?)",(orderNo[-1]))
                # cur.execute("UPDATE CustomerScreen SET status='yellow' WHERE token_no=(?)",(orderNo[-1]))
                curr.execute("UPDATE KitchenScreen SET status='green' WHERE order_no=(?)",(orderNo[-1]))
                curr.execute("UPDATE CustomerScreen SET status='green' WHERE token_no=(?)",(orderNo[-1]))
                conn.commit()  
                print("=====Updated=====")
        except:  
            conn.rollback()  
            print("=====Not updated=====") 
        finally:
            print("=====Done arduino=====")  
            conn.close()
        while count > 0:
            board.digital_write(4,0)
            board.digital_write(5,1)
            board.digital_write(3,1)
            time.sleep(0.1)
            board.digital_write(3,0)
            board.digital_write(5,0)
            time.sleep(0.1)
            count -= 1
    



    
    
