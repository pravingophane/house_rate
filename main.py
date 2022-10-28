from sre_constants import SUCCESS
from flask import Flask, jsonify, render_template, request
from Pune_House_data.utils import PuneHousePricePrediction
import config

app = Flask(__name__) # instance

@app.route("/")   #"/" >> home page
def hello_flask():
    print("Welcome to Pune House Price Prediction")
    return render_template("index.html")
    return "SUCCESS"

@app.route("/Pune_House_Price_prediction", methods=["POST", "GET"])
def get_house_price():
    if request.method == "GET":
        print("We are using GET Method") 

        # data = request.form
        # print("Data ::",data)

        # availability = data["availability"]
        # size = data["size"]
        # new_total_sqft = eval(data["new_total_sqft"])
        # bath = int(data["bath"])
        # balcony = int(data["balcony"])
        # site_location = data["site_location"]
        # area_type = data["area_type"]




        availability = request.args.get("availability")
        size = request.args.get("size")
        new_total_sqft = (request.args.get("new_total_sqft"))
        bath = (request.args.get("bath"))
        balcony = request.args.get("balcony")
        site_location = request.args.get("site_location")
        area_type = request.args.get("area_type")
        
        Pune_house = PuneHousePricePrediction(availability, size, new_total_sqft, bath, balcony, site_location, area_type)
        #Pune_house = PuneHousePricePrediction(size, new_total_sqft, bath, balcony, site_location, area_type)

        charges = Pune_house.get_Pune_House_price()
        return render_template("index.html", prediction = charges)
        print(f"Pune House price prediction is {round(charges,2)}/- Rs. Only")  
        # return "Working"
          

    else:
        print("We are using POST Method")
        
        availability = request.form.get("availability")
        # print("availability >>>",availability)
        size = request.form.get("size")  
        new_total_sqft = (request.form.get("new_total_sqft"))
        bath = (request.form.get("bath"))
        balcony = request.form.get("balcony")
        site_location = request.form.get("site_location")
        area_type = request.form.get("area_type")

        med_ins = PuneHousePricePrediction(availability, size, new_total_sqft, bath, balcony, site_location, area_type)
        charges = med_ins.get_Pune_House_price()
        return render_template("index.html", prediction = charges)
        return "Success"


if __name__ =="__main__":
    app.run(host = "0.0.0.0", port=5001,debug=True)
