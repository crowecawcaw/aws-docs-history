# Resource

policy example for AWS SAM

You can control access to your APIs by attaching a resource policy within your AWS SAM
template. To do this, you use the [ApiAuth](sam-property-api-apiauth.md "sam-property-api-apiauth.md") data type.

The following is an example AWS SAM template for a private API. A private API must have a resource policy to deploy.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  MyPrivateApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      EndpointConfiguration: PRIVATE  # Creates a private API. Resource policies are required for all private APIs.
      Auth:
        ResourcePolicy:
          CustomStatements:
            - Effect: 'Allow'
              Action: 'execute-api:Invoke'
              Resource: ['execute-api:/*/*/*']
              Principal: '*'
            - Effect: 'Deny'
              Action: 'execute-api:Invoke'
              Resource: ['execute-api:/*/*/*']
              Principal: '*'
  MyFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      InlineCode: |
        def handler(event, context):
          return {'body': 'Hello World!', 'statusCode': 200}
      Handler: index.handler
      Runtime: python3.10
      Events:
        AddItem:
          Type: Api
          Properties:
            RestApiId:
              Ref: MyPrivateApi
            Path: /
            Method: get
```

For more information about resource policies, see [Controlling access
to an API with API Gateway resource policies](../../../apigateway/latest/developerguide/apigateway-resource-policies.md "../../../apigateway/latest/developerguide/apigateway-resource-policies.md") in the
_API Gateway Developer Guide_. For more information about private APIs, see
[Creating a private API
in Amazon API Gateway](../../../apigateway/latest/developerguide/apigateway-private-apis.md "../../../apigateway/latest/developerguide/apigateway-private-apis.md") in the
_API Gateway Developer Guide_.
