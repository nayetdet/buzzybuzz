from pydantic import BaseModel, Field


class EmailDecisionSchema(BaseModel):
    is_important: bool = Field(
        description="Whether the email requires attention, action, or timely awareness."
    )
    reason: str = Field(
        description="Short explanation for the importance decision."
    )
