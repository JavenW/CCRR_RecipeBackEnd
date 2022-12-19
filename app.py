from flask import Flask
import http.client

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