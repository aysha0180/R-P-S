import streamlit as st

# Define operations
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Cannot divide by zero"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Streamlit UI
st.title("🧮 Streamlit Calculator")
st.markdown("Welcome to the **Streamlit Calculator**. Select an operation and do your math!")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
operation = st.selectbox("Pick an operation", list(operations.keys()))
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Calculate
if st.button("Calculate"):
    result = operations[operation](num1, num2)
    st.success(f"Result: {num1} {operation} {num2} = {result}")
