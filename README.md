# KYF_Esports_FURIA
Um site de notícias que disponibiliza informações sobre os gostos do usuário.

Aplicação web que exibe notícias personalizadas sobre eSports com base nos interesses do usuário, suas atividades e perfis que ele segue nas redes sociais como Twitter.

Funcionalidades

- Formulário de cadastro com dados pessoais e interesses.
- Integração com a [NewsAPI](https://newsapi.org) para exibição de notícias.
- Opção de fornecer usuário do Twitter para coletar perfis seguidos.
- Filtro automático de notícias baseado:
  - Em interesses manuais.
  - Em perfis seguidos no Twitter.
  - (Opcional futuramente: posts curtidos nas redes sociais).

Tecnologias utilizadas

- Python + Flask
- HTML/CSS/JavaScript
- NewsAPI (para notícias)
- Twitter API (opcional, para seguir perfis)
- Bootstrap (opcional para estilo)

Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/esports-news-app.git
   cd esports-news-app

   depois use o comando no terminal:
   python app.py
