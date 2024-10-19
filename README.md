# Job-Scraper
This is the web scraper that I built to get recruiter emails of different job postings


Job Scraper Project
This project is a web scraper built using Python that collects job listings and recruiter emails from various job boards and company websites. The data is stored in an SQLite database and displayed in a web interface using Flask.

Features
Automatically scrapes job postings from multiple URLs.
Extracts recruiter emails from job descriptions.
The scraped data (job title, company, recruiter email) is stored in an SQLite database.
It provides a simple web interface through which you can view job listings.
Easily customizable to scrape different websites.
Scheduled scraping using cron jobs (Linux/Mac) or Task Scheduler (Windows).
Project Structure
graphql
Copy code
/job_scraper_project/

├── app.py                 # Flask application to display job listings

├── scraper.py             # Web scraper to collect job data

├── models.py              # Database setup with SQLAlchemy

├── job_urls.txt           # File containing URLs of job boards to scrape

├── jobs.db                # SQLite database where scraped data is stored (auto-generated)

├── requirements.txt       # List of required Python packages

Requirements

Python 3.x

SQLite (automatically installed with Python)

Python packages: Requests, BeautifulSoup4, SQLAlchemy, Flask
