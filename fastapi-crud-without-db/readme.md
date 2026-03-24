# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

# 3. Install dependencies 
pip install fastapi uvicorn

# 4. Save dependencies
pip freeze > requirements.txt

# 5. Run FastAPI app
uvicorn main:app --reload