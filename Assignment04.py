# Task 1: Read a File and Handle Errors  

# Problem Statement:  Write a Python program that: 
# 1.   Opens and reads a text file named sample.txt. 
# 2.   Prints its content line by line. 
# 3.   Handles errors gracefully if the file does not exist.

def read(read_file):
    try :
        with open(read_file,'r') as f:
            content = f.readlines()
            for n, line in enumerate(content):
                print(f"line:{n+1} {line.strip()}")
    except FileNotFoundError:
        print(f"the file {read_file} does not exist.")
        
read('sample.txt')


# Task 2: Write and Append Data to a File 
  
# Problem Statement: Write a Python program that: 
# 1.   Takes user input and writes it to a file named output.txt. 
# 2.   Appends additional data to the same file. 
# 3.   Reads and displays the final content of the file
 
 
def write():
    with open('output.txt','w') as f:
         user_input = input("enter some text you wants to write in the file output.txt:")
         f.write(user_input + '\n')
         f.write("this i the new line added to the file \n")
    with open('output.txt','a') as f:
                f.write("this line is appended to the file \n")
                print("-"*30)
    with open('output.txt','r') as f:
        con = f.readlines()
        print("the final content of the file output.txt is :")
        for n , line in enumerate(con):
            print(f"line {n+1}: {line.strip()}")
                        
                        
                        
write()
