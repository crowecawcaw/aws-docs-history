# FunctionCode

The [deployment package](../../../lambda/latest/dg/deployment-package-v2.md "../../../lambda/latest/dg/deployment-package-v2.md") for a Lambda function.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Bucket: `String`
  Key: `String`
  StorageMode: `String`
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

`StorageMode`

Controls how Lambda stores the deployment package.

- `COPY` – Lambda uploads a copy of your deployment package to Lambda-managed storage. You can delete the Amazon S3 object after
  Lambda creates the function.
- `REFERENCE` – Lambda references the deployment package from your Amazon S3 bucket and doesn't store a copy. The object must
  remain in place, and Lambda must keep access to it, for the lifetime of the function.

To use `REFERENCE`, enable versioning on your Amazon S3 bucket and grant the Lambda service principal access to the object. For more information, see
[Self-managed Amazon S3 code storage](../../../lambda/latest/dg/configuration-self-managed-storage.md "../../../lambda/latest/dg/configuration-self-managed-storage.md") in the
_AWS Lambda Developer Guide_.

_Type_: String

_Valid values_: `COPY` | `REFERENCE`

_Required_: No

_Default_: `COPY`

_CloudFormation compatibility_: This property is passed directly to the `S3ObjectStorageMode` property of the `AWS::Lambda::Function` `Code` data type.

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

### Self-managed Amazon S3 code storage

The following `CodeUri` references the deployment package from your own Amazon S3 bucket instead of copying it to Lambda-managed storage.

#### YAML

```
`CodeUri`:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
  StorageMode: REFERENCE

```
