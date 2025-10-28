# Api

The object describing an `Api` event source type. If an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource is defined, the path and method values must correspond to an operation in the OpenAPI definition of the API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Auth: `ApiStateMachineAuth`
  Method: `String`
  Path: `String`
  RestApiId: `String`
  UnescapeMappingTemplate: `Boolean`

```

## Properties

`Auth`

The authorization configuration for this API, path, and method.

Use this property to override the API's `DefaultAuthorizer` setting for an individual path,
when no `DefaultAuthorizer` is specified, or to override the default `ApiKeyRequired`
setting.

_Type_: [ApiStateMachineAuth](sam-property-statemachine-apistatemachineauth.md "sam-property-statemachine-apistatemachineauth.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Method`

The HTTP method for which this function is invoked.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Path`

The URI path for which this function is invoked. The value must start with `/`.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`RestApiId`

The identifier of a `RestApi` resource, which must contain an operation with the given path and method. Typically, this is set to reference an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource that is defined in this template.

If you don't define this property, AWS SAM creates a default [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource using a generated `OpenApi` document. That resource contains a union of all paths and methods defined by `Api` events in the same template that do not specify a `RestApiId`.

This property can't reference an [AWS::Serverless::Api](sam-resource-api.md "sam-resource-api.md") resource that is defined in another template.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`UnescapeMappingTemplate`

Unescapes single quotes, by replacing `\'` with `'`, on the input that is passed
to the state machine. Use when your input contains single quotes.

###### Note

If set to `False` and your input contains single quotes, an error will occur.

_Type_: Boolean

_Required_: No

_Default_: False

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation
equivalent.

## Examples

### ApiEvent

The following is an example of an event of the `Api` type.

#### YAML

```
Events:
  ApiEvent:
    Type: Api
    Properties:
      Path: /path
      Method: get

```
