# AWS::Serverless::HttpApi

Creates an Amazon API Gateway HTTP API, which enables you to create RESTful APIs with lower latency
and lower costs than REST APIs. For more information, see [Working with HTTP
APIs](../../../apigateway/latest/developerguide/http-api.md "../../../apigateway/latest/developerguide/http-api.md") in the _API Gateway Developer Guide_.

We recommend that you use AWS CloudFormation hooks or IAM policies to verify that API Gateway resources have
authorizers attached to them to control access to them.

For more information about using AWS CloudFormation hooks, see [Registering hooks](../../../cloudformation-cli/latest/userguide/registering-hook-python.md "../../../cloudformation-cli/latest/userguide/registering-hook-python.md") in the _AWS CloudFormation CLI user guide_ and
the [apigw-enforce-authorizer](https://github.com/aws-cloudformation/aws-cloudformation-samples/tree/main/hooks/python-hooks/apigw-enforce-authorizer/ "https://github.com/aws-cloudformation/aws-cloudformation-samples/tree/main/hooks/python-hooks/apigw-enforce-authorizer/") GitHub repository.

For more information about using IAM policies, see [Require that API routes have authorization](../../../apigateway/latest/developerguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-require-authorization "../../../apigateway/latest/developerguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-require-authorization") in the _API Gateway Developer Guide_.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources.
For more information, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::HttpApi
Properties:
  AccessLogSettings: `AccessLogSettings`
  Auth: `HttpApiAuth`
  CorsConfiguration: `String | HttpApiCorsConfiguration`
  DefaultRouteSettings: `RouteSettings`
  DefinitionBody: `JSON`
  DefinitionUri: `String | HttpApiDefinition`
  Description: `String`
  DisableExecuteApiEndpoint: `Boolean`
  Domain: `HttpApiDomainConfiguration`
  FailOnWarnings: `Boolean`
  Name: `String`
  PropagateTags: `Boolean`
  RouteSettings: `RouteSettings`
  StageName: `String`
  StageVariables: `Json`
  Tags: `Map`

```

## Properties

`AccessLogSettings`

The settings for access logging in a stage.

_Type_: [AccessLogSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-accesslogsettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-accesslogsettings")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`AccessLogSettings` property of an
`AWS::ApiGatewayV2::Stage` resource.

`Auth`

Configures authorization for controlling access to your API Gateway HTTP API.

For more information, see [Controlling access to HTTP APIs with JWT authorizers](../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md "../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md") in the _API Gateway Developer Guide_.

_Type_: [HttpApiAuth](sam-property-httpapi-httpapiauth.md "sam-property-httpapi-httpapiauth.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`CorsConfiguration`

Manages cross-origin resource sharing (CORS) for all your API Gateway HTTP APIs. Specify
the domain to allow as a string, or specify an `HttpApiCorsConfiguration`
object. Note that CORS requires AWS SAM to modify your OpenAPI definition, so CORS works
only if the `DefinitionBody` property is specified.

For more information, see [Configuring
CORS for an HTTP API](../../../apigateway/latest/developerguide/http-api-cors.md "../../../apigateway/latest/developerguide/http-api-cors.md") in the _API Gateway Developer Guide_.

###### Note

If `CorsConfiguration` is set both in an OpenAPI definition and at the
property level, then AWS SAM merges both configuration sources with the properties
taking precedence. If this property is set to `true`, then all origins are
allowed.

_Type_: String | [HttpApiCorsConfiguration](sam-property-httpapi-httpapicorsconfiguration.md "sam-property-httpapi-httpapicorsconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`DefaultRouteSettings`

The default route settings for this HTTP API. These settings apply to all routes
unless overridden by the `RouteSettings` property for certain routes.

_Type_: [RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RouteSettings` property of an `AWS::ApiGatewayV2::Stage`
resource.

`DefinitionBody`

The OpenAPI definition that describes your HTTP API. If you don't specify a
`DefinitionUri` or a `DefinitionBody`, AWS SAM generates a
`DefinitionBody` for you based on your template configuration.

_Type_: JSON

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Body` property of an `AWS::ApiGatewayV2::Api` resource. If
certain properties are provided, AWS SAM may insert content into or modify the
`DefinitionBody` before it is passed to AWS CloudFormation. Properties include
`Auth` and an `EventSource` of type HttpApi for a corresponding
`AWS::Serverless::Function` resource.

`DefinitionUri`

The Amazon Simple Storage Service (Amazon S3) URI, local file path, or location object of the the OpenAPI
definition that defines the HTTP API. The Amazon S3 object that this property references must
be a valid OpenAPI definition file. If you don't specify a `DefinitionUri` or
a `DefinitionBody` are specified, AWS SAM generates a
`DefinitionBody` for you based on your template configuration.

If you provide a local file path, the template must go through the workflow that
includes the `sam deploy` or `sam package` command for the
definition to be transformed properly.

Intrinsic functions are not supported in external OpenApi definition files that you
reference with `DefinitionUri`. To import an OpenApi definition into the
template, use the `DefinitionBody` property with the [Include transform](../../../AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.md "../../../AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.md").

_Type_: String | [HttpApiDefinition](sam-property-httpapi-httpapidefinition.md "sam-property-httpapi-httpapidefinition.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`BodyS3Location` property of an `AWS::ApiGatewayV2::Api`
resource. The nested Amazon S3 properties are named differently.

`Description`

The description of the HTTP API resource.

When you specify `Description`, AWS SAM will modify the HTTP API resource's
OpenApi definition by setting the `description` field. The following
scenarios will result in an error:

- The `DefinitionBody` property is specified with the
  `description` field set in the Open API definition – This
  results in a conflict of the `description` field that AWS SAM won't
  resolve.
- The `DefinitionUri` property is specified – AWS SAM won't modify
  an Open API definition that is retrieved from Amazon S3.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`DisableExecuteApiEndpoint`

Specifies whether clients can invoke your HTTP API by using the default
`execute-api` endpoint
`https://{api_id}.execute-api.{region}.amazonaws.com`. By default, clients
can invoke your API with the default endpoint. To require that clients only use a custom
domain name to invoke your API, disable the default endpoint.

To use this property, you must specify the `DefinitionBody` property instead of the `DefinitionUri` property
or define `x-amazon-apigateway-endpoint-configuration` with `disableExecuteApiEndpoint` in your OpenAPI definition.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DisableExecuteApiEndpoint` property of an
`AWS::ApiGatewayV2::Api` resource. It is passed directly to the
`disableExecuteApiEndpoint` property of an `x-amazon-apigateway-endpoint-configuration` extension, which gets
added to the `Body` property of an `AWS::ApiGatewayV2::Api`
resource.

`Domain`

Configures a custom domain for this API Gateway HTTP API.

_Type_: [HttpApiDomainConfiguration](sam-property-httpapi-httpapidomainconfiguration.md "sam-property-httpapi-httpapidomainconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`FailOnWarnings`

Specifies whether to roll back the HTTP API creation (`true`) or not
(`false`) when a warning is encountered. The default value is
`false`.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FailOnWarnings` property of an `AWS::ApiGatewayV2::Api`
resource.

`Name`

The name of the HTTP API resource.

When you specify `Name`, AWS SAM will modify the HTTP API resource's
OpenAPI definition by setting the `title` field. The following scenarios will
result in an error:

- The `DefinitionBody` property is specified with the
  `title` field set in the Open API definition – This results in a
  conflict of the `title` field that AWS SAM won't resolve.
- The `DefinitionUri` property is specified – AWS SAM won't modify
  an Open API definition that is retrieved from Amazon S3.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`PropagateTags`

Indicate whether or not to pass tags from the `Tags` property to your
[AWS::Serverless::HttpApi](sam-specification-generated-resources-httpapi.md "sam-specification-generated-resources-httpapi.md") generated
resources. Specify `True` to propagate tags in your generated
resources.

_Type_: Boolean

_Required_: No

_Default_: `False`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`RouteSettings`

The route settings, per route, for this HTTP API. For more information, see [Working with routes for HTTP APIs](../../../apigateway/latest/developerguide/http-api-develop-routes.md "../../../apigateway/latest/developerguide/http-api-develop-routes.md") in the _API Gateway Developer Guide_.

_Type_: [RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RouteSettings` property of an `AWS::ApiGatewayV2::Stage`
resource.

`StageName`

The name of the API stage. If no name is specified, AWS SAM uses the
`$default` stage from API Gateway.

_Type_: String

_Required_: No

_Default_: $default

_AWS CloudFormation compatibility_: This property is passed directly to the
`StageName` property of an `AWS::ApiGatewayV2::Stage`
resource.

`StageVariables`

A map that defines the stage variables. Variable names can have alphanumeric and
underscore characters. The values must match [A-Za-z0-9-.\_~:/?#&=,]+.

_Type_: [Json](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-stagevariables "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-stagevariables")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StageVariables` property of an `AWS::ApiGatewayV2::Stage`
resource.

`Tags`

A map (string to string) that specifies the tags to add to this API Gateway stage. Keys
can be 1 to 128 Unicode characters in length and cannot include the prefix
`aws:`. You can use any of the following characters: the set of Unicode
letters, digits, whitespace, `_`, `.`, `/`,
`=`, `+`, and `-`. Values can be 1 to 256 Unicode
characters in length.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

_Additional notes_: The `Tags` property requires AWS SAM
to modify your OpenAPI definition, so tags are added only if the
`DefinitionBody` property is specified—no tags are added if the
`DefinitionUri` property is specified. AWS SAM automatically adds an
`httpapi:createdBy:SAM` tag. Tags are also added to the
`AWS::ApiGatewayV2::Stage` resource and the
`AWS::ApiGatewayV2::DomainName` resource (if `DomainName` is
specified).

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref`
function, `Ref` returns the API ID of the underlying
`AWS::ApiGatewayV2::Api` resource, for example, `a1bcdef2gh`.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

## Examples

### Simple HttpApi

The following example shows the minimum needed to set up an HTTP API endpoint backed by
an Lambda function. This example uses the default HTTP API that AWS SAM creates.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS SAM template with a simple API definition
Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      Events:
        ApiEvent:
          Type: HttpApi
      Handler: index.handler
      InlineCode: |
        def handler(event, context):
            return {'body': 'Hello World!', 'statusCode': 200}
      Runtime: python3.7
Transform: AWS::Serverless-2016-10-31

```

### HttpApi with

Auth

The following example shows how to set up authorization on HTTP API endpoints.

#### YAML

```
Properties:
  FailOnWarnings: true
  Auth:
    DefaultAuthorizer: OAuth2
    Authorizers:
      OAuth2:
        AuthorizationScopes:
          - scope4
        JwtConfiguration:
          issuer: "https://www.example.com/v1/connect/oauth2"
          audience:
            - MyApi
        IdentitySource: "$request.querystring.param"

```

### HttpApi

with OpenAPI definition

The following example shows how to add an OpenAPI definition to the template.

Note that AWS SAM fills in any missing Lambda integrations for HttpApi events that
reference this HTTP API. AWS SAM also also adds any missing paths that HttpApi events
reference.

#### YAML

```
Properties:
  FailOnWarnings: true
  DefinitionBody:
    info:
      version: '1.0'
      title:
        Ref: AWS::StackName
    paths:
      "/":
        get:
          security:
          - OpenIdAuth:
            - scope1
            - scope2
          responses: {}
    openapi: 3.0.1
    securitySchemes:
      OpenIdAuth:
        type: openIdConnect
        x-amazon-apigateway-authorizer:
          identitySource: "$request.querystring.param"
          type: jwt
          jwtConfiguration:
            audience:
            - MyApi
            issuer: https://www.example.com/v1/connect/oidc
          openIdConnectUrl: https://www.example.com/v1/connect/oidc/.well-known/openid-configuration

```

### HttpApi with configuration settings

The following example shows how to add HTTP API and stage configurations to the
template.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Parameters:
  StageName:
    Type: String
    Default: Prod

Resources:
  HttpApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      InlineCode: |
          def handler(event, context):
              import json
              return {
                  "statusCode": 200,
                  "body": json.dumps(event),
              }
      Handler: index.handler
      Runtime: python3.7
      Events:
        ExplicitApi: # warning: creates a public endpoint
          Type: HttpApi
          Properties:
            ApiId: !Ref HttpApi
            Method: GET
            Path: /path
            TimeoutInMillis: 15000
            PayloadFormatVersion: "2.0"
            RouteSettings:
              ThrottlingBurstLimit: 600

  HttpApi:
    Type: AWS::Serverless::HttpApi
    Properties:
      StageName: !Ref StageName
      Tags:
        Tag: Value
      AccessLogSettings:
        DestinationArn: !GetAtt AccessLogs.Arn
        Format: $context.requestId
      DefaultRouteSettings:
        ThrottlingBurstLimit: 200
      RouteSettings:
        "GET /path":
          ThrottlingBurstLimit: 500 # overridden in HttpApi Event
      StageVariables:
        StageVar: Value
      FailOnWarnings: true

  AccessLogs:
    Type: AWS::Logs::LogGroup

Outputs:
  HttpApiUrl:
    Description: URL of your API endpoint
    Value:
      Fn::Sub: 'https://${HttpApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/${StageName}/'
  HttpApiId:
    Description: Api id of HttpApi
    Value:
      Ref: HttpApi

```
