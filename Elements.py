import random
from Elements_data import *
from Elements_List import * 

def elementfunc(Element):
    print("What would like to know about The Element" + str(Element) + "\n(1) Atomic Number\n(2) Symbol\n(3) Melting Point\n(4) Family")
    while True:
        try:
            option = int(input("Enter Choice: "))
            break
        except ValueError:
            print("Enter Int")
    if option == 1:
        return (f"Atomic Number : {(Element['Atomic Number'])}")
    elif option == 2:
        return (f"Symbol : {(Element['Symbol'])}")
    elif option == 3:
        return (f"Melting Point : {(Element['Melting Point'])}")
    elif option == 4:
        return (f"Family : {(Element['Family'])}")
def get_element(num=1):
    pass

