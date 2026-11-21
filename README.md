# 🥑 PyShop

PyShop is a modern, premium Django-based e-commerce platform for purchasing fresh fruits and organic produce. It combines Django's backend capabilities with high-end, responsive Vanilla CSS styling, dynamic client-side caching, coupon code processing, and a live search catalog.

---

## 🌟 Key Features

- **Elegant Landing Page**: Clean, visually rich landing page featuring a hero showcase banner, responsive trust badges, highlighted promo discount coupons, and top featured fruits.
- **Interactive Shopping Cart Drawer**: Built-in slide-out cart sidebar that handles local cart persistence (`localStorage`), item quantity modifications, deletion, and real-time total updates.
- **Promo Coupon Codes**: Validates coupon codes (e.g., `VC9903`, `VC9904`) dynamically from the database and applies percentage-based discounts to the cart subtotal.
- **Instant Live Filter Search**: Allows users to filter the fruit catalog instantly by typing in the search bar, with no page reload.
- **Django Admin Panel Integration**: Out-of-the-box support for database management of items (`Product`) and promo deals (`Offer`).

---

## 📁 Project Structure

```text
PyShop/
│
├── pyshop/                 # Django Core configuration
│   ├── settings.py         # App configurations, static file registers
│   ├── urls.py             # Project-wide url routes mapping root path
│   └── ...
│
├── products/               # Products and offers app
│   ├── templates/          # HTML Templates (home.html, index.html)
│   ├── models.py           # Product & Offer database definitions
│   ├── urls.py             # Named routes mapping
│   ├── views.py            # Main business logic views (home, index, etc.)
│   └── ...
│
├── templates/              # Base global layouts
│   └── base.html           # Brand header, navigation links, offcanvas cart drawer, CSS & JS imports
│
├── static/                 # Custom static asset files
│   └── css/
│       └── custom.css      # Premium stylesheet variables, grid, custom elements and animations
│
├── manage.py               # Django utility CLI script
```

---

## 🚀 Setup & Local Installation

### Prerequisites
Make sure you have **Python 3.x** and **pip** installed on your system.

### Steps to Run PyShop
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pyshop.git
   cd pyshop
   ```

2. **Verify Django Dependencies**:
   Ensure Django is installed:
   ```bash
   pip install django
   ```

3. **Database Migration**:
   If starting with a clean database:
   ```bash
   python manage.py migrate
   ```

4. **Verify Application Integrity**:
   Run the Django diagnostic checks to verify everything compiles successfully:
   ```bash
   python manage.py check
   ```

5. **Start Development Server**:
   Launch the local dev server:
   ```bash
   python manage.py runserver
   ```

6. **Open in Browser**:
   Open your browser and navigate to:
   - Homepage: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Catalog: [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)
   - Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 💳 Testing Promo Codes (Checkout Demo)
Try using these active coupon codes inside the shopping cart drawer to test discounts:
* **`VC9903`**: Applies a **50% discount** on your cart total.
* **`VC9904`**: Applies a **30% discount** on your cart total.

