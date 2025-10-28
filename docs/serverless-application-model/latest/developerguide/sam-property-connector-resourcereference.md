# ResourceReference

A reference to a resource that the [AWS::Serverless::Connector](sam-resource-connector.md "sam-resource-connector.md") resource type uses.

###### Note

For resources in the same template, provide the `Id`. For resources not in the same template, use a combination of other properties. For more information, see [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Arn: `String`
  Id: `String`
  Name: `String`
  Qualifier: `String`
  QueueUrl: `String`
  ResourceId: `String`
  RoleName: `String`
  Type: `String`

```

## Properties

`Arn`

The ARN of a resource.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Id`

The [logical ID](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md") of a resource in the same template.

###### Note

When `Id` is specified, if the connector generates AWS Identity and Access Management (IAM) policies, the IAM role associated to those policies will be inferred from the resource `Id`. When `Id` is not specified, provide `RoleName` of the resource for connectors to attach generated IAM policies to an IAM role.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Name`

The name of a resource.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Qualifier`

A qualifier for a resource that narrows its scope. `Qualifier` replaces the `*` value at the end of a resource constraint ARN. For an example, see [API Gateway invoking a Lambda function](#sam-property-connector-resourcereference--examples--api-gateway-invoking-a-lambda-function "#sam-property-connector-resourcereference--examples--api-gateway-invoking-a-lambda-function").

###### Note

Qualifier definition varies per resource type. For a list of supported source and destination resource types, see [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md").

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`QueueUrl`

The Amazon SQS queue URL. This property only applies to Amazon SQS resources.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ResourceId`

The ID of a resource. For example, the API Gateway API ID.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`RoleName`

The role name associated with a resource.

###### Note

When `Id` is specified, if the connector generates IAM policies, the IAM role associated to those policies will be inferred from the resource `Id`. When `Id` is not specified, provide `RoleName` of the resource for connectors to attach generated IAM policies to an IAM role.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Type`

The AWS CloudFormation type of a resource. For more information, go to [AWS resource and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md").

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### API Gateway invoking a Lambda function

The following example uses the [AWS::Serverless::Connector](sam-resource-connector.md "sam-resource-connector.md") resource to allow Amazon API Gateway to invoke an AWS Lambda function.

#### YAML

```
Transform: AWS::Serverless-2016-10-31
Resources:
  MyRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Action: sts:AssumeRole
            Principal:
              Service: lambda.amazonaws.com
      ManagedPolicyArns:
        - !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role: !GetAtt MyRole.Arn
      Runtime: nodejs16.x
      Handler: index.handler
      Code:
        ZipFile: |
          exports.handler = async (event) => {
            return {
              statusCode: 200,
              body: JSON.stringify({
                "message": "It works!"
              }),
            };
          };

  MyApi:
    Type: AWS::ApiGatewayV2::Api
    Properties:
      Name: MyApi
      ProtocolType: HTTP

  MyStage:
    Type: AWS::ApiGatewayV2::Stage
    Properties:
      ApiId: !Ref MyApi
      StageName: prod
      AutoDeploy: True

  MyIntegration:
    Type: AWS::ApiGatewayV2::Integration
    Properties:
      ApiId: !Ref MyApi
      IntegrationType: AWS_PROXY
      IntegrationUri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${MyFunction.Arn}/invocations
      IntegrationMethod: POST
      PayloadFormatVersion: "2.0"

  MyRoute:
    Type: AWS::ApiGatewayV2::Route
    Properties:
      ApiId: !Ref MyApi
      RouteKey: GET /hello
      Target: !Sub integrations/${MyIntegration}

  MyConnector:
    Type: AWS::Serverless::Connector
    Properties:
      Source: # Use 'Id' when resource is in the same template
        Type: AWS::ApiGatewayV2::Api
        ResourceId: !Ref MyApi
        Qualifier: prod/GET/hello # Or "*" to allow all routes
      Destination: # Use 'Id' when resource is in the same template
        Type: AWS::Lambda::Function
        Arn: !GetAtt MyFunction.Arn
      Permissions:
        - Write

Outputs:
  Endpoint:
    Value: !Sub https://${MyApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/prod/hello

```
