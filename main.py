from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Define a dictionary with your find and replace mappings
text_to_code = {
    "Living Room": "123456789",
    "Bedroom": "987654321"
    # Add more mappings as needed
}

class TextRequest(BaseModel):
    text: str

@app.post("/find_and_replace")
async def find_and_replace(request: TextRequest):
    input_text = request.text
    output_text = input_text

    for key, value in text_to_code.items():
        output_text = output_text.replace(key, value)

    return {"output": output_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
