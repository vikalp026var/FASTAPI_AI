from fastapi import FastAPI, Query, HTTPException
from models import  MenuResponse, MenuItem
from data import menu_items


app = FastAPI(
    title="FastAPI with AI",
    description="This is a FastAPI application that integrates AI capabilities.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get('/menu', response_model=MenuResponse)
def get_menu(category: str | None = Query(None, description="Filter menu items by category")):
    """Get menu items, optionally filtered by category"""
    if category:
        filtered = [item for item in menu_items if item['category'].lower() == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No menu items found for category '{category}'")

        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(menu_items), items=menu_items)


@app.get('/menu/{item_id}', response_model=MenuItem)
def get_menu_items(item_id: int):
    for item in menu_items:
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Menu item with id {item_id} not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")