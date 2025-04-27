from pydantic import BaseModel

class UserAuthProvidersCreate(BaseModel):
    user_id: int
    provider: str
    provider_user_id: str

class UserAuthProviders(UserAuthProvidersCreate):
    id: int