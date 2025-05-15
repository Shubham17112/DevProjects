#what is context?
# context refres to the envireometn in which u r working  


# what is app context?
# app context u saying to the flask which app should u use to do something like for db.createall() u using app context
'''
with app.app_context():
    db.creat_all()
    
'''
'''
app2 = Flas(__name__)
this is secound app so how flask now htat u workign ur db shoudl commit with app1 or app2?
for thi u will use
with app2.app_context():
    db.creat_all()

'''

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

api= Api(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


class UserResource(Resource):
    def get(self,id):
        pass
    
    def post(self,id):
        data = request.get_json()
        new_user = User(id=id,)
        pass
    
    def delete(self,id):
        pass
    
    def update(self,id):
        pass
    
    
    
api.add_resource(UserResource,'/user/<id:int>')
if __name__ == "__main__":
    
    with app.app_context():
        db.create_all()
    
        
    app.run(debug=True)