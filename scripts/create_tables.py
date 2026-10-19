
from app.db.base import Base
from app.db.session import engine
import app.db.models  # Registers all models


def main():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

    print("Tables:", sorted(Base.metadata.tables.keys()))


if __name__ == "__main__":
    main()
