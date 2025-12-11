import streamlit as st
from utils.cart_manager import initialize_cart, get_cart_count
from utils.product_data import get_all_products

# Initialize session state
initialize_cart()

# Page configuration
st.set_page_config(page_title="Premium Bag Store - Home", page_icon="👜", layout="wide")

# Custom CSS
st.markdown(
    """
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        color: #3276EA;
        margin-bottom: 1rem;
    }
    .hero-section {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }
    /* Feature / Testimonial cards: ensure readable text on light backgrounds */
    .feature-card {
        border: 1px solid #e6e6e6;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06);
        background-color: #ffffff;
        color: #222222; /* dark text for contrast */
        height: 100%;
    }
    .feature-card h3 {
        color: #111111;
        margin-bottom: 8px;
    }
    .feature-card p {
        color: #333333;
        margin-bottom: 0.5rem;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        display: block;
    }
    .cta-button {
        background-color: #3276EA;
        color: white;
        padding: 15px 40px;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .product-preview {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .product-preview:hover {
        transform: scale(1.05);
    }
    .cart-indicator {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #3276EA;
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        z-index: 1000;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
</style>
""",
    unsafe_allow_html=True,
)

# Cart indicator
cart_count = get_cart_count()
if cart_count > 0:
    st.markdown(
        f'<div class="cart-indicator">🛒 {cart_count} items</div>',
        unsafe_allow_html=True,
    )

# Header
st.markdown('<h1 class="main-header">👜 Premium Bag Store</h1>', unsafe_allow_html=True)

# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Welcome to Your Bag Destination</h2>
        <p style="font-size: 1.3rem; margin-bottom: 30px;">
            Discover premium quality bags for every occasion. From elegant clutches to professional briefcases.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Welcome to Your Bag Destination</h2>
        <p style="font-size: 1.3rem; margin-bottom: 30px;">
            Discover premium quality bags for every occasion. From elegant clutches to professional briefcases.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# CTA Buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    col_shop, col_support = st.columns(2)
    with col_shop:
        if st.button("🛍️ Start Shopping", use_container_width=True, type="primary"):
            st.switch_page("pages/1_🛍️_Shop.py")
    with col_support:
        if st.button("💬 Get Support", use_container_width=True):
            st.switch_page("pages/3_💬_Support.py")

st.markdown("---")

# Features Section
st.markdown("### ✨ Why Choose Us?")
feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)

with feat_col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <h3>Premium Quality</h3>
            <p>Handcrafted bags made from the finest materials</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with feat_col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🚚</div>
            <h3>Free Shipping</h3>
            <p>Free delivery on orders over $100</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with feat_col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">↩️</div>
            <h3>Easy Returns</h3>
            <p>30-day hassle-free return policy</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with feat_col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI Support</h3>
            <p>24/7 intelligent customer assistance</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Featured Products
st.markdown("### 🔥 Featured Products")
products = get_all_products()[:3]  # Show first 3 products

prod_cols = st.columns(3)
for i, product in enumerate(products):
    with prod_cols[i]:
        st.markdown('<div class="product-preview">', unsafe_allow_html=True)
        st.image(product["image"], use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"**${product['price']:.2f}**")
        stars = "⭐" * int(product["rating"])
        st.caption(f"{stars} ({product['reviews']} reviews)")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("View All Products →", use_container_width=True):
        st.switch_page("pages/1_🛍️_Shop.py")

st.markdown("---")

# Testimonials
st.markdown("### 💬 What Our Customers Say")
test_col1, test_col2, test_col3 = st.columns(3)

with test_col1:
    st.markdown(
        """
        <div class="feature-card">
            <p style="font-style: italic; margin-bottom: 15px;">
                "Absolutely love my new leather tote! The quality is outstanding and it arrived faster than expected."
            </p>
            <p><strong>- Sarah M.</strong></p>
            <p>⭐⭐⭐⭐⭐</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with test_col2:
    st.markdown(
        """
        <div class="feature-card">
            <p style="font-style: italic; margin-bottom: 15px;">
                "Best online shopping experience! The AI support helped me find the perfect bag for my needs."
            </p>
            <p><strong>- Michael R.</strong></p>
            <p>⭐⭐⭐⭐⭐</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with test_col3:
    st.markdown(
        """
        <div class="feature-card">
            <p style="font-style: italic; margin-bottom: 15px;">
                "Great selection and prices! The briefcase I bought has become my favorite work companion."
            </p>
            <p><strong>- Jennifer L.</strong></p>
            <p>⭐⭐⭐⭐⭐</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Newsletter Signup
st.markdown("### 📧 Stay Updated")
st.write("Subscribe to our newsletter for exclusive deals and new arrivals!")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.form("newsletter_form"):
        email = st.text_input("Email Address", placeholder="your.email@example.com")
        subscribe = st.form_submit_button(
            "Subscribe", use_container_width=True, type="primary"
        )

        if subscribe:
            if email:
                st.success("✅ Thank you for subscribing!")
            else:
                st.error("Please enter a valid email address")

st.markdown("---")

# Quick Stats
stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Happy Customers", "10,000+", "+1,234")

with stat_col2:
    st.metric("Products Sold", "25,000+", "+2,456")

with stat_col3:
    st.metric("Countries Served", "50+", "+3")

with stat_col4:
    st.metric("Average Rating", "4.8⭐", "+0.2")


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
