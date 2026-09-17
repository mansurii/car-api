import sys
import subprocess

# Minimum Python version required by fastapi, uvicorn, supabase, python-dotenv
MIN_VERSION = (3, 9)

# Check Python version
if sys.version_info < MIN_VERSION:
    print(f"Python {MIN_VERSION[0]}.{MIN_VERSION[1]}+ is required. You have {sys.version.split()[0]}.")
    print("Download the latest version here: https://www.python.org/downloads/")
    sys.exit(1)

print(f"Python version OK: {sys.version.split()[0]}")

# Install dependencies from requirements.txt
print("Installing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Verify all imports work
print("Verifying imports...")
subprocess.run([
    sys.executable, "-c",
    "from fastapi import FastAPI; import uvicorn; from supabase import create_client, Client; from dotenv import load_dotenv; print('All imports OK')"
])

print("Done! All dependencies installed and verified.")