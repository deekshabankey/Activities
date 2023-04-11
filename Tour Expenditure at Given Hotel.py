"""
Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.
"""
def trip(Deluxe_Room,day,food):
    if Deluxe_Room == True:
        room_t=7500*day
        tax=0.18*food
    elif Deluxe_Room==False:
        room_t=4500*day
        tax=0.05*food
    tip=0.1*food
    cgst=tax/2
    sgst=tax/2
    total=room_t+tax+food+tip
    print("room_t: INR",round(room_t,2))
    print("GST-CGST=INR",round(cgst,2),"SGST=INR",round(sgst,2))
    print("Tip: INR",round(tip,2))
    print("Grand Total: INR",round(total,2))
    
A=trip(True,4,10050.9)
