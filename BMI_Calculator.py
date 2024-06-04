import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to handle the calculation button press
def calculate():
    # Get weight and height from the entry fields
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    # Classify BMI into categories
    category = classify_bmi(bmi)

    # Update the result label with the calculated BMI and category
    result_text.set("Your BMI is: {:.2f}\nYou are classified as: {}".format(bmi, category))
    
# Function to clear entry fields
def clear_entries():
    weight_entry.delete(0, 'end')
    height_entry.delete(0, 'end')

# Creating the main application window
root = tk.Tk()
root.title("BMI Calculator")

# Labels and entry fields for weight
weight_label = tk.Label(root, text="Enter your Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

# Labels and entry fields for height
height_label = tk.Label(root, text="Enter your Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Button to clear entry fields
clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Label to display the result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the main event loop
root.mainloop()
