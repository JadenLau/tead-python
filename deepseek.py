print("# Deepseek模拟器\n")
import time
from rational_calc import isRational

print("(Deepseek) Hello, I'm Deepseek. What can I help you today?")
while True:
    e = input('Answer: ')
    print("Thinking...")
    begin_funk = time.time()
    time.sleep(5)
    # if e[0:4] == "run ":
    #    eval(e[5:len(e)])
    end_funk = time.time() # think mistake -> funk
    print(f"(回应用时{round(end_funk-begin_funk,2)}秒): \033[91mServer is busy. Please try again later.\033[0m\n")
