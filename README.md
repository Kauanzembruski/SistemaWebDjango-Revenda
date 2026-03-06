Web system developed with Django for car listing and management.

The project allows:

Adding cars

Viewing a list of cars

Seeing detailed information for each car

Generating automatic descriptions using AI

Uploading images

🧰 Technologies Used

Python

Django

SQLite

HTML / CSS / JavaScript

Google Gemini API

📦 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
2️⃣ Create Virtual Environment
python -m venv venv

Activate the virtual environment:

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Database Migrations
python manage.py migrate
5️⃣ Create Superuser (Admin)

To access the Django admin panel, create a superuser:

python manage.py createsuperuser

You will be prompted for:

Username:
Email:
Password:
Password again:

After that, you can access the admin at:

http://127.0.0.1:8000/admin

For deployment (e.g., Render), you can automatically create the superuser using environment variables and --noinput.

6️⃣ Run the Server
python manage.py runserver

Open your browser:

http://127.0.0.1:8000
🔑 Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

On deployment (Render or other servers), configure these variables in the environment settings.

📂 Project Structure
CARROS/                     # Root directory
│
├── accounts/               # App for user management (login, registration, logout)
├── app/                    # Main project app (settings, URLs, WSGI)
├── cars/                   # App for car management
├── gemini_api/             # App or module for Google Gemini API integration
├── media/                  # Folder for uploaded images
├── static/                 # Static files (CSS, JS, fixed images)
├── venv/                   # Python virtual environment
├── .env                    # Environment variables (API keys, SECRET_KEY, etc.)
├── .gitignore              # Files/folders to ignore in Git
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
👨‍💻 Author

Project developed for learning Python and Django.
Kauan Zembruski
