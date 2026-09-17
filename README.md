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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify installation

Run this from the project root to confirm all imports work correctly:

```bash
python -c "from fastapi import FastAPI; import uvicorn; from supabase import create_client, Client; from dotenv import load_dotenv; print('All imports OK')"
```