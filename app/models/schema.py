from pydantic import BaseModel

class SignRequest(BaseModel):
    user_id: str
    document_id: str
    signature: str
    face_image: str