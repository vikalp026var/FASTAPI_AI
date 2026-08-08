from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode: str 

    #pincode must be 6 digits long
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls, v):
        if len(v) != 6 or not v.isdigit():
            raise ValueError("Pincode must be 6 digits long")
        return v


class PincodeResponse(BaseModel):
    pincode: str 
    city: str 
    state: str 
    district: str 


class BulkRequest(BaseModel):
    pincodes: list[str]

    @field_validator('pincodes')
    @classmethod
    def validate_pincodes(cls, v):
        if len(v) == 0:
            raise ValueError('At least one pincode is required')
        if len(v) > 20:
            raise ValueError('Maximum 20 pincodes allowed per request')

        for code in v:
            if len(code) != 6 or not code.isdigit():
                raise ValueError('Each pincode must be 6 digits long')
        return v

class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str
    
class BulkResponse(BaseModel):
    status: str = 'success'
    found: int 
    not_found: int 
    results: list[LocationResponse]
    missing: list[str]
