import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from app.exceptions.custom_exceptions import InvalidSQSParametersException
from app.process import Process

event = {
    'body': {
        'message': 'Essa é uma mensagem que deverá ser enviada na fila sqs-test'
    }
}


class TestProcess(TestCase):

    def setUp(self):
        self.process = Process()

    def test_execute(self):
        message_id = '12345-67890-abcdef'
        message = event['body']['message']
        expected_response = self.process.build_response(message_id)
        self.process.validate_param_values = MagicMock(return_value=message)
        self.process.sqs_service = MagicMock()
        self.process.sqs_service.get_client = MagicMock()
        self.process.sqs_service.execute_send_message = MagicMock(return_value=message_id)
        self.process.build_response = MagicMock(return_value=expected_response)

        result = self.process.execute(event)

        self.process.validate_param_values.assert_called_with(event)
        self.process.sqs_service.get_client.assert_called_once()
        self.process.sqs_service.execute_send_message.assert_called_with(self.process.sqs_service.get_client(),
                                                                         message)
        self.process.build_response.assert_called_with(message_id)
        assert expected_response == result, 'O retorno da execução é igual ao esperado'

    def test_validate_params_success(self):
        message = self.process.validate_param_values(event)

        assert message is not None, 'Parâmetro message está vazio'
        assert message == event['body']['message'], 'Valor do parâmetro mensagem está diferente do esperado'

    def test_validate_params_fail(self):
        with self.assertRaises(InvalidSQSParametersException):
            self.process.validate_param_values({})


if __name__ == '__main__':
    unittest.main()
