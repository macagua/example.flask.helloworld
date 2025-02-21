# Hello World Tests

def test_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_request_example(client):
    response = client.get("/")
    assert b"<p>Hello, World!</p>\n" in response.data
