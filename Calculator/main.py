from tkinter import *
from tkinter import messagebox

class calculator:
    def __init__(self, root):
        self.master = root
        self.master.title("Calculator")
        self.master.geometry("400x600") # Adjusted height slightly
        self.master.resizable(0,0)
        
        # State variables
        self.expression = ""
        self.text_input = StringVar()
        
        # Build the UI
        self.create_widgets()
        
    def create_widgets(self):
        # 1. Create Display
        input_frame = self.create_display()
        input_frame.pack(side=TOP, fill=BOTH) 

        # 2. Create Buttons
        btns_frame = self.create_buttons()
        btns_frame.pack()

    def create_display(self):
        # Creates a frame to hold the text entry
        frame = Frame(self.master, height=100, bg="lightgray")
        
        # The screen widget
        display = Entry(frame, textvariable=self.text_input, font=('arial', 20, 'bold'), 
                        justify='right', bd=10, insertwidth=4)
        display.pack(expand=True, fill=BOTH, padx=10, pady=10)
        
        return frame

    def create_buttons(self):
        frame = Frame(self.master)
        
        # The Layout Plan (Text, Row, Column)
        buttons_layout = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        # Loop to create buttons automatically
        for (text, row, col) in buttons_layout:
            b = Button(frame, text=text, width=8, height=3, font=('arial', 12, 'bold'),
                       # We use lambda to pass the specific 'text' value to the function
                       command=lambda t=text: self.on_button_click(t))
            
            b.grid(row=row, column=col, padx=5, pady=5)
            
        return frame

    def on_button_click(self, char):
        # Logic to handle button presses
        try:
            if char == 'C':
                self.expression = ""  # Clear internal memory
                self.text_input.set("") # Clear screen
            elif char == '=':
                # Calculate result
                # str(eval(...)) converts the math result back to string for the screen
                total = str(eval(self.expression))
                self.text_input.set(total)
                self.expression = total # Store result so we can continue calculating
            else:
                # Append the number/operator to the expression
                self.expression += str(char)
                self.text_input.set(self.expression)
                
        except ZeroDivisionError:
            self.text_input.set("Error")
            self.expression = ""
        except SyntaxError:
            self.text_input.set("Error")
            self.expression = ""

# --- Run the App ---
if __name__ == "__main__":
    root = Tk()
    app = calculator(root)
    root.mainloop()