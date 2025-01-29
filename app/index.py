from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [
    {"name": "ho8ePmxFs", "marks": 70},
    {"name": "Zfmi", "marks": 55},
    {"name": "J", "marks": 23},
    # Add more students here...
]

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [s["marks"] for s in students_data if s["name"] in name]
        return {"marks": marks}
    return {"marks": []}
