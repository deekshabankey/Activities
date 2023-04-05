"""
Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
"""
t_amount=float(input("assets: "))
i=input("prime member? ")
def dis(t_amount,i):
    if(i=='yes' or i=='YES'):
        discount_1 = 0.15*t_amount
        total=t_amount-discount_1
        discount_2 = 0.08*total
        t_1 = total-discount_2
        return t_1
    else:
        d_2 = 0.08*t_amount
        t_2 = t_amount-d_2
        return t_2
print('final amount: ',dis(t_amount,i))
