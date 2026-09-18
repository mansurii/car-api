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

### 5. Create your `.env` file

Create a file named `.env` in the project root (this file is git-ignored and should never be committed):

**Windows (Command Prompt):**
```cmd
type nul > .env
```

**Windows (PowerShell):**
```powershell
New-Item .env
```

**macOS/Linux:**
```bash
touch .env
```

Add your Supabase project credentials to it:

```env
SUPABASE_URL=your-project-url
SUPABASE_KEY=your-api-key
```

You can find these values in your Supabase project dashboard:
- **SUPABASE_URL** — go to **Project Settings → Data API**, under **Project URL**
- **SUPABASE_KEY** — go to **Project Settings → API Keys**, under **Secret keys**

### 6. Set up the database

1. Go to your [Supabase dashboard](https://supabase.com/dashboard) and open your project.
2. In the left sidebar, click **SQL Editor**.
3. Click **New query**.
4. Open the `cars.sql` file from this repo, copy its contents, and paste them into the SQL Editor.
5. Click **Run** (or press `Ctrl + Enter`).

This creates the `cars` table, enables Row Level Security, and allows public read access.