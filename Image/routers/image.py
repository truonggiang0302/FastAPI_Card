from fastapi import APIRouter, HTTPException
from .. import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from typing import Optional
import requests, random
import os
from datetime import datetime
from typing import List

router = APIRouter(
    prefix='/image',
    tags=['Images']
)
get_db = database.get_db

@router.get("/{param}")
async def save_image(param: Optional[str] = None, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    url_img = requests.get(f'https://cataas.com/cat/{param}', stream=True)
    name = random.randrange(1, 100)
    filename = 'cat' + str(name) + '.jpeg'
    file = open('Image/static/images/'+filename, 'wb')
    url = f'http://127.0.0.1:8000/static/images/{filename}'
    file.write(url_img.content)
    new_user_request = models.User_Request(image_url=url, time=datetime.now())
    db.add(new_user_request)
    db.commit()
    db.refresh(new_user_request)
    file.close()
    return new_user_request

@router.get("/",response_model=List[schemas.ShowUser_Request])
async def return_image(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    all_image_url = db.query(models.User_Request).all()
    return all_image_url
