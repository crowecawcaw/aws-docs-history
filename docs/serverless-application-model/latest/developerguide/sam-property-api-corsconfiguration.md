# CorsConfiguration

Manage cross-origin resource sharing (CORS) for your API Gateway APIs. Specify the domain to allow as a string or specify a dictionary with additional Cors configuration.

###### Note

CORS requires AWS SAM to modify your OpenAPI definition. Create an inline OpenAPI
definition in the `DefinitionBody` to turn on CORS. If the `CorsConfiguration` is
set in the OpenAPI definition and also at the property level, AWS SAM merges them. The
property level takes precedence over the OpenAPI definition.

For more information about CORS, see [Enable CORS for
an API Gateway REST API Resource](../../../apigateway/latest/developerguide/how-to-cors.md "../../../apigateway/latest/developerguide/how-to-cors.md") in the _API Gateway Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AllowCredentials: `Boolean`
  AllowHeaders: `String`
  AllowMethods: `String`
  AllowOrigin: `String`
  MaxAge: `String`

```

## Properties

`AllowCredentials`

Boolean indicating whether request is allowed to contain credentials.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowHeaders`

String of headers to allow.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowMethods`

String containing the HTTP methods to allow.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowOrigin`

String of origin to allow. This can be a comma-separated list in string format.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`MaxAge`

String containing the number of seconds to cache CORS Preflight request.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### CorsConfiguration

CORS Configuration example. This is just a portion of an AWS SAM template file
showing an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md")
definition with CORS configured and a [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md"). If you use a Lambda proxy integration or
a HTTP proxy integration, your backend must return the
`Access-Control-Allow-Origin`,
`Access-Control-Allow-Methods`, and
`Access-Control-Allow-Headers` headers.

#### YAML

```
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      Cors:
        AllowMethods: "'POST, GET'"
        AllowHeaders: "'X-Forwarded-For'"
        AllowOrigin: "'https://example.com'"
        MaxAge: "'600'"
        AllowCredentials: true
  ApiFunction: # Adds a GET method at the root resource via an Api event
    Type: AWS::Serverless::Function
    Properties:
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /
            Method: get
            RestApiId:
              Ref: ApiGatewayApi
      Runtime: python3.10
      Handler: index.handler
      InlineCode: |
        import json
        def handler(event, context):
          return {
          'statusCode': 200,
          'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://example.com',
            'Access-Control-Allow-Methods': 'POST, GET'
            },
          'body': json.dumps('Hello from Lambda!')
          }

```
