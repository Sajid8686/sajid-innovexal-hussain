# URL Shortener API - Innovaxel Take Home Assignment

A RESTful API to shorten long URLs, built using Django and Django REST Framework.

## 🌐 Features

- 🔗 Create short URLs
- 📥 Retrieve original URLs via short code
- ✏️ Update original URLs
- ❌ Delete short URLs
- 📊 Track and view access statistics

---

## ⚙️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- MySQL   

---

## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Sajid8686/sajid-innovexal-hussain.git
   cd url_shortening_service


2. **Create Virtual Environment**
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Database**

Update `DATABASES` in `url_shortening_service/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'urlshortener_db',
        'USER': 'urluser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Or use MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'url_shortening',
        'USER': 'root',
        'PASSWORD': 'Password',  
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

5. **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run Server**
```bash
python manage.py runserver
```

---

## 📬 API Endpoints

| Method | Endpoint                         | Description                     |
|--------|----------------------------------|---------------------------------|
| POST   | `/shorten`                       | Create a short URL              |
| GET    | `/shorten/<short_code>`         | Retrieve original URL           |
| PUT    | `/shorten/<short_code>/update`  | Update original URL             |
| DELETE | `/shorten/<short_code>/delete`  | Delete short URL                |
| GET    | `/shorten/<short_code>/stats`   | Get access statistics           |

---

## 📦 Sample Request & Response

### POST `/shorten`
**Request:**
```json
{
  "url": "https://example.com/very/long/url"
}
```

**Response:**
```json
{
  "id": 1,
  "url": "https://example.com/very/long/url",
  "short_code": "aZ8kL2",
  "created_at": "2025-05-01T12:00:00Z",
  "updated_at": "2025-05-01T12:00:00Z",
  "access_count": 0
}
```

---

## 🔍 Branching Strategy

- `main` – contains only the README
- `dev` – complete source code and development work
- ✅ At least 15 meaningful commits
- ✅ Reviewer added: junaid@innovaxel.com

---

## 📩 Contact

**Reviewer:** Junaid Hussnain  
📧 `junaid@innovaxel.com`  

---

## ✅ Notes

- The project meets all assignment requirements
- Code is clean, modular, and well-structured
- Feel free to switch between MySQL and SQLite as needed

---

## 🙌 Thank You!

_This project was submitted as part of the ASE - Python Specialist (Fresher – 1 year) take-home assignment._

```
