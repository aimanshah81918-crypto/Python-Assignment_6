#CLASS TASK .PY
'''#QUESTION NO 1
#STUDENT PROFILE SUSTEM
name=input("ENTER YOUR NAME:")
print("NAME:",name)
age=int(input("ENTER YOUR AGE:"))
print("AGE:",age)
city=input("ENTER CITY NAME:")
print("CITY:",city)
course=input("ENTER COURSE NAME:")
print("COURSE:",course)
total_marks=int(input("ENTER TOTAL MARKS:"))
print("TOTAL MARKS:",total_marks)
obtaine_marks=int(input("ENTER OBTAINE MARKS:"))
print("OBTAINSD MARKS:",obtaine_marks)
percentage=obtaine_marks*100/total_marks
print("PERCENTAGE:",percentage)
print(type(name),type(age),type(city),type(course),type(total_marks),type(obtaine_marks),type(percentage))'''
'''
#QUESTION NO 2
#USERNAME GENRATOR
first_name=input("ENTER YOUR FIRST NAME:")
last_name=input("ENTER YOUR LAST NAME:")
birth_year=int(input("ENTER YOUR BIRTH YEAR:"))
username=first_name+last_name
print("USERNAME:",username)
print("USERNAME",len("AMEENASHAH"))
print(username[:1])
print(username[9:])'''
'''#QUESTION NO 3
#SMART CALCULATOR
num_1=int(input("ENTER FIRST NUMBER:"))
num_2=int(input("ENTER SECOUND NUMBER:"))
print("ADDITION:",num_1+num_2)
print("SUBTRACTION:",num_1-num_2)
print("MULTIPLACTION:",num_1*num_2)
print("DIVISION:",num_1/num_2)
print("MODULUS:",num_1%num_2)
print("EXPONENT:",num_1**num_2)
'''
'''#QUESTION NO 4
#STRING ANALYZER
sentence=input("ENTER YOUR SENTENCE:")
print("sentence:",sentence.upper())
print("sentence:",sentence.lower())
print("sentence",sentence.capitalize())
print("sentence",sentence.count("L"))
print("sentence:",sentence.replace("WORLD","PAKISTAN"))
print("reverse",sentence[::-1])'''
'''
#QUESTION NO 5
#EMAIL CHEAKER SYSTEM
email=input("ENTER YOUR EMAIL:")
print(email.endswith(".COM"))
print("USERNAME",email[:6])
print(len(email))'''
'''#QUESTION NO 6
#SHOPPING BILL GENARATER
product_name=input("ENTER PRODUCT NAME:")
price=float(input("ENTER PRICE:"))
quantity=int(input("ENTER QUANTITY:"))
total_bill=price*quantity
discount=total_bill*10/100
final_bill=total_bill-discount
print("TOTAL BILL",total_bill)
print("DISCOUNT",discount)
print("FINAL BILL",final_bill)
'''
'''#QUESTION NO 7
#MINI BIO DATA CARD
age=int(input("ENTER YOUR AGE:"))
city=input("ENTER CITY NAME: ")
course=input("ENTER COURSE NAME:")
print("\n===========BIO CARD==========")
print("COURSE\t:"+course,"\nCITY\t:"+city)
print("AGE\t:"+str(age))
'''
'''#QUESTION  NO 8
#PASSWORD STRENGHT CHEAKER
password=input("ENTER YOUR PASSWPRD:")
print("password lenght:",len("PASSWORD:"))
print("contains @","@ in PASSWORD")
print("first 3 characters:",password[:3])
print("last 3 characters",password[-3:])'''
'''#QUESTION NO 9
#MOVIE TICKET STSTEM
movie=input("ENTER MOVIE NAME:")
price=int(input("ENTER TICKET PRICE:"))
quantity=int(input("ENTER TICKETS QUANTITY:"))
total_bill=price*quantity
print("MOVIE",movie)
print("PRICE",price)
print("QUANTITY",quantity)
print("TOTAL BILL",total_bill)
'''
'''#QUESTION NO 10
#ONLINE  ORDER FOOD SYSTEM
customer_name=input("ENTER YOUR NAME:")
food=input("ENTER FOOD ITEM:")
price=float(input("ENTER PRICE"))
quantity=int(input("ENTER YOUR QUANTITY"))
total_bill=price*quantity
delivery_charges=total_bill*5/100
final_bill=total_bill+delivery_charges
print("CUSTOMER NAME:",customer_name.upper())
print("FOOD:",food.upper())
print("TOTAL BILL:", total_bill)
print("DELIVERY CHARGES:",delivery_charges)
print("FINAL BILL:",final_bill)
'''