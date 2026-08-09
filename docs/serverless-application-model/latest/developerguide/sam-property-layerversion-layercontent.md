# LayerContent

A ZIP archive that contains the contents of an [Lambda layer](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md").

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

The Amazon S3 bucket of the layer archive.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `S3Bucket` property of the `AWS::Lambda::LayerVersion` `Content` data type.

`Key`

The Amazon S3 key of the layer archive.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `S3Key` property of the `AWS::Lambda::LayerVersion` `Content` data type.

`StorageMode`

Controls how Lambda stores the layer archive.

- `COPY` – Lambda uploads a copy of your layer archive to Lambda-managed storage. You can delete the Amazon S3 object after
  Lambda creates the layer version.
- `REFERENCE` – Lambda references the layer archive from your Amazon S3 bucket and doesn't store a copy. The object must
  remain in place, and Lambda must keep access to it, for the lifetime of the layer version.

To use `REFERENCE`, enable versioning on your Amazon S3 bucket and grant the Lambda service principal access to the object. For more information, see
[Self-managed Amazon S3 code storage](../../../lambda/latest/dg/configuration-self-managed-storage.md "../../../lambda/latest/dg/configuration-self-managed-storage.md") in the
_AWS Lambda Developer Guide_.

_Type_: String

_Valid values_: `COPY` | `REFERENCE`

_Required_: No

_Default_: `COPY`

_CloudFormation compatibility_: This property is passed directly to the `S3ObjectStorageMode` property of the `AWS::Lambda::LayerVersion` `Content` data type.

`Version`

For versioned objects, the version of the layer archive object to use.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `S3ObjectVersion` property of the `AWS::Lambda::LayerVersion` `Content` data type.

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

### Self-managed Amazon S3 code storage

The following `LayerContent` references the layer archive from your own Amazon S3 bucket instead of copying it to Lambda-managed storage.

#### YAML

```
LayerContent:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
  StorageMode: REFERENCE

```
