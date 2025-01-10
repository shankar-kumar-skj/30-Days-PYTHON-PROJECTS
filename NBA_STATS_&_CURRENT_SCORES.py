# JSON => JAVA SCRIPT OBJECT ROTATION 
from requests import get
from pprint import PrettyPrinter

BASE_URL="https://data.nba.net"
All_JSON="/prod/v1/today.json"

printer=PrettyPrinter()

def get_links():
    data=get(BASE_URL+All_JSON).json()
    # print(data)
    links = data['links']
    return links
    # printer.pprint(links)

def get_scoreboard():
    scoreboard=get_links()['currentScoreboard']
    # data = get(BASE_URL + scoreboard).json()['games']
    games = get(BASE_URL + scoreboard).json()['games']

    # printer.pprint(data)
    for game in games:
        home_team=game['hTeam']
        away_team=game['vTeam']
        clock=game['clock']
        peroid=game['period']
        # printer.pprint(game.keys())
        # print(f"{home_team} vs {away_team}, {clock}, {peroid}")
        print("-----------------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} vs {away_team['score']}")
        print(f"{clock} vs {peroid['current']}")
        
    # printer.pprint(data.keys())

def get_stats():
    stats=get_links()['leagueTeamStatsLeaders']
    teams=get(BASE_URL+stats).json()['league']['standard']['regularSeason']['teams']
    # printer.pprint(teams[0].keys())

    teams=list(filter(lambda x: x['team'] != "Team",teams))
    team.sort(key=lambda x: int (x['ppg']['rank']))



    for i, team in enumerate(teams):
        name=team['name']
        nickname=team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i +1}. {name}-{nickname}-{ppg}")

get_stats()