# 🚗 Car Sales System Sistema web desenvolvido com **Django** para cadastro e visualização de carros à venda. O projeto permite: * cadastrar carros * visualizar lista de carros * ver detalhes de cada carro * gerar descrição automática usando IA * upload de imagens --- # 🧰 Tecnologias utilizadas * Python * Django * SQLite * HTML / CSS / JavaScript * Google Gemini API --- # 📦 Como rodar o projeto ## 1️⃣ Clonar o repositório
bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
--- ## 2️⃣ Criar ambiente virtual
bash
python -m venv venv
Ativar o ambiente virtual: ### Windows
bash
venv\Scripts\activate
### Linux / Mac
bash
source venv/bin/activate
--- ## 3️⃣ Instalar dependências
bash
pip install -r requirements.txt
--- ## 4️⃣ Rodar migrações do banco
bash
python manage.py migrate
--- 5️⃣ Criar superusuário (admin) Para acessar o painel de administração do Django, crie um superusuário: python manage.py createsuperuser Ele vai pedir: Username: Email: Password: Password again: Depois você poderá acessar o admin em: http://127.0.0.1:8000/admin ## 6️⃣ Rodar o servidor
bash
python manage.py runserver
Acesse no navegador:
http://127.0.0.1:8000
--- # 🔑 Variáveis de ambiente Crie um arquivo .env na raiz do projeto:
GEMINI_API_KEY=sua_chave_aqui
--- # 📂 Estrutura do projeto
CARROS/                     # Diretório raiz do projeto
│
├── accounts/               # App para gerenciamento de usuários (login, registro, logout)
├── app/                    # App principal do projeto (configurações, URLs, WSGI)
├── cars/                   # App para cadastro e gerenciamento de carros
├── gemini_api/             # App ou módulo para integração com a API do Google Gemini
├── media/                  # Pasta para armazenar imagens enviadas (uploads)
├── static/                 # Arquivos estáticos ( imagens fixas)
├── venv/                   # Ambiente virtual do Python
├── .env                    # Variáveis de ambiente (chaves de API, SECRET_KEY, etc.)
├── .gitignore              # Arquivo para ignorar arquivos/pastas no Git
├── db.sqlite3              # Banco de dados SQLite (local)
├── manage.py               # Script principal do Django para gerenciamento do projeto
└── requirements.txt        # Dependências do projeto
--- # 👨‍💻 Autor Projeto desenvolvido para estudos de **Python e Django**. Kauan Zembruski
