from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Barbell(db.Model):
    id = db.Column(db.Integer,  nullable=False,  primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class BarbellSchema(ma.Schema):
    class Meta:
        fields = ('name', 'price', 'weight')


barbell_schema = BarbellSchema()
barbells_schema = BarbellSchema(many=True)
db.create_all()


@app.route("/barbell", methods=["POST"])
def add_barbell():
    name = request.json['name']
    price = request.json['price']
    weight = request.json['weight']

    new_barbell = Barbell(name, price, weight)

    db.session.add(new_barbell)
    db.session.commit()

    return barbell_schema.jsonify(new_barbell)


@app.route("/barbell", methods=["GET"])
def get_barbells():
    all_barbells = Barbell.query.all()
    result = barbells_schema.dump(all_barbells)
    return jsonify(result.data)


@app.route("/barbell/<id>", methods=["GET"])
def barbell_detail(id):
    barbell = Barbell.query.get(id)
    return barbell_schema.jsonify(barbell)


@app.route("/barbell/<id>", methods=["PUT"])
def barbell_update(id):
    barbell = Barbell.query.get(id)

    name = request.json['name']
    price = request.json['price']
    weight = request.json['weight']

    barbell.name = name
    barbell.price = price
    barbell.weight = weight

    db.session.commit()
    return barbell_schema.jsonify(barbell)


@app.route("/barbell/<id>", methods=["DELETE"])
def barbell_delete(id):
    barbell = Barbell.query.get(id)
    db.session.delete(barbell)
    db.session.commit()

    return barbell_schema.jsonify(barbell)


if __name__ == '__main__':
    app.run()
