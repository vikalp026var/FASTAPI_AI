from fastapi import FastAPI
import uvicorn
from exceptions import PinCodeNotFoundError, pincode_not_found_handler, InvalidPinCodeError, invalid_pincode_handler
from models import PincodeRequest, PincodeResponse, BulkRequest, BulkResponse, LocationResponse
from data import pincode_data


app = FastAPI(
    title="My FastAPI Application",
    description='Auto Fill City and State from Indian Pincode During Checkout'
)

@app.get('/')
def root():
    return {"message": "Pincode Lookup API"}

#register your custom exception handlers
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code, 'Invalid Format')

    if code not in pincode_data:
        raise PinCodeNotFoundError(code)

    return pincode_data[code]


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []

    for code in request.pincodes:
        if code in pincode_data:
            results.append(pincode_data[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing,
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
