import requests
from bs4 import BeautifulSoup
from models import Job, session

# Sample scraping (this URL is just an example)
def scrape_jobs():
    url = 'https://example.com/jobs'  # Replace with a real URL
    response = requests.get(url)
    
    # For demo purposes, let's just simulate the job data
    jobs_data = [
        {'title': 'Data Scientist', 'company': 'Company A', 'email': 'hr@companya.com'},
        {'title': 'Business Analyst', 'company': 'Company B', 'email': 'hr@companyb.com'}
    ]
    
    for job_data in jobs_data:
        new_job = Job(title=job_data['title'], company=job_data['company'], recruiter_email=job_data['email'])
        session.add(new_job)
    
    session.commit()
    print("Jobs scraped and saved to database!")

scrape_jobs()
