import streamlit as st
from utils.product_data import get_all_products, get_categories, search_products
from utils.cart_manager import add_to_cart, get_cart_count

st.set_page_config(page_title="Shop - Bag Store", page_icon="🛍️", layout="wide")

# Custom CSS
st.markdown(
    """
<style>
    .product-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .price {
        font-size: 1.5rem;
        font-weight: bold;
        color: #3276EA;
    }
    .rating {
        color: #FFD700;
    }
    .cart-badge {
        background-color: #3276EA;
        color: white;
        border-radius: 50%;
        padding: 5px 10px;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header with cart count
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🛍️ Shop Our Collection")
with col2:
    cart_count = get_cart_count()
    st.markdown(
        f"### 🛒 <span class='cart-badge'>{cart_count}</span>", unsafe_allow_html=True
    )

# Search and filter
col1, col2 = st.columns([3, 1])
with col1:
    search_query = st.text_input(
        "🔍 Search products", placeholder="Search by name or description..."
    )
with col2:
    categories = ["All"] + get_categories()
    selected_category = st.selectbox("Category", categories)

# Get products based on filters
if search_query:
    products = search_products(search_query)
else:
    products = get_all_products()

if selected_category != "All":
    products = [p for p in products if p["category"] == selected_category]

# Display products
if not products:
    st.warning("No products found matching your criteria.")
else:
    st.markdown(f"### Showing {len(products)} products")

    # Display products in a grid (3 columns)
    cols_per_row = 3
    for i in range(0, len(products), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(products):
                product = products[i + j]
                with col:
                    st.image(product["image"], use_container_width=True)
                    st.markdown(f"**{product['name']}**")
                    st.markdown(
                        f'<p class="price">${product["price"]:.2f}</p>',
                        unsafe_allow_html=True,
                    )

                    # Rating
                    stars = "⭐" * int(product["rating"])
                    st.markdown(f"{stars} ({product['reviews']} reviews)")

                    st.write(product["description"])

                    # Add to cart with quantity
                    col_qty, col_btn = st.columns([1, 2])
                    with col_qty:
                        qty = st.number_input(
                            "Qty",
                            min_value=1,
                            max_value=10,
                            value=1,
                            key=f"qty_{product['id']}",
                            label_visibility="collapsed",
                        )
                    with col_btn:
                        if st.button(
                            "Add to Cart",
                            key=f"add_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(
                                product["id"], product["name"], product["price"], qty
                            )
                            st.success(f"Added {qty}x to cart!")
                            st.rerun()

                    if not product["in_stock"]:
                        st.error("Out of Stock")

                    st.markdown("---")

# Quick navigation
st.markdown("### 🧭 Quick Navigation")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛒 View Cart", use_container_width=True):
        st.switch_page("pages/2_🛒_Cart.py")
with col2:
    if st.button("💬 Customer Support", use_container_width=True):
        st.switch_page("pages/3_💬_Support.py")
with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")
