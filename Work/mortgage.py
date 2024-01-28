# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
count_extra_payment = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    if principal < 0:
        continue
    # if count_extra_payment >= extra_payment_start_month or count_extra_payment <= extra_payment_end_month:
    #     principal = principal - extra_payment
    #     total_paid = total_paid + extra_payment
    total_paid = total_paid + payment
    count_extra_payment = count_extra_payment + 1
    print(count_extra_payment, total_paid, principal)
    
# print('Total paid', total_paid)