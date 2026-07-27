import requests
from bs4 import BeautifulSoup

# BBC News Website
url = "https://www.bbc.com/news"

try:
    # Send HTTP request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <h2> tags
    headlines = soup.find_all("h2")

    # Open text file for writing
    with open("headlines.txt", "w", encoding="utf-8") as file:

        print("\n========== TOP NEWS HEADLINES ==========\n")

        count = 1

        # Display only the first 10 headlines
        for headline in headlines[:10]:
            text = headline.get_text(strip=True)

            if text:
                print(f"{count}. {text}")
                file.write(f"{count}. {text}\n")
                count += 1

    print("\n========================================")
    print("Headlines saved successfully in headlines.txt")

except requests.exceptions.RequestException as error:
    print("Error while fetching the website:")
    print(error)