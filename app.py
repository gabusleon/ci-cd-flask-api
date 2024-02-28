from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://example_sum_postgres_use:0l7c0l80KYKnbRL6VvCclRhgmchN2uu7@dpg-cnfqblnsc6pc73el8be0-a/example-sum-postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer, nullable=False)
    num2 = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Sum {self.id}: {self.num1} + {self.num2} = {self.result}>'
    
@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2

    # Guardar el resultado en la tabla Sum
    sum_entry = Sum(num1=num1, num2=num2, result=result)
    db.session.add(sum_entry)
    db.session.commit()

    return jsonify({'result': result})

with app.app_context():
        db.drop_all()
        db.create_all()

'''
if __name__ == '__main__':
    app.run(debug=True)
'''