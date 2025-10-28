# CloudWatchLogs

The object describing a `CloudWatchLogs` event source type.

This event generates a [AWS::Logs::SubscriptionFilter](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.md") resource and specifies a subscription filter and associates it with the specified log group.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  FilterPattern: `String`
  LogGroupName: `String`

```

## Properties

`FilterPattern`

The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see [Filter and Pattern Syntax](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md").

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `FilterPattern` property of an `AWS::Logs::SubscriptionFilter` resource.

`LogGroupName`

The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `LogGroupName` property of an `AWS::Logs::SubscriptionFilter` resource.

## Examples

### Cloudwatchlogs Subscription filter

Cloudwatchlogs Subscription filter Example

#### YAML

```
CWLog:
  Type: CloudWatchLogs
  Properties:
    LogGroupName:
      Ref: CloudWatchLambdaLogsGroup
    FilterPattern: My pattern

```
