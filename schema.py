from pydantic import BaseModel

class CustomerModel(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    day: int
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str