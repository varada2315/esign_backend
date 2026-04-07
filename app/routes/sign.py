from fastapi import APIRouter, HTTPException
from app.models.schema import SignRequest
from app.services.image_utils import decode_base64_image, save_image
from app.services.face_detection import detect_face
from datetime import datetime
import os

router = APIRouter()

@router.post("/sign-document")
def sign_document(data: SignRequest):

    # Decode images
    signature_img = decode_base64_image(data.signature)
    face_img = decode_base64_image(data.face_image)

    if signature_img is None or face_img is None:
        raise HTTPException(status_code=400, detail="Invalid image data")

    # Face detection
    if not detect_face(face_img):
        raise HTTPException(status_code=403, detail="No face detected")

    # Create storage folder
    os.makedirs("storage/signatures", exist_ok=True)
    os.makedirs("storage/faces", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    sig_path = f"storage/signatures/{data.user_id}_{timestamp}.png"
    face_path = f"storage/faces/{data.user_id}_{timestamp}.png"

    # Save images
    save_image(signature_img, sig_path)
    save_image(face_img, face_path)

    # Audit log
    with open("storage/log.txt", "a") as f:
        f.write(f"{data.user_id},{data.document_id},{timestamp}\n")

    return {
        "message": "Document signed successfully",
        "signature_path": sig_path
    }