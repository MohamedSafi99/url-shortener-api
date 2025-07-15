# 🔗 URL Shortener API (Django REST Framework)

A high-performance URL shortening backend with RESTful API endpoints. Built with Django and PostgreSQL.

## 🚀 Features
- ✅ Generate unique short codes for any URL
- 🔄 302 redirects to original URLs
- 🛡️ Secure URL validation
- 📊 Ready for analytics integration

## 🛠️ Tech Stack
- Python 3.10+
- Django 4.2
- Django REST Framework
- PostgreSQL
- Redis (caching)

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL

### Installation
```bash
# Clone repo
git clone https://github.com/yourusername/url-shortener-api.git
cd url-shortener-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt


🏃 Running Locally
bash
python manage.py runserver
API will be available at http://localhost:8000

📚 API Documentation
Endpoint	Method	Description
/shorten/	POST	Create short URL
/{short_code}/	GET	Redirect to original URL
Example Request:

bash
curl -X POST http://localhost:8000/shorten/ \
  -H "Content-Type: application/json" \
  -d '{"original_url":"https://example.com"}'
