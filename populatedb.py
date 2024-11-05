from app import create_app, db
from app.models import Shift
from datetime import datetime

app = create_app()

with app.app_context():
    db.create_all()  

    shift1 = Shift(
        employee='John Doe',
        start_time=datetime(2024, 10, 25, 9, 0),
        end_time=datetime(2024, 10, 25, 17, 0)
    )
    shift2 = Shift(
        employee='Jane Smith',
        start_time=datetime(2024, 10, 25, 12, 0),
        end_time=datetime(2024, 10, 25, 20, 0)
    )
    
    db.session.add(shift1)
    db.session.add(shift2)
    db.session.commit()

    print("Database populated with sample shifts!")
