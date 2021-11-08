from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from urllib.request import urlopen as uReq, Request
import requests
from flask_cors import CORS
from selenium import webdriver
app = Flask(__name__)
CORS(app)


ALLTEAMS = [
    "Hawks",
    "Celtics",
    "Nets",
    "Hornets",
    "Bulls",
    "Cavaliers",
    "Mavericks",
    "Nuggets",
    "Pistons",
    "Warriors",
    "Rockets",
    "Pacers",
    "Clippers",
    "Lakers",
    "Grizzlies",
    "Heat",
    "Bucks",
    "Timberwolves",
    "Pelicans",
    "Knicks",
    "Thunder",
    "Magic",
    "76ers",
    "Suns",
    "Blazers",
    "Kings",
    "Spurs",
    "Raptors",
    "Jazz",
    "Wizards",
]


@app.route('/nba', methods=["GET"])
def nba():
    # url = request.args.get('url')
    url = "https://www.streameast.io/live-nba-streams/"
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    ls = soup.find_all('li', class_="f1-podium--item")
    res = []
    for i in ls:
        a = i.find("a", class_="f1-podium--link f1-bg--white")
        suffix = a["href"]
        m = dict()
        team1 = None
        team2 = team1
        if "nba" in suffix:
            m["url"] = "https://www.streameast.io/" + suffix
            teams = suffix[4:-1].split('-')
            teams = [s for s in teams if not s.isdigit()]

            team1 = teams[0].capitalize() + " " + teams[1].capitalize()
            team2 = teams[2].capitalize() + " " + teams[3].capitalize()
            if len(teams) == 5:
                if teams[2].capitalize() in ALLTEAMS:
                    team1 = teams[0].capitalize() + " " + teams[1].capitalize() + " " + teams[2].capitalize()
                elif teams[4].capitalize() in ALLTEAMS:
                    team2 = teams[2].capitalize() + " " + teams[3].capitalize() + " " + teams[4].capitalize()
            elif len(teams) == 6:
                if teams[2].capitalize() in ALLTEAMS:
                    team1 = teams[0].capitalize() + " " + teams[1].capitalize() + " " + teams[2].capitalize()
                if teams[5].capitalize() in ALLTEAMS:
                    team2 = teams[3].capitalize() + " " + teams[4].capitalize() + " " + teams[5].capitalize()
            if teams[1] + teams[2] == "Trail Blazers":
                team1 = "Trail Blazers"
            elif (len(teams) == 5 and teams[3] + teams[4] == "Trail Blazers") or (len(teams)==6 and teams[4] + teams[5] == "Trail Blazers"):
                team2 = "Trail Blazers"
            m["team1"] = team1
            m["team2"] = team2
            res.append(m)
    return jsonify(res), 200


@app.route("/nba/stream", methods=["GET"])
def nbaStream():
    url = request.args.get('url')
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    ls = soup.find_all("div", id="PlayerDuzenBolumu")
    print(ls)
    print(type(ls))
    return str(ls)[1:-1], 200
    # return jsonify(res), 200



if __name__ == '__main__':
  app.run(debug=True)