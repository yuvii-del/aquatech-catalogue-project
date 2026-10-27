# AquaTech Product Catalogue Starter

Angular standalone frontend + Bootstrap 5 + FastAPI + PostgreSQL.

## Requirements
- Node.js 22 LTS recommended
- Python 3.11+
- PostgreSQL running

## Backend (PowerShell)
1. Create a PostgreSQL database if needed:
   `CREATE DATABASE aquatech_catalogue;`
2. In a terminal:
```powershell
cd D:\Catalogues\aquatech-catalogue-project\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```
3. Set `DATABASE_URL` in `backend\.env` to your own PostgreSQL password. Do not share it. URL-encode special characters in passwords.
4. Run:
```powershell
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs and http://127.0.0.1:8000/api/health.

## Frontend (open a second terminal)
```powershell
cd D:\Catalogues\aquatech-catalogue-project\frontend
npm install
npm start
```
Open http://localhost:4200.

## API
- GET /api/health
- GET /api/brands
- GET /api/categories
- GET /api/products?search=&brand=&category=&featured=
- GET /api/products/{slug}

The backend creates tables and inserts demo records on first start. Demo product names, prices and specs are placeholders, not verified manufacturer information. Replace with verified data and approved image URLs before publication.

If Angular reports a missing builder, confirm you are in this ZIP's `frontend` directory and run `npm install`. Avoid copying only `src` into another folder; this folder includes `angular.json` and all workspace config.
