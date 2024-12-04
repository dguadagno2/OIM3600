import requests
from collections import defaultdict

# Need to Replace API Key every 24 hours, expire wednesday 6:27AM
API_KEY = "RGAPI-cd6f26cf-a784-4618-bb4b-58d6f9a241c0"
PUUID = "3uamI3EKz73OMvxFeDZ7wm6cN8TYvgFBmvIkKe3btn5jSaoyzZ_9Z8DhMLC6A2dTiNwHBiypUJ2GAw"
COUNTS = [50, 20] # Number of matches analyzed

def get_match_ids(puuid, count=50, api_key=API_KEY) :
    """
    Retrieves a list of match IDs for the given player (puuid)
    """
    match_id_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={api_key}"
    response = requests.get(match_id_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching match IDs: {response.status_code}, {response.text}") # Used ChatGPT to debug as it was not showing the error response before, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a  
        return []

def get_match_data(match_id, api_key=API_KEY):
    """
    Retrieves match data for given match ID 
    """
    match_data_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response = requests.get(match_data_url)

    if response.status_code == 200:
        return response.json()
    else: 
        print(f"Error fetching match data: {response.status_code}, {response.text}")
        return []
    
def calculate_kda(kills, death, assists):
    """
    Calculates the KDA 
    """
    if death == 0:
        return kills + assists # used chatGPT to debug, would return zero without this addition, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a 
    else:
        return (kills + assists) / death
    
def get_top_champions(puuid, counts=COUNTS, api_key=API_KEY):
    """
    Retrieves the top 5 champions based on the combined highest kda , win rate, and number of games played for 50 and 20 game increments 
    """
    top_champions_by_count = {}

    for count in counts:
        print(f"\nFetching top champions for the last {count} games...\n")
        match_ids = get_match_ids(puuid, count, api_key)
        if not match_ids:
            return f"No match data available for the last {count} games"

        champion_stats = defaultdict(lambda: {'kda': 0, 'wins': 0, 'games': 0})

        for match_id in match_ids:
            match_data = get_match_data(match_id, api_key)
            if not match_data:
                continue

            for participant in match_data['info']['participants']: # Used ChatGPT as code would return all participants when I wanted it to only return my information, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a
                if participant['puuid'] == puuid:
                    champion = participant['championName']
                    kills = participant['kills']
                    deaths = participant['deaths']
                    assists = participant['assists']
                    win = participant['win']

                    kda = calculate_kda(kills, deaths, assists)

                    # Used chatGpt to debug, champion stats were only being taken from one game, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a 
                    champion_stats[champion]['kda'] += kda 
                    champion_stats[champion]['wins'] += 1 if win else 0 
                    champion_stats[champion]['games'] += 1

        # Used ChatGPT to debug my calculation, for incorporating win rate, kda and games played, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a 
        champion_rankings = []
        for champion, stats in champion_stats.items():
            win_rate = stats['wins'] / stats['games'] if stats['games'] > 0 else 0
            avg_kda = stats['kda'] / stats['games'] if stats['games'] > 0 else 0
            games_played = stats['games']

            # Combine KDA, win rate, and games played 
            combined_score = (avg_kda * 0.5) + (win_rate * 0.3) + (games_played * 0.2) 

            champion_rankings.append({
                'champion': champion, 
                'avg_kda': avg_kda, 
                'win_rate': win_rate, 
                'games_played': games_played, 
                'score': combined_score
            })

        # Sort by combined score (highest first)
        champion_rankings.sort(key=lambda x: x['score'], reverse=True) # Used ChatGPT to help sort the data 

        # Store the top 5 champions for this count 
        top_champions_by_count[count] = champion_rankings[:5]

    return top_champions_by_count

