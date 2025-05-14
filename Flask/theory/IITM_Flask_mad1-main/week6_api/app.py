# creating basic flask Raw data 
# BY Defult methode is get
from flask import Flask, request

app = Flask(__name__)  # creating an instance of the Flask class

data = [
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Jane", "age": 30},
    {"id": 3, "name": "Bob", "age": 35}
]

@app.route("/")
def Index():
    return data



@app.route("/<id>")
def get_data(id):
    for e in data:
        if e["id"] == int(id):
            return e
    return {"message":"sorry nothing found for id %s"%(id)}


    
# Post request to create new data
# post request always send though the body 

@app.route("/add_emp",methods=["POST","GET"])
def add_emp():
    if request.method == "POST":
        name = request.json["name"]
        age = request.json["age"]
        id = request.json["id"]
        
        data.append({"name":name,"age":age,"id":id})
        return {"message":"employee added successfully"}
    return "add an employe"

    
    






if __name__ == "__main__":
    app.run(debug=True)  # running the application in debug mode
    
    


