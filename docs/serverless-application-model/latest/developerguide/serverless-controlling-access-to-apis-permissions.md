# IAM permission

example for AWS SAM

You can control access to your APIs by defining IAM permissions within your AWS SAM
template. To do this, you use the [ApiAuth](sam-property-api-apiauth.md "sam-property-api-apiauth.md") data type.

The following is an example AWS SAM template that uses for IAM permissions:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      Description: 'API with IAM authorization'
      Auth:
        DefaultAuthorizer: AWS_IAM #sets AWS_IAM auth for all methods in this API
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: python3.10
      Events:
        GetRoot:
          Type: Api
          Properties:
            RestApiId: !Ref MyApi
            Path: /
            Method: get
      InlineCode: |
        def handler(event, context):
          return {'body': 'Hello World!', 'statusCode': 200}
```

For more information about IAM permissions, see [Control access for invoking an API](../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md "../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md")
in the _API Gateway Developer Guide_.
