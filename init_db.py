from sqlalchemy.orm import Session
from database import get_db  # Adjust the import according to your project structure
from models import User
from utils import hash_password

def create_admin_user(db: Session):
    admin_username = "admin"
    admin_password = "admin"
    hashed_password = hash_password(admin_password)

    # Check if admin user already exists
    existing_user = db.query(User).filter(User.username == admin_username).first()
    if not existing_user:
        admin_user = User(username=admin_username, password=hashed_password, user_type="admin")
        db.add(admin_user)
        db.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")

if __name__ == "__main__":
    db = next(get_db())
    create_admin_user(db)
