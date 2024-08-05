import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="kayroze",charset="utf8",autocommit=True)
cur=db.cursor()
cur.execute("create database if not exists irctc")
cur.execute("use irctc")
cur.execute("create table if not exists user_record(username varchar(30) primary key,password varchar(30))")
cur.execute("create table if not exists user_ticket(id int primary key,name varchar(50) ,age varchar(4),sex varchar(2),train varchar(30),pnr varchar(15))")

cur.execute("create table if not exists user_food(id int primary key,name varchar(30) , food_ordered varchar(30))")
import random
print('''

                   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                 .                 
               .    . . . .             
              .   .      .
    . . . . .    . . . .                                     WELCOME TO Indian Railways Catering and Tourism Corporation                                              
  . 
.
 .
   .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

''')

cur=db.cursor()



def register():
     print("""
=====================================
 PLEASE REGISTER IN THE IRCTC PORTAL
=====================================
                """)
     rname=input("enter user name :")
     rpassword=input("enter password  :")
     cur.execute("insert into user_record values('"+rname+"','"+rpassword+"')")
     
                 
     print("""
===============================
   REGISTERED SUCCESSFULLY
===============================
               """)
     db.commit()
     
                 


def login():
     print("""
==============================
         {{LOG IN }}  
==============================
     """)
     lname=input("entered registered name :")
     lpassword=input("enter password : ")
     cur.execute("select * from user_record")
     row=tuple(cur.fetchall())
     
        
     if (lname,lpassword) in row:
           print("""
===============================
       LOGIN SUCCESSFUL
===============================
               """)

          
            
     else:
          print("INVALID USERNAME OR PASSWORD")
          print("PLEASE TRY AGAIN OR IF NEW USER THEN REGISTER YOURSELF")
          login()
     db.commit()         

         
print("CHOOSE FROM A WIDE RANGES OF TRAINS AND ORDER FOOD FROM HERE")

def check():
    print(" YOU CAN CHECK YOUR PNR STATUS ")
    choice=int(input('''
                 1=check pnr
                 2=TO CHECK TRAIN BETWEEN STATIONS ,COST OF TRAIN,TIME OF ARRIVAL
                 3=EXIT :'''))




    
    if choice==1:
          b=input("enter your 10 digit code no :")
          cur.execute("select pnr from user_ticket")
          data = cur.fetchall()
          
          PNRS = []
          for d in data:
               PNRS.append(d[0])
               
          if b in PNRS:
               print(' YOUR TRAIN TICKET IS RESERVED ,YOUR TRAIN IS ON TIME')
          else:
               print("PNR not found in database")
          
               
          






        
    if choice==3:
        print("(:we hope you enjoyed our service have a nice and safe journey :)")



    if choice==2:
        print(''' (:SEE YOUR TRAIN HERE:)
             ------------------------------------------------------------------------------------------------------------------------------------------------
             -sr    -   train                  -  types of seat  - departure    - arrival    -   cost per ticket-time         - time         -              
             -num   -    name and number       -  available      - place        - place      -   (respectively) -of depature  - of arrival   -                     
             -----------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                      -                      
             - 01   - rajdhani express(23450)   -A.C              - ahemdabad    - mumbai     - 1100             -8:30am       -8:00pm       -                                                                                                                                                          -
             - 02   - duronto express(27659     -A.C              - mumbai       - delhi      - 1200             -9:00pm       -5:00am       -                       
             - 03   - golden chairiot(54760)    -A.C              - delhi        - mumbai     - 500              -10:00pm      -5:45am       -                 
             - 04   - shatabdi express(99421)   -A.C              - mumbai       - ahemdabad  - 2000             -6:00am       -6:55pm       -                         
             - 05   - tejas express(990980      -A.C              - kolkata      - chennai    - 540              -7:00am       -7:45pm       -                
             - 06   - bharat express(25671)     -A.C              - chennai      - banglore   - 680              -8:45pm       -7:00am       -                      
             - 07   - jan shatabdi(17825)       -A.C              - banglore     - hyderabad  - 700              -7:30pm       -8:00am       -                              
             - 08   - gatiman express(99761)    -A.C              - hyderabad    - allahbad   - 760              -5:20pm       -9:00am       -                                   
             - 09   - suvidha expess(75748)     -A.C              - allahbad     - kolkata    - 600              -4:30am       -1:54pm       -                           
             - 10   - gujrat mail(83440)        -A.C              - ahemdabad    - manipur    - 230              -3:15pm       -12:43am      -                     
             - 11   - humsafar express(99240)   -A.C              - manipur      - uri        - 250              -4:55am       -9:36pm       -                                                                
             - 12   - vivek express(44013)      -A.C              - uri          - surat      - 321              -3:40am       -7:56pm       -             
             - 13   - navyug express(50017)     -A.C              - surat        - assam      - 630              -2:00pm       -2:48am       -                
             - 14   - yuva express(88601)       -A.C              - assam        - amritsar   - 780              -1:00am       -8:43am       -                  
             - 15   - uday express(67849)       -A.C              - amritsar     - merut      - 670              -9:00pm       -3:00pm       -                
             - 16   - deccan oddessy(67476)     -A.C              - hydrabad     - odisha     - 1000             -5:45am       -4:34am       -                
             - 17   - kranti express(98799)     -A.C              - odisha       - pune       - 548              -6:30pm       -8:34am       -                        
             - 18   - maharashtra mail(95897)   -A.C              - pune         - ratnagiri  - 900              -4:35am       -5:42pm       -                     
             - 19   - goa express(749890)       -A.C              - goa          - chandigarh - 599              -6:30am       -3:32pm       -                  
            -----------------------------------------------------------------------------------------------------------------------------------------------------------                           

                ''')



        
