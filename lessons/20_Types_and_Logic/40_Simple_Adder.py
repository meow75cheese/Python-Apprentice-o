"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog, Tk
# Import the required modules

# Create a window object
window = Tk()

# Hide the window, hint: use the withdraw method
window.withdraw()

# Ask the user for the first number  
n1 = simpledialog.askfloat("","enter a number")

# Ask the user for the second number
n2 = simpledialog.askfloat("","enter another number")

# Display the sum of the two numbers 
messagebox.showinfo("","the sum of those numbers is {}".format(n1+n2))

# Keep the window open
window.mainloop()

