from classes.Search import Search
from classes.Logger import Logger

search = Search()
logger = Logger()

game_name = str(input('Digite o nome do jogo para procurar: ')) 
results = search.find_game_price(game_name)
logger.log_results(game_name, results)
