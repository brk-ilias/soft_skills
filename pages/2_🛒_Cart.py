import streamlit as st
from utils.cart_manager import (
    get_cart_items,
    get_cart_total,
    get_cart_count,
    update_quantity,
    remove_from_cart,
    clear_cart,
    checkout,
)

st.set_page_config(page_title="Cart - Bag Store", page_icon="🛒", layout="wide")

# Custom CSS
st.markdown(
    """
<style>
    .cart-item {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    .total-price {
        font-size: 2rem;
        font-weight: bold;
        color: #3276EA;
    }
    .empty-cart {
        text-align: center;
        padding: 50px;
        color: #666;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🛒 Shopping Cart")

cart_items = get_cart_items()
cart_count = get_cart_count()

if not cart_items:
    st.markdown(
        """
        <div class="empty-cart">
            <h2>Your cart is empty</h2>
            <p>Add some products to get started!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🛍️ Continue Shopping", use_container_width=True):
        st.switch_page("pages/1_🛍️_Shop.py")
else:
    st.markdown(f"### You have {cart_count} item(s) in your cart")

    # Display cart items
    for product_id, item in cart_items.items():
        st.markdown('<div class="cart-item">', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        with col1:
            st.markdown(f"**{item['name']}**")
            st.write(f"Price: ${item['price']:.2f}")

        with col2:
            new_qty = st.number_input(
                "Quantity",
                min_value=0,
                max_value=20,
                value=item["quantity"],
                key=f"qty_{product_id}",
                label_visibility="collapsed",
            )
            if new_qty != item["quantity"]:
                update_quantity(product_id, new_qty)
                st.rerun()

        with col3:
            subtotal = item["price"] * item["quantity"]
            st.write(f"**${subtotal:.2f}**")

        with col4:
            if st.button("🗑️", key=f"remove_{product_id}"):
                remove_from_cart(product_id)
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # Cart summary
    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        if st.button("🗑️ Clear Cart", type="secondary"):
            clear_cart()
            st.rerun()
        if st.button("🛍️ Continue Shopping"):
            st.switch_page("pages/1_🛍️_Shop.py")

    with col2:
        total = get_cart_total()
        st.markdown(
            f'<p class="total-price">Total: ${total:.2f}</p>', unsafe_allow_html=True
        )

    # Checkout section
    st.markdown("---")
    st.markdown("### 📦 Checkout")

    with st.form("checkout_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name *", placeholder="John Doe")
            email = st.text_input("Email *", placeholder="john@example.com")
            phone = st.text_input("Phone *", placeholder="+1 234 567 8900")

        with col2:
            address = st.text_area(
                "Shipping Address *", placeholder="123 Main St\nCity, State 12345"
            )
            payment_method = st.selectbox(
                "Payment Method",
                ["Credit Card", "Debit Card", "PayPal", "Cash on Delivery"],
            )
            notes = st.text_area(
                "Order Notes (Optional)", placeholder="Any special instructions..."
            )

        submitted = st.form_submit_button(
            "🎉 Place Order", use_container_width=True, type="primary"
        )

        if submitted:
            if not all([name, email, phone, address]):
                st.error("Please fill in all required fields!")
            else:
                customer_info = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "payment_method": payment_method,
                    "notes": notes,
                }

                if checkout(customer_info):
                    st.success("🎉 Order placed successfully!")
                    st.balloons()
                    st.info("You will receive a confirmation email shortly.")

                    # Show order summary
                    st.markdown("### Order Summary")
                    st.write(f"**Order Total:** ${total:.2f}")
                    st.write(f"**Payment Method:** {payment_method}")
                    st.write(f"**Shipping to:** {address}")

                    if st.button("🏠 Return to Home"):
                        st.switch_page("main.py")
                else:
                    st.error("Checkout failed. Please try again.")

# Quick navigation
st.markdown("---")
st.markdown("### 🧭 Quick Navigation")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛍️ Shop", use_container_width=True):
        st.switch_page("pages/1_🛍️_Shop.py")
with col2:
    if st.button("💬 Customer Support", use_container_width=True):
        st.switch_page("pages/3_💬_Support.py")
with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")
