# Api

The object describing an `Api` event source type. If an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource is defined, the path
and method values must correspond to an operation in the OpenAPI definition of the API.

If no [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") is defined, the
function input and output are a representation of the HTTP request and HTTP response.

For example, using the JavaScript API, the status code and body of the response can be
controlled by returning an object with the keys statusCode and body.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  Auth: `ApiFunctionAuth`
  Method: `String`
  Path: `String`
  RequestModel: `RequestModel`
  RequestParameters: `List of [ String | RequestParameter ]`
  RestApiId: `String`
  TimeoutInMillis: `Integer`

```

## Properties

`Auth`

Auth configuration for this specific Api+Path+Method.

Useful for overriding the API's `DefaultAuthorizer` setting auth config
on an individual path when no `DefaultAuthorizer` is specified or overriding
the default `ApiKeyRequired` setting.

_Type_: [ApiFunctionAuth](sam-property-function-apifunctionauth.md "sam-property-function-apifunctionauth.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Method`

HTTP method for which this function is invoked. Options include `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT`, and `ANY`.
Refer to [Set up an HTTP method](../../../apigateway/latest/developerguide/api-gateway-method-settings-method-request.md#setup-method-add-http-method "../../../apigateway/latest/developerguide/api-gateway-method-settings-method-request.md#setup-method-add-http-method")
in the _API Gateway Developer Guide_ for details.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Path`

Uri path for which this function is invoked. Must start with `/`.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`RequestModel`

Request model to use for this specific Api+Path+Method. This should reference the
name of a model specified in the `Models` section of an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource.

_Type_: [RequestModel](sam-property-function-requestmodel.md "sam-property-function-requestmodel.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`RequestParameters`

Request parameters configuration for this specific Api+Path+Method. All parameter names must start with
`method.request` and must be limited to `method.request.header`,
`method.request.querystring`, or `method.request.path`.

A list can contain both parameter name strings and
[RequestParameter](sam-property-function-requestparameter.md "sam-property-function-requestparameter.md") objects. For strings, the
`Required` and `Caching` properties will default to `false`.

_Type_: List of [ String | [RequestParameter](sam-property-function-requestparameter.md "sam-property-function-requestparameter.md") ]

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`RestApiId`

Identifier of a RestApi resource, which must contain an operation with the given
path and method. Typically, this is set to reference an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource defined in this template.

If you don't define this property, AWS SAM creates a default [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource using a
generated `OpenApi` document. That resource contains a union of all paths and
methods defined by `Api` events in the same template that do not specify a
`RestApiId`.

This cannot reference an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource defined in another template.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`TimeoutInMillis`

Custom timeout between 50 and 29,000 milliseconds.

###### Note

When you specify this property, AWS SAM modifies your OpenAPI definition. The OpenAPI definition must be
specified inline using the `DefinitionBody` property.

_Type_: Integer

_Required_: No

_Default_: 29,000 milliseconds or 29 seconds

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation
equivalent.

## Examples

### Basic example

#### YAML

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
