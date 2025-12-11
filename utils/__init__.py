"""
Initialize utility modules
"""

from .product_data import (
    get_all_products,
    get_product_by_id,
    get_products_by_category,
    get_categories,
    search_products,
)

from .cart_manager import (
    initialize_cart,
    add_to_cart,
    remove_from_cart,
    update_quantity,
    get_cart_items,
    get_cart_total,
    get_cart_count,
    clear_cart,
    checkout,
)

__all__ = [
    # Product functions
    "get_all_products",
    "get_product_by_id",
    "get_products_by_category",
    "get_categories",
    "search_products",
    # Cart functions
    "initialize_cart",
    "add_to_cart",
    "remove_from_cart",
    "update_quantity",
    "get_cart_items",
    "get_cart_total",
    "get_cart_count",
    "clear_cart",
    "checkout",
]
