### Flask : moteur de l'application
### render_template : Affiche les gabarit d'affichage (templates)
### request : Traitement des requêtes HTTP
### url_for : Génère des Url
### redirect : redirection HTTP
from flask import Flask, render_template, request, url_for, redirect
### Objet d'interaction avec MongoDB
from pymongo import MongoClient
### Gestion des ids ade MongoDB
from bson.objectid import ObjectId
### Client Mongo
client = MongoClient('localhost', 27017)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "hello"

# Restaurants
@app.route('/restaurants', methods=['GET'])
def list_restaurants():     
    # Récupérer tous les documents de la collection restaurants
    restaurants_list = restaurants.find()   
    return render_template('restaurants.html', restaurants_list=restaurants_list)

## books
@app.route('/books', methods=['GET'])
def list_books():
    # return books
    books_list = books.find().limit(10)
    return render_template('index.html', books_list=books_list)

## companies
@app.route('/companies', methods=['GET'])
def list_companies():
    # return companies
    companies_list = companies.find().limit(15)
    return render_template('companies.html', companies_list=companies_list)

if __name__  == "__main__":
        ### Choix de la base de donnés
    db = client.school
    ### Accéder  aux requêtes sur les documents (la collection) 
    restaurants = db.restaurants
    books = db.books
    companies = db.companies
    ### Démarrage du Serveur
    app.run(debug=True, port=5000)



