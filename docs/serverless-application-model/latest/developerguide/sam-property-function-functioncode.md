# FunctionCode

The [deployment package](../../../lambda/latest/dg/deployment-package-v2.md "../../../lambda/latest/dg/deployment-package-v2.md") for a Lambda function.

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

An Amazon S3 bucket in the same AWS Region as your function.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `S3Bucket` property of the `AWS::Lambda::Function` `Code` data type.

`Key`

The Amazon S3 key of the deployment package.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `S3Key` property of the `AWS::Lambda::Function` `Code` data type.

`Version`

For versioned objects, the version of the deployment package object to use.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `S3ObjectVersion` property of the `AWS::Lambda::Function` `Code` data type.

## Examples

### FunctionCode

`CodeUri`: Function Code example

#### YAML

```
`CodeUri`:
  Bucket: sam-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212

```
