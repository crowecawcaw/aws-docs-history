# Target

Configures the AWS resource that EventBridge invokes when a rule is triggered.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Id: `String`

```

## Properties

`Id`

The logical ID of the target.

The value of `Id` can include alphanumeric characters, periods (`.`),
hyphens (`-`), and underscores (`_`).

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`Id`
property of the `AWS::Events::Rule` `Target` data type.

## Examples

### Target

#### YAML

```
EBRule:
  Type: Schedule
  Properties:
    Target:
      Id: MyTarget

```
