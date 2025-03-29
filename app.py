#
# import streamlit as st
#
# st.title("AI-Powered Customer Support Chatbot 🤖")
# st.write("Ask a question, and I'll try to help!")
#
# user_input = st.text_input("Enter your query here:")
# if st.button("Get Response"):
#     st.success(f"Response: AI-generated response for '{user_input}'")


import streamlit as st

# Define some example responses
responses = {
    "where is my order": "Your order is being processed. You can track it in your account.",
    "i want a refund": "Please visit the returns section on our website or contact support for assistance.",
    "how to reset my password": "Click on 'Forgot Password' on the login page and follow the instructions.",
    "what is your return policy": "You can return any item within 30 days of purchase. Terms and conditions apply.",
    "I can’t log into my account. What should I do? ": "Try resetting your password. If the issue persists, contact customer support.",
    "How do I update my email address?":" Go to ‘Account Settings’ > ‘Email’ and update your email. A verification link will be sent to confirm the change.",
"How do I delete my account?": "To request account deletion, go to ‘Account Settings’ > ‘Delete Account’ or contact support.",
    "Do you have a warranty on your products? ":" Yes, we offer a warranty on most products. Check the product page or contact support for details"
}

st.title("AI-Powered Customer Support Chatbot 🤖")
st.write("Ask a question, and I'll try to help!")

# Get user input
user_input = st.text_input("Enter your query here:")

# Generate response
if st.button("Get Response"):
    user_input = user_input.lower().strip()  # Normalize text
    response = responses.get(user_input, "I'm not sure. Please contact support.")
    st.success(f"Response: {response}")

