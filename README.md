# 👜 Premium Bag Store - Multi-Page Streamlit Application

A fully functional e-commerce web application built with Streamlit featuring AI-powered customer support via Botpress, complete shopping cart, and order management.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🏠 Home Page (`main.py`)
- Attractive landing page with hero section
- Featured products showcase
- Customer testimonials
- Newsletter subscription
- Quick stats and metrics
- Real-time cart indicator

### 🛍️ Shop Page
- Complete product catalog with 8+ products
- Search functionality
- Category filtering (Tote Bags, Backpacks, Clutches, Travel Bags, Crossbody, Briefcases)
- Product ratings and reviews
- Add to cart with quantity selection
- Responsive grid layout

### 🛒 Shopping Cart
- View all cart items
- Update quantities or remove items
- Real-time price calculations
- Full checkout form with validation
- Order confirmation with balloons animation
- Clear cart functionality

### 💬 Customer Support
- Integrated Botpress AI chatbot (24/7)
- Comprehensive FAQ section with expandable items
- Contact form
- Business hours and contact information
- Multiple contact methods (email, phone, address)

### 📦 Order History
- View all past orders
- Detailed order information
- Customer and shipping details
- Order status tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd soft_skills
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

4. Open your browser and navigate to:
```
http://localhost:8501
```

## 📁 Project Structure

```
soft_skills/
├── main.py                 # Home/Landing page
├── pages/
│   ├── 1_🛍️_Shop.py      # Product catalog & shopping
│   ├── 2_🛒_Cart.py       # Shopping cart & checkout
│   ├── 3_💬_Support.py    # Customer support with AI chatbot
│   └── 4_📦_Orders.py     # Order history
├── utils/
│   ├── product_data.py    # Product catalog and search functions
│   └── cart_manager.py    # Cart operations and checkout logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛒 Products Featured

1. **Classic Leather Tote** - $129.99 ⭐4.5 (128 reviews)
2. **Designer Backpack** - $89.99 ⭐4.7 (256 reviews)
3. **Evening Clutch** - $59.99 ⭐4.3 (89 reviews)
4. **Travel Duffle** - $149.99 ⭐4.8 (342 reviews)
5. **Crossbody Bag** - $79.99 ⭐4.6 (175 reviews)
6. **Business Briefcase** - $199.99 ⭐4.9 (421 reviews)
7. **Canvas Tote** - $39.99 ⭐4.2 (93 reviews)
8. **Mini Backpack** - $69.99 ⭐4.4 (167 reviews)

##  Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Botpress](https://botpress.com/)** - AI chatbot platform
- **Python 3.12** - Programming language
- **HTML/CSS** - Custom styling and chatbot integration

##  Chatbot Integration

The application uses Botpress Cloud's webchat widget for customer support. The chatbot features:

- Auto-opens when the page loads
- Blue theme matching the store branding
- Glass header design
- Responds to customer inquiries about products, shipping, and more

### Chatbot Configuration

The chatbot is configured in `main.py` with:
- Bot ID: `b64a1f4f-ff95-49e0-8eee-eb8241cabb3c`
- Client ID: `55df48d2-4f03-4dbb-bc17-e1068b13137b`
- Custom styling to fit seamlessly in the layout

##  Customization

### Adding Your Own Images

1. Replace images in the `assets/` folder with your product photos
2. Keep the same filenames or update paths in `main.py`
3. Recommended image size: 800x800px (square format)

### Changing Colors

Edit the CSS in `main.py` to match your brand:
```python
color: #3276EA  # Change this to your brand color
```

### Updating Products

Modify the product sections in `main.py`:
- Change product names, prices, and descriptions
- Update image paths
- Adjust button labels and messages
