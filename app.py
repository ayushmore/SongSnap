from flask import Flask, render_template, request, redirect, url_for
import lyricsgenius as lg
import openai
import os
from dotenv import load_dotenv

load_dotenv() 

# Load API keys from environment variables
genius = lg.Genius(os.getenv('LYRICS_GENIUS_API_KEY'), timeout=10)
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        length = request.form['length']
        return redirect(url_for('result', title = title, artist = artist, length = length))
    
    return render_template('home.html', title='', artist='', length='', summary=None)

@app.route('/result')
def result():
    title = request.args.get('title')
    artist = request.args.get('artist')
    length = request.args.get('length')
    try:
        song = genius.search_song(title, artist)
        context = "You are a renowned expert in understanding and explaining the lyrics of popular songs. A major music magazine has asked you to provide an in-depth analysis of the lyrics of a new hit song that has taken the music world by storm. Your job is to break down the meaning of the song and explain the underlying themes and metaphors used by the songwriter. You must provide a detailed and insightful analysis that will leave the magazine's readers with a greater appreciation and understanding of the song."
        prompt_refined = f"I'd like you to summarize the meaning of the lyrics of a song that I'll provide. Your task is to listen to the song and identify the key themes and messages conveyed by the lyrics. You should then provide {length} summarizing the lyrics in a way that captures the essence of the song and the emotions it conveys. Your summary should be concise yet insightful, and should provide a clear understanding of the song's meaning to someone who may not be familiar with it. The song is {song.title} by {song.artist}. The lyrics are provided below in a JSON format:\n\n{{\"Lyrics\":  {song.lyrics}}}"
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt_refined}
                ]
        )
        summary = response["choices"][0]["message"]["content"]
        return render_template('index.html', summary=summary, title=title, artist=artist)
    except Exception as e:
        error = "Song does not exist! Check your spelling and try again."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(port=8000, debug=True)






