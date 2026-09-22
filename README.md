# Books Capstone API

A Python backend project that demonstrates **web scraping, SQLite database management, CRUD operations, and REST API development using FastAPI**.

## Features

* Scrapes the first 20 books from Books to Scrape
* Extracts title, price, stock status, and rating
* Stores data in SQLite
* Implements CRUD operations
* Exposes data through FastAPI REST APIs
* Interactive Swagger API documentation

## Tech Stack

* Python
* Requests
* BeautifulSoup4
* SQLite
* FastAPI
* Uvicorn

## Project Structure

```text
Books-Capstone/
│
├── scraper.py       # Web scraping
├── database.py      # SQLite CRUD operations
├── main.py          # FastAPI REST API
├── books.db         # SQLite database
├── requirements.txt
└── README.md
```

## Architecture

```text
Books to Scrape
      ↓
  scraper.py
      ↓
  database.py
      ↓
   books.db
      ↓
    main.py
      ↓
   REST API
```

## API Endpoints

| Method | Endpoint      | Purpose       |
| ------ | ------------- | ------------- |
| GET    | `/books`      | Get all books |
| GET    | `/books/{id}` | Get one book  |
| POST   | `/books`      | Create book   |
| PUT    | `/books/{id}` | Update book   |
| DELETE | `/books/{id}` | Delete book   |

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python scraper.py
```

Start the API:

```bash
python main.py
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Learning Focus

**Web Scraping → Data Processing → SQLite → OOP CRUD → REST API**

Built as a hands-on Python backend capstone project.
