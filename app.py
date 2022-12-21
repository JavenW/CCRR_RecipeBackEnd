from flask import Flask, request, Response
import http.client
import requests
import json
import pymysql
import os
# from storageService import StorageService
# from user import User
import boto3

api = Flask(__name__)

@api.route('/detaileddata')
def my_profile():
    conn = http.client.HTTPSConnection("spoonacular-recipe-food-nutrition-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "d0a33d5f84msh255c7930db96d6ap1d6ee0jsn992a6ed22da7",
        'X-RapidAPI-Host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    conn.request("GET", "/recipes/479101/information", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print("lalal")
    print(data.decode("utf-8"))


    return data.decode("utf-8")


@app.route("/getrecipe/<email>", methods=["GET"])
def get_recipe(email):
    ingredients = StorageService.get_items(email)
    user_id = User.get_userid_by_email(email)
    allergy = User.get_user_allergy_by_id(user_id)

    for food in allergy:
        if food in ingredients:
            del ingredients[food]

    ingredients = ingredients.keys()
    ingredients = ','.join(ingredients)

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients": ingredients, "number": "5", "ignorePantry": "true", "ranking": "1"}

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
