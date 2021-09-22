import json

from app.exceptions.custom_exceptions import InvalidSQSParametersException
from app.sqs_service import SQSService


class Process(object):

    def __init__(self) -> object:
        self.sqs_service = SQSService()

    def execute(self, event):

        try:

            message = self.validate_param_values(event)

            sqs_client = self.sqs_service.get_client()

            response = self.sqs_service.execute_send_message(sqs_client, message)

            return self.build_response(response)

        except InvalidSQSParametersException as ex:
            print(ex)
            return self.build_response(None)
        except Exception as ex:
            print(ex)
            return self.build_response(None)

    def validate_param_values(self, event):

        if 'body' not in event:
            raise InvalidSQSParametersException('O parâmetro body não foi enviado')

        body = json.loads(event['body'])

        if 'message' not in event['body'] or body['message'] == '':
            raise InvalidSQSParametersException('O parâmetro message não foi enviado')

        return body['message']

    def build_response(self, message_id=None):
        """
        Método que constrói a resposta da execução desse processo
        :param message_id: ID da mensagem quando enviada com sucesso
        :return: Resposta no padrão do API Gateway
        """

        if message_id is not None:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'MessageId': message_id
                })
            }

        return {
            'statusCode': 500,
            'body': json.dumps('Mensagem não enviada com sucesso')
        }
