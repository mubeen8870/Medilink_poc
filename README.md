<<<<<<< HEAD
# Medilink_poc
public repository for medilink_project
=======
# MediLink API (Professional FastAPI Structure)

A clean, realistic FastAPI project with **different endpoints** (CRUD) for patients and medicines.
Data is stored in **MongoDB (Compass)** and mirrored to **JSON files** under `data/`.

## Endpoints (look professional)
Base path: `/api`

### Health
- `GET /api/health` — service health

### Patients
- `POST /api/patients` — create
- `GET /api/patients` — list
- `GET /api/patients/{id}` — get by id
- `PUT /api/patients/{id}` — update
- `DELETE /api/patients/{id}` — delete

### Medicines
- `POST /api/medicines` — create
- `GET /api/medicines` — list
- `GET /api/medicines/{id}` — get by id
- `PUT /api/medicines/{id}` — update
- `DELETE /api/medicines/{id}` — delete

## Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env  # then edit if needed
uvicorn app.main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs

## MongoDB & JSON Mirroring
- Configure Mongo in `.env`.
- Every create/update/delete is **mirrored** to JSON files:
  - `data/patients.json`
  - `data/medicines.json`

## Notes
- Uses `motor` (async Mongo).
- Avoids `module 'app.services' has no attribute ...'` by organizing repositories and routers clearly.
- Clean separation: routers → repositories → Mongo + JSON mirror.
>>>>>>> 69df08d (Initial commit - FastAPI MongoDB project)
