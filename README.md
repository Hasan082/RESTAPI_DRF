
# 🚀 REST API Development with Django REST Framework (DRF)

This project is a RESTful API built using **Django** and **Django REST Framework (DRF)**.  
It includes a **Status App** for managing status entries (or similar entities), designed to be scalable, modular, and easy to extend.



## 📂 Project Structure
```

project-root/
│
├── core                 # Proejct folder
├── status/              # Django app: Status API
├── manage.py
├── requirements.txt     # List of Python dependencies
└── db.sqlite3           # SQLite database (default)

````

---

## 📦 Features

- ✅ Django-based backend API
- ✅ DRF for quick and powerful serialization
- ✅ CRUD operations for `Status` model
- ✅ JSON API responses
- ✅ Admin interface
- ✅ Ready for deployment

---

## ⚙️ Requirements

All required libraries are listed in `requirements.txt` and can be installed via:

```bash
pip install -r requirements.txt
````

---

## 🚀 How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Apply migrations**:

```bash
python manage.py migrate
```

4. **Run the development server**:

```bash
python manage.py runserver
```

5. Visit `http://127.0.0.1:8000/` to access the API or admin panel.

---

## 🛠 API Endpoints (Example)

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| GET    | `/api/status/`      | List all statuses   |
| POST   | `/api/status/`      | Create a new status |
| GET    | `/api/status/<id>/` | Retrieve a status   |
| PUT    | `/api/status/<id>/` | Update a status     |
| DELETE | `/api/status/<id>/` | Delete a status     |

---

## 🔒 Authentication (Optional)

If authentication is enabled, token or session-based auth may be required. (Configure in `settings.py`)

---

## 🧑‍💻 Admin Panel

Visit: `http://127.0.0.1:8000/admin/`
Login with the superuser created via:

```bash
python manage.py createsuperuser
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)

```

