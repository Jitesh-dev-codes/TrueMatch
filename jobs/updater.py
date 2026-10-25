from apscheduler.schedulers.background import BackgroundScheduler
from jobs.scraper import run_scraper

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scraper, 'interval', hours=24)
    scheduler.start()