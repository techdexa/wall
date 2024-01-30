import requests
from bs4 import BeautifulSoup

def extract_src_from_id(url, id_name):
    try:
        # Set the headers for the request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        # Send a GET request to the URL with the specified headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Use BeautifulSoup to find elements with the specified ID
            element = soup.find(id=id_name)

            # Extract src attribute from the found element
            src = element.get('src') if element and element.has_attr('src') else None

            return src

        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Read URLs from a text file, assuming one URL per line
with open('wallpaperflareanimegirls.txt', 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

# Replace 'show_img' with the actual ID you want to extract
id_name = 'show_img'

# Loop through each URL in the file
for url in urls:
    # Extract src attribute from the element with the specified ID for each URL
    result = extract_src_from_id(url, id_name)

    # Print the result and append to the file
    if result:
        
        with open('all_src_attributes.txt', 'a', encoding='utf-8') as output_file:
            output_file.write("%s\n" % result)
            
    else:
        print(f"URL: {url}, No element found with the ID: {id_name}")

print("All src attributes appended to all_src_attributes.txt")
