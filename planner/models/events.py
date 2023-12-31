from pydantic import BaseModel
from beanie import Document
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    creator: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'title': 'FastAPI Book Launch',
                'image': 'https://linktomyimage.com/image.png',
                'description': 'We will be discussing the contents of the FastAPI book in this event...',
                'tags': ['python','fastapi','book','launch'],
                'location': 'Google Meet',
            }
        }
    class Settings:
        name = 'events'
class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'title': 'FastAPI Book Launch',
                'image': 'https://linktomyimage.com/image.png',
                'description': 'We will be discussing the contents of the FastAPI book in this event...',
                'tags': ['python','fastapi','book','launch'],
                'location': 'Google Meet',
            }
        }
