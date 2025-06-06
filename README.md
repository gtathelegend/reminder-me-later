**Remind-Me-Later Project Documentation**

**🕒 Remind-Me-Later**
A minimalist web app to schedule and store message reminders via Email or SMS.
Built with Flask and deployed on Render.

**🚀 Features**
• Add reminders with date & time
• Choose reminder method: Email or SMS
• View all upcoming reminders
• Built using Flask + SQLite
• Deployed on Render

**🌐 Live Demo**

🔗 [https://reminder-me-later.onrender.com](https://reminder-me-later.onrender.com)

**📁 Project Structure**
remind-me-later/
├── app.py                 # Main Flask app

├── models.py              # SQLAlchemy models

├── templates/

│   └── index.html         # HTML frontend

├── static/

│   └── style.css          # CSS for styling

├── requirements.txt       # Python dependencies

├── Procfile               # Render process file

├── render.yaml            # Render deployment config

└── README.md

**🛠️ Tech Stack**
• Frontend: HTML, CSS, JavaScript (no framework)
• Backend: Python Flask
• Database: SQLite (via SQLAlchemy)
• Deployment: Render (Free Tier)
• Web Server: Gunicorn

**🔧 Local Setup Instructions**
1. Clone the Repository
   git clone https://github.com/gtathelegend/reminder-me-later.git
   cd remind-me-later

2. Set Up Virtual Environment (Optional)
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)

3. Install Requirements
   pip install -r requirements.txt

4. Run the App
   python app.py

   Visit: http://127.0.0.1:5000

**🧪 API Endpoints**
• POST /api/reminders/create – Add a new reminder
• GET /api/reminders – Get all reminders

Example request:
{
  "message": "Meeting at 5 PM",
  "remind_at": "2025-06-08T17:00:00",
  "method": "email"
}

**📦 Deployment on Render**
Render automatically builds and serves your Flask app.

Files Needed:
• requirements.txt
• Procfile
• render.yaml

Steps:
1. Push code to GitHub
2. Sign in to Render.com
3. New Web Service → Connect Repo
4. Set build & start commands:
   - Build: pip install -r requirements.txt
   - Start: gunicorn app:app

5. Deploy 🎉

**🙋‍♂️ Author**
Vedaang Sharma
📧 gta.thelegend@gmail.com
🌐 [Linkedin](https://linkedin.com/in/vedaangsharma2006) 
🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.
📄 License
MIT License — feel free to use and modify this project.
