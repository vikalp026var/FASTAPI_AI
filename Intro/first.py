from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(
    title="FastAPI with AI",
    description="This is a FastAPI application that integrates AI capabilities.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
    )


@app.get("/")
async def root():
    """"Root endpoint - Health Check"""
    return {"message": "Hello World"}


@app.get('/orders')
async def list_orders():
    """List all orders"""
    return {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 2},
            {"id": 2, "item": "Mouse", "quantity": 5},
            {"id": 3, "item": "Keyboard", "quantity": 3}
        ]
    } 

@app.get("/orders/{status}")
async def order_status():
    """Get order status"""
    return {
        'total_today': 2_340_23,
        'top_city': 'New York',
    }

@app.get('/debug/request-info')
async def request_info(request: Request):
    """Debug endpoint to get request information"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }


@app.get(
    '/orders/active',
    summary="Get active orders",
    description="This endpoint returns a list of active orders.",
    tags=['Orders'],
    response_description="A list of active orders",
    deprecated=False
)
def get_active_order():
    """This docstring also appears in docs"""
    return {
        "active_orders": [
            {"id": 1, "item": "Laptop", "quantity": 2},
            {"id": 2, "item": "Mouse", "quantity": 5}
        ]
    }


@app.get('/restaurants/delhi', tags=['Restaurants'])
def list_restro():
    """Another endpoint to list restaurants"""
    return {
        "restaurants": [
            {"id": 1, "name": "Pizza Place", "location": "Downtown"},
            {"id": 2, "name": "Sushi Spot", "location": "Uptown"},
            {"id": 3, "name": "Burger Joint", "location": "Midtown"}
        ]
    }


if __name__ == "__main__":
    uvicorn.run("first:app", host="0.0.0.0", port=8000, reload=True)