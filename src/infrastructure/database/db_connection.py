from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class DbSessionHandler:
    def __init__(self, connection_url: str) -> None:
        # TODO: read values from config for DB connection url!
        self._connection_url = "postgresql://satoshi:satoshi123@localhost:5432/satoshiguard"
        self._engine = create_engine(self._connection_url, echo=True)
        self._session: Session

    def __enter__(self):
        session = sessionmaker(self._engine)
        self._session = session
        return self._session

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is not None:  # An exception occurred
            self._session.rollback()
        else:  # No exceptions, so commit the changes
            self._session.commit()

        self._session.close()

    @property
    def session(self):
        return self._session
