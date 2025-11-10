import streamlit as st
import math

class Calculator:
    def __init__(self):
        self.operations = {}
        self.init()

    def init(self):
        self.operations["+"] = self.add
        self.operations["-"] = self.subtract
        self.operations["*"] = self.multiply
        self.operations["/"] = self.divide

    # Basic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def add_operation(self, symbol, func):
        self.operations[symbol] = func

    def calculate(self, num1, op, num2):
        if op not in self.operations:
            return "Invalid operation"
        return self.operations[op](num1, num2)

# Advanced operations
def exponent(base, exp):
    return base ** exp

def square_root(number, _):
    return math.sqrt(number)

def logarithm(number, base):
    return math.log(number, base)

# ---- Streamlit UI ----

st.title("Simple Streamlit Calculator")

calc = Calculator()
calc.add_operation("^", exponent)
calc.add_operation("sqrt", square_root)
calc.add_operation("log", logarithm)

operations = list(calc.operations.keys())

num1 = st.number_input("Enter first number", value=0.0)
op = st.selectbox("Choose operation", operations)

# Handle second input
if op == "sqrt":
    num2 = 0
else:
    num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    try:
        result = calc.calculate(num1, op, num2)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
