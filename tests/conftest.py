import pytest
from app import create_app
from app.models import db

@pytest.fixture
def app():
    import tempfile
    import os

    fd, db_path = tempfile.mkstemp()
    app = create_app({
        'environment': 'test',
        'db_path': db_path,
        })
    with app.test_client() as client:
        with app.app_context():
            db.session.create_all()
        yield app
    os.close(fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()
