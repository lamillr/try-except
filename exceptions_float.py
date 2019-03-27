# You're doing great! Just one more task but it's a bigger one.
#Add a try block before where you turn your arguments into floats.
#Then add an except to catch the possible ValueError. Inside the except block, return None.
#If you're following the structure from the videos, add an else: for your final return of the added floats.

def add(num1,num2):
    try:
        fl_num1=float(num1)
        fl_num2=float(num2)
    except ValueError:
        return None
    else:
        return fl_num1 +fl_num2
