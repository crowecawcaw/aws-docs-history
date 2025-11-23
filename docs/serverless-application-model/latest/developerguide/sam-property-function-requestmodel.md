# RequestModel

Configures a Request Model for a specific Api+Path+Method.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Model: `String`
  Required: `Boolean`
  ValidateBody: `Boolean`
  ValidateParameters: `Boolean`

```

## Properties

`Model`

Name of a model defined in the Models property of the [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md").

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Required`

Adds a `required` property in the parameters section of the OpenApi definition for the given API endpoint.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ValidateBody`

Specifies whether API Gateway uses the `Model` to validate the request body. For more information, see [Enable request validation in API Gateway](../../../apigateway/latest/developerguide/api-gateway-method-request-validation.md "../../../apigateway/latest/developerguide/api-gateway-method-request-validation.md") in the _API Gateway Developer Guide_.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ValidateParameters`

Specifies whether API Gateway uses the `Model` to validate request path parameters, query strings, and headers. For more information, see [Enable request validation in API Gateway](../../../apigateway/latest/developerguide/api-gateway-method-request-validation.md "../../../apigateway/latest/developerguide/api-gateway-method-request-validation.md") in the _API Gateway Developer Guide_.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### Request Model

Request Model Example

#### YAML

```
RequestModel:
  Model: User
  Required: true
  ValidateBody: true
  ValidateParameters: true

```
