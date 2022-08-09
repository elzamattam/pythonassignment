from pydantic import BaseModel
from typing import Optional


class electronics_table(BaseModel):
    electronic_device_name: str
    transistor_used: str
    transistor_used:str
    ic_used:str
    cmos_semi_used:str
    number_required: Optional[int] = None