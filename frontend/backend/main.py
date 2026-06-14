from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/generate")
def generate(file: UploadFile = File(...)):

    path = f"{UPLOAD_DIR}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🧠 AI PLACEHOLDER (we upgrade later to YOLO)
    return {
        "clips": [
            {
                "clip": "https://sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4",
                "style": "🔥 AI Highlight"
            }
        ]
    }
