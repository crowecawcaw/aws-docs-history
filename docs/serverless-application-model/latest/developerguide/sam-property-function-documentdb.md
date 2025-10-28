# DocumentDB

The object describing a `DocumentDB` event source type. For more information, see
[Using AWS Lambda with Amazon DocumentDB](../../../lambda/latest/dg/with-documentdb.md "../../../lambda/latest/dg/with-documentdb.md") in the
_AWS Lambda Developer Guide_.

## Syntax

To declare this entity in your AWS SAM template, use the following syntax.

### YAML

```
BatchSize: `Integer`
Cluster: String
CollectionName: `String`
DatabaseName: `String`
Enabled: `Boolean`
FilterCriteria: FilterCriteria
FullDocument: `String`
KmsKeyArn: `String`
MaximumBatchingWindowInSeconds: `Integer`
SecretsManagerKmsKeyId: `String`
SourceAccessConfigurations: `List`
StartingPosition: `String`
StartingPositionTimestamp: `Double`
```

## Properties

`BatchSize`

The maximum number of items to retrieve in a single batch.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`BatchSize` property of an `AWS::Lambda::EventSourceMapping` resource.

`Cluster`

The Amazon Resource Name (ARN) of the Amazon DocumentDB cluster.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`EventSourceArn` property of an `AWS::Lambda::EventSourceMapping` resource.

`CollectionName`

The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes
all collections.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`CollectionName` property of an `AWS::Lambda::EventSourceMapping`
`DocumentDBEventSourceConfig` data type.

`DatabaseName`

The name of the database to consume within the Amazon DocumentDB cluster.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`DatabaseName` property of an `AWS::Lambda::EventSourceMapping`
`DocumentDBEventSourceConfig`data type.

`Enabled`

If `true`, the event source mapping is active. To pause polling and invocation, set to
`false`.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Enabled` property of an `AWS::Lambda::EventSourceMapping` resource.

`FilterCriteria`

An object that defines the criteria that determines whether Lambda should process an event. For more
information, see [Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") in the _AWS Lambda Developer Guide_.

_Type_: [FilterCriteria](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FilterCriteria` property of an `AWS::Lambda::EventSourceMapping` resource.

`FullDocument`

Determines what Amazon DocumentDB sends to your event stream during document update operations. If set to
`UpdateLookup`, Amazon DocumentDB sends a delta describing the changes, along with a copy of the entire document.
Otherwise, Amazon DocumentDB sends only a partial document that contains the changes.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FullDocument` property of an `AWS::Lambda::EventSourceMapping`
`DocumentDBEventSourceConfig` data type.

`KmsKeyArn`

The Amazon Resource Name (ARN) of the key to encrypt information related to this event.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn`
property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumBatchingWindowInSeconds`

The maximum amount of time to gather records before invoking the function, in seconds.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MaximumBatchingWindowInSeconds` property of an `AWS::Lambda::EventSourceMapping` resource.

`SecretsManagerKmsKeyId`

The AWS Key Management Service (AWS KMS) key ID of a customer managed key from AWS Secrets Manager. Required when you use
a customer managed key from Secrets Manager with a Lambda execution role that doesn’t include
the `kms:Decrypt` permission.

The value of this property is a UUID. For example: `1abc23d4-567f-8ab9-cde0-1fab234c5d67`.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn’t have an AWS CloudFormation
equivalent.

`SourceAccessConfigurations`

An array of the authentication protocol or virtual host. Specify this using the [SourceAccessConfigurations](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md") data type.

For the `DocumentDB` event source type, the only valid configuration type is
`BASIC_AUTH`.

- `BASIC_AUTH` – The Secrets Manager secret that stores your broker
  credentials. For this type, the credential must be in the following format: `{"username": "your-username", 
"password": "your-password"}`. Only one object of type `BASIC_AUTH` is allowed.

_Type_: List

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`SourceAccessConfigurations` property of an `AWS::Lambda::EventSourceMapping`
resource.

`StartingPosition`

The position in a stream from which to start reading.

- `AT_TIMESTAMP` – Specify a time from which to start reading records.
- `LATEST` – Read only new records.
- `TRIM_HORIZON` – Process all available records.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartingPosition` property of an `AWS::Lambda::EventSourceMapping` resource.

`StartingPositionTimestamp`

The time from which to start reading, in Unix time seconds. Define `StartingPositionTimestamp`
when `StartingPosition` is specified as `AT_TIMESTAMP`.

_Type_: Double

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartingPositionTimestamp` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples

### Amazon DocumentDB event source

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
    ...
      Events:
        MyDDBEvent:
          Type: DocumentDB
          Properties:
            Cluster: "arn:aws:rds:us-west-2:123456789012:cluster:docdb-2023-01-01"
            BatchSize: 10
            MaximumBatchingWindowInSeconds: 5
            DatabaseName: "db1"
            CollectionName: "collection1"
            FullDocument: "UpdateLookup"
            SourceAccessConfigurations:
              - Type: BASIC_AUTH
                URI: "arn:aws:secretsmanager:us-west-2:123456789012:secret:doc-db"
```
