import asyncio
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import io
import logging
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API
GOOGLE_API_KEY = ""  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Timeout for Gemini API calls
GEMINI_TIMEOUT = 10  # seconds

async def generate_content(prompt, image):
    """Run Gemini OCR in a separate thread to avoid blocking."""
    try:
        response = await asyncio.to_thread(model.generate_content, [prompt, image])
        response.resolve()
        return response.text.strip()
    except Exception as e:
        logger.error(f"Gemini API error: {str(e)}")
        return None

@app.post("/ocr")
async def perform_ocr(frame: UploadFile = File(...)):
    try:
        # Read image
        image_data = await frame.read()
        image = Image.open(io.BytesIO(image_data))

        # Ensure image is in RGB mode
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        # Run Gemini OCR in parallel
        extracted_text = await asyncio.gather(
            generate_content("Extract and read all text from this image. Only return the text, nothing else.", image)
        )

        if extracted_text[0] is None:
            return JSONResponse(
                content={"error": "Gemini API call failed"},
                status_code=500
            )

        return JSONResponse(content={
            "text": extracted_text[0] if extracted_text[0] else "No text detected",
            "engine": "gemini"
        })

    except Exception as e:
        logger.error(f"Gemini OCR error: {str(e)}")
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Gemini Vision service...")
    uvicorn.run(app, host="0.0.0.0", port=5001, workers=4)
