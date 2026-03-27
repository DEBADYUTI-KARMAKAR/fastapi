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


pip install "pydantic[email]"
pip install passlib==1.7.4
pip install bcrypt==3.2.2

