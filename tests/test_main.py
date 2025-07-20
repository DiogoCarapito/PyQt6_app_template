from main import create_app


def test_create_app():
    app, window = create_app()
    assert app is not None
    assert window is not None
