from flask import Flask, render_template, request, jsonify
from models import db, Artist, Song

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///montreal_music.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/songs', methods=['POST'])
def add_song():
    print(f"POST /api/songs called with data: {request.json}")  # Print statement 1
    data = request.json
    try:
        new_song = Song(title=data['title'], artist_id=data['artist_id'])
        db.session.add(new_song)
        print(f"Inserting new song: {new_song.title}")  # Print statement 2
        db.session.commit()
        print(f"New song added successfully: {new_song.to_dict()}")  # Print statement 3
        return jsonify(new_song.to_dict()), 201
    except Exception as e:
        print(f"Error adding song: {str(e)}")  # Print statement 4
        return jsonify({"error": str(e)}), 400

@app.route('/api/artists', methods=['GET'])
def get_artists():
    print("GET /api/artists called")  # Print statement 5
    artists = Artist.query.all()
    print(f"Returning {len(artists)} artists")  # Print statement 6
    return jsonify([artist.to_dict() for artist in artists])

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
