# AWS::Serverless::Api

Creates a collection of Amazon API Gateway resources and methods that can be invoked through
HTTPS endpoints.

An AWS::Serverless::Api resource need not be
explicitly added to a AWS Serverless Application Definition template. A resource of this type
is implicitly created from the union of Api events defined on [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md") resources defined in
the template that do not refer to an AWS::Serverless::Api resource.

An AWS::Serverless::Api resource should be
used to define and document the API using OpenApi, which provides more ability to configure the
underlying Amazon API Gateway resources.

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
Type: AWS::Serverless::Api
Properties:
  AccessLogSetting: `AccessLogSetting`
  AlwaysDeploy: `Boolean`
  ApiKeySourceType: `String`
  Auth: `ApiAuth`
  BinaryMediaTypes: `List`
  CacheClusterEnabled: `Boolean`
  CacheClusterSize: `String`
  CanarySetting: `CanarySetting`
  Cors: `String | CorsConfiguration`
  DefinitionBody: `JSON`
  DefinitionUri: `String | ApiDefinition`
  Description: `String`
  DisableExecuteApiEndpoint: `Boolean`
  Domain: `DomainConfiguration`
  EndpointConfiguration: `EndpointConfiguration`
  FailOnWarnings: `Boolean`
  GatewayResponses: `Map`
  MergeDefinitions: `Boolean`
  MethodSettings: `MethodSettings`
  MinimumCompressionSize: `Integer`
  Mode: `String`
  Models: `Map`
  Name: `String`
  OpenApiVersion: `String`
  PropagateTags: `Boolean`
  Policy: `JSON`
  StageName: `String`
  Tags: `Map`
  TracingEnabled: `Boolean`
  Variables: `Map`

```

## Properties

`AccessLogSetting`

Configures Access Log Setting for a stage.

_Type_: [AccessLogSetting](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md#cfn-apigateway-stage-accesslogsetting "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md#cfn-apigateway-stage-accesslogsetting")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`AccessLogSetting` property of an `AWS::ApiGateway::Stage`
resource.

`AlwaysDeploy`

Always deploys the API, even when no changes to the API have been detected.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`ApiKeySourceType`

The source of the API key for metering requests according to a usage plan. Valid
values are `HEADER` and `AUTHORIZER`.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ApiKeySourceType` property of an
`AWS::ApiGateway::RestApi` resource.

`Auth`

Configure authorization to control access to your API Gateway API.

For more information about configuring access using AWS SAM see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md"). For an example showing how to override a global authorizer, see [Override a global authorizer for your Amazon API Gateway REST API](sam-property-function-apifunctionauth.md#sam-property-function-apifunctionauth--examples--override "sam-property-function-apifunctionauth.md#sam-property-function-apifunctionauth--examples--override").

_Type_: [ApiAuth](sam-property-api-apiauth.md "sam-property-api-apiauth.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`BinaryMediaTypes`

List of MIME types that your API could return. Use this to enable binary support for
APIs.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`BinaryMediaTypes` property of an
`AWS::ApiGateway::RestApi` resource. The list of BinaryMediaTypes is added
to both the AWS CloudFormation resource and the OpenAPI document.

`CacheClusterEnabled`

Indicates whether caching is enabled for the stage. To cache responses, you must
also set `CachingEnabled` to `true` under
`MethodSettings`.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`CacheClusterEnabled` property of an
`AWS::ApiGateway::Stage` resource.

`CacheClusterSize`

The stage's cache cluster size.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`CacheClusterSize` property of an `AWS::ApiGateway::Stage`
resource.

`CanarySetting`

Configure a canary setting to a stage of a regular deployment.

_Type_: [CanarySetting](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md#cfn-apigateway-stage-canarysetting "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md#cfn-apigateway-stage-canarysetting")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`CanarySetting` property of an `AWS::ApiGateway::Stage`
resource.

`Cors`

Manage Cross-origin resource sharing (CORS) for all your API Gateway APIs. Specify
the domain to allow as a string or specify a dictionary with additional Cors
configuration.

###### Note

CORS requires AWS SAM to modify your OpenAPI definition. Create an inline OpenAPI
definition in the `DefinitionBody` to turn on CORS.

For more information about CORS, see [Enable CORS
for an API Gateway REST API Resource](../../../apigateway/latest/developerguide/how-to-cors.md "../../../apigateway/latest/developerguide/how-to-cors.md") in the _API Gateway Developer Guide_.

_Type_: String | [CorsConfiguration](sam-property-api-corsconfiguration.md "sam-property-api-corsconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`DefinitionBody`

OpenAPI specification that describes your API. If neither `DefinitionUri`
nor `DefinitionBody` are specified, SAM will generate a
`DefinitionBody` for you based on your template configuration.

To reference a local OpenAPI file that defines your API, use the
`AWS::Include` transform. To learn more, see [How AWS SAM uploads local files](deploy-upload-local-files.md "deploy-upload-local-files.md").

_Type_: JSON

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Body` property of an `AWS::ApiGateway::RestApi` resource.
If certain properties are provided, content may be inserted or modified into the
DefinitionBody before being passed to CloudFormation. Properties include
`Auth`, `BinaryMediaTypes`, `Cors`,
`GatewayResponses`, `Models`, and an `EventSource` of
type Api for a corresponding `AWS::Serverless::Function`.

`DefinitionUri`

Amazon S3 Uri, local file path, or location object of the the OpenAPI document
defining the API. The Amazon S3 object this property references must be a valid OpenAPI file.
If neither `DefinitionUri` nor `DefinitionBody` are specified, SAM
will generate a `DefinitionBody` for you based on your template
configuration.

If a local file path is provided, the template must go through the workflow that
includes the `sam deploy` or `sam package` command, in order for
the definition to be transformed properly.

Intrinsic functions are not supported in external OpenApi files referenced by
`DefinitionUri`. Use instead the `DefinitionBody` property with
the [Include Transform](../../../AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.md "../../../AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.md") to import an OpenApi definition into the template.

_Type_: String | [ApiDefinition](sam-property-api-apidefinition.md "sam-property-api-apidefinition.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`BodyS3Location` property of an `AWS::ApiGateway::RestApi`
resource. The nested Amazon S3 properties are named differently.

`Description`

A description of the Api resource.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::ApiGateway::RestApi`
resource.

`DisableExecuteApiEndpoint`

Specifies whether clients can invoke your API by using the default
`execute-api` endpoint. By default, clients can invoke your API with the
default `https://{api_id}.execute-api.{region}.amazonaws.com`. To require
that clients use a custom domain name to invoke your API, specify
`True`.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DisableExecuteApiEndpoint` property of an
`AWS::ApiGateway::RestApi` resource. It is passed directly to the
`disableExecuteApiEndpoint` property of an `x-amazon-apigateway-endpoint-configuration` extension, which gets
added to the `Body` property of an `AWS::ApiGateway::RestApi`
resource.

`Domain`

Configures a custom domain for this API Gateway API.

_Type_: [DomainConfiguration](sam-property-api-domainconfiguration.md "sam-property-api-domainconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`EndpointConfiguration`

The endpoint type of a REST API.

_Type_: [EndpointConfiguration](sam-property-api-endpointconfiguration.md "sam-property-api-endpointconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`EndpointConfiguration` property of an
`AWS::ApiGateway::RestApi` resource. The nested configuration properties
are named differently.

`FailOnWarnings`

Specifies whether to roll back the API creation (`true`) or not
(`false`) when a warning is encountered. The default value is
`false`.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FailOnWarnings` property of an `AWS::ApiGateway::RestApi`
resource.

`GatewayResponses`

Configures Gateway Responses for an API. Gateway Responses are responses returned by
API Gateway, either directly or through the use of Lambda Authorizers. For more
information, see the documentation for the [Api Gateway OpenApi extension for Gateway Responses](../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.md "../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.md").

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`MergeDefinitions`

AWS SAM generates an OpenAPI specification from your API event source.
Specify `true` to have AWS SAM merge this into the inline
OpenAPI specification defined in your `AWS::Serverless::Api`
resource. Specify `false` to not merge.

`MergeDefinitions` requires the `DefinitionBody` property for
`AWS::Serverless::Api` to be defined. `MergeDefinitions` is not
compatible with the `DefinitionUri` property for
`AWS::Serverless::Api`.

_Default value_: `false`

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`MethodSettings`

Configures all settings for API stage including Logging, Metrics, CacheTTL,
Throttling.

_Type_: List of [MethodSetting](../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MethodSettings` property of an `AWS::ApiGateway::Stage`
resource.

`MinimumCompressionSize`

Allow compression of response bodies based on client's Accept-Encoding header.
Compression is triggered when response body size is greater than or equal to your
configured threshold. The maximum body size threshold is 10 MB (10,485,760 Bytes). - The
following compression types are supported: gzip, deflate, and identity.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MinimumCompressionSize` property of an
`AWS::ApiGateway::RestApi` resource.

`Mode`

This property applies only when you use OpenAPI to define your REST API. The
`Mode` determines how API Gateway handles resource updates. For more information,
see [Mode](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md#cfn-apigateway-restapi-mode "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md#cfn-apigateway-restapi-mode") property of the [AWS::ApiGateway::RestApi](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md") resource type.

_Valid values_: `overwrite` or
`merge`

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Mode` property of an `AWS::ApiGateway::RestApi`
resource.

`Models`

The schemas to be used by your API methods. These schemas can be described using
JSON or YAML. See the Examples section at the bottom of this page for example
models.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Name`

A name for the API Gateway RestApi resource

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::ApiGateway::RestApi`
resource.

`OpenApiVersion`

Version of OpenApi to use. This can either be `2.0` for the Swagger
specification, or one of the OpenApi 3.0 versions, like `3.0.1`. For more
information about OpenAPI, see the [OpenAPI Specification](https://swagger.io/specification/ "https://swagger.io/specification/").

###### Note

AWS SAM creates a stage called `Stage` by default. Setting this property
to any valid value will prevent the creation of the stage `Stage`.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`PropagateTags`

Indicate whether or not to pass tags from the `Tags` property to your
[AWS::Serverless::Api](sam-specification-generated-resources-api.md "sam-specification-generated-resources-api.md") generated resources.
Specify `True` to propagate tags in your generated resources.

_Type_: Boolean

_Required_: No

_Default_: `False`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Policy`

A policy document that contains the permissions for the API. To set the ARN for the
policy, use the `!Join` intrinsic function with `""`
as delimiter and values of `"execute-api:/"` and
`"*"`.

_Type_: JSON

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to
the [Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md#cfn-apigateway-restapi-policy "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.md#cfn-apigateway-restapi-policy") property of an `AWS::ApiGateway::RestApi` resource.

`StageName`

The name of the stage, which API Gateway uses as the first path segment in the
invoke Uniform Resource Identifier (URI).

To reference the stage resource, use
``<api-logical-id>`.Stage`. For more
information about referencing resources generated when an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource is specified,
see [AWS CloudFormation resources generated when
AWS::Serverless::Api is specified](sam-specification-generated-resources-api.md "sam-specification-generated-resources-api.md"). For general information
about generated AWS CloudFormation resources, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is similar to the
`StageName` property of an `AWS::ApiGateway::Stage`
resource. It is required in SAM, but not required in API Gateway

_Additional notes_: The Implicit API has a stage name of
"Prod".

`Tags`

A map (string to string) that specifies the tags to be added to this API Gateway stage.
For details about valid keys and values for tags, see [Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md") in the
_AWS CloudFormation User Guide_.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Tags` property of an `AWS::ApiGateway::Stage` resource.
The Tags property in SAM consists of Key:Value pairs; in CloudFormation it consists of a
list of Tag objects.

`TracingEnabled`

Indicates whether active tracing with X-Ray is enabled for the stage. For more
information about X-Ray, see [Tracing
user requests to REST APIs using X-Ray](../../../apigateway/latest/developerguide/apigateway-xray.md "../../../apigateway/latest/developerguide/apigateway-xray.md") in the _API Gateway Developer Guide_.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`TracingEnabled` property of an `AWS::ApiGateway::Stage`
resource.

`Variables`

A map (string to string) that defines the stage variables, where the variable name
is the key and the variable value is the value. Variable names are limited to
alphanumeric characters. Values must match the following regular expression:
`[A-Za-z0-9._~:/?#&=,-]+`.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Variables` property of an `AWS::ApiGateway::Stage`
resource.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic
function, it returns the ID of the underlying API Gateway API.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The
following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`RootResourceId`

The root resource ID for a `RestApi` resource, such as
`a0bc123d4e`.

## Examples

### SimpleApiExample

A Hello World AWS SAM template file that contains a Lambda Function with an API endpoint.
This is a full AWS SAM template file for a working serverless application.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
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
        def handler(event, context):
            return {'body': 'Hello World!', 'statusCode': 200}

```

### ApiCorsExample

An AWS SAM template snippet with an API defined in an external Swagger file along with
Lambda integrations and CORS configurations. This is just a portion of an AWS SAM template
file showing an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md")
definition.

#### YAML

```
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      # Allows www.example.com to call these APIs
      # SAM will automatically add AllowMethods with a list of methods for this API
      Cors: "'www.example.com'"
      DefinitionBody: # Pull in an OpenApi definition from S3
        'Fn::Transform':
          Name: 'AWS::Include'
          # Replace "bucket" with your bucket name
          Parameters:
            Location: s3://bucket/swagger.yaml

```

### ApiCognitoAuthExample

An AWS SAM template snippet with an API that uses Amazon Cognito to authorize requests against the
API. This is just a portion of an AWS SAM template file showing an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") definition.

#### YAML

```
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      Cors: "'*'"
      Auth:
        DefaultAuthorizer: MyCognitoAuthorizer
        Authorizers:
          MyCognitoAuthorizer:
            UserPoolArn:
              Fn::GetAtt: [MyCognitoUserPool, Arn]

```

### ApiModelsExample

An AWS SAM template snippet with an API that includes a Models schema. This is just a
portion of an AWS SAM template file, showing an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") definition with two model schemas.

#### YAML

```
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      Models:
        User:
          type: object
          required:
            - username
            - employee_id
          properties:
            username:
              type: string
            employee_id:
              type: integer
            department:
              type: string
        Item:
          type: object
          properties:
            count:
              type: integer
            category:
              type: string
            price:
              type: integer

```

### Caching example

A Hello World AWS SAM template file that contains a Lambda Function with an API endpoint.
The API has caching enabled for one resource and method. For more information about caching,
see [Enabling API caching to enhance responsiveness](../../../apigateway/latest/developerguide/api-gateway-caching.md "../../../apigateway/latest/developerguide/api-gateway-caching.md") in the _API Gateway Developer Guide_.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template with a simple API definition with caching turned on
Resources:
  ApiGatewayApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      CacheClusterEnabled: true
      CacheClusterSize: '0.5'
      MethodSettings:
        - ResourcePath: /
          HttpMethod: GET
          CachingEnabled: true
          CacheTtlInSeconds: 300
      Tags:
        CacheMethods: All

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
        def handler(event, context):
            return {'body': 'Hello World!', 'statusCode': 200}

```

### Custom domain with a private API example

A Hello World AWS SAM template file that contains a Lambda function with an API endpoint
mapped to a private domain. The template creates a domain access association between
a VPC endpoint and the private domain. For more information, see [Custom domain names for private APIs in API Gateway](../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md "../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md").

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS SAM template configured with a custom domain using a private API

Parameters:
    DomainName:
      Type: String
      Default: mydomain.example.com
    CertificateArn:
      Type: String
    HostedZoneId:
      Type: String
    VpcEndpointId:
      Type: String
    VpcEndpointDomainName:
      Type: String
    VpcEndpointHostedZoneId:
      Type: String

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      InlineCode: |
        def handler(event, context):
            return {'body': 'Hello World!', 'statusCode': 200}
      Handler: index.handler
      Runtime: python3.13
      Events:
        Fetch:
          Type: Api
          Properties:
            RestApiId:
              Ref: MyApi
            Method: Get
            Path: /get
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      EndpointConfiguration:
        Type: PRIVATE
        VPCEndpointIds:
        - !Ref VpcEndpointId
      Policy:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal: '*'
          Action: execute-api:Invoke
          Resource: execute-api:/*
        - Effect: Deny
          Principal: '*'
          Action: execute-api:Invoke
          Resource: execute-api:/*
          Condition:
            StringNotEquals:
              aws:SourceVpce: !Ref VpcEndpointId
      Domain:
        DomainName: !Ref DomainName
        CertificateArn: !Ref CertificateArn
        EndpointConfiguration: PRIVATE
        BasePath:
        - /
        Route53:
          HostedZoneId: !Ref HostedZoneId
          VpcEndpointDomainName: !Ref VpcEndpointDomainName
          VpcEndpointHostedZoneId: !Ref VpcEndpointHostedZoneId
        AccessAssociation:
          VpcEndpointId: !Ref VpcEndpointId
        Policy:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Principal: '*'
            Action: execute-api:Invoke
            Resource: execute-api:/*
          - Effect: Deny
            Principal: '*'
            Action: execute-api:Invoke
            Resource: execute-api:/*
            Condition:
              StringNotEquals:
                aws:SourceVpce: !Ref VpcEndpointId

```
