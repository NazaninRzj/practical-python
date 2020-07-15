principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = int(input("Starting your month"))
extra_payment_end_month = int(input("Ending your month"))
extra_payment = int(input("Extra payment"))

while principal > 0:
    month += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
        extra_payment_start_month += 1

    print(month, round(total_paid, 2), round(principal,2))

print("Total paid=", round(total_paid,1))
print('Months=', month)