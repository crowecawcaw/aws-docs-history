# Cognito

The object describing a `Cognito` event source type.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Trigger: `List`
  UserPool: `String`

```

## Properties

`Trigger`

The Lambda trigger configuration information for the new user pool.

_Type_: List

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `LambdaConfig` property of an `AWS::Cognito::UserPool` resource.

`UserPool`

Reference to UserPool defined in the same template

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### Cognito Event

Cognito Event Example

#### YAML

```
CognitoUserPoolPreSignup:
  Type: Cognito
  Properties:
    UserPool:
      Ref: MyCognitoUserPool
    Trigger: PreSignUp

```
