# Recording resources with the AWS CLI

You can use the AWS CLI to select the types of resources that you want AWS Config to record.
You do this by creating a customer managed configuration recorder, which records the types of
resources that you specify in a recording group. In the recording group, you specify whether
you want to record all supported resource types, or to include or exclude specific types of
resources.

Record all current and future supported resource types
Set up AWS Config to record configuration changes for all current and future supported
resource types in this Region. For a list of supported resources types, see [Supported Resource
Types](resource-config-reference.md "resource-config-reference.md").

1. Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command:

This command uses the `--configuration-recorder` and
`---recording-group` fields.

```
$ **aws configservice put-configuration-recorder \
--configuration-recorder `file://configurationRecorder.json` \
--recording-group `file://recordingGroup.json`**
```

**The `configuration-recorder`
field**

The `configurationRecorder.json` file specifies
`name` and `roleArn` as well as the default recording
frequency for the configuration recorder (`recordingMode`).

```
`{
 "name": "`default`",
 "roleARN": "`arn:aws:iam::123456789012:role/config-role`",
 "recordingMode": {
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "recordingModeOverrides": [
 {
 "description": "`Description you provide for the override`",
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "resourceTypes": [ `Comma-separated list of resource types to include in the override` ]
 }
 ]
 }
}`
```

**The `recording-group` field**

The `recordingGroup.json` file specifies which resource types
are recorded.

```
`{
 "allSupported": true,
 "recordingStrategy": {
 "useOnly": "ALL_SUPPORTED_RESOURCE_TYPES"
 },
 "includeGlobalResourceTypes": true
}`
```

For more information about these fields, see
[`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") in the _AWS CLI Command
Reference_. 2. (Optional) To verify that your customer managed configuration recorder has the
settings that you want, use the following
[`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command.

```
$ **aws configservice describe-configuration-recorders**
```

The following is an example response.

```
{
    "ConfigurationRecorders": [
        {
            "name": "default"
            "recordingGroup": {
                "allSupported": true,
                "exclusionByResourceTypes": {
                     "resourceTypes": []
                },
                "includeGlobalResourceTypes": true,
                "recordingStrategy": {
                    "useOnly": "ALL_SUPPORTED_RESOURCE_TYPES"
                },
                "resourceTypes": [],
            },
            "recordingMode": {
                "recordingFrequency": `CONTINUOUS` or `DAILY`,
                "recordingModeOverrides": [
                 {
                     "description": "`Description you provide for the override`,
                     "recordingFrequency": `CONTINUOUS` or `DAILY`,
                     "resourceTypes": [ `Comma-separated list of resource types to include in the override`]
                }
              ]
            },
            "roleARN": "arn:aws:iam::123456789012:role/config-role"
        }
    ]
}
```

Record all current and future supported resources types excluding the types you
specify
Set up AWS Config to record configuration changes for all current and future supported
resource types, including global resource types, except the resource types that you
specify to exclude from recording.

If you choose to stop recording for a resource type, the configuration items that
were already recorded will remain unchanged. For a list of supported resources types,
see [Supported Resource
Types](resource-config-reference.md "resource-config-reference.md").

1. Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command:

This command uses the `--configuration-recorder` and
`---recording-group` fields.

```
$ **aws configservice put-configuration-recorder \
--configuration-recorder `file://configurationRecorder.json` \
--recording-group `file://recordingGroup.json`**
```

**The `configuration-recorder`
field**

The `configurationRecorder.json` file specifies
`name` and `roleArn` as well as the default recording
frequency for the configuration recorder (`recordingMode`).

```
`{
 "name": "`default`",
 "roleARN": "`arn:aws:iam::123456789012:role/config-role`",
 "recordingMode": {
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "recordingModeOverrides": [
 {
 "description": "`Description you provide for the override`",
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "resourceTypes": [ `Comma-separated list of resource types to include in the override` ]
 }
 ]
 }
}`
```

**The `recording-group` field**

The `recordingGroup.json` file specifies which types of
resources AWS Config will record. Pass one or more resource types to exclude in the
`resourceTypes` field of `exclusionByResourceTypes`, as
shown in the following example.

```
`{
 "allSupported": false,
 "exclusionByResourceTypes": {
 "resourceTypes": [
 "`AWS::Redshift::ClusterSnapshot`",
 "`AWS::RDS::DBClusterSnapshot`",
 "`AWS::CloudFront::StreamingDistribution`"
 ]
 },
 "includeGlobalResourceTypes": false,
 "recordingStrategy": {
 "useOnly": "EXCLUSION_BY_RESOURCE_TYPES"
 },

}`
```

For more information about these fields, see
[`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") in the _AWS CLI Command
Reference_. 2. (Optional) To verify that your customer managed configuration recorder has the
settings that you want, use the following
[`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command.

```
$ `aws configservice describe-configuration-recorders`
```

The following is an example response.

```
{
    "ConfigurationRecorders": [
        {
            "name": "default",
            "recordingGroup": {
                "allSupported": false,
                "exclusionByResourceTypes": {
                    "resourceTypes": [
                        "AWS::Redshift::ClusterSnapshot",
                        "AWS::RDS::DBClusterSnapshot",
                        "AWS::CloudFront::StreamingDistribution"
                    ]
                },
                "includeGlobalResourceTypes": false,
                "recordingStrategy": {
                    "useOnly": "EXCLUSION_BY_RESOURCE_TYPES"
                },
                "resourceTypes": [],
            },
            "recordingMode": {
                "recordingFrequency": `CONTINUOUS` or `DAILY`,
                "recordingModeOverrides": [
                 {
                     "description": "`Description you provide for the override`,
                     "recordingFrequency": `CONTINUOUS` or `DAILY`,
                     "resourceTypes": [ `Comma-separated list of resource types to include in the override`]
                }
              ]
            },
            "roleARN": "arn:aws:iam::123456789012:role/config-role"
        }
    ]
}
```

Record specific resource types
Set up AWS Config to record configuration changes for only the resource types that you
specify.

If you choose to stop recording for a resource type, the configuration items that
were already recorded will remain unchanged. For a list of supported resources types,
see [Supported Resource
Types](resource-config-reference.md "resource-config-reference.md").

1. Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command:

This command uses the `--configuration-recorder` and
`---recording-group` fields.

```
$ **aws configservice put-configuration-recorder \
--configuration-recorder `file://configurationRecorder.json` \
--recording-group `file://recordingGroup.json`**
```

**The `configuration-recorder`
field**

The `configurationRecorder.json` file specifies
`name` and `roleArn` as well as the default recording
frequency for the configuration recorder (`recordingMode`).

```
`{
 "name": "`default`",
 "roleARN": "`arn:aws:iam::123456789012:role/config-role`",
 "recordingMode": {
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "recordingModeOverrides": [
 {
 "description": "`Description you provide for the override`",
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "resourceTypes": [ `Comma-separated list of resource types to include in the override` ]
 }
 ]
 }
}`
```

**The `recording-group` field**

The `recordingGroup.json` file specifies which types of
resources AWS Config will record. Pass one or more resource types to exclude in the
`resourceTypes` field as shown in the following example.

```
`{
 "allSupported": false,
 "recordingStrategy": {
 "useOnly": "INCLUSION_BY_RESOURCE_TYPES"
 },
 "includeGlobalResourceTypes": false,
 "resourceTypes": [
 "`AWS::EC2::EIP`",
 "`AWS::EC2::Instance`",
 "`AWS::EC2::NetworkAcl`",
 "A`WS::EC2::SecurityGroup`",
 "`AWS::CloudTrail::Trail`",
 "`AWS::EC2::Volume`",
 "`AWS::EC2::VPC`",
 "`AWS::IAM::User`",
 "`AWS::IAM::Policy`"
 ]
}`
```

For more information about these fields, see
[`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") in the _AWS CLI Command
Reference_. 2. (Optional) To verify that your customer managed configuration recorder has the
settings that you want, use the following
[`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command.

```
$ `aws configservice describe-configuration-recorders`
```

The following is an example response.

```
{
    "ConfigurationRecorders": [
        {
            "name": "default",
            "recordingGroup": {
                "allSupported": false,
                "exclusionByResourceTypes": {
                    "resourceTypes": []
                },
                "includeGlobalResourceTypes": false
                "recordingStrategy": {
                    "useOnly": "INCLUSION_BY_RESOURCE_TYPES"
                },
                "resourceTypes": [
                    "AWS::EC2::EIP",
                    "AWS::EC2::Instance",
                    "AWS::EC2::NetworkAcl",
                    "AWS::EC2::SecurityGroup",
                    "AWS::CloudTrail::Trail",
                    "AWS::EC2::Volume",
                    "AWS::EC2::VPC",
                    "AWS::IAM::User",
                    "AWS::IAM::Policy"
                ]
            },
            "recordingMode": {
                "recordingFrequency": `CONTINUOUS` or `DAILY`,
                "recordingModeOverrides": [
                 {
                     "description": "`Description you provide for the override`,
                     "recordingFrequency": `CONTINUOUS` or `DAILY`,
                     "resourceTypes": [ `Comma-separated list of resource types to include in the override`]
                }
              ]
            },
            "roleARN": "arn:aws:iam::123456789012:role/config-role"
        }
    ]
}
```
