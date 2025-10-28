# LayerContent

A ZIP archive that contains the contents of an [Lambda layer](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Bucket: `String`
  Key: `String`
  Version: `String`

```

## Properties

`Bucket`

The Amazon S3 bucket of the layer archive.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `S3Bucket` property of the `AWS::Lambda::LayerVersion` `Content` data type.

`Key`

The Amazon S3 key of the layer archive.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `S3Key` property of the `AWS::Lambda::LayerVersion` `Content` data type.

`Version`

For versioned objects, the version of the layer archive object to use.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `S3ObjectVersion` property of the `AWS::Lambda::LayerVersion` `Content` data type.

## Examples

### LayerContent

Layer Content example

#### YAML

```
LayerContent:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212

```
