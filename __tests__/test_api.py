import pytest
import requests
import responses

# Function to test
def fetch_artworks(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Test Case
@responses.activate
def test_fetch_artworks():
    api_url = 'https://api.example.com/artworks'
    
    # Mocking API Response
    responses.add(
        responses.GET,
        api_url,
        json=[{'id': 1, 'title': 'Artwork 1'}, {'id': 2, 'title': 'Artwork 2'}],
        status=200
    )
    
    # Call the function
    data = fetch_artworks(api_url)
    
    # Assertions
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['title'] == 'Artwork 1'

if __name__ == '__main__':
    pytest.main()
