# S3

The object describing an `S3` event source type.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Bucket: `String`
  Events: `String | List`
  Filter: `NotificationFilter`

```

## Properties

`Bucket`

S3 bucket name. This bucket must exist in the same template.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is similar to the `BucketName` property of an `AWS::S3::Bucket` resource. This is a required field in SAM. This field only accepts a reference to the S3 bucket created in this template

`Events`

The Amazon S3 bucket event for which to invoke the Lambda function. See [Amazon S3 supported event types](../../../AmazonS3/latest/dev/NotificationHowTo.md#supported-notification-event-types "../../../AmazonS3/latest/dev/NotificationHowTo.md#supported-notification-event-types") for a list of valid values.

_Type_: String | List

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `Event` property of the `AWS::S3::Bucket` `LambdaConfiguration` data type.

`Filter`

The filtering rules that determine which Amazon S3 objects invoke the Lambda function. For information about Amazon S3 key name filtering, see [Configuring Amazon S3 Event Notifications](../../../AmazonS3/latest/dev/NotificationHowTo.md "../../../AmazonS3/latest/dev/NotificationHowTo.md") in the _Amazon Simple Storage Service User Guide_.

_Type_: [NotificationFilter](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Filter` property of the `AWS::S3::Bucket` `LambdaConfiguration` data type.

## Examples

### S3-Event

Example of an S3 Event.

#### YAML

```
Events:
  S3Event:
    Type: S3
    Properties:
      Bucket:
        Ref: ImagesBucket     # This must be the name of an S3 bucket declared in the same template file
      Events: s3:ObjectCreated:*
      Filter:
        S3Key:
          Rules:
          - Name: prefix      # or "suffix"
            Value: value      # The value to search for in the S3 object key names

```
