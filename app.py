# app.py
from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
    return f"""
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href="/animals/dogs">Dogs</a></li>
        <li><a href="/animals/cats">Cats</a></li>
        <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    """

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1>List of {pet_type.capitalize()}</h1><ul>"
    for i, pet in enumerate(pets.get(pet_type, [])):
        html += f'<li><a href="/animals/{pet_type}/{i}">{pet["name"]}</a></li>'
    html += "</ul>"
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    try:
        pet = pets[pet_type][pet_id]
        return f"""
        <h1>{pet['name']}</h1>
        <img src="{pet['url']}" width="300" style="border-radius:10px;">
        <p>{pet['description']}</p>
        <ul>
            <li><strong>Breed:</strong> {pet['breed']}</li>
            <li><strong>Age:</strong> {pet['age']} years</li>
        </ul>
        <a href="/animals/{pet_type}">← Back to {pet_type.capitalize()}</a>
        """
    except:
        return "<h1>Pet not found</h1>"

if __name__ == '__main__':
    app.run(debug=True)
