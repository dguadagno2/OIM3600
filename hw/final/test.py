import requests
from collections import defaultdict

# Define constants such as the API key and the predefined puuid
API_KEY = "RGAPI-c9bca582-a76f-41c3-b4d4-02ee1446eb54"
PUUID = "3uamI3EKz73OMvxFeDZ7wm6cN8TYvgFBmvIkKe3btn5jSaoyzZ_9Z8DhMLC6A2dTiNwHBiypUJ2GAw"
COUNTS = [50, 20]  # The number of most recent games to analyze

def get_match_ids(puuid, count=50, api_key=API_KEY):
    """
    Retrieves a list of match IDs for the given player (puuid).
    """
    match_id_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={api_key}"
    response = requests.get(match_id_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching match IDs: {response.status_code}, {response.text}")
        return []

def get_match_data(match_id, api_key=API_KEY):
    """
    Retrieves the match data for a given match ID.
    """
    match_data_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response = requests.get(match_data_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching match data: {response.status_code}, {response.text}")
        return {}

def calculate_kda(kills, deaths, assists):
    """
    Calculate the KDA for a player.
    """
    if deaths == 0:
        return kills + assists  # If no deaths, KDA can be just kills + assists
    else:
        return (kills + assists) / deaths

def get_top_champions(puuid, counts=COUNTS, api_key=API_KEY):
    """
    Retrieves the top 5 champions based on the combined highest KDA, win rate, and number of games played for the most recent 50 and 20 games.
    """
    top_champions_by_count = {}
    
    for count in counts:
        print(f"\nFetching top champions for the last {count} games...\n")
        match_ids = get_match_ids(puuid, count, api_key)
        if not match_ids:
            return f"No match data available for the last {count} games."
        
        champion_stats = defaultdict(lambda: {'kda': 0, 'wins': 0, 'games': 0})
        
        for match_id in match_ids:
            match_data = get_match_data(match_id, api_key)
            if not match_data:
                continue
            
            for participant in match_data['info']['participants']:
                if participant['puuid'] == puuid:
                    champion = participant['championName']
                    kills = participant['kills']
                    deaths = participant['deaths']
                    assists = participant['assists']
                    win = participant['win']
                    
                    kda = calculate_kda(kills, deaths, assists)
                    
                    # Update champion stats
                    champion_stats[champion]['kda'] += kda
                    champion_stats[champion]['wins'] += 1 if win else 0
                    champion_stats[champion]['games'] += 1
        
        # Calculate KDA, win rate, and incorporate games played into the score
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
        champion_rankings.sort(key=lambda x: x['score'], reverse=True)
        
        # Store the top 5 champions for this count
        top_champions_by_count[count] = champion_rankings[:5]
    
    return top_champions_by_count

# Fetch top champions for the 50 and 20 most recent games using the hardcoded PUUID
top_champions = get_top_champions(PUUID, counts=COUNTS)

if isinstance(top_champions, dict):
    for count, champions in top_champions.items():
        print(f"\nTop 5 champions for the last {count} games:")
        for i, champion in enumerate(champions, 1):
            print(f"Rank {i}: Champion: {champion['champion']}, Average KDA: {champion['avg_kda']:.2f}, Win Rate: {champion['win_rate']*100:.2f}%, Games Played: {champion['games_played']}")
else:
    print(top_champions)