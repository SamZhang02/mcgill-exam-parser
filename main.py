from PDFParser import PDFParser
from pathlib import Path
import json 

EXAM_SCHEDULE_PDF = Path("exam_schedule_2025.pdf")
OUT_PATH = Path("exams.json")

def main():
    parser = PDFParser(EXAM_SCHEDULE_PDF)
    exams = parser.parse()
    with open(OUT_PATH, 'w') as fp:
        json.dump([exam.to_dict() for exam in exams], fp)


if __name__ == "__main__":
    main()
