from flask import Flask, render_template
from backend.champion_stats import get_top_champions  # Import from backend folder

app = Flask(__name__)

# My personal PUUID
PUUID = "3uamI3EKz73OMvxFeDZ7wm6cN8TYvgFBmvIkKe3btn5jSaoyzZ_9Z8DhMLC6A2dTiNwHBiypUJ2GAw"

@app.route('/')
def index():
    #fetch top champions from personal PUUID
    top_champions = get_top_champions(PUUID)

    return render_template('index.html', top_champions=top_champions)
                           
if __name__ == '__main__':
    app.run(debug=True)