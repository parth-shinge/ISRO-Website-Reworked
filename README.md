# ISRO Website Reworked

A Flask-based website inspired by ISRO content, with public pages and an authenticated admin panel to manage missions.

## Tech Stack

- Python 3.11
- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-MySQLdb
- MySQL
- Pytest (for smoke tests)

## Project Structure

- app.py: Main Flask application and routes
- templates/: HTML templates for public and admin pages
- static/: Static assets (images/CSS/JS)
- isro_missions.sql: SQL schema for initial database setup
- tests/: Automated smoke tests

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create MySQL database and tables:

```sql
SOURCE isro_missions.sql;
```

5. Configure environment variables (recommended):

```bash
SECRET_KEY=replace-with-a-strong-secret
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_DB=isro_mission
```

6. Run the app:

```bash
python app.py
```

The app runs on:

- http://127.0.0.1:5000/

## Default Behavior and Notes

- Admin routes require login.
- Logout now supports both GET and POST to match existing templates.
- Feedback form submission is handled and redirects back to the feedback page.
- Forgot-password currently shows an informational message; full email reset flow is not implemented.

## Running Tests

```bash
pytest -q
```

Current tests are smoke tests for core public routes and repaired endpoints.

## Security Notes

- Do not commit real credentials.
- Use environment variables for secrets and database settings.
- Disable debug mode in production.

## Future Improvements

- Add CSRF protection (Flask-WTF)
- Add structured logging and error handling
- Add unit tests for authentication and mission CRUD flows
- Implement a proper password reset flow with email token support
