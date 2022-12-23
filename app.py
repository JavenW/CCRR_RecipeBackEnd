from flask import Flask, request, Response
import requests
import http.client
import json
import pymysql
import os
from user import User
from receipe_rec import ReceipeRec
from storageService import StorageService

import boto3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detaileddata/<id>', methods=["GET"])
def detailed_data(id):
    conn = http.client.HTTPSConnection("spoonacular-recipe-food-nutrition-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "d0a33d5f84msh255c7930db96d6ap1d6ee0jsn992a6ed22da7",
        'X-RapidAPI-Host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    conn.request("GET", "/recipes/" + id + "/information", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print("lalal")
    print(data.decode("utf-8"))


    return data.decode("utf-8")


@app.route("/getrecipe/<email>", methods=["GET"])
def get_recipe(email):
    # storage_url = "http://127.0.0.1:5011/getitems/" + email
    # ingredients = requests.request("GET", storage_url).json()
    # email = request.args.get('email', None)
    ingredients = StorageService.get_items(email)

    print(ingredients)
    user_id = User.get_userid_by_email(email)
    allergy = User.get_user_allergy_by_id(user_id)

    for food in allergy:
        if food in ingredients:
            del ingredients[food]

    ingredients = ingredients.keys()
    ingredients = ','.join(ingredients)

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients": ingredients, "number": "15", "ignorePantry": "true", "ranking": "1"}

    headers = {
        "X-RapidAPI-Key": "0f4d0b06f4mshe2ebd0d399fb0fcp1186e5jsne33884e5779d",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    if response:
        rsp = Response(json.dumps(response), status=200, content_type="app.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/randomreceipe", methods=["GET"])
def get_random_recei():

    result = ReceipeRec.get_random_receipe()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="app.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)