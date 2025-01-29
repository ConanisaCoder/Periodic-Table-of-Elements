import random
from Elements_Data import *
from Element_Dict import * 
from Elements_Dict_num import *
def elementfunc_element(Element):
    print(f"(1) Atomic Number\n(2) Symbol\n(3) Boiling point\n(4) Family \n(5) All")
    while True:
        try:
            option = int(input("Enter Choice: "))
            break
        except ValueError:
            print("Enter Int")
    match option:
        case 1:
            return (f"Atomic Number : {(Element['Atomic Number'])}")
        case  2:
            return (f"Symbol : {(Element['Symbol'])}")
        case  3:
            return (f"Boiling point: {(Element['Boiling point'])}")
        case 4:
            return (f"Family : {(Element['Family'])}")
        case 5:
            tuplevaule = (f"Atomic Number : {(Element['Atomic Number'])}"), (f"Symbol : {(Element['Symbol'])}"), (f"Boiling point: {(Element['Boiling point'])}"), (f"Family : {(Element['Family'])}") 
            return "\n".join(tuplevaule)
def element_return_num(number_of_element):
    '''Enter amount amout of elements '''
    '''Store in List'''
    List = []
    for i in range(number_of_element):
        while True:
            try:
                element_number = int(input("Enter element number: "))
                break
            except ValueError:
                print("Enter Int")
        if element_number > 118:
            element_number = 118
        else:
            element_number = element_number
        vaule = elements_dict_num[element_number]
        List.append("Element Number "+ str(element_number) +" : "+ vaule )
    return "\n".join(List)
    ''' Number / Proton Number and Return the Element'''
# enter_elem = input("Enter element: ")
# print(elementfunc((elements_dictonary[enter_elem]))) return and print vaule