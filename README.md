# Panchakarma Patient Management System

Production-ready starter for SIH25023 that digitizes Panchakarma workflows with AI Dosha analysis, therapist suggestion, RBAC, and Supabase-ready schema.

## Stack
- Frontend: React + Vite + Tailwind
- Backend: Flask REST API + JWT middleware
- Database: Supabase PostgreSQL + RLS
- Deployment targets: Vercel (frontend), Render (backend), Supabase Cloud (DB)

## Project Structure
```
frontend/
backend/
supabase/
```

## Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Core APIs
- `POST /api/appointments`
- `POST /api/ai-dosha-analysis`
- `POST /api/suggest-therapist`
- `POST /api/generate-prescription`
- `POST /api/assign-therapy`
- `GET /api/dashboard-data`

## Security
- JWT validation middleware for protected APIs.
- Role-aware authorization checks (`admin`, `doctor`, `therapist`, `patient`).
- Supabase Row-Level Security policies in `supabase/schema.sql`.

## Environment Variables
Copy and configure:
- `frontend/.env.example`
- `backend/.env.example`

## Deployment
- Frontend: connect `frontend/` to Vercel.
- Backend: deploy `backend/` as a Python web service on Render.
- DB: execute `supabase/schema.sql` in Supabase SQL editor.
