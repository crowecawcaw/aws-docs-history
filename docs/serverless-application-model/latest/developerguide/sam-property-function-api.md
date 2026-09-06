

# Api
<a name="sam-property-function-api"></a>

The object describing an `Api` event source type. If an [AWS::Serverless::Api](sam-resource-api.md) resource is defined, the path and method values must correspond to an operation in the OpenAPI definition of the API.

If no [AWS::Serverless::Api](sam-resource-api.md) is defined, the function input and output are a representation of the HTTP request and HTTP response.

For example, using the JavaScript API, the status code and body of the response can be controlled by returning an object with the keys statusCode and body.

## Syntax
<a name="sam-property-function-api-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-api-syntax.yaml"></a>

```
  [Auth](#sam-function-api-auth): {{ApiFunctionAuth}}
  [Method](#sam-function-api-method): {{String}}
  [Path](#sam-function-api-path): {{String}}
  [RequestModel](#sam-function-api-requestmodel): {{RequestModel}}
  [RequestParameters](#sam-function-api-requestparameters): {{List of [ String | RequestParameter ]}}
  [RestApiId](#sam-function-api-restapiid): {{String}}
  [ResponseTransferMode](#sam-function-api-responsetransfermode): {{String}}
  TimeoutInMillis: {{Integer}}
```

## Properties
<a name="sam-property-function-api-properties"></a>

 `Auth`   <a name="sam-function-api-auth"></a>
Auth configuration for this specific Api\+Path\+Method.  
Useful for overriding the API's `DefaultAuthorizer` setting auth config on an individual path when no `DefaultAuthorizer` is specified or overriding the default `ApiKeyRequired` setting.  
*Type*: [ApiFunctionAuth](sam-property-function-apifunctionauth.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Method`   <a name="sam-function-api-method"></a>
HTTP method for which this function is invoked. Options include `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT`, and `ANY`. Refer to [Set up an HTTP method](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-request.html#setup-method-add-http-method) in the *API Gateway Developer Guide* for details.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Path`   <a name="sam-function-api-path"></a>
Uri path for which this function is invoked. Must start with `/`.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `RequestModel`   <a name="sam-function-api-requestmodel"></a>
Request model to use for this specific Api\+Path\+Method. This should reference the name of a model specified in the `Models` section of an [AWS::Serverless::Api](sam-resource-api.md) resource.  
*Type*: [RequestModel](sam-property-function-requestmodel.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `RequestParameters`   <a name="sam-function-api-requestparameters"></a>
Request parameters configuration for this specific Api\+Path\+Method. All parameter names must start with `method.request` and must be limited to `method.request.header`, `method.request.querystring`, or `method.request.path`.  
A list can contain both parameter name strings and [RequestParameter](sam-property-function-requestparameter.md) objects. For strings, the `Required` and `Caching` properties will default to `false`.  
*Type*: List of [ String \| [RequestParameter](sam-property-function-requestparameter.md) ]  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `RestApiId`   <a name="sam-function-api-restapiid"></a>
Identifier of a RestApi resource, which must contain an operation with the given path and method. Typically, this is set to reference an [AWS::Serverless::Api](sam-resource-api.md) resource defined in this template.  
If you don't define this property, AWS SAM creates a default [AWS::Serverless::Api](sam-resource-api.md) resource using a generated `OpenApi` document. That resource contains a union of all paths and methods defined by `Api` events in the same template that do not specify a `RestApiId`.  
This cannot reference an [AWS::Serverless::Api](sam-resource-api.md) resource defined in another template.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ResponseTransferMode`  <a name="sam-function-api-responsetransfermode"></a>
The response transfer mode for the Lambda function integration. Set to `RESPONSE_STREAM` to enable Lambda response streaming through API Gateway, allowing the function to stream responses back to clients. When set to `RESPONSE_STREAM`, API Gateway uses the Lambda InvokeWithResponseStreaming API.  
*Type*: String  
*Required*: No  
*Valid values*: `BUFFERED` \| `RESPONSE_STREAM`  
*CloudFormation compatibility*: This property is passed directly to the [`ResponseTransferMode`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-method-integration.html#cfn-apigateway-method-integration-responsetransfermode) property of an `AWS::ApiGateway::Method Integration`.

`TimeoutInMillis`  <a name="sam-function-api-timeoutinmillis"></a>
Custom timeout between 50 and 29,000 milliseconds.  
When you specify this property, AWS SAM modifies your OpenAPI definition. The OpenAPI definition must be specified inline using the `DefinitionBody` property. 
*Type*: Integer  
*Required*: No  
*Default*: 29,000 milliseconds or 29 seconds  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples
<a name="sam-property-function-api--examples"></a>

### Basic example
<a name="sam-property-function-api--examples--apievent"></a>

#### YAML
<a name="sam-property-function-api--examples--apievent--yaml"></a>

```
Events:
  ApiEvent:
    Type: Api
    Properties:
      Path: /path
      Method: get
      RequestParameters:
        - method.request.header.Authorization
        - method.request.querystring.keyword:
            Required: true
            Caching: false
```