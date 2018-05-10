import traceback

try:
    print("try...")
    r = 10/0
    print("result:", r)
except ZeroDivisionError as e:
    print("except:",traceback.print_exc(e))
    #raise
finally:
    print("finally....")
print("end")


