# 👜 Premium Bag Store - Streamlit Application

A modern e-commerce web application built with Streamlit, featuring an integrated AI-powered customer support chatbot using Botpress.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Product Showcase**: Display 6 premium bag products with high-quality images
- **AI Customer Support**: Integrated Botpress chatbot for real-time customer assistance
- **Responsive Design**: Wide layout optimized for desktop viewing
- **Interactive Shopping**: Add-to-cart functionality with instant feedback
- **Modern UI**: Clean, professional design with custom CSS styling

## 📦 Products Featured

1. **Classic Leather Tote** - $129.99
2. **Designer Backpack** - $89.99
3. **Evening Clutch** - $59.99
4. **Travel Duffle** - $149.99
5. **Crossbody Bag** - $79.99
6. **Business Briefcase** - $199.99

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
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── assets/             # Product images and resources
│   ├── README.md       # Asset documentation
│   ├── leather_tote.jpg
│   ├── designer_backpack.jpg
│   ├── evening_clutch.jpg
│   ├── travel_duffle.jpg
│   ├── crossbody_bag.jpg
│   └── business_briefcase.jpg
└── README.md           # This file
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Botpress](https://botpress.com/)** - AI chatbot platform
- **Python 3.12** - Programming language
- **HTML/CSS** - Custom styling and chatbot integration

## 💬 Chatbot Integration

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

## 🎨 Customization

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

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👤 Author

**Your Name**
- GitHub: [@god-s-lonely-man](https://github.com/god-s-lonely-man)

## 📞 Support

For support, email support@bagstore.com or join our community chat.

## 🙏 Acknowledgments

- Product images from [Unsplash](https://unsplash.com/)
- Chatbot powered by [Botpress](https://botpress.com/)
- Built with [Streamlit](https://streamlit.io/)

---

⭐ Star this repo if you find it helpful!
