import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_happy_path():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/execute", json={
            "request": "Diagnose and generate script and email",
            "require_approval": False
        })
        data = response.json()
        assert data["status"] == "completed"
        assert "diagnosis" in data
        assert "script" in data
        assert "email_draft" in data