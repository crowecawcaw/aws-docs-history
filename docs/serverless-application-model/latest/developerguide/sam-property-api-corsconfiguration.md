

# CorsConfiguration
<a name="sam-property-api-corsconfiguration"></a>

Manage cross-origin resource sharing (CORS) for your API Gateway APIs. Specify the domain to allow as a string or specify a dictionary with additional Cors configuration.

**Note**  
CORS requires AWS SAM to modify your OpenAPI definition. Create an inline OpenAPI definition in the `DefinitionBody` to turn on CORS. If the `CorsConfiguration` is set in the OpenAPI definition and also at the property level, AWS SAM merges them. The property level takes precedence over the OpenAPI definition.

For more information about CORS, see [Enable CORS for an API Gateway REST API Resource](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html) in the *API Gateway Developer Guide*.

## Syntax
<a name="sam-property-api-corsconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-api-corsconfiguration-syntax.yaml"></a>

```
  [AllowCredentials](#sam-api-corsconfiguration-allowcredentials): {{Boolean}}
  [AllowHeaders](#sam-api-corsconfiguration-allowheaders): {{String}}
  [AllowMethods](#sam-api-corsconfiguration-allowmethods): {{String}}
  [AllowOrigin](#sam-api-corsconfiguration-alloworigin): {{String}}
  [MaxAge](#sam-api-corsconfiguration-maxage): {{String}}
```

## Properties
<a name="sam-property-api-corsconfiguration-properties"></a>

 `AllowCredentials`   <a name="sam-api-corsconfiguration-allowcredentials"></a>
Boolean indicating whether request is allowed to contain credentials.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AllowHeaders`   <a name="sam-api-corsconfiguration-allowheaders"></a>
String of headers to allow.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AllowMethods`   <a name="sam-api-corsconfiguration-allowmethods"></a>
String containing the HTTP methods to allow.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AllowOrigin`   <a name="sam-api-corsconfiguration-alloworigin"></a>
String of origin to allow. This can be a comma-separated list in string format.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `MaxAge`   <a name="sam-api-corsconfiguration-maxage"></a>
String containing the number of seconds to cache CORS Preflight request.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples
<a name="sam-property-api-corsconfiguration--examples"></a>

### CorsConfiguration
<a name="sam-property-api-corsconfiguration--examples--corsconfiguration"></a>

CORS Configuration example. This is just a portion of an AWS SAM template file showing an [AWS::Serverless::Api](sam-resource-api.md) definition with CORS configured and a [AWS::Serverless::Function](sam-resource-function.md). If you use a Lambda proxy integration or a HTTP proxy integration, your backend must return the `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers` headers.

#### YAML
<a name="sam-property-api-corsconfiguration--examples--corsconfiguration--yaml"></a>

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