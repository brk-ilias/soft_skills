import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import os

# Page configuration
st.set_page_config(
    page_title="Bag Store - Customer Support", page_icon="👜", layout="wide"
)

# Custom CSS
st.markdown(
    """
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #3276EA;
        margin-bottom: 1rem;
    }
    .product-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .price {
        font-size: 1.5rem;
        font-weight: bold;
        color: #3276EA;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown('<h1 class="main-header">👜 Premium Bag Store</h1>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; font-size: 1.2rem; color: #666;">Find your perfect bag with our AI-powered customer support</p>',
    unsafe_allow_html=True,
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Our Collection")

    # Product showcase
    prod_col1, prod_col2, prod_col3 = st.columns(3)

    with prod_col1:
        img_path = "assets/leather_tote.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Classic Leather Tote**")
        st.markdown('<p class="price">$129.99</p>', unsafe_allow_html=True)
        st.write("Premium leather construction with spacious interior")
        if st.button("Add to Cart", key="bag1"):
            st.success("Added to cart!")

    with prod_col2:
        img_path = "assets/designer_backpack.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Designer Backpack**")
        st.markdown('<p class="price">$89.99</p>', unsafe_allow_html=True)
        st.write("Modern design with laptop compartment")
        if st.button("Add to Cart", key="bag2"):
            st.success("Added to cart!")

    with prod_col3:
        img_path = "assets/evening_clutch.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Evening Clutch**")
        st.markdown('<p class="price">$59.99</p>', unsafe_allow_html=True)
        st.write("Elegant design perfect for special occasions")
        if st.button("Add to Cart", key="bag3"):
            st.success("Added to cart!")

    st.markdown("---")

    # Additional products
    prod_col4, prod_col5, prod_col6 = st.columns(3)

    with prod_col4:
        img_path = "assets/travel_duffle.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Travel Duffle**")
        st.markdown('<p class="price">$149.99</p>', unsafe_allow_html=True)
        st.write("Durable travel companion with multiple compartments")
        if st.button("Add to Cart", key="bag4"):
            st.success("Added to cart!")

    with prod_col5:
        img_path = "assets/crossbody_bag.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1564422170194-896b89110ef8?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Crossbody Bag**")
        st.markdown('<p class="price">$79.99</p>', unsafe_allow_html=True)
        st.write("Perfect for hands-free convenience")
        if st.button("Add to Cart", key="bag5"):
            st.success("Added to cart!")

    with prod_col6:
        img_path = "assets/business_briefcase.jpg"
        if not os.path.exists(img_path):
            img_path = "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop"
        st.image(img_path, width="stretch")
        st.markdown("**Business Briefcase**")
        st.markdown('<p class="price">$199.99</p>', unsafe_allow_html=True)
        st.write("Professional leather briefcase for business")
        if st.button("Add to Cart", key="bag6"):
            st.success("Added to cart!")

with col2:
    st.header("💬 Customer Support")
    st.write("Have questions? Chat with our AI assistant!")

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

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>Premium Bag Store</strong> | Quality Bags for Every Occasion</p>
    <p>📧 support@bagstore.com | 📞 1-800-BAG-STORE | 📍 123 Fashion Ave, New York, NY</p>
    <p>© 2025 Premium Bag Store. All rights reserved.</p>
</div>
""",
    unsafe_allow_html=True,
)