def admin():
     foo=int(input('''enter your choice:
                    1.food
                    2. book ticket'''))




        
     if foo==1:
          h=input("enter your name :")
          d=int(input('''
                           1.water=rs20,
                           2.lunch meal=rs200,
                           3.dinner meal=rs250,
                           4.breakfast=rs100
                           5.all the above stuff=rs550 :'''))



           
          if d==1:
               print('''you have selected,water ,price to pay is RS20''')
               food='water'

               
          elif d==2:
               print('''you have selected ,lunch,price to pay is RS200''')
               food='lunch'

               
          elif d==3 :               
               print('''you have selected,dinner,prices to pay is RS250''')
               food='dinner'


               
          elif d==4 :
               print('''you have selected,breakfast,prices to pay is RS100''')
               food='breakfast'

               
          elif d==5:
               print("you have entered all the things ,so amount payable is RS550")
               food='complete package(breakfast+lunch+dinner+water)' 
               
          else:
               print("sorry we don't have anything like that" )
               
          cur.execute("insert into user_food values('"+str(c)+"','"+h+"','"+food+"')")
          db.commit()     

     else:
          e=int(input('''------------------------------------------------------------------------------------------------------------------------------------------------
             -sr    -   train                  -  types of seat  - departure    - arrival    -  cost per ticket -time         - time        -              
             -num   -    name and number       -  available      - place        - place      -  (respectively)  -of depature  - of arrival  -                     
             -----------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                      -                      
             - 01   - rajdhani express(23450)   -A.C             - ahemdabad    - mumbai     - 1100             -8:30am       -8:00pm       -                                                                                                                                                          -
             - 02   - duronto express(27659     -A.C             - mumbai       - delhi      - 1200             -9:00pm       -5:00am       -                       
             - 03   - golden chairiot(54760)    -A.C             - delhi        - mumbai     - 500              -10:00pm      -5:45am       -                 
             - 04   - shatabdi express(99421)   -A.C             - mumbai       - ahemdabad  - 2000             -6:00am       -6:55pm       -                         
             - 05   - tejas express(990980      -A.C             - kolkata      - chennai    - 540              -7:00am       -7:45pm       -                
             - 06   - bharat express(25671)     -A.C             - chennai      - banglore   - 680              -8:45pm       -7:00am       -                      
             - 07   - jan shatabdi(17825)       -A.C             - banglore     - hyderabad  - 700              -7:30pm       -8:00am       -                              
             - 08   - gatiman express(99761)    -A.C             - hyderabad    - allahbad   - 760              -5:20pm       -9:00am       -                                   
             - 09   - suvidha expess(75748)     -A.C             - allahbad     - kolkata    - 600              -4:30am       -1:54pm       -                           
             - 10   - gujrat mail(83440)        -A.C             - ahemdabad    - manipur    - 230              -3:15pm       -12:43am      -                     
             - 11   - humsafar express(99240)   -A.C             - manipur      - uri        - 250              -4:55am       -9:36pm       -                                                                
             - 12   - vivek express(44013)      -A.C             - uri          - surat      - 321              -3:40am       -7:56pm       -             
             - 13   - navyug express(50017)     -A.C             - surat        - assam      - 630              -2:00pm       -2:48am       -                
             - 14   - yuva express(88601)       -A.C             - assam        - amritsar   - 780              -1:00am       -8:43am       -                  
             - 15   - uday express(67849)       -A.C             - amritsar     - merut      - 670              -9:00pm       -3:00pm       -                
             - 16   - deccan oddessy(67476)     -A.C             - hydrabad     - odisha     - 1000             -5:45am       -4:34am       -                
             - 17   - kranti express(98799)     -A.C             - odisha       - pune       - 548              -6:30pm       -8:34am       -                        
             - 18   - maharashtra mail(95897)   -A.C             - pune         - ratnagiri  - 900              -4:35am       -5:42pm       -                     
             - 19   - goa express(749890)       -A.C             - goa          - chandigarh - 599              -6:30am       -3:32pm       -                  
            -----------------------------------------------------------------------------------------------------------------------------------------------------------                           

              select your train from above'''))


           
           
          if e==1 :
               print("you have selected train - 01 rajdhani express(23450)and seat selected is in A.C train per ticket cost is RS1100")
               cost=1100
               train='rajdhani express'
                
                
          elif e==2:
               print("you have selected train -02 duronto express(27659) and seat selected is in A.C train  your per ticket cost is RS1200 ")
               cost=1200
               train='duronto express'
                
          elif e==3:
               print("you have selected train- 03  golden chairiot(54760) and seat selected is in A.C train your per ticket cost is RS500")
               cost=500
               train='golden chairot' 
                
          elif e==4:
               print("you have selected train - 04 shatabdi express(99421)   and seat seected is in A.C train  your per ticket cost is RS2000")
               cost=2000
               train='shatabdi express'
                
          elif e==5 :
               print("you have selected train - 05  tejas express(990980) and seat selected is in A.C train  your per ticket cost is RS540")
               cost=540
               train='tejas express' 
                
          elif e==6:
               print("you have selected train - 06 bharat express(25671)  and seat selected is in A.C train  your per ticket cost is RS680")
               cost=680
               train='bharat express'
           
          elif e==7:
               print("you have selected train - 07 jan shatabdi(17825)    and seat selected is in A.C train  your per ticket cost is RS700")
               cost=700
               train='jan shatabdi'
           
           
          elif e==8:
               print("you have selected train  - 08 gatiman express(99761)   and seat selected is in A.C train  your per ticket cost is RS760")
               cost=760
               train='gatiman express'

           
           
          elif e==9 :
               print("you have selected train - 09 suvidha expess(75748) and seat selected is in A.C train  your per ticket cost is RS600")
               cost=600
               train='suvidha express'
           
           
          elif  e==10:
               print("you have selected train - 10  gujrat mail(83440) and seat selected is in A.C train  your per ticket cost is RS230")
               cost=230
               train='gujrat mail'
           
          elif e==11:
               print("you have selected train- 11  humsafar express(99240) and seat selected is in A.C train  your per ticket cost is RS250")
               cost=250
               train='humsafar express'
          
           
          elif e==12:
               print("you have selected train- 12 vivek express(44013) and seat selected is in A.C train  your per ticket cost is RS321")
               cost=321
               train='vivek express'
           
          elif e==13 :
               print("you have selected train   - 13 navyug express(50017)  and seat selected is in A.C train  your per ticket cost is RS630")
               cost=630
               train='navyuk express'
           
          elif e==14:
                print("you have selected train  - 14 yuva express(88601)  and seat selected is in A.C train your per ticket cost is RS780")
                cost=780
                train='yuva express'
           
          elif e==15:
                print("you have selected train - 15  uday express(67849)  and seat selected is in A.C train  your per ticket cost is RS670")
                cost=670
                train='uday express'

           
          elif e==16:
                print("you have selected train- 16 deccan oddessy(67476) and seat selected is in A.C train  your per ticket cost is RS1000")
                cost=1000
                train='deccan express'

           
          elif e==17:
                print("you have selected train- 17  kranti express(98799)  and seat selected is in A.C train  your per ticket cost is RS548")
                cost=548
                train='kranti express'
           
          elif e==18:
                print("you have selected train - 18 maharashtra mail(95897) and seat selected is in A.C train  your per ticket cost is RS900")
                cost=900
                train='maharashtra mail'
           
          elif e==19:
                print("you have selected train- 19 goa express(749890) and seat selected is in A.C train  your per ticket cost is RS599")
                cost=599
                train='goa express'

          else:
                print("no trains found")



           
           
          Names = []
          Ages = []
          Sexs = []
          Pnrs = []

          nlen = alen = plen = 0

          Pnr = None
          

          inputs = int(input("How many tickets do you want to buy ? : "))
          for i in range(inputs):
               Name = input("Enter Name :")
               Names.append(Name)
               if len(Name) > nlen:
                    nlen = len(Name)
               Age = int(input("Enter Age :"))
               Ages.append(Age)
               if len(str(Age)) > alen:
                    alen = len(str(Age))
               Sex = input("Enter Sex(M/F) :")
               Sexs.append(Sex)
               while True:
                    
                    Pnr = random.randint(1000000000,9999999999)
                    if Pnr not in Pnrs:
                         Pnrs.append(Pnr)
                    
                         break
               if len(str(Pnr)) > plen:
                    plen = len(str(Pnr))                  
               print("-"*20)
           

          T = nlen + alen + plen 
          print("|"+(" "*((nlen - 4)//2)) + "Name" + " "*(nlen % 2 != 0) + (" "*((nlen - 4)//2)) + "| Age | Sex | Coach | Seat |" +" "*((plen-3)//2) + "PNR")
          print("-"*(T+30))
          seat = 10
          for i in range(len(Names)):
               cur.execute("select * from user_ticket")
               Data = cur.fetchall()
               r = random.randint(10000,99999)
               for j in range(len(Data)):
                    
                    if Data[j][0] in R:
                         R.append(r)
               while r in R:
                    
                    r = random.randint(10000,99999)
               
               newstr="|" + str(Names[i]) + (" "*(nlen-len(Names[i]))) + "|" + " "*(len(str(Ages[i]))% 2 == 0) + "  "*(len(str(Ages[i])) % 2 != 0) + str(Ages[i])
               newnewstr="  |  " + str(Sexs[i]) + "  |" + "   D1  |  " + str(seat) + "  | " + str(Pnrs[i]) + "|"
               print(newstr+newnewstr)
               seat += 1
               cur.execute("insert into user_ticket values('"+str(r)+"','"+str(Names[i])+"','"+str(Ages[i])+"','"+Sexs[i]+"','"+train+"','"+str(Pnrs[i])+"')")
               db.commit()
          print("-"*(T+30))
          print("Per ticket cost = ",cost,"\nTotal cost  = ",cost*inputs)  

def cancel():
    print('PRESS(1)TO CANCEL FOOD BOOKING')
    print('PRESS(2) TO CANCEL TRAIN BOOKING')
    canc=int(input("ENTER YOUR CHOICE:"))

    
    if canc ==1:
         print('IF YOU DO NOT KNOW YOUR ID THEN GO TO SEARCH')
         idf=input("ENTER YOUR ID :")
         statmt = "DELETE FROM user_food WHERE id = %s"
         cur.execute(statmt, (idf,))
         for i in cur:
              print(i)
         db.commit() 
         print("The Food has been cancelled succesfully")
         
         
         
    elif canc ==2:
         print('IF YOU DO NOT KNOW YOUR PNR THEN GO TO SEARCH')
         can=input("Enter your 10 digit PNR number:")
         statmt = "DELETE FROM user_ticket WHERE pnr = %s"
         cur.execute(statmt, (can,))
         for i in cur:
              print(i)
         db.commit() 
        
         print("The ticket has been cancelled succesfully")
         print('THANKYOU FOR USING IRCTC PORTAL')
         
         
         
  
         
         
    else:
         print("SORRY YOU HAVEN'T ENTERED ANY INPUT ")
         print('THANKYOU FOR USING IRCTC PORTAL')
    

    db.commit()

def search():
     sea=int(input('''
press (1) for user records
press (2) for user food table
press (3) for user ticket table:'''))
     if sea ==1:
          print("you have selected user record table")
          se=input("enter username to search :")
          print("FIRST COLUMN SIGNIFIES USERNAME ")
          print("SECOND COLUMN SIGNIFIES PASSWORD")
          cur.execute("SELECT * FROM user_record WHERE username LIKE %s ", ("%" + se + "%",))
          for i in cur:
               print(i)
     if sea ==2:
          print("you have selected user food table")
          pq=int(input('''
press (1) to search with ID
press (2) to search with name
press (3) to search with food ordered'''))
          if pq==1:
               se=input("enter id to search :")
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES FOOD ORDERED")
               
               cur.execute("SELECT * FROM user_food WHERE id LIKE %s ", ("%" + se + "%",))
               abc= cur.fetchall
               for i in cur:
                    print(i)
          if pq==2:
               
               se=input("enter name to search :")
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES FOOD ORDERED")
               cur.execute("SELECT * FROM user_food WHERE name LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          if pq==3:
               se=input("enter food to search :")
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES FOOD ORDERED")
               cur.execute("SELECT * FROM user_food WHERE food_ordered LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          
     if sea ==3:
          print("you have selected user ticket table record")
          sq=int(input('''
press (1) to search with ID
press (2) to search with name
press (3) to search with age
press (4) to search with sex
press (5) to search with train
press (6) to search with pnr:'''))
          if sq==1:
               se=input("enter id to search :")
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE id LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          if sq==2:
               
               se=input("enter name to search :")
              
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE name LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          if sq==3:
               se=input("enter age to search :")
               
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE age LIKE %s ", ("%" + se + "%",))
               for i in cur:
                   print(i)
          if sq==4:
               se=input("enter sex to search :")
               
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE sex LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          if sq==5:
               se=input("enter train name to search :")
               
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE train LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          if sq==6:
               se=input("enter pnr to search :")
               
               print("FIRST COLUMN SIGNIFIES ID ")
               print("SECOND COLUMN SIGNIFIES NAME")
               print("THIRD COLUMN SIGNIFIES AGE")
               print("FOURTH COLUMN SIGNIFIES SEX ")
               print("FIFTH COLUMN SIGNIFIES TRAIN")
               print("SIXTH COLUMN SIGNIFIES PNR")
               cur.execute("SELECT * FROM user_ticket WHERE pnr LIKE %s ", ("%" + se + "%",))
               for i in cur:
                    print(i)
          





def update():
     
     up=int(input('''
press (1) for user records
press (2) for user food table
press (3) for user ticket table :'''))
     if up ==1:
          print("You have selected user_record table")
          upd=int(input('''
press(1) to change username
press(2) to change password :'''))
          if upd==1:
               upname=input("entered registered name :")
               uppassword=input("enter password : ")
               cur.execute("select * from user_record")
               row=tuple(cur.fetchall())


               if (upname,uppassword) in row:
                    us=input("enter name to change :")
                    cur.execute("update user_record SET username='{}'  where password='{}'".format(str(us),str(uppassword)))
                    for i in cur:
                         print(i)
                    db.commit()     

               



               else:
                    print("INVALID USERNAME OR PASSWORD")
                    print("PLEASE TRY AGAIN OR IF NEW USER THEN REGISTER YOURSELF THEN TRY AGAIN")

          if upd==2:
               upname=input("entered registered name :")
               uppassword=input("enter password : ")
               cur.execute("select * from user_record")
               row=tuple(cur.fetchall())
     
        
               if (upname,uppassword) in row:
                    us=input("enter password to change :")
             
                    cur.execute("update user_record SET password='{}' where username='{}'".format(str(us),str(upname)))
                    for i in cur:
                         print(i)
                    db.commit()     

               else:
                    print("INVALID USERNAME OR PASSWORD")
                    print("PLEASE TRY AGAIN OR IF NEW USER THEN REGISTER YOURSELF THEN TRY AGAIN")
     
     if up == 2:
          print("You have selected user_food table")
          upd=int(input('''
press(1) to change name
press(2) to change food :'''))
          if upd==1:
               IDS=[]
               NAMES=[]
               FOOD=[]
               uid = int(input("Enter the id :"))
               cur.execute("select * from user_food")
               row=cur.fetchall()
               for i in row:
                    IDS.append(i[0])
                    NAMES.append(i[1])
                    FOOD.append(i[2])
               
               if uid not in IDS:
                    print("ID NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
                    fname=input('Enter name to change :')
                    fid=input('Enter your id again to confirm :')
                    cur.execute("update user_food SET name='{}'  where id='{}'".format(str(fname),str(fid)))
                    for i in cur:
                         print(i)
                    db.commit() 
                    
          if upd==2:
               IDS=[]
               NAMES=[]
               FOOD=[]
               uid = int(input("Enter the id :"))
               cur.execute("select * from user_food")
               row=cur.fetchall()
               for i in row:
                    IDS.append(i[0])
                    NAMES.append(i[1])
                    FOOD.append(i[2])
              
               if uid not in IDS:
                    print("PNR NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
               
                    ffood=input('Enter name of the food to change :')
                    fid=input('Enter your id again  to confirm :')
                    cur.execute("update user_food SET food_ordered='{}'  where id='{}'".format(str(ffood),str(fid)))
                    for i in cur:
                         print(i)
                    db.commit() 

     if up == 3:
          print("You have selected user_ticket table")
          upd=int(input('''
press(1) to change NAME
press(2) to change AGE
press(3) to change SEX
press(4) to change TRAIN :'''))
          if upd==1:
               PNRS=[]
               NAMES=[]
               AGES=[]
               SEXS=[]
               TRAINS=[]
               upnr = input("Enter the pnr :")
               cur.execute("select pnr,name,age,sex,train from user_ticket")
               row=cur.fetchall()
               for i in row:
                    PNRS.append(i[0])
                    NAMES.append(i[1])
                    AGES.append(i[2])
                    SEXS.append(i[3])
                    TRAINS.append(i[4])
               if upnr not in PNRS:
                    print("PNR NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
                    tname=input('Enter name to change :')
                    tpnr=input('Enter your pnr again to confirm :')
                    cur.execute("update user_ticket SET name='{}'  where pnr='{}'".format(str(tname),str(tpnr)))
                    for i in cur:
                         print(i)
                    db.commit() 
          if upd==2:
               PNRS=[]
               NAMES=[]
               AGES=[]
               SEXS=[]
               TRAINS=[]
               upnr = input("Enter the pnr :")
               cur.execute("select pnr,name,age,sex,train from user_ticket")
               row=cur.fetchall()
               for i in row:
                    PNRS.append(i[0])
                    NAMES.append(i[1])
                    AGES.append(i[2])
                    SEXS.append(i[3])
                    TRAINS.append(i[4])
               if upnr not in PNRS:
                    print("PNR NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
                    tage=input('Enter age to change :')
                    tpnr=input('Enter your pnr again confirm :')
                    cur.execute("update user_ticket SET age='{}' where pnr='{}'".format(str(tage),str(tpnr)))
                    for i in cur:
                         print(i)
                    db.commit() 
          if upd==3:
               PNRS=[]
               NAMES=[]
               AGES=[]
               SEXS=[]
               TRAINS=[]
               upnr = input("Enter the pnr :")
               cur.execute("select pnr,name,age,sex,train from user_ticket")
               row=cur.fetchall()
               for i in row:
                    PNRS.append(i[0])
                    NAMES.append(i[1])
                    AGES.append(i[2])
                    SEXS.append(i[3])
                    TRAINS.append(i[4])
               if upnr not in PNRS:
                    print("PNR NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
                    tsex=input('Enter sex to change :')
                    tpnr=input('Enter your pnr again to confirm :')
                    cur.execute("update user_ticket SET sex='{}'  where pnr='{}'".format(str(tsex),str(tpnr)))
                    for i in cur:
                         print(i)
                    db.commit() 
          if upd==4:
               PNRS=[]
               NAMES=[]
               AGES=[]
               SEXS=[]
               TRAINS=[]
               upnr = input("Enter the pnr :")
               cur.execute("select pnr,name,age,sex,train from user_ticket")
               row=cur.fetchall()
               for i in row:
                    PNRS.append(i[0])
                    NAMES.append(i[1])
                    AGES.append(i[2])
                    SEXS.append(i[3])
                    TRAINS.append(i[4])
               if upnr not in PNRS:
                    print("PNR NOT FOUND IN DATABASE. PLEASE TRY AGAIN")
               else:
                    ttrain=input('Enter train to change :')
                    tpnr=input('Enter your pnr again to confirm :')
                    cur.execute("update user_ticket SET train='{}'  where pnr='{}'".format(str(ttrain),str(tpnr)))
                    for i in cur:
                         print(i)
                    db.commit() 
        

def display():
     diss=int(input('''
press (1) to see all records of user record table
press (2) to see all records of user ticket table
press (3) to see all records of user food table :'''))
     if diss==1:
          cur.execute("SELECT * FROM user_record ")
          print("FIRST COLUMN SIGNIFIES USERNAME ")
          print("SECOND COLUMN SIGNIFIES PASSWORD")
          for i in cur:
               print(i)
     if diss==2:
          cur.execute("SELECT * FROM user_ticket ")
          print("FIRST COLUMN SIGNIFIES ID ")
          print("SECOND COLUMN SIGNIFIES NAME")
          print("THIRD COLUMN SIGNIFIES AGE")
          print("FOURTH COLUMN SIGNIFIES SEX ")
          print("FIFTH COLUMN SIGNIFIES TRAIN")
          print("SIXTH COLUMN SIGNIFIES PNR")
          for i in cur:
               print(i)
     if diss==3:
          cur.execute("SELECT * FROM user_food ")
          print("FIRST COLUMN SIGNIFIES ID ")
          print("SECOND COLUMN SIGNIFIES NAME")
          print("THIRD COLUMN SIGNIFIES FOOD ORDERED")
          for i in cur:
               print(i)
         

def Help():
    print('''
              In check section you can check  pnr,CHECK TRAIN BETWEEN STATIONS ,COST OF TRAIN,TIME OF ARRIVAL.
              In admin section you can order food or you can book tickets.
              In cancel section you can cancel your ticket or food
              In search section you can search your ticket or food or userid-password
              In display section you can see the whole table of food , ticket and id/password which you have stored
              In update section you can update your user record,food booking,ticket booking


              :)HOPE THE INFORMATION WAS USEFULL(:

      ''')

   

R = []
C = []
while True:
     cur.execute("select * from user_ticket")
     data = cur.fetchall()
     c = str(random.randint(10000,99999))
     for i in range(len(data)):
          if data[i][0] in C:
               C.append(c)
     while c in C:  
          c = str(random.randint(10000,99999))
     print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ************  ***********  ************ ***********   ************* ")
     print("+    press 1. to check                                       +       *       *         *  *                 *        *             ")
     print("+    press 2. for admin                                      +       *       *         *  *                 *        *             ")
     print("+    press 3. to cancel your ticket                          +       *       *         *  *                 *        *             ")
     print("+    press 4. to get help to understand the program          +       *       ***********  *                 *        *             ")
     print("+    press 5. to search                                      +       *       * *          *                 *        *             ")
     print("+    press 6. to display all records of a table              +       *       *   *        *                 *        *             ")
     print("+    press 7. to update                                      +       *       *     *      *                 *        *             ")
     print("+    press 8. to exit the program                            +       *       *       *    *                 *        *             ")
     print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ************  *         *  ************      *        ************* ")
     a=int(input('Enter your choice :'))
     if a==1:
         
          check()
     if a==2:
          Input = int(input("Choose Option:\n1.Register\n2.Login :"))
          if Input == 1:
               register()
          elif Input == 2:
               login()
          else:
               break
          admin()
     if a==3:
          cancel()
          db.commit()
     if a==4:
          Help()
     if a==5:
          search()
     if a==6:
          display()
     if a==7:
          update()
          
        
     if a==8:
          print(":)hope you must have enjoyed our  great  project:)")
          
          print('''



====================    =               =   =================    =                             =     =              =           =                   =   ================     =            =                    
         =              =               =   =               =    = =                           =     =            =               =               =     =              =     =            =  
         =              =               =   =               =    =   =                         =     =          =                   =           =       =              =     =            =       
         =              =               =   =               =    =     =                       =     =        =                       =       =         =              =     =            =        
         =              =               =   =               =    =       =                     =     =      =                           =   =           =              =     =            =   
         =              =               =   =               =    =         =                   =     =    =                               =             =              =     =            =      
         =              =               =   =               =    =           =                 =     =  =                                 =             =              =     =            =     
         =              =================   =================    =            =                =     =    =                               =             =              =     =            = 
         =              =               =   =               =    =              =              =     =      =                             =             =              =     =            =
         =              =               =   =               =    =                =            =     =        =                           =             =              =     =            =         
         =              =               =   =               =    =                  =          =     =          =                         =             =              =     =            =          
         =              =               =   =               =    =                    =        =     =            =                       =             =              =     =            =       
         =              =               =   =               =    =                      =      =     =              =                     =             =              =     =            =                                                                             
         =              =               =   =               =    =                        =    =     =                =                   =             =              =     =            =   
         =              =               =   =               =    =                          =  =     =                  =                 =             =              =     =            =         
         =              =               =   =               =    =                             =     =                    =               =             ================     ============== 




============================================================================================================================================================================================



                     =================================================================================================================================================




                                          ==============================================================================================================






                                                        ===========================================================================




''')
          break      
        
