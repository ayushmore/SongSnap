from flask import Flask, render_template, request, redirect, url_for, session
import lyricsgenius as lg
import openai
import os
import time
from dotenv import load_dotenv
import urllib.parse


load_dotenv() 

# Load API keys from environment variables
genius = lg.Genius(os.getenv('LYRICS_GENIUS_API_KEY'), timeout=10)
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['title'] = request.form['title']
        session['artist'] = request.form['artist']
        return redirect(url_for('result'))
    
    session.clear()
    return render_template('index.html', title='', artist='', length='', summary=None)

@app.route('/result')
def result():
    if not session.get('title'):
        return redirect(url_for('index'))
    title = session.get('title')
    artist = session.get('artist')
    # length = session.get('length')
    try:
        start_time = time.time()
        song = genius.search_song(title, artist)
        end_time = time.time()

        print(f"Time taken to search song: {end_time - start_time} seconds")
        context = f"You are a master wordsmith and musical connoisseur with an engaging and humorous tone tasked with providing a thought-provoking and original 'lyrical insight' into the hit song '{title}' by '{artist}'"
        prompt_refined = f"Your mission is to provide a 'lyrical insight' into the song that captures its essence. Your lyrical insight should be: a single, powerful, in-depth sentence that captures the essence of the song and its underlying themes. Provide a unique and captivating 'lyrical insight' that sheds new light on the song's message that amazes the readers. Be engaging and humorous in your tone. The lyrics are provided below in a JSON format:\n\n{{\"Lyrics\":  {song.lyrics}}}"
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt_refined}
                ]
        )
        end_time = time.time()
        print(f"Time taken to create summary: {end_time - start_time} seconds")
        
        summary = response["choices"][0]["message"]["content"]
        session.clear()
        return render_template('index.html', summary=summary, title=title, artist=artist)
    
    except Exception as e:
        print(e)
        error = f"Could not generate summary! See if your song is on Genius and type out the song title and artist as is."
        return render_template('index.html', error=error, title=title, artist=artist)

if __name__ == '__main__':
    app.run(port=8000, debug=True)






