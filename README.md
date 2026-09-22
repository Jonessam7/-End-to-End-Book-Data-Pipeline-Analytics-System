# Book Data Pipeline Capstone

## Setup
```
python -m venv venv
venv\Scripts\activate      (Windows)  /  source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
```

## Run order
1. `python scraper.py`   → scrapes first 20 books, fills `books.db`
2. `python main.py`      → starts FastAPI at http://127.0.0.1:8000
3. `python client.py`    → (new terminal) hits API, saves `exported_books.csv` + `price_vs_rating.png`

Docs: http://127.0.0.1:8000/docs
