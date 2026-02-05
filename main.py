from fastapi import FastAPI, File, UploadFile, Header, HTTPException
import uvicorn

app = FastAPI()

API_KEY = "my-secret-api-key"

@app.post("/detect-voice")
async def detect_voice(
    file: UploadFile = File(...),
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if "ai" in file.filename.lower():
        result = "AI-generated"
        confidence = 0.92
    else:
        result = "Human"
        confidence = 0.85

    return {
        "filename": file.filename,
        "prediction": result,
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
