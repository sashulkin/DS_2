from flask import Flask, render_template

# экземпляр класса Flask
app = Flask(__name__)

# декоратор машрутизации 
@app.route('/')
def index_page():
    """
    Функция логики страницы 'index page'
    """
    return render_template('index.html')

@app.route('/product')
def product_page():
    """
    Функция логики страницы 'product page'
    """
    return render_template('product.html')

@app.route('/contact')
def contact_page():
    """
    Функция логики страницы 'contact page'
    """
    return render_template('contact.html')

# конструкция запуска 
if __name__ == "__main__":
    app.run(debug=True)