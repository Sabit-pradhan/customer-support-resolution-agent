
from sqlalchemy import text

from app.db.session import engine


def main():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar_one()

        print("Database connection successful!")
        print(f"Test query result: {value}")

    except Exception as exc:
        print("Database connection failed.")
        print(f"Error: {exc}")
        raise


if __name__ == "__main__":
    main()
