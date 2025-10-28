# Hooks

Validation Lambda functions that are run before and after traffic shifting.

###### Note

The Lambda functions referenced in this property configure the `CodeDeployLambdaAliasUpdate` object of the resulting [AWS::Lambda::Alias](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md") resource. For more information, see [CodeDeployLambdaAliasUpdate Policy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.md#cfn-attributes-updatepolicy-codedeploylambdaaliasupdate "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.md#cfn-attributes-updatepolicy-codedeploylambdaaliasupdate") in the _AWS CloudFormation User Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  PostTraffic: `String`
  PreTraffic: `String`

```

## Properties

`PostTraffic`

Lambda function that is run after traffic shifting.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`PreTraffic`

Lambda function that is run before traffic shifting.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### Hooks

Example hook functions

#### YAML

```
Hooks:
  PreTraffic:
    Ref: PreTrafficLambdaFunction
  PostTraffic:
    Ref: PostTrafficLambdaFunction

```
