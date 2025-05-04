from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

usuario = {}  # Em produção, substitua por banco de dados

# NewsAPI Key (ou variável de ambiente)
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '783346084cdd43c2b4a89c3441e09886')

# ---------------- CPF Validation Function ----------------
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True
# ---------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    mensagem = ''
    if request.method == 'POST':
        cpf_digitado = request.form['cpf']
        if not validar_cpf(cpf_digitado):
            mensagem = 'CPF inválido! Tente novamente.'
            return render_template('home.html', mensagem=mensagem)

        usuario['nome'] = request.form.get('nome')
        usuario['cpf'] = cpf_digitado
        usuario['endereco'] = request.form.get('endereco')
        usuario['interesses'] = request.form.getlist('interesses')
        usuario['atividades'] = request.form.get('atividades')
        usuario['eventos'] = request.form.get('eventos')
        usuario['compras'] = request.form.get('compras')

        return redirect(url_for('noticias'))
    return render_template('home.html', mensagem=mensagem)

@app.route('/noticias')
def noticias():
    query = request.args.get('q')

    if not query:
        query = ' OR '.join(usuario.get('interesses', [])) if usuario.get('interesses') else 'esports'

    url = f'https://newsapi.org/v2/everything?q={query}&language=pt&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    noticias_filtradas = []
    if data.get('articles'):
        for artigo in data['articles'][:10]:
            noticias_filtradas.append({
                'title': artigo['title'],
                'description': artigo['description'],
                'url': artigo['url'],
                'image': artigo['urlToImage']
            })

    return render_template('noticias.html', noticias=noticias_filtradas, usuario=usuario, query=query)

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    mensagem = ''
    if request.method == 'POST':
        cpf_digitado = request.form['cpf']
        if not validar_cpf(cpf_digitado):
            mensagem = 'CPF inválido! Tente novamente.'
            return render_template('perfil.html', usuario=usuario, mensagem=mensagem)

        usuario['nome'] = request.form.get('nome')
        usuario['cpf'] = cpf_digitado
        usuario['endereco'] = request.form.get('endereco')
        usuario['interesses'] = request.form.getlist('interesses')
        usuario['atividades'] = request.form.get('atividades')
        usuario['eventos'] = request.form.get('eventos')
        usuario['compras'] = request.form.get('compras')

        return redirect(url_for('noticias'))
    
    return render_template('perfil.html', usuario=usuario, mensagem=mensagem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
