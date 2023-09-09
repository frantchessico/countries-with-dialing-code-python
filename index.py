from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

class Country(BaseModel):
    name: str
    dial_code: str
    code: str

@app.get("/countries-with-dialing-code", response_model=List[Country])
async def get_countries_with_dialing_code():
    try:
        # Open and read the JSON file
        with open("datas.json", "r") as file:
            countries_data = json.load(file)
            countries = [Country(**country) for country in countries_data]

        return countries
    except Exception as e:
        return {"error": str(e)}

def get_port():
    port = os.getenv("PORT")
    if port is None:
        port = "8080"  # Default port
    return port

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(get_port()))
