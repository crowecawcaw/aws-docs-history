# HttpApi

The object describing an event source with type HttpApi.

If an OpenApi definition for the specified path and method exists on the API, SAM will add the Lambda integration and security section (if applicable) for you.

If no OpenApi definition for the specified path and method exists on the API, SAM will create this definition for you.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  ApiId: `String`
  Auth: `HttpApiFunctionAuth`
  Method: `String`
  Path: `String`
  PayloadFormatVersion: `String`
  RouteSettings: `RouteSettings`
  TimeoutInMillis: `Integer`

```

## Properties

`ApiId`

Identifier of an [AWS::Serverless::HttpApi](sam-resource-httpapi.md "sam-resource-httpapi.md") resource defined in this template.

If not defined, a default [AWS::Serverless::HttpApi](sam-resource-httpapi.md "sam-resource-httpapi.md") resource is created called `ServerlessHttpApi` using a generated OpenApi document containing a union of all paths and methods defined by Api events defined in this template that do not specify an `ApiId`.

This cannot reference an [AWS::Serverless::HttpApi](sam-resource-httpapi.md "sam-resource-httpapi.md") resource defined in another template.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Auth`

Auth configuration for this specific Api+Path+Method.

Useful for overriding the API's `DefaultAuthorizer` or setting auth config on an individual path when no `DefaultAuthorizer` is specified.

_Type_: [HttpApiFunctionAuth](sam-property-function-httpapifunctionauth.md "sam-property-function-httpapifunctionauth.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Method`

HTTP method for which this function is invoked.

If no `Path` and `Method` are specified, SAM will create a default API path that routes any request that doesn't map to a different endpoint to this Lambda function. Only one of these default paths can exist per API.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Path`

Uri path for which this function is invoked. Must start with `/`.

If no `Path` and `Method` are specified, SAM will create a default API path that routes any request that doesn't map to a different endpoint to this Lambda function. Only one of these default paths can exist per API.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`PayloadFormatVersion`

Specifies the format of the payload sent to an integration.

NOTE: PayloadFormatVersion requires SAM to modify your OpenAPI definition, so it only works with inline OpenApi defined in the `DefinitionBody` property.

_Type_: String

_Required_: No

_Default_: 2.0

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`RouteSettings`

The per-route route settings for this HTTP API. For more information about route settings, see [AWS::ApiGatewayV2::Stage RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.md") in the _API Gateway Developer Guide_.

Note: If RouteSettings are specified in both the HttpApi resource and event source, AWS SAM merges them with the event source properties taking precedence.

_Type_: [RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `RouteSettings` property of an `AWS::ApiGatewayV2::Stage` resource.

`TimeoutInMillis`

Custom timeout between 50 and 29,000 milliseconds.

NOTE: TimeoutInMillis requires SAM to modify your OpenAPI definition, so it only works with inline OpenApi defined in the `DefinitionBody` property.

_Type_: Integer

_Required_: No

_Default_: 5000

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### Default HttpApi Event

HttpApi Event that uses the default path. All unmapped paths and methods on this API will route to this endpoint.

#### YAML

```
Events:
  HttpApiEvent:
    Type: HttpApi

```

### HttpApi

HttpApi Event that uses a specific path and method.

#### YAML

```
Events:
  HttpApiEvent:
    Type: HttpApi
    Properties:
      Path: /
      Method: GET

```

### HttpApi Authorization

HttpApi Event that uses an Authorizer.

#### YAML

```
Events:
  HttpApiEvent:
    Type: HttpApi
    Properties:
      Path: /authenticated
      Method: GET
      Auth:
        Authorizer: OpenIdAuth
        AuthorizationScopes:
          - scope1
          - scope2

```
