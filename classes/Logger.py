from datetime import datetime

class Logger:
    def __init__(self) -> None:
        pass

    def log_results(self, search_term: str, results: list) -> None:
        data_hora_atual = datetime.now()
        data_hora = data_hora_atual.strftime("[%d/%m/%Y - %H:%M]")
        
        if not results:
            log_message = f"{data_hora} - No results found for '{search_term}'\n"
        else:
            log_message = f"{data_hora} - Search results for '{search_term}':\n"
            for idx, (name, price, final_price, discount) in enumerate(results, 1):
                if discount:
                    log_message += f"  {idx}. {name}: Original {price}, {discount} off → {final_price}\n"
                else:
                    log_message += f"  {idx}. {name}: (no discount)\n"
        
        try:
            with open("price_logger.txt", "a", encoding='utf-8') as log:
                log.write(log_message)
        except Exception as e:
            print(f"Error writing to log file: {e}")
