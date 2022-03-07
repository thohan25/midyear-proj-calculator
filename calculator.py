from tkinter import *
import math
import random
class Application(Frame):
    """ GUI Applcation that performs calculations based on user input. """
    def __init__(self, master):
        """ Initialize Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Create and display widgets """
        # stored numbers
        self.number1 = 0
        self.current = ""

        # Entry for input

        self.calc_pad = Entry(self, bg = "#007016", fg = "#000000")
        self.calc_pad.grid(row = 1, column = 0, sticky = N + S + W + E, columnspan = 5, )

        # Simple Buttons:

        #  Number buttons: These buttons range from 0-9, and upon clicking will append the displayed number on the button into the entry "calc_pad"

        number_1_bttn = Button(self, text = "1", command = self.print_num_one, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_2_bttn = Button(self, text = "2", command = self.print_num_two, fg = "#000000", bg = "#b6d8d9",  width = 5)
        number_3_bttn = Button(self, text = "3", command = self.print_num_three, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_4_bttn = Button(self, text = "4", command = self.print_num_four, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_5_bttn = Button(self, text = "5", command = self.print_num_five, fg = "#000000", bg = "#b6d8d9",  width = 5)
        number_6_bttn = Button(self, text = "6", command = self.print_num_six, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_7_bttn = Button(self, text = "7", command = self.print_num_seven, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_8_bttn = Button(self, text = "8", command = self.print_num_eight, fg = "#000000", bg = "#b6d8d9",  width = 5)
        number_9_bttn = Button(self, text = "9", command = self.print_num_nine, fg = "#000000", bg = "#b6d8d9", width = 5)
        number_0_bttn = Button(self, text = "0", command = self.print_num_zero, fg = "#000000", bg = "#b6d8d9", width = 5)
        decimal_bttn = Button(self, text = ".", command = self.print_num_decimal_point, fg = "#000000", bg = "#b6d8d9",  width = 5)
        negative_sign_bttn = Button(self, text = "(-)", command = self.print_num_negative_sign, fg = "#000000", bg = "#b6d8d9", width = 5)

        negative_sign_bttn.grid(row = 8, column = 3,sticky = E)
        decimal_bttn.grid(row = 8, column = 2, sticky = W + E)
        number_0_bttn.grid(row = 8, column = 1, sticky = W)
        number_9_bttn.grid(row = 5, column = 3, sticky = E)
        number_8_bttn.grid(row = 5, column = 2, sticky = W + E)
        number_7_bttn.grid(row = 5, column = 1, sticky = W)
        number_6_bttn.grid(row = 6, column = 3, sticky = E)
        number_5_bttn.grid(row = 6, column = 2, sticky = W + E)
        number_4_bttn.grid(row = 6, column = 1, sticky = W)
        number_3_bttn.grid(row = 7, column = 3, sticky = E)
        number_2_bttn.grid(row = 7, column = 2, sticky = W + E)
        number_1_bttn.grid(row = 7, column = 1, sticky = W)
        
        #  Operator buttons: These buttons include the 4 computational operators, "+/-/*/'/'" and have functions assigned with them

        addition_bttn = Button(self, text = "+", command = self.addition, fg = "#000000", bg = "#c2c2c2",  width = 5)
        subtraction_bttn = Button(self, text = "-", command = self.subtraction, fg = "#000000", bg = "#c2c2c2",  width = 5)
        multiplication_bttn = Button(self, text = "*", command = self.multiplication, fg = "#000000", bg = "#c2c2c2",  width = 5)
        division_bttn = Button(self, text = "/", command = self.division, fg = "#000000", bg = "#c2c2c2",  width = 5)
        equal_sign_bttn = Button(self, text = "=", command = self.print_total, fg = "#FFFFFF", bg = "#FF0000",  width = 5)

        equal_sign_bttn.grid(row = 8, column = 4, sticky = E)
        division_bttn.grid(row = 4, column = 4, sticky = E)
        multiplication_bttn.grid(row = 5, column = 4, sticky = E)
        subtraction_bttn.grid(row = 6, column = 4, sticky = E)
        addition_bttn.grid(row = 7, column = 4, sticky = E)

        # Advanced Buttons

        #  Clear button: This button, upon clicking clears the text in the entry "calc_pad"

        clear_bttn = Button(self, text = "CLEAR", fg = "#FFFFFF", bg = "#FF0000", command = self.clear_text)
        clear_bttn.grid(row = 2, column = 4, sticky = E)

        #  Power button: This button, upon clicking raises a number, n to a specified power, y and displays it in the entry "calc_pad"

        power_bttn = Button(self, text = "^", command = self.exponent, fg = "#FFFFFF", bg = "#08004f", width = 5)
        power_bttn.grid(row = 3, column = 4, sticky = E)

        #  Sin, Cos and Tan buttons: These buttons, upon clicking will perfom the sin(), cos() and tan() functions depending on which button is clicked, along with displayying it in the entry "calc_pad"
        
        sin_bttn = Button(self, text = "sin", command = self.sin, fg = "#FFFFFF", bg = "#08004f")
        cos_bttn = Button(self, text = "cos", command = self.cos, fg = "#FFFFFF", bg = "#08004f")
        tan_bttn = Button(self, text = "tan", command = self.tan, fg = "#FFFFFF", bg = "#08004f")

        tan_bttn.grid(row = 3, column = 3, sticky = E + W)
        cos_bttn.grid(row = 3, column = 2, sticky = W + E)
        sin_bttn.grid(row = 3, column = 1, sticky = W + E)

        #  Parentheses buttons, Comma button: Insert parenthesis, Insert comma

        comma_bttn = Button(self, text = ",", command = self.print_num_comma, fg = "#FFFFFF", bg = "#08004f", width = 5)
        left_parenthesis_bttn = Button(self, text = "(", command = self.print_num_left_parentheses, fg= "#FFFFFF", bg = "#08004f")
        right_parenthesis_bttn = Button(self, text = ")", command = self.print_num_right_parentheses, fg = "#FFFFFF", bg = "#08004f",  width = 5)

        right_parenthesis_bttn.grid(row = 4, column = 3, sticky = E)
        left_parenthesis_bttn.grid(row = 4, column = 2, sticky = W + E)
        comma_bttn.grid(row = 4, column = 1, sticky = W)

        #  Squared button, x**-1: This button multiplies a number, x by itself and displays it in the entry, "calc_pad", this button multiplies a number to the negative 

        squared_bttn = Button(self, text = "x^2", command = self.square, fg = "#FFFFFF", bg = "#08004f")

        squared_bttn.grid(row = 4, column = 0, sticky = W + E)

        #  Log button, ln button: Calculates log(n) of a number, n where base = 10, calculates logx(n) where x is a specified base for ln() to calculate the log of number, n

        ln_bttn = Button(self, text = "ln", command = self.ln, fg = "#FFFFFF", bg = "#08004f", width = 5)
        log_bttn = Button(self, text = "log", command = self.log10, fg = "#FFFFFF", bg = "#08004f", width = 5)

        log_bttn.grid(row = 5, column = 0, sticky = W)
        ln_bttn.grid(row = 6, column = 0, sticky = W)

        #  Sq.rt button: Calculates the square root of a given number or expression, n

        sqrt_bttn = Button(self, text = "sqrt", command = self.sqrt, fg = "#FFFFFF", bg = "#08004f", width = 5)

        sqrt_bttn.grid(row = 7, column = 0, sticky = W)

        #  Random Button: Generates a random number, n based on specified parameters

        random_bttn = Button(self, text = "rand", command = self.rand_num, fg = "#FFFFFF", bg = "#08004f", width = 5)

        random_bttn.grid(row = 2, column = 3, sticky = E)

        #  Delete button: Deletes a character in the entry "calc_pad"

        del_bttn = Button(self, text = "del", command = self.delete_text, fg = "#FFFFFF", bg = "#08004f")

        del_bttn.grid(row = 2, column = 2, sticky = W + E)

        #  Set operations: Operations dealing with or including sets

        # left_braces_bttn = Button(self, text = "{", command = self.print_num_left_braces, fg = "#FFFFFF", bg = "#08004f", width = 5)
        # right_braces_bttn = Button(self, text = "}", command = self.print_num_right_braces, fg = "#FFFFFF", bg = "#08004f", width = 5)
        # union_bttn = Button(self, text = "U", command = self.union, fg = "#FFFFFF", bg = "#08004f", width = 5)
        intersect_bttn = Button(self, text = "∩", command = self.intersect, fg = "#FFFFFF", bg = "#08004f", width = 5)
        infinity_bttn = Button(self, text = "∞", command = self.print_num_infinity, fg = "#FFFFFF", bg = "#08004f", width = 5)
        left_bracket_bttn = Button(self, text = "[", command = self.print_num_left_brackets, fg = "#FFFFFF", bg = "#08004f", width = 5)
        right_bracket_bttn = Button(self, text = "]", command = self.print_num_right_brackets, fg = "#FFFFFF", bg = "#08004f", width = 5)

        right_bracket_bttn.grid(row = 2, column = 1, sticky = W)
        left_bracket_bttn.grid(row = 2, column = 0, sticky = W)
        infinity_bttn.grid(row = 8, column = 0, sticky = W)
        intersect_bttn.grid(row = 3, column = 0, sticky = W)
        # union_bttn.grid(row = 2, column = 5, sticky = N)
        # right_braces_bttn.grid(row = 3, column = 6, sticky = W)
        # left_braces_bttn.grid(row = 3, column = 5, sticky = W)

    def print_num_one(self):
        """Append the number 1, to the entry "calc_pad"""
        self.calc_pad.insert(len(str(self.calc_pad.get)), '1')
    def print_num_two(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '2')
    def print_num_three(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '3')
    def print_num_four(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '4')
    def print_num_five(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '5')
    def print_num_six(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '6')
    def print_num_seven(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '7')
    def print_num_eight(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '8')
    def print_num_nine(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '9')
    def print_num_zero(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '0')
    def print_num_decimal_point(self):
        self.calc_pad.insert(len(str(self.calc_pad.get)), '.')
    def print_num_negative_sign(self):
        self.calc_pad.insert(0, "-")
    def print_num_comma(self):
        pass
    def print_num_left_parentheses(self):
        pass
    def print_num_right_parentheses(self):
        pass
    def print_num_left_braces(self):
        pass
    def print_num_right_braces(self):
        pass
    def print_num_infinity(self):
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', 'Inf')
    def print_num_left_brackets(self):
        pass
    def print_num_right_brackets(self):
        pass
    def addition(self):
        self.number1 = float(self.calc_pad.get())
        self.current = "add"
        self.calc_pad.delete('0', '10000')
    def subtraction(self):
        self.number1 = float(self.calc_pad.get())
        self.current = "sub"
        self.calc_pad.delete('0', '10000')
    def multiplication(self):
        self.number1 = float(self.calc_pad.get())
        self.current = "mult"
        self.calc_pad.delete('0', '10000')
    def division(self):
        self.number1 = float(self.calc_pad.get())
        self.current = "div"
        self.calc_pad.delete('0', '10000')
    def print_total(self):
        num2 = float(self.calc_pad.get())
        if self.current == "add":
            self.calc_pad.delete('0', '10000')
            self.calc_pad.insert('0', self.number1 + num2)
        if self.current == "sub":
            self.calc_pad.delete('0', '10000')
            self.calc_pad.insert('0', self.number1 - num2)
        if self.current == "mult":
            self.calc_pad.delete('0', '10000')
            self.calc_pad.insert('0', self.number1 * num2)
        if self.current == "div":
            self.calc_pad.delete('0', '10000')
            self.calc_pad.insert('0', self.number1 / num2)
        if self.current == "exp":
            self.calc_pad.delete('0', '10000')
            self.calc_pad.insert('0', self.number1 ** num2)
    def clear_text(self):
        self.number1 = 0
        self.current = ""
        self.calc_pad.delete('0', '10000')
    def exponent(self):
        self.number1 = float(self.calc_pad.get())
        self.current = "exp"
        self.calc_pad.delete('0', '10000')
    def sin(self):
        sin = math.sin(float(self.calc_pad.get()))
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', sin)
    def cos(self):
        cos = math.cos(float(self.calc_pad.get()))
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', cos)
    def tan(self):
        tan = math.tan(float(self.calc_pad.get()))
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', tan)
    def square(self):
        square = float(self.calc_pad.get()) ** 2
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', square)
    def ln(self):
        ln = math.log(float(self.calc_pad.get()))
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', ln)
    def log10(self):
        log10 = math.log(float(self.calc_pad.get()), 10)
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', log10)
    def sqrt(self):
        sqrt = math.sqrt(float(self.calc_pad.get()))
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', sqrt)
    def rand_num(self):
        self.calc_pad.delete('0', '10000')
        self.calc_pad.insert('0', random.uniform(0, 1))
    def delete_text(self):
        self.calc_pad.delete(len(str(self.calc_pad.get())) - 1)
    def union(self):
        pass
    def intersect(self):
        pass

root = Tk()
root.title("Calculator GUI")
root.geometry("350x500")
app = Application(root)
root.mainloop()