# Periodic Table of Elements

## Elements.py

#### Elementsfunc_element(Element)

This Function needs Variable as a Parameter that is Stored in Elements_Data.py . It allows user input and lets the program return 5 string values with Information on that Element

In the (Element) parameter you enter a variable stored in Elements_Data.py File. 

The program returns a print statement f"(1) Atomic Number\n(2) Symbol\n(3) Boiling point\n(4) Family \n(5) All".

You enter the Option Var, if the is not Option == int, the try except statement makes you try again. If the option var > 5, the Option Var is set to five and if the Option Var < 1, The option is set to 1. 

Match option Case 1: Returns The Val of The Atomic Number Stored in Elements_Data.py in the form of The Formatted String  (f"Atomic Number : {(Element['Atomic Number'])}").

Match option Case 2: Returns The Val of The Symbol Stored in Elements_Data.py in the form of The Formatted String(f"Symbol : {(Element['Symbol'])}")

Match option Case 3: Returns the Val of The Boiling Point stored in Elements_Data.py in the form of The Formatted String (f"Boiling point: {(Element['Boiling point'])}"

Match option Case 4: Returns the Val of Family stored in Elements_Data.py in the form of The formatted String return (f"Family : {(Element['Family'])}")

Match option Case 5: Stores all the Mentioned vaules above in a tuple called tuple Vaule which looks like
tuplevaule = (f"Atomic Number : {(Element['Atomic Number'])}"), (f"Symbol : {(Element['Symbol'])}"), (f"Boiling point: {(Element['Boiling point'])}"), (f"Family : {(Element['Family'])}"). 

Then it joins the tuple and seprated each vaule that separted with a new line which looks like
return "\n".join(tuplevaule).

### element_num_return_element(number_of_element):

This function is a Function that takes the Parameter of how many Elements you want you return. It creates a list for int vals to be stored. A range is run for the user to eneter the element_number. Using the Try , except Statement if the input is not an int val the program makes you try again. If the Element Number is greated than 118 the element_number = 118. 
The program then stores a variable called Value which  = element_dict_num[element_num] *element_dict_num is from the Elements_Dict_num.py*. 
It then adds this this value to list in a string List.append("Element Number "+ str(element_number) +" : "+ vaule ). When the Loop is done it joins these values using the New Line "\n"
