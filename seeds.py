# seeds.py

import sys
from pathlib import Path

# Dodaj ścieżkę do katalogu projektu
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from blog import app, db
from blog.models import Entry
from faker import Faker

def generate_entries(how_many=10):
    fake = Faker()

    with app.app_context():
        for i in range(how_many):
            post = Entry(
                title=fake.sentence(),
                body='\n'.join(fake.paragraphs(15)),
                is_published=True
            )
            db.session.add(post)

        db.session.commit()

if __name__ == "__main__":
    generate_entries()
