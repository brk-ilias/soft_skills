import streamlit as st
from utils.cart_manager import initialize_cart

st.set_page_config(page_title="Orders - Bag Store", page_icon="📦", layout="wide")

# Initialize session state
initialize_cart()

# Custom CSS
st.markdown(
    """
<style>
    .order-card {
        border: 1px solid #ddd;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        background-color: #f9f9f9;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .order-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 2px solid #3276EA;
    }
    .order-status {
        background-color: #28a745;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
    }
    .no-orders {
        text-align: center;
        padding: 60px 20px;
        color: #666;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("📦 Order History")

# Get order history from session state
if "order_history" not in st.session_state or not st.session_state.order_history:
    st.markdown(
        """
        <div class="no-orders">
            <h2>No orders yet</h2>
            <p>When you place an order, it will appear here.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🛍️ Start Shopping", use_container_width=True, type="primary"):
        st.switch_page("pages/1_🛍️_Shop.py")
else:
    st.markdown(f"### You have {len(st.session_state.order_history)} order(s)")

    # Display orders (most recent first)
    for order in reversed(st.session_state.order_history):
        st.markdown('<div class="order-card">', unsafe_allow_html=True)

        # Order header
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"### Order #{order['order_id']:04d}")
            st.write(f"**Customer:** {order['customer']['name']}")
        with col2:
            st.markdown(
                '<span class="order-status">✓ Confirmed</span>', unsafe_allow_html=True
            )

        st.markdown("---")

        # Order details
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("#### Items Ordered")
            for product_id, item in order["items"].items():
                st.write(
                    f"• **{item['name']}** - ${item['price']:.2f} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}"
                )

            st.markdown("#### Shipping Information")
            st.write(f"**Address:** {order['customer']['address']}")
            st.write(f"**Phone:** {order['customer']['phone']}")
            st.write(f"**Email:** {order['customer']['email']}")

            if order["customer"].get("notes"):
                st.markdown("#### Order Notes")
                st.write(order["customer"]["notes"])

        with col2:
            st.markdown("#### Order Summary")
            st.write(f"**Payment Method:**")
            st.write(order["customer"]["payment_method"])
            st.markdown(f"### Total: ${order['total']:.2f}")

            # Action buttons
            st.button("📧 Email Receipt", key=f"email_{order['order_id']}")
            st.button("📞 Contact Support", key=f"support_{order['order_id']}")

        st.markdown("</div>", unsafe_allow_html=True)

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
