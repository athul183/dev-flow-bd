# DevFlow Backend

This is a lightweight FastAPI backend containing only signup and login authentication logic.

## 🚀 Setup & Run

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. (Optional but recommended) Create a virtual environment:
   ```bash
   # On Windows (use `py` to avoid Microsoft Store shortcut issues):
   py -m venv venv
   venv\Scripts\activate
   
   # On Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## 🔗 Endpoints

The server runs on `http://127.0.0.1:8000` by default.

- `POST /signup`: Expects a JSON payload with `email`, `password`, and `name`.
- `POST /login`: Standard OAuth2 form-data login. Expects `username` (use email here) and `password`. Returns a JWT token.
- `GET /me`: Returns the profile of the currently logged-in user. Requires the JWT token as a Bearer token in the Authorization header.

**💡 Tip:** You can easily test all these endpoints by visiting the automatically generated interactive documentation at `http://127.0.0.1:8000/docs` once the server is running!
