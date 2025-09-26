# Leave Management System (LMS)
# 📌 Project Overview

The Leave Management System (LMS) is a web-based application designed to streamline the process of applying, tracking, and managing employee leave requests. The system provides role-based access for employees and administrators, ensuring secure and efficient leave management within an organization.

🚀 Features
👨‍💼 Employee Features

Apply for leave online.

Track the status of leave applications in real time.

Receive automated email notifications about leave approvals, rejections, or expiry reminders.

# 👨‍💻 Administrator Features

Role-based authentication and secure login/signup.

Manage employee records and leave applications.

Configure organizational leave policies.

Approve or reject leave requests.

Generate detailed leave reports through the Django Admin Panel.

# 📬 Notifications

Automated email reminders to employees:

When leave is about to expire (1 day left).

When leave duration is fully completed.

# 🛠️ Tech Stack

Frontend: HTML, CSS (Responsive UI)

Backend: Python, Django

Database: MySQL

Authentication & Security: Django Authentication System

Additional Tools: Django Admin Panel for reporting and management

# ⚙️ Installation & Setup
1. Clone the Repository
   git clone https://github.com/your-username/LMS_FINAL.git
   cd LMS_FINAL

2. Create Virtual Environment & Activate
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate   # On Mac/Linux

3. Install Dependencies
   pip install -r requirements.txt
   
4. Configure Environment Variables
   Create a credentials.env file in the project root directory and add:
      SECRET_KEY=your-django-secret-key
      DB_NAME=your-database-name
      DB_USER=your-database-username
      DB_PASSWORD=your-database-password
      DB_HOST=localhost
      DB_PORT=3306

5. Apply Database Migrations
   python manage.py migrate

6. Run the Server
   python manage.py runserver
   Now visit 👉 http://127.0.0.1:8000/

# 📊 Database Schema (Core Tables)

Employees – Stores employee information.

Leave Applications – Tracks all leave requests with status.

Approval History – Logs approval/rejection activities.

Policies – Organizational leave rules and settings.

# 📈 Future Enhancements

Integration with Google/Outlook Calendar.

Mobile application support (React Native / Flutter).

Advanced reporting and analytics dashboard.

Multi-language support for global teams.

# 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# 👨‍💻 Author
   Aamir Khan
