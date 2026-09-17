# CarAPI

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

> If you hit an execution policy error on PowerShell, run this once:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 3. Run the setup script

```bash
python setup_env.py
```

This checks that you have Python 3.9+, installs all dependencies from `requirements.txt`, and verifies that everything imports correctly.

### 4. (Optional) Manual install

If you'd rather install dependencies manually instead of using the setup script:

```bash
pip install -r requirements.txt
```

Then verify imports:

```bash
python -c "from fastapi import FastAPI; import uvicorn; from supabase import create_client, Client; from dotenv import load_dotenv; print('All imports OK')"
```