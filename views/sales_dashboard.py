import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Constants
DATA_FILE = "data/expenses.csv"  # use forward slash or raw string

# Load existing data or create new
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Save data
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Initialize session state
if "expenses_df" not in st.session_state:
    st.session_state.expenses_df = load_data()

# App UI
st.title(" Expense dashboard")

# Expense Entry Form on Main Page
st.subheader("➕ Add a New Expense")
with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0, step=0.5)
    with col2:
        category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Others"])
        description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")
    if submitted:
        new_entry = {
            "Date": date.strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        new_df = pd.DataFrame([new_entry])
        st.session_state.expenses_df = pd.concat([st.session_state.expenses_df, new_df], ignore_index=True)
        save_data(st.session_state.expenses_df)
        st.success("✅ Expense added!")

# Display Data
st.subheader("📋 Expense History")
st.dataframe(st.session_state.expenses_df)

# Summary Chart
if not st.session_state.expenses_df.empty:
    st.subheader("📊 Expense Summary")
    category_sum = st.session_state.expenses_df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_sum)

    fig, ax = plt.subplots()
    ax.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.info("No expenses recorded yet.")
