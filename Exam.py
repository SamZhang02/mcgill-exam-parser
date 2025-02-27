from dataclasses import dataclass
from datetime import datetime

@dataclass 
class Exam:
    title:str
    course_code:str
    description:str
    section:str
    start:datetime
    end:datetime

    def to_dict(self):
        return {
            "title": self.title,
            "course_code": self.course_code,
            "description": self.description,
            "section": self.section,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
        }
