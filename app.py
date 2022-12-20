from flask import Flask, request
import http.client
import requests

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

@app.route("/getrecipe", methods=["GET"])
def get_recipe():
    userid = request.args.get('userid', None)
    print(userid)
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients": "apples,flour,sugar", "number": "5", "ignorePantry": "true", "ranking": "1"}

    headers = {
        "X-RapidAPI-Key": "0f4d0b06f4mshe2ebd0d399fb0fcp1186e5jsne33884e5779d",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()

    ret = []

    for res in result:
        ret.append(res['id'])

    return ret
