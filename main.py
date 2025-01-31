from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow any origin to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Marks data of 100 students (using imaginary names for this example)
student_marks = {
    "John": 10,
    "Alice": 20,
    "Bob": 30,
    "Charlie": 40,
    "David": 50,
    "Eve": 60,
    # You would normally fill in data for 100 students
}

@app.get("/api")
async def get_marks(name: list[str]):
    # Return the marks for the students in the name list
    marks = [student_marks.get(student, "Not found") for student in name]
    return JSONResponse(content={"marks": marks})

