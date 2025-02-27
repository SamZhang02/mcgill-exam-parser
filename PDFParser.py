import fitz  

from pathlib import Path
import re 
from datetime import datetime

from Exam import Exam

class PDFParser:
    exam_pattern = re.compile(
        r"(?P<course>\w+ \d+)\n"
        r"(?P<section>\d+)\n"
        r"(?P<title>.+?)\n"
        r"(?P<description>.+?)\n"
        r"(?P<start_date>\d{2}-[A-Za-z]+-\d{4} at \d+:\d+ [APM]+)\n"
        r"(?P<end_date>\d{2}-[A-Za-z]+-\d{4} at \d+:\d+ [APM]+)",
        re.DOTALL
    )

    def __init__(self, pdf:Path) -> None:
        self.pdf: Path = pdf

    def parse(self) -> list[Exam]:
        doc = fitz.open(self.pdf)
        matches = [] 
        for page in doc:
            text:str = page.get_text("text") #pyright: ignore
            matches += [m.groupdict() for m in self.exam_pattern.finditer(text)]

        return [Exam(
            match['title'], 
            match['course'],
            match['description'],
            match['section'],
            self._parse_date(match['start_date']),
            self._parse_date(match['end_date']),

        ) for match in matches]


    def _parse_date(self, date_str: str) -> datetime:
        return datetime.strptime(date_str, "%d-%b-%Y at %I:%M %p")
