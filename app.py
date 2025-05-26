import streamlit as st

# ----- Sample Mock Data -----
mock_profiles = {
    "Jane Doe": {
        "status": "Denied",
        "score": 620,
        "threshold": 650,
        "factors": [
            ("✅", "Regular mobile payments"),
            ("❌", "No formal income verification"),
            ("❌", "Short credit history")
        ],
        "recommendations": [
            "Upload your recent utility bill or payslip",
            "Connect a mobile wallet to boost your profile",
            "Request re-evaluation in 7 days"
        ]
    },
    "John Musa": {
        "status": "Approved",
        "score": 700,
        "threshold": 650,
        "factors": [
            ("✅", "Verified NIN + BVN"),
            ("✅", "Stable income source"),
            ("✅", "Strong repayment history")
        ],
        "recommendations": [
            "Loan approved – funds disbursed",
            "Keep your records up to date",
            "Monitor repayment schedule on dashboard"
        ]
    }
}

# ----- Streamlit App Interface -----
st.set_page_config(page_title="LendaBank Credit Clarity Portal", layout="centered")
st.title("💡 LendaBank Credit Clarity Portal")

# Input
st.markdown("Other details would have been collected during the real application process. In this demo, we will use" \
" a mock profile to demonstrate the decision-making process.")
name = st.text_input("Enter Customer Name")

if name in mock_profiles:
    profile = mock_profiles[name]
    st.subheader(f"Loan Decision: {'✅ Approved' if profile['status'] == 'Approved' else '❌ Denied'}")
    st.write(f"**Credit Score:** {profile['score']} / **Threshold:** {profile['threshold']}")

    st.markdown("### 🔍 Top Factors")
    for icon, reason in profile["factors"]:
        st.markdown(f"- {icon} **{reason}**")

    st.markdown("### 📌 What You Can Do")
    for step in profile["recommendations"]:
        st.markdown(f"- {step}")

else:
    st.warning("Customer not found. Try 'Jane Doe' or 'John Musa'.")

# Footer
st.markdown("---")
st.caption("Powered by Explainable AI · LendaBank Prototype · v1.0 . Team Analysts")
