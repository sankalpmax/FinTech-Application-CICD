from flask import Flask, render_template # type: ignore

app = Flask(__name__)

transactions = [
    {'id': 1, 'description': 'Investment', 'amount': 1000, 'type': 'Income'},
    {'id': 2, 'description': 'Groceries', 'amount': -50, 'type': 'Expense'},
    {'id': 3, 'description': 'Salary', 'amount': 3000, 'type': 'Income'},
    {'id': 4, 'description': 'Rent', 'amount': -800, 'type': 'Expense'}
]

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)

