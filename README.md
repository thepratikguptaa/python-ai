# Python AI Project

This project is a simple Python AI script.

## Setup

It is recommended to use `uv` for creating and managing the virtual environment.

### Using uv

1. **Install uv:**
   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root of the project and add your Gemini API key:

```
API_KEY="your_api_key_here"
```

## Running the script

```bash
python AI.py
```
