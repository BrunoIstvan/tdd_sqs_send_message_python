from app.process import Process


def lambda_handler(event, context):
    return Process().execute(event)


if __name__=='__main__':

    lambda_handler({
        'resource': '/send_message', 'path': '/send_message', 'httpMethod': 'POST', 'headers': None, 'multiValueHeaders': None, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': '7lblxn', 'resourcePath': '/send_message', 'httpMethod': 'POST', 'extendedRequestId': 'GD8ixEkZoAMFRlg=', 'requestTime': '22/Sep/2021:11:05:53 +0000', 'path': '/send_message', 'accountId': '427831145075', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1632308753536, 'requestId': '1f12c87e-d734-441b-ba23-6e5c6a216f17', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:iam::427831145075:user/brunoistvan', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'aws-internal/3 aws-sdk-java/1.12.68 Linux/5.4.134-73.228.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.302-b08 java/1.8.0_302 vendor/Oracle_Corporation cfg/retry-mode/standard', 'accountId': '427831145075', 'caller': 'AIDAWHHFZGJZ3IEOX3TT4', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIAWHHFZGJZ6LCVFUOF', 'cognitoAuthenticationProvider': None, 'user': 'AIDAWHHFZGJZ3IEOX3TT4'}, 'domainName': 'testPrefix.testDomainName', 'apiId': '7e4gxg78rl'}, 'body': '{\n    "message": "Essa é uma mensagem que deve ser enviada na fila sqs-test"\n}', 'isBase64Encoded': False
    }, None)
