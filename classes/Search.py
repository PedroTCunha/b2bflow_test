import requests
from bs4 import BeautifulSoup

class Search:
    def __init__(self) -> None:
        pass

    def find_game_price(self, name):
        search_name = name.replace(" ", "+")
        url = f"https://store.steampowered.com/search/?sort_by=Price_DESC&term={search_name}&supportedlang=brazilian&category1=998"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = []
            games = soup.select('a.search_result_row')[:10]  # Get first 10 results            

            if not games:
                return None, None, None, None
            
            for game in games:

                name_element = game.select_one('span.title')
                game_name = name_element.text.strip() if name_element else "Unknown"
                
                discount_block = game.select_one('div.discount_block')
                
                if discount_block:
                    discount_element = discount_block.select_one('div.discount_pct')
                    original_price_element = discount_block.select_one('div.discount_original_price')
                    final_price_element = discount_block.select_one('div.discount_final_price')
                    
                    discount = discount_element.text.strip() if discount_element else None
                    original_price = original_price_element.text.strip() if original_price_element else None
                    final_price = final_price_element.text.strip() if final_price_element else None
                else:
                    discount = None
                    price_element = game.select_one('div.search_price')
                    if price_element:
                        original_price = ' '.join(price_element.text.strip().split())
                        final_price = original_price
                    else:
                        original_price = final_price = "Price not available"
            
                results.append((game_name, original_price, final_price, discount))

            return results
        
        except Exception as e:
            print(f"Error occurred while searching for game: {e}")
            return None, None, None, None
