from flask import Flask, render_template

app = Flask ("Lista de Filmes")

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/filmes')
def livros():
    return render_template('filmes.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/home')
def home():
    return render_template('home.html')

app.run(debug=True)
