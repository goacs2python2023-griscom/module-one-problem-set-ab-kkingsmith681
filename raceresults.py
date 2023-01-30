'''You are an olympic athlete who has just finished a race against three opponents.  Write a function that takes all four race times as arguments (your time as the first argument), and returns a string describing the medal you just won ("gold", "silver", "bronze", or "no medal").  No ties!!  '''

def times():
    your_time = float(input("What was your time? (in seconds) "))
    time2 = float(input("What was another competitors time? (in seconds) "))
    time3 = float(input("What was another competitors time? (in seconds) "))
    time4 = float(input("What was another competitors time? (in seconds) "))




def medalPlacement(your_time, time2, time3, time4):
    if your_time > time2 and your_time > time3 and your_time > time4:
        return("You just won the gold medal!")
    elif your_time < time2 and your_time > time3 and your_time > time4 or your_time > time2 and your_time < time3 and your_time > time4 or your_time > time2 and your_time > time3 and your_time < time4:
        return("You just won the silver medal!")
    elif your_time < time2 and your_time < time3 and your_time < time4:
        return("You came 4th!")
    else:
        return("You got the bronze medal!") 

times()

print(medalPlacement(your_time, time2, time3, time4)) 