# tdd_sqs_send_message_python

Criar virtualenv:

    pip install virtualenv
    virtualenv venv
    
Ativar virtualenv

    source venv/bin/activate

Instalar dependências:

    pip install -r requirements.txt

Rodar os testes unitários:

    pytest --cov=app tests/   

Criar arquivo zip para subir no lambda:

    zip -r sqs_send_message_python.zip lambda_function.py app/* -x "*.pyc" 

Desativar virtualenv

    deactivate

Atualizar código do lambda:

    aws lambda update-function-code --function-name <lambda-function-name> --zip-file fileb://sqs_send_message_python.zip

    