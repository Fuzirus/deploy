from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi import status

from backend.db import MysqlConnector


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def index(request: Request):
    connector = MysqlConnector()
    items = connector.get_items()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"items": items}
    )


@router.post("/addItem")
async def create_note(name: str = Form(...)):
    connector = MysqlConnector()
    connector.insert_item(name)
    return RedirectResponse('/', status_code=status.HTTP_302_FOUND)
