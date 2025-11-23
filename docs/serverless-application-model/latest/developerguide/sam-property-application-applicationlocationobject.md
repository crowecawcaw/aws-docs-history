# ApplicationLocationObject

An application that has been published to the [AWS Serverless Application Repository](../../../serverlessrepo/latest/devguide/what-is-serverlessrepo.md "../../../serverlessrepo/latest/devguide/what-is-serverlessrepo.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  ApplicationId: `String`
  SemanticVersion: `String`

```

## Properties

`ApplicationId`

The Amazon Resource Name (ARN) of the application.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`SemanticVersion`

The semantic version of the application.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### my-application

Example application location object

#### YAML

```
Location:
  ApplicationId: 'arn:aws:serverlessrepo:us-east-1:012345678901:applications/my-application'
  SemanticVersion: 1.0.0

```
