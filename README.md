# eSign Backend with Face Detection

## Features
- Upload signature
- Capture face image
- Backend face verification
- Prevent signing without face
- Audit logging

## API Endpoint

POST /sign-document

### Request Body:
```json
{
  "user_id": "123",
  "document_id": "abc",
  "signature": "base64",
  "face_image": "base64"
}

#RUN PROJECT 
pip install -r requirements.txt
uvicorn app.main:app --reload

#RESPONSE 
{
  "message": "Document signed successfully"
}

#OPEN 
http://127.0.0.1:8000/docs