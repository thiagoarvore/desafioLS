
<body>
    <header>
        <p>Este repositório contém um desafio backend para o Lacrei Saúde.</p>
        <p>Se você quiser discutir ideias, problemas ou contribuições, sinta-se à vontade para nos contactar.</p>
    </header>
    <section>
        <h2>Tecnologias Utilizadas</h2>
        <ul>
            <li><img src="https://skillicons.dev/icons?i=python" width="20" height="20"/> Python: Ambiente de execução.</li>
            <li><img src="https://skillicons.dev/icons?i=django" width="20" height="20"/> Django: ORM facilitando o gerenciamento do banco de dados.</li>
        </ul>
    </section>
    <section>
        <h2>Requisitos</h2>
        <p>Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:</p>
        <ul>
            <li>Python (versão recomendada: 3.10 ou superior)</li>
            <li>Django (instalado automaticamente ao seguir as instruções abaixo)</li>
            <li>Outras dependências listadas no arquivo <code>requirements.txt</code></li>
        </ul>
    </section>
    <section>
        <h2>Instalação</h2>
        <p>Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>pip install -r requirements.txt</pre></div>
    </section>
    <section>
        <h2>Rodar o projeto</h2>
        <p>Após instalar as dependências, aplique as migrations no banco de dados com o comando:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py migrate</pre></div>
        <p>Crie o super usuário: (para o teste, login: admin, password: 1234578)</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py createsuperuser</pre></div>
        <p>Inicie o servidor:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py runserver</pre></div>
        <p>Para rodar o teste de criação de profissional (com criação automática de usuário no sistema):</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py test</pre></div>  
        </div>
    </section>
    <section>
        <h2>Utilizando a API</h2>
        <p>Para criar o registro de profissional (POST), ou listar todos os profissionais (GET):</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>url/professionals/</pre></div>
        <div>
            <h4>Requisitos para criação de profissional</h4>
            <table>
                <thead>
                    <th>Variável</th>
                    <th>Tipo</th>
                    <th>Explicação</th>
                </thead>
                <tbody>
                    <tr>
                        <td>user</td>
                        <td>Dict</td>
                        <td>Dicionário com "username" e "password"</td>
                    </tr>
                    <tr>
                        <td>address</td>
                        <td>Str</td>
                        <td>Endereço</td>
                    </tr>
                    <tr>
                        <td>occupation</td>
                        <td>Str</td>
                        <td>Profissão</td>
                    </tr>
                    <tr>
                        <td>name</td>
                        <td>Str</td>
                        <td>Nome completo</td>
                    </tr>
                    <tr>
                        <td>social_name</td>
                        <td>Str</td>
                        <td>Nome social</td>
                    </tr>
                </tbody>
            </table>
            <p>Exemplos:</p>
            <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>Request
            + Body
                {
                "user": {
                    "username": "usertest",
                    "password": "12345"
                }
                "address": "Rua Python",
                "occupation": "Dev"
                }</pre></div>
            <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>Response
            + Body
                {
                    "professional": {
                        "id": "6a5a1e36-9c00-4ee3-ab44-cdc8d5096b54",
                        "user": {
                            "id": "128aa3f2-e52b-4ff4-9a8a-8ca9c461cdf0",
                            "password": "12345",
                            "last_login": null,
                            "is_superuser": false,
                            "username": "usertest",
                            "first_name": "",
                            "last_name": "",
                            "email": "",
                            "is_staff": false,
                            "is_active": true,
                            "date_joined": "2024-10-30T11:28:11.050565-03:00",
                            "created_at": "2024-10-30T11:28:11.050565-03:00",
                            "updated_at": "2024-10-30T11:28:11.050565-03:00",
                            "groups": [],
                            "user_permissions": []
                        },
                        "social_name": null,
                        "name": null,
                        "address": "Rus Python",
                        "occupation": "dev",
                        "created_at": "2024-10-30T11:28:11.059562-03:00",
                        "updated_at": "2024-10-30T11:28:11.059562-03:00"
                    },
                }
            </pre></div>            
        </div>
    </section>
</body>