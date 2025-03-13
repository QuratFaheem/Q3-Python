import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Title and Description
st.title("🔐 Password Strength Checker")
st.markdown("""
### Check the strength of your password!  
Enter a password below, and we'll analyze its security level.
""")

# Input Field in a Responsive Column Layout
col1, col2 = st.columns([3, 2])  # Wider column for input, smaller for padding
with col1:
    password = st.text_input("Enter your password:", type="password")

# Initialize Variables
feedback = []
score = 0

# Password Strength Checks
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    if re.search(r'[!@%$&^]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character [!@%$&^].")

    # Display Password Strength Level
    st.markdown("### Password Strength:")
    if score == 4:
        st.success("✅ Strong password!")
    elif score == 3:
        st.warning("🟡 Medium strength password.")
    else:
        st.error("🟠 Weak password. Improve it using the suggestions below.")

    # Display Feedback
    if feedback:
        with st.expander("💡 Improvement Suggestions", expanded=True):
            for tip in feedback:
                st.write(tip)

else:
    st.info("🔑 Enter your password to analyze its strength.")

