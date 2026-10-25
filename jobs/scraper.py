import requests
from jobs.models import Job

def fetch_remotive():
    url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=25"
    added = 0
    try:
        data = requests.get(url).json().get('jobs', [])
        for j in data:
            title = str(j.get('title', '')).lower()
            if 'senior' in title or 'lead' in title or 'manager' in title:
                continue
                
            Job.objects.get_or_create(
                job_url=j.get('url'),
                defaults={
                    'title': j.get('title'),
                    'company_name': j.get('company_name'),
                    'description': 'Remote Tech'
                }
            )
            added += 1
    except Exception as e:
        print(e)
    return added

def fetch_arbeitnow():
    url = "https://www.arbeitnow.com/api/job-board-api"
    added = 0
    try:
        data = requests.get(url).json().get('data', [])
        for item in data:
            title = str(item.get('title', '')).lower()
            
            if 'senior' in title or 'manager' in title or 'lead' in title or 'head' in title:
                continue
                
            Job.objects.get_or_create(
                job_url=item.get('url'),
                defaults={
                    'title': item.get('title'),
                    'company_name': item.get('company_name'),
                    'description': 'Global Tech'
                }
            )
            added += 1
            if added >= 20: break
    except Exception as e:
        print(e)
    return added

def run_scraper():
    Job.objects.all().delete()
    remote = fetch_remotive()
    global_jobs = fetch_arbeitnow()
    print(f"Scraped {remote} remote and {global_jobs} global jobs.")