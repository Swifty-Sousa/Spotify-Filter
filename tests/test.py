import os
def main():
    a=["a","b","c"]
    os.system("g++ -std=c++11 test.cpp")
    a=input(os.system("./a.out"))
    print("recived number")
    print(a)

main()