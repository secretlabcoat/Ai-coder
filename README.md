# Ai-coder

A simple AI assistant that now runs as a browser-based web app.

## Run it locally

1. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open your browser to:
   ```text
   http://localhost:5000
   ```

## Notes

- The project still keeps the original CLI logic in `ai_assistant.py`.
- The browser UI communicates with the Python backend through `/api/chat`.
