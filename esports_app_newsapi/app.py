from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
usuario = {}  # Aqui você poderia usar banco de dados futuramente

NEWS_API_KEY = '783346084cdd43c2b4a89c3441e09886'  # Substitua pela sua chave real da NewsAPI

@app.route('/', methods=['GET', 'POST'])
def home():
    global usuario
    mensagem = ''
    if request.method == 'POST':
        usuario = {
            'nome': request.form['nome'],
            'cpf': request.form['cpf'],
            'endereco': request.form['endereco'],
            'interesses': request.form.getlist('interesses'),
            'atividades': request.form['atividades'],
            'eventos': request.form['eventos'],
            'compras': request.form['compras']
        }
        mensagem = 'Cadastro realizado com sucesso!'
        return redirect(url_for('noticias'))
    return render_template('home.html', mensagem=mensagem)

@app.route('/noticias')
def noticias():
    query = request.args.get('q')

    if not query:
        # Junta todos os interesses em uma string separada por "OR" para busca mais ampla
        if usuario.get('interesses'):
            query = ' OR '.join(usuario['interesses'])
        else:
            query = 'esports'

    url = f'https://newsapi.org/v2/everything?q={query}&language=pt&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    noticias_filtradas = []
    if data.get('articles'):
        for artigo in data['articles'][:10]:  # Limita a 10 resultados
            noticias_filtradas.append({
                'title': artigo['title'],
                'description': artigo['description'],
                'url': artigo['url'],
                'image': artigo['urlToImage']
            })

    return render_template('noticias.html', noticias=noticias_filtradas, usuario=usuario, query=query)

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    global usuario
    if request.method == 'POST':
        usuario['nome'] = request.form['nome']
        usuario['cpf'] = request.form['cpf']
        usuario['endereco'] = request.form['endereco']
        usuario['interesses'] = request.form.getlist('interesses')
        usuario['atividades'] = request.form['atividades']
        usuario['eventos'] = request.form['eventos']
        usuario['compras'] = request.form['compras']
        return redirect(url_for('noticias'))
    return render_template('perfil.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)
