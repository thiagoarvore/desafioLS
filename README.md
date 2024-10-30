
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
        <p>Inicie o servidor:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py runserver</pre></div>
        <p>Para rodar o teste de criação de profissional (com criação automática de usuário no sistema):</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py test</pre></div>  
        </div>
    </section>
</body>