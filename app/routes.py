from flask import Blueprint, render_template, request, redirect, url_for
from .models import add_transaction, get_all_transactions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        add_transaction(description, amount, date)
        return redirect(url_for('main.dashboard'))

    transactions = get_all_transactions()
    return render_template('dashboard.html', transactions=transactions)