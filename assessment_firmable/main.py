from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, HttpUrl
from bs4 import BeautifulSoup
import requests

SECRET_KEY = "solar_system"

def authenticate(secret_key: str = Header(...)):
    if secret_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

class URLRequest(BaseModel):
    url: HttpUrl

class WebsiteDetails(BaseModel):
    industry: str | None
    company_size: str | None
    location: str | None

app = FastAPI()

@app.post("/scrape", response_model=WebsiteDetails)
async def scrape_website(data: URLRequest, secret_key: str = Depends(authenticate)):
    try:
        # Fetch the homepage content
        response = requests.get(data.url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract details from the homepage
        text_content = soup.get_text(" ", strip=True).lower()

        industry = extract_industry(text_content)
        company_size = extract_company_size(text_content)
        location = extract_location(text_content)

        return WebsiteDetails(
            industry=industry,
            company_size=company_size,
            location=location
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch the URL: {str(e)}")
# Helper functions for extraction

def extract_industry(content: str) -> str | None:
    if "technology" in content:
        return "Technology"
    if "finance" in content:
        return "Finance"
    return None

def extract_company_size(content: str) -> str | None:
    if any(term in content for term in ["small business", "startup"]):
        return "Small"
    if any(term in content for term in ["enterprise", "large organization"]):
        return "Large"
    return None

def extract_location(content: str) -> str | None:
    if "headquartered in" in content:
        start = content.find("headquartered in") + len("headquartered in")
        return content[start:].split(" ")[0]
    if "located at" in content:
        start = content.find("located at") + len("located at")
        return content[start:].split(" ")[0]
    return None
