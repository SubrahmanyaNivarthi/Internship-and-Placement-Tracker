Internship and Placement Tracker (Flask) - Minimal skeleton
--------------------------------------------
What's included:
- app.py : main Flask application
- templates/ : HTML templates (Bootstrap CDN used)
- requirements.txt : required Python packages

How to run (Windows):
1. Extract the zip and open a terminal inside the extracted folder.
2. (Optional but recommended) create a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install requirements:
   python -m pip install -r requirements.txt
4. Run the app:
   python app.py
5. Open your browser at: http://127.0.0.1:5000

Troubleshooting: "Flask appears not installed"
- Make sure you're installing into the same Python you use to run the app.
  Use: python -m pip install Flask
- On Windows, try: py -m pip install Flask
- Check versions:
  python --version
  python -m pip --version
- If pip says installation succeeded but import fails, your PATH might point to another Python.
  Using the full path helps: C:\path\to\python.exe -m pip install Flask
- Ensure templates folder is exactly named 'templates' and contains the HTML files.

Quick note: This project stores data in memory (no database). It's fine for demo purposes.
Good luck with your hackathon — you got this! 🚀
