import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Support - Bag Store", page_icon="💬", layout="wide")

# Custom CSS
st.markdown(
    """
<style>
    .support-header {
        text-align: center;
        color: #3276EA;
        margin-bottom: 2rem;
    }
    .faq-item {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    .contact-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        background-color: #f9f9f9;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<h1 class="support-header">💬 Customer Support</h1>', unsafe_allow_html=True
)
st.markdown(
    '<p style="text-align: center; font-size: 1.2rem; color: #666;">We\'re here to help you!</p>',
    unsafe_allow_html=True,
)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🤖 Chat with our AI Assistant")
    st.write("Get instant answers to your questions!")

    # Botpress chatbot integration
    chatbot_html = """
    <head>
        <script src="https://cdn.botpress.cloud/webchat/v3.3/inject.js"></script>
        <style>
          #webchat .bpWebchat {
            position: unset;
            width: 100%;
            height: 100%;
            max-height: 100%;
            max-width: 100%;
          }

          #webchat .bpFab {
            display: none;
          }
        </style>
    </head>
    <body>
        <div id="webchat" style="width: 100%; height: 600px;"></div>
        <script>
          window.botpress.on("webchat:ready", () => {
            window.botpress.open();
          });
          window.botpress.init({
          "botId": "b64a1f4f-ff95-49e0-8eee-eb8241cabb3c",
          "configuration": {
            "version": "v2",
            "botName": "Customer Support Agent",
            "botDescription": "",
            "website": {},
            "email": {},
            "phone": {},
            "termsOfService": {},
            "privacyPolicy": {},
            "color": "#3276EA",
            "variant": "solid",
            "headerVariant": "glass",
            "themeMode": "light",
            "fontFamily": "inter",
            "radius": 4,
            "feedbackEnabled": false,
            "footer": "[⚡ by Botpress](https://botpress.com/?from=webchat)",
            "soundEnabled": false,
            "proactiveMessageEnabled": false,
            "proactiveBubbleMessage": "Hi! 👋 Need help?",
            "proactiveBubbleTriggerType": "afterDelay",
            "proactiveBubbleDelayTime": 10
          },
          "clientId": "55df48d2-4f03-4dbb-bc17-e1068b13137b",
          "selector": "#webchat"
        });
        </script>
    </body>
    """

    components.html(chatbot_html, height=650, scrolling=False)

with col2:
    st.markdown("### 📞 Contact Information")

    st.markdown(
        """
        <div class="contact-card">
            <h3>📧 Email</h3>
            <p>support@bagstore.com</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="contact-card">
            <h3>📱 Phone</h3>
            <p>1-800-BAG-STORE</p>
            <p style="font-size: 0.9rem; color: #666;">Mon-Fri: 9AM-6PM EST</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="contact-card">
            <h3>📍 Address</h3>
            <p>123 Fashion Ave<br>New York, NY 10001</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🕒 Business Hours")
    st.write("**Monday - Friday:** 9:00 AM - 6:00 PM EST")
    st.write("**Saturday:** 10:00 AM - 4:00 PM EST")
    st.write("**Sunday:** Closed")

# FAQ Section
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")

faqs = [
    {
        "question": "What is your return policy?",
        "answer": "We offer a 30-day return policy for all unused items in original condition with tags attached. Shipping costs are non-refundable.",
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 5-7 business days. Express shipping (2-3 days) and overnight shipping are also available at checkout.",
    },
    {
        "question": "Do you ship internationally?",
        "answer": "Yes! We ship to over 50 countries worldwide. International shipping times vary by location (7-14 business days typically).",
    },
    {
        "question": "How can I track my order?",
        "answer": "Once your order ships, you'll receive a tracking number via email. You can use this to track your package on our website or the carrier's site.",
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept all major credit cards (Visa, Mastercard, Amex, Discover), PayPal, and Apple Pay.",
    },
    {
        "question": "Are your bags genuine leather?",
        "answer": "Yes! All our leather bags are made from 100% genuine leather. We also offer vegan leather alternatives in select styles.",
    },
]

for i, faq in enumerate(faqs):
    with st.expander(f"**{faq['question']}**"):
        st.write(faq["answer"])

# Contact Form
st.markdown("---")
st.markdown("### 📝 Send us a Message")

with st.form("contact_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name *")
        email = st.text_input("Email *")

    with col2:
        subject = st.text_input("Subject *")
        category = st.selectbox(
            "Category",
            [
                "General Inquiry",
                "Order Status",
                "Product Question",
                "Returns",
                "Technical Issue",
                "Other",
            ],
        )

    message = st.text_area("Message *", height=150)

    submitted = st.form_submit_button(
        "Send Message", use_container_width=True, type="primary"
    )

    if submitted:
        if not all([name, email, subject, message]):
            st.error("Please fill in all required fields!")
        else:
            st.success(
                "✅ Message sent successfully! We'll get back to you within 24 hours."
            )
            st.balloons()

# Quick navigation
st.markdown("---")
st.markdown("### 🧭 Quick Navigation")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛍️ Shop", use_container_width=True):
        st.switch_page("pages/1_🛍️_Shop.py")
with col2:
    if st.button("🛒 Cart", use_container_width=True):
        st.switch_page("pages/2_🛒_Cart.py")
with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")
