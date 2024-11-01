import requests

BASE_URL = "http://127.0.0.1:8000"


def test_shorten_url():
    url = {"original_url": "https://example.com"}
    response = requests.post(f"{BASE_URL}/shorten", json=url)
    assert response.status_code == 200
    data = response.json()
    assert "original_url" in data
    assert "short_url" in data
    assert data["original_url"] == "https://example.com"
    print("Тест на добавление сокращённой ссылки в базу данных пройден.")


def test_redirect_to_original():
    url = {"original_url": "https://example.com"}
    response = requests.post(f"{BASE_URL}/shorten", json=url)
    data = response.json()
    short_url = data["short_url"]

    redirect_response = requests.get(f"{BASE_URL}/{short_url}")
    assert redirect_response.status_code == 200
    assert redirect_response.url == "https://example.com"
    print("Тест на редирект пройден.")


if __name__ == "__main__":
    test_shorten_url()
    test_redirect_to_original()
