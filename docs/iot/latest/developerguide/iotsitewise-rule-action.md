# AWS IoT SiteWise

The AWS IoT SiteWise (`iotSiteWise`) action sends data from an MQTT message to
asset properties in AWS IoT SiteWise.

You can follow a tutorial that shows you how to ingest data from AWS IoT things. For
more information, see the [Ingesting data to AWS IoT SiteWise
from AWS IoT things](../../../iot-sitewise/latest/userguide/ingest-data-from-iot-things.md "../../../iot-sitewise/latest/userguide/ingest-data-from-iot-things.md") tutorial or the [Ingesting data using AWS IoT Core rules](../../../iot-sitewise/latest/userguide/iot-rules.md "../../../iot-sitewise/latest/userguide/iot-rules.md") section in the _AWS IoT SiteWise
User Guide_.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `iotsitewise:BatchPutAssetPropertyValue`
  operation. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

You can attach the following example trust policy to the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "*"
 }
 ]
}`

```

To improve security, you can specify an AWS IoT SiteWise asset hierarchy path in
the `Condition` property. The following example is a trust
policy that specifies an asset hierarchy path.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iotsitewise:assetHierarchyPath": [
 "/`root node asset ID`",
 "/`root node asset ID`/*"
 ]
 }
 }
 }
 ]
}`

```

- When you send data to AWS IoT SiteWise with this action, your data must meet the
  requirements of the `BatchPutAssetPropertyValue` operation.
  For more information, see [BatchPutAssetPropertyValue](../../../iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.md "../../../iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.md") in the _AWS IoT SiteWise API
  Reference_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`putAssetPropertyValueEntries`

A list of asset property value entries that each contain the
following information:

`propertyAlias`

(Optional) The property alias associated with your
asset property. Specify either a
`propertyAlias` or both an
`assetId` and a `propertyId`.
For more information about property aliases, see [Mapping industrial data streams to asset
properties](../../../iot-sitewise/latest/userguide/connect-data-streams.md "../../../iot-sitewise/latest/userguide/connect-data-streams.md") in the _AWS IoT SiteWise User
Guide_.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`assetId`

(Optional) The ID of the AWS IoT SiteWise asset. Specify either
a `propertyAlias` or both an
`assetId` and a
`propertyId`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`propertyId`

(Optional) The ID of the asset's property. Specify
either a `propertyAlias` or both an
`assetId` and a
`propertyId`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`entryId`

(Optional) A unique identifier for this entry. Define
the `entryId` to better track which message
caused an error if failure occurs. Defaults to a new
UUID.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`propertyValues`

A list of property values to insert that each contain
timestamp, quality, and value (TQV) in the following
format:

`timestamp`

A timestamp structure that contains the
following information:

`timeInSeconds`

A string that contains the time in seconds
in Unix epoch time. If your message payload
doesn't have a timestamp, you can use [timestamp()](iot-sql-functions.md#iot-function-timestamp "iot-sql-functions.md#iot-function-timestamp"), which
returns the current time in milliseconds. To
convert that time to seconds, you can use the
following substitution template:
`${floor(timestamp() /
 1E3)}`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`offsetInNanos`

(Optional) A string that contains the
nanosecond time offset from the time in seconds.
If your message payload doesn't have a timestamp,
you can use [timestamp()](iot-sql-functions.md#iot-function-timestamp "iot-sql-functions.md#iot-function-timestamp"), which
returns the current time in milliseconds. To
calculate the nanosecond offset from that time,
you can use the following substitution template:
`${(timestamp() % 1E3) *
 1E6}`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

Regarding Unix epoch time, AWS IoT SiteWise accepts
only entries that have a timestamp of up to 7 days
in the past up to 5 minutes in the future.

`quality`

(Optional) A string that describes the
quality of the value. Valid values:
`GOOD`, `BAD`,
`UNCERTAIN`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`value`

A value structure that contains one of the
following value fields, depending on the asset
property's data type:

`booleanValue`

(Optional) A string that contains the
Boolean value of the value entry.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`doubleValue`

(Optional) A string that contains the double
value of the value entry.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`integerValue`

(Optional) A string that contains the
integer value of the value entry.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`stringValue`

(Optional) The string value of the value
entry.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleArn`

The ARN of the IAM role that grants AWS IoT permission to send an
asset property value to AWS IoT SiteWise. For more information, see [Requirements](#iotsitewise-rule-action-requirements "#iotsitewise-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines a basic IoT SiteWise action in an AWS IoT
rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "iotSiteWise": {
                    "putAssetPropertyValueEntries": [
                        {
                            "propertyAlias": "/some/property/alias",
                            "propertyValues": [
                                {
                                    "timestamp": {
                                        "timeInSeconds": "${my.payload.timeInSeconds}"
                                    },
                                    "value": {
                                        "integerValue": "${my.payload.value}"
                                    }
                                }
                            ]
                        }
                    ],
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sitewise"
                }
            }
        ]
    }
}
```

The following JSON example defines an IoT SiteWise action in an AWS IoT rule.
This example uses the topic as the property alias and the
`timestamp()` function. For example, if you publish data to
`/company/windfarm/3/turbine/7/rpm`, this action sends the data
to the asset property with a property alias that's the same as the topic that
you specified.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM '/company/windfarm/+/turbine/+/+'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "iotSiteWise": {
                    "putAssetPropertyValueEntries": [
                        {
                            "propertyAlias": "${topic()}",
                            "propertyValues": [
                                {
                                    "timestamp": {
                                        "timeInSeconds": "${floor(timestamp() / 1E3)}",
                                        "offsetInNanos": "${(timestamp() % 1E3) * 1E6}"
                                    },
                                    "value": {
                                        "doubleValue": "${my.payload.value}"
                                    }
                                }
                            ]
                        }
                    ],
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sitewise"
                }
            }
        ]
    }
}
```

## See also

- [What is
  AWS IoT SiteWise?](../../../iot-sitewise/latest/userguide/what-is-sitewise.md "../../../iot-sitewise/latest/userguide/what-is-sitewise.md") in the
  _AWS IoT SiteWise User Guide_
- [Ingesting data
  using AWS IoT Core rules](../../../iot-sitewise/latest/userguide/iot-rules.md "../../../iot-sitewise/latest/userguide/iot-rules.md") in the
  _AWS IoT SiteWise User Guide_
- [Ingesting data to AWS IoT SiteWise from AWS IoT things](../../../iot-sitewise/latest/userguide/ingest-data-from-iot-things.md "../../../iot-sitewise/latest/userguide/ingest-data-from-iot-things.md") in the
  _AWS IoT SiteWise User Guide_
- [Troubleshooting
  an AWS IoT SiteWise rule action](../../../iot-sitewise/latest/userguide/troubleshoot-rule.md "../../../iot-sitewise/latest/userguide/troubleshoot-rule.md") in the _AWS IoT SiteWise User
  Guide_
