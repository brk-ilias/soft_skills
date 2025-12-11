"""Shopping cart management utilities"""

import streamlit as st


def initialize_cart():
    """Initialize the shopping cart in session state"""
    if "cart" not in st.session_state:
        st.session_state.cart = {}
    if "order_history" not in st.session_state:
        st.session_state.order_history = []


def add_to_cart(product_id, product_name, price, quantity=1):
    """Add a product to the cart"""
    initialize_cart()

    if product_id in st.session_state.cart:
        st.session_state.cart[product_id]["quantity"] += quantity
    else:
        st.session_state.cart[product_id] = {
            "name": product_name,
            "price": price,
            "quantity": quantity,
        }


def remove_from_cart(product_id):
    """Remove a product from the cart"""
    initialize_cart()

    if product_id in st.session_state.cart:
        del st.session_state.cart[product_id]


def update_quantity(product_id, quantity):
    """Update the quantity of a product in the cart"""
    initialize_cart()

    if quantity <= 0:
        remove_from_cart(product_id)
    elif product_id in st.session_state.cart:
        st.session_state.cart[product_id]["quantity"] = quantity


def get_cart_items():
    """Get all items in the cart"""
    initialize_cart()
    return st.session_state.cart


def get_cart_total():
    """Calculate the total price of items in the cart"""
    initialize_cart()
    total = sum(
        item["price"] * item["quantity"] for item in st.session_state.cart.values()
    )
    return total


def get_cart_count():
    """Get the total number of items in the cart"""
    initialize_cart()
    return sum(item["quantity"] for item in st.session_state.cart.values())


def clear_cart():
    """Clear all items from the cart"""
    initialize_cart()
    st.session_state.cart = {}


def checkout(customer_info):
    """Process checkout and add to order history"""
    initialize_cart()

    if not st.session_state.cart:
        return False

    order = {
        "items": st.session_state.cart.copy(),
        "total": get_cart_total(),
        "customer": customer_info,
        "order_id": len(st.session_state.order_history) + 1,
    }

    st.session_state.order_history.append(order)
    clear_cart()
    return True
