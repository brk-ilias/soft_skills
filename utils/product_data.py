"""Product data and management utilities"""

PRODUCTS = [
    {
        "id": 1,
        "name": "Classic Leather Tote",
        "price": 129.99,
        "description": "Premium leather construction with spacious interior",
        "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=400&h=400&fit=crop",
        "category": "Tote Bags",
        "in_stock": True,
        "rating": 4.5,
        "reviews": 128,
    },
    {
        "id": 2,
        "name": "Designer Backpack",
        "price": 89.99,
        "description": "Modern design with laptop compartment",
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop",
        "category": "Backpacks",
        "in_stock": True,
        "rating": 4.7,
        "reviews": 256,
    },
    {
        "id": 3,
        "name": "Evening Clutch",
        "price": 59.99,
        "description": "Elegant design perfect for special occasions",
        "image": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=400&h=400&fit=crop",
        "category": "Clutches",
        "in_stock": True,
        "rating": 4.3,
        "reviews": 89,
    },
    {
        "id": 4,
        "name": "Travel Duffle",
        "price": 149.99,
        "description": "Durable travel companion with multiple compartments",
        "image": "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=400&h=400&fit=crop",
        "category": "Travel Bags",
        "in_stock": True,
        "rating": 4.8,
        "reviews": 342,
    },
    {
        "id": 5,
        "name": "Crossbody Bag",
        "price": 79.99,
        "description": "Perfect for hands-free convenience",
        "image": "https://images.unsplash.com/photo-1564422170194-896b89110ef8?w=400&h=400&fit=crop",
        "category": "Crossbody",
        "in_stock": True,
        "rating": 4.6,
        "reviews": 175,
    },
    {
        "id": 6,
        "name": "Business Briefcase",
        "price": 199.99,
        "description": "Professional leather briefcase for business",
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop",
        "category": "Briefcases",
        "in_stock": True,
        "rating": 4.9,
        "reviews": 421,
    },
    {
        "id": 7,
        "name": "Canvas Tote",
        "price": 39.99,
        "description": "Eco-friendly canvas with reinforced handles",
        "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=400&h=400&fit=crop",
        "category": "Tote Bags",
        "in_stock": True,
        "rating": 4.2,
        "reviews": 93,
    },
    {
        "id": 8,
        "name": "Mini Backpack",
        "price": 69.99,
        "description": "Compact and stylish for everyday use",
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop",
        "category": "Backpacks",
        "in_stock": True,
        "rating": 4.4,
        "reviews": 167,
    },
]


def get_all_products():
    """Return all products"""
    return PRODUCTS


def get_product_by_id(product_id):
    """Get a specific product by ID"""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def get_products_by_category(category):
    """Filter products by category"""
    return [p for p in PRODUCTS if p["category"] == category]


def get_categories():
    """Get all unique categories"""
    return list(set(p["category"] for p in PRODUCTS))


def search_products(query):
    """Search products by name or description"""
    query = query.lower()
    return [
        p
        for p in PRODUCTS
        if query in p["name"].lower() or query in p["description"].lower()
    ]
