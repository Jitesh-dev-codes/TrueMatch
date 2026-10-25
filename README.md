# TrueMatch Jobs API

This is the backend service for my portfolio project, TrueMatch Jobs. I built this to solve a personal problem: job boards are full of expired listings and fake agencies. 

## Tech Stack Used
- Django & Django REST Framework (Core backend API)
- PostgreSQL / Supabase (Database)
- APScheduler (For automated daily background tasks)
- Requests (For fetching fresh data from open APIs)

## Architecture
Instead of using heavy scrapers like Selenium, this backend directly consumes open APIs (like Remotive and Arbeitnow). It automatically filters out 'Senior', 'Lead', and 'Manager' roles to specifically aggregate entry-level, internship, and relocation-friendly roles. It uses APScheduler to run background syncs automatically without external cron jobs.