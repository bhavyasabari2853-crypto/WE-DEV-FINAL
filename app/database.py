"""Database configuration and session management."""

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Allow configuring the database URL via environment (recommended for production)
# Defaults to a local SQLite file for development.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./finance.db")

# SQLite requires a special connect arg. Only set it for sqlite URLs.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False,
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create base class for models
Base = declarative_base()


def get_db() -> Generator:
    """
    Dependency function to get database session.
    
    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)
