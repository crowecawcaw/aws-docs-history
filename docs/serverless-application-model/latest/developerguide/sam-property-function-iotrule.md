# IoTRule

The object describing an `IoTRule` event source type.

Creates an [AWS::IoT::TopicRule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.md") resource to declare an AWS IoT rule. For more information see [AWS CloudFormation documentation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.md")

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AwsIotSqlVersion: `String`
  Sql: `String`

```

## Properties

`AwsIotSqlVersion`

The version of the SQL rules engine to use when evaluating the rule.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `AwsIotSqlVersion` property of an `AWS::IoT::TopicRule TopicRulePayload` resource.

`Sql`

The SQL statement used to query the topic. For more information, see [AWS IoT SQL Reference](../../../iot/latest/developerguide/iot-rules.md#aws-iot-sql-reference "../../../iot/latest/developerguide/iot-rules.md#aws-iot-sql-reference") in the _AWS IoT Developer Guide_.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `Sql` property of an `AWS::IoT::TopicRule TopicRulePayload` resource.

## Examples

### IOT Rule

IOT Rule Example

#### YAML

```
IoTRule:
  Type: IoTRule
  Properties:
    Sql: SELECT * FROM 'topic/test'

```
