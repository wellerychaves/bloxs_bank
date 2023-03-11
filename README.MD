## 1. Configuração inicial

Ao clonar o repositorio execute os seguintes comandos:

Para criar o ambiente virtual

```shell
python -m venv venv
```

(Linux) Para ativar o ambiente virtual

```shell
source venv/bin/activate
```

(Windows) Para ativar o ambiente virtual

```shell
.\venv\Scripts\activate.ps1
```

em seguida troque para pasta MySQL para executar os comandos do docker

```shell
cd MySQL
```

```shell
pip install -r requirements.txt
```

```shell
docker compose build
```

```shell
docker compose up -d
```

Em seguida volte para pasta principal do projeto

```shell
cd ..
```

Crie e execute as migrations

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

Por fim, execute a api

```shell
python manage.py runserver
```

<!-- 
exemplo para criar Pessoa
{

}

exemplo para criar Conta
{
    
} 
-->