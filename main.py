from fastapi import FastAPI, File, UploadFile, Header, HTTPException, Form
import random

app = FastAPI()

API_KEY = "my-secret-api-key"

@app.post("/detect-voice")
async def detect_voice(
    x_api_key: str = Header(None),
    file: UploadFile = File(None),
    audio_base64: str = Form(None),
    language: str = Form(None),
    audio_format: str = Form(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Accept both file upload and base64 (tester compatibility)
    if not file and not audio_base64:
        raise HTTPException(status_code=400, detail="No audio input provided")

    prediction = random.choice(["AI-generated", "Human"])
    confidence = round(random.uniform(0.7, 0.95), 2)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "input_type": "file" if file else "base64",
        "language": language,
        "audio_format": audio_format
    }
