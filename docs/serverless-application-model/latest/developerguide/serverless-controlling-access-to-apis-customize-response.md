# Customized

response example for AWS SAM

You can customize some API Gateway error responses by defining response headers within your
AWS SAM template. To do this, you use the [Gateway Response Object](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#gateway-response-object "https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#gateway-response-object") data type.

The following is an example AWS SAM template that creates a customized response for the
`DEFAULT_5XX` error.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      GatewayResponses:
        DEFAULT_5XX:
          ResponseParameters:
            Headers:
              Access-Control-Expose-Headers: "'WWW-Authenticate'"
              Access-Control-Allow-Origin: "'*'"
              ErrorHeader: "'MyCustomErrorHeader'"
          ResponseTemplates:
            application/json: "{\"message\": \"Error on the $context.resourcePath resource\" }"

  GetFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: python3.10
      Handler: index.handler
      InlineCode: |
        def handler(event, context):
          raise Exception('Check out the new response!')
      Events:
        GetResource:
          Type: Api
          Properties:
            Path: /error
            Method: get
            RestApiId: !Ref MyApi
```

For more information about API Gateway responses, see [Gateway responses in API Gateway](../../../apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.md "../../../apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.md") in the
_API Gateway Developer Guide_.
