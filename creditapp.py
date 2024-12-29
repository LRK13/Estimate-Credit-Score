import streamlit as st

# Define scoring functions
def payment_history_score(late_payments):
    if late_payments == 0:
        return 300
    elif late_payments <= 2:
        return 250
    else:
        return 200

def utilization_score(credit_utilization):
    if credit_utilization < 30:
        return 300
    elif credit_utilization < 50:
        return 250
    else:
        return 200

def credit_length_score(years):
    if years >= 10:
        return 200
    elif years >= 5:
        return 150
    else:
        return 100

def debt_to_income_score(income, debt):
    dti_ratio = (debt / income) * 100
    if dti_ratio < 20:
        return 200
    elif dti_ratio < 40:
        return 150
    else:
        return 100

# App Title
st.title("Credit Score Estimator")

# User Inputs
income = st.number_input("Monthly Income ($):", min_value=0.0, step=100.0, value=5000.0)
debt = st.number_input("Total Debt ($):", min_value=0.0, step=100.0, value=2000.0)
credit_utilization = st.slider("Credit Utilization (%)", min_value=0, max_value=100, value=30)
late_payments = st.number_input("Number of Late Payments (past year):", min_value=0, step=1, value=1)
credit_history_length = st.number_input("Length of Credit History (years):", min_value=0, step=1, value=5)

# Calculate Credit Score
if st.button("Estimate Credit Score"):
    total_score = (
        payment_history_score(late_payments) +
        utilization_score(credit_utilization) +
        credit_length_score(credit_history_length) +
        debt_to_income_score(income, debt)
    )
    credit_score = round((total_score / 1000) * 850)

    # Display Results
    st.write(f"### Your Estimated Credit Score: {credit_score}")
    if credit_score > 750:
        st.success("Excellent credit! Keep it up!")
    elif credit_score > 650:
        st.info("Good credit. Consider improving credit utilization or payment history.")
    else:
        st.warning("Fair credit. Focus on timely payments and reducing debt.")

  