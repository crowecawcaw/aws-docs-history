# ManagedResourceTags

Applies explicit tags to the Amazon Elastic Compute Cloud instances and other resources that the
capacity provider provisions and manages on your behalf.

###### Note

The `ManagedResourceTags` property controls tagging of the Amazon EC2 instances
and other resources that Lambda manages for the capacity provider. This property differs from
the [PropagateTags](sam-resource-capacityprovider.md#sam-capacityprovider-propagatetags "sam-resource-capacityprovider.md#sam-capacityprovider-propagatetags") property,
which specifies whether AWS SAM propagates the [Tags](sam-resource-capacityprovider.md#sam-capacityprovider-tags "sam-resource-capacityprovider.md#sam-capacityprovider-tags")
property to the CloudFormation resources that AWS SAM generates from your template.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Tags: `Map`
```

## Properties

The following properties are supported for `ManagedResourceTags`.

`Tags`

A map of key-value pairs to apply to the Amazon EC2 instances and other resources that the
capacity provider manages.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: AWS SAM uses this property to construct the
`PropagateTags` property of an
`AWS::Lambda::CapacityProvider` resource. AWS SAM sets `Mode` to
`Explicit` and converts the key-value pairs to a list of Tag objects in
`ExplicitTags`.

## Examples

### Apply explicit tags to managed resources

The following example applies an explicit set of tags to the Amazon EC2 instances that the
capacity provider manages.

```
ManagedResourceTags:
  Tags:
    CostCenter: `cc-1234`
    Environment: `Production`
```
