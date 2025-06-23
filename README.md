# REST API Development with Django REST Framework (DRF)

This project is a **RESTful API** built with **Django** and **Django REST Framework (DRF)**. It demonstrates over **30 different ways** to create API views using:

* ViewSets
* Generic Views
* Mixins
* APIView
* Function-based views (FBVs) *(optional)*

It includes a `Status` app for managing status entries (or similar content types), showcasing the power and flexibility of DRF.


## Project Structure

```
project-root/
├── core/                  # Django project root
├── status/                # Django app: Status API
├── manage.py
├── requirements.txt       # Project dependencies
└── db.sqlite3             # Default SQLite database
```


## Features

* ✔️ Full CRUD for `Status` model
* ✔️ DRF `ModelViewSet` with router support
* ✔️ `APIView` with manual method handling
* ✔️ `GenericAPIView` with mixins (List, Create, Retrieve, Update, Delete)
* ✔️ Built-in file upload support (FormParser, MultiPartParser)
* ✔️ Admin panel for easy data management
* ✔️ Clean and extensible code
* ✔️ Ready for deployment


## Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

1. **Clone the project**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Apply migrations**

```bash
python manage.py migrate
```

4. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

5. **Run development server**

```bash
python manage.py runserver
```

6. Access your API at: `http://127.0.0.1:8000/api/status/`


## API Endpoints

| Method | Endpoint            | Description                   |
| ------ | ------------------- | ----------------------------- |
| GET    | `/api/status/`      | List all status objects       |
| POST   | `/api/status/`      | Create a new status           |
| GET    | `/api/status/<id>/` | Retrieve a status by ID       |
| PUT    | `/api/status/<id>/` | Full update to a status by ID |
| PATCH  | `/api/status/<id>/` | Partial update of a status    |
| DELETE | `/api/status/<id>/` | Delete a status by ID         |

> Depending on the registered URL routes, you may see paths like `/api/status/detail/<id>/`, `/update/<id>/`, or `/delete/<id>/` for class-based views built with `RetrieveAPIView`, `UpdateAPIView`, and `DestroyAPIView`.


## Demonstrated View Types

* `ModelViewSet`
* `ListCreateAPIView`
* `RetrieveUpdateDestroyAPIView`
* `GenericAPIView` with `mixins`
* Custom `APIView` subclasses
* Separate views for List, Create, Update, Delete (CRUD granularity)

All of these are implemented in the `status/views.py` file with clear comments and usage examples.


## Authentication

You can enable optional authentication (Token, Session, JWT) in your `settings.py`.


## Admin Panel

Visit the admin interface at:
`http://127.0.0.1:8000/admin/`



## License

This project is licensed under the [MIT License](LICENSE).


## Acknowledgements

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* Inspired by best practices for API development in Python


