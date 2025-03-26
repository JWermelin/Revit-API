# defining a function 
def computepay(hours, rate) :
    # print out the input
    print("In computepay", hours, rate)
    # conditional statement defining overtime pay
    if fh > 40:
        # regular pay is rate times hours
        reg = rate * hours
        # overtime pay is 50% higher than regular pay
        otp = (hours - 40.0) * (rate * 0.5)
        # total pay is regular pay plus overtime
        pay = reg + otp
    # if we dont have any overtime we just have the regular hours
    else:
        pay = hours * rate
    return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

pay = computepay(fh, fr)

print("Pay:", pay)