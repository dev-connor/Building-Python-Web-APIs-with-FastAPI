from beanie import Document
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
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
class EventUpdate(Document):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'FastAPI Book Launch',
                'image': 'https://linktomyimage.com/image.png',
                'description': 'We will be discussing the contents of the FastAPI book in this event...',
                'tags': ['python','fastapi','book','launch'],
                'location': 'Google Meet',
            }
        }
