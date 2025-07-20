🎬 Movie & Series API with Django REST Framework

📝 Project Description

This project is a robust RESTful API built using Django and Django REST Framework (DRF). It's designed to manage a catalog of movies and series, allowing for seamless creation, retrieval, updating, and deletion of content. The API features a well-structured data model for movies, series, categories, and casts, with a focus on demonstrating core DRF functionalities, including serialization, function-based views, and handling both full and partial updates.

✨ Key Features

This API provides comprehensive functionalities for managing cinematic content:

API Structure & Core Functionality:

REST API Design: Implemented a clear and intuitive REST API structure.

CRUD Operations: Full Create, Retrieve, Update (Full & Partial), and Delete operations for movies.

Function-Based Views (FBVs): All CRUD operations are implemented using Django REST Framework's function-based views.

Data Models:

Movie Model: Represents individual movies with common attributes.

Series Model: Represents TV series with shared attributes, allowing for potential future expansion beyond current CRUD scope.

Category Model: Defines categories for movies and series (e.g., Action, Drama, Comedy).

Cast Model: Defines actors/actresses associated with movies and series.


Common Information Shared by Movie & Series Models:

title (string)

description (text)

release_date (date)

categories (Many-to-Many relationship with Category model)

casts (Many-to-Many relationship with Cast model)

poster_image (image field for the movie/series poster)

Serialization:

Serializers for all Models: Custom serializers are implemented for Movie, Series, Category, and Cast models to handle data conversion between Django models and JSON/XML representations. Notably, when retrieving a movie, its associated categories and casts are displayed using their string representation (e.g., category name, cast member's name) instead of just their primary keys, enhancing API readability.

🛠️ Technologies Used

Python 3.x: The core programming language.

Django 4.x: The web framework for building the application backend.

Django REST Framework (DRF): Powerful toolkit for building Web APIs.

SQLite3 / PostgreSQL: Database management system (SQLite3 is default for development, PostgreSQL recommended for production).

Pillow: (Likely required for image handling with poster_image field).

🚀 Installation & Setup

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository:
   
Bash

git clone https://github.com/alyaah95/DRF_movies_project.git
cd DRF_movies_project

2. Create a Virtual Environment (Recommended):
   
Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies:
   
Bash

pip install -r requirements.txt
(Note: If you don't have requirements.txt yet, create it by running pip freeze > requirements.txt after installing Django, djangorestframework, Pillow, and your chosen database adapter like psycopg2-binary for PostgreSQL or mysqlclient for MySQL.)

4. Configure Database:
   
For SQLite3 (Default for development): No specific configuration is usually needed in settings.py as it's the default.

For PostgreSQL (Recommended for production):

Install PostgreSQL and create a new database (e.g., movie_series_db).

Update DATABASES settings in your project's settings.py with your database credentials:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_series_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

5. Run Migrations:
   
Bash

python manage.py makemigrations
python manage.py migrate

6. Create a Superuser (for Admin Panel access and initial data seeding):
   
Bash

python manage.py createsuperuser
Follow the prompts to set up username, email, and password.

7. Run the Development Server:
   
Bash

python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.
The Django Admin Panel will be accessible at http://127.0.0.1:8000/admin/.

💡 API Usage & Endpoints

All API interactions will be performed via HTTP requests to the following endpoints. You can use tools like Postman, Insomnia, curl, or directly your web browser for GET requests.

(Base URL for API): http://127.0.0.1:8000/api/ (or your chosen API base path)

Movie Endpoints:

List all Movies / Create a New Movie:

URL: /api/movies/

Method: GET (List), POST (Create)

Request Body (for POST):

JSON

{
    "title": "Movie Title",
    "description": "Movie Description",
    "release_date": "YYYY-MM-DD",
    "categories": [1, 2],         // Array of Category IDs
    "casts": [3, 4],              // Array of Cast IDs
    "poster_image": null          // Or a base64 encoded string/file upload if configured
}

Retrieve / Update / Delete a Specific Movie:

URL: /api/movies/{id}/ (replace {id} with the movie's primary key)

Method: GET (Retrieve), PUT (Full Update), PATCH (Partial Update), DELETE (Delete)

Request Body (for PUT/PATCH):

PUT (Full Update): Requires all fields of the movie.

JSON

{
    "title": "Updated Movie Title",
    "description": "Updated Description",
    "release_date": "YYYY-MM-DD",
    "categories": [1],
    "casts": [3],
    "poster_image": null
}

PATCH (Partial Update): Only requires the fields you want to update.

JSON

{
    "description": "Just updating the description"
}

Category Endpoints (Example - if implemented for direct access):
List all Categories / Create a New Category:

URL: /api/categories/

Method: GET (List), POST (Create)

Request Body (for POST): {"name": "New Category Name"}

Cast Endpoints (Example - if implemented for direct access):

List all Cast Members / Create a New Cast Member:

URL: /api/casts/

Method: GET (List), POST (Create)

Request Body (for POST): {"name": "New Cast Name"}

🤝 Contributing

Contributions are welcome! If you have suggestions or want to improve the project, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.



🧑‍💻 Author

Alyaah95

GitHub: https://github.com/alyaah95

