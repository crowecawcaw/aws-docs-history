# API key example for AWS SAM

You can control access to your APIs by requiring API keys within your AWS SAM template.
To do this, you use the [ApiAuth](sam-property-api-apiauth.md "sam-property-api-apiauth.md") data type.

The following is an example AWS SAM template section for API keys:

```
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      Auth:
        ApiKeyRequired: true # sets for all methods

  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Handler: index.handler
      Runtime: nodejs12.x
      Events:
        ApiKey:
          Type: Api
          Properties:
            RestApiId: !Ref MyApi
            Path: /
            Method: get
            Auth:
              ApiKeyRequired: true
```

For more information about API keys, see [Creating and using
usage plans with API keys](../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md "../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md") in the _API Gateway Developer Guide_.
