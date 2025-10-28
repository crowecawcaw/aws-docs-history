# Scoping metrics in security profiles using

dimensions

Dimensions are attributes that you can define to get more precise data about metrics and
behaviors in your security profile. You define the scope by providing a value or pattern that is
used as a filter. For example, you can define a topic filter dimension that applies a metric
only to MQTT topics that match a particular value, such as "data/bulb/+/activity". For
information about defining a dimension that you can use in your security profile, see [CreateDimension](../../../iot/latest/apireference/API_CreateDimension.md "../../../iot/latest/apireference/API_CreateDimension.md").

Dimension values support MQTT wildcards. MQTT wildcards help you subscribe to multiple
topics simultaneously. There are two different kinds of wildcards: single-level (`+`)
and multi-level `(#`). For example, the dimension value
`Data/bulb/+/activity` creates a subscription that matches all topics that exist on
the same level as the `+`. Dimension values also support the MQTT client ID
substitution variable ${iot:ClientId}.

Dimensions of type TOPIC_FILTER are compatible with the following set of cloud-side
metrics:

- Number of authorization failures
- Message byte size
- Number of messages received
- Number of messages sent
- Source IP address (only available for Rules Detect)

## How to use dimensions in the console

###### To create and apply a dimension to a security profile behavior

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Detect**, and then choose **Security profiles**.
2. On the **Security Profiles** page, choose **Create Security Profile**, and then choose **Create Rule-based anomaly Detect profile**. Or, to apply a dimension to an existing Rule-based security profile, select the security profile and choose **Edit**.
3. On the **Specify security profile properties** page, enter a name for the security profile.
4. Choose the group of devices that you want to target for anomalies.
5. Choose **Next**.
6. On the **Configure metric behaviors** page, choose one of the cloud-side metric dimensions under **Metric type**.
7. For **Metric behavior**, choose **Send an alert (define metric behavior)** to define the expected metric behavior.
8. Choose when you want to be notified for unusual device behavior.
9. Choose **Next**.
10. Review the security profile configuration and choose **Create**.

###### To view your alarms

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Detect**, and then choose **Alarms**.
2. In the **Thing name** column, choose the thing to see information about what caused the alarm.

###### To view and update your dimensions

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Detect**, and then choose **Dimensions**.
2. Select the dimension and choose **Edit**.
3. Edit the dimension and choose **Update**.

###### To delete a dimension

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Detect**, and then choose **Dimensions**.
2. Before deleting a dimension, you must delete the metric behavior that references the dimension. Confirm that the dimension isn’t attached to a security profile by checking the **Security Profiles** column. If the dimension is attached to a security profile, open the **Security profiles** page on the left, and edit the security profile that the dimension is attached to. Then you can proceed with deleting the behavior. If you want to delete another dimension, follow the steps in this section.
3. Select the dimension and choose **Delete**.
4. Enter the dimension name to confirm, and then choose
   **Delete**.

## How to use dimensions on the AWS CLI

###### To create and apply a dimension to a security profile behavior

1. First create the dimension before attaching it to a security profile. Use the [CreateDimension](../../../iot/latest/apireference/API_CreateDimension.md "../../../iot/latest/apireference/API_CreateDimension.md")
   command to create a dimension:

```
aws iot create-dimension \
  --name `TopicFilterForAuthMessages` \
  --type TOPIC_FILTER \
  --string-values `device/+/auth`
```

The output of this command looks like the following:

```
{
    "arn": "`arn:aws:iot:us-west-2:123456789012:dimension/TopicFilterForAuthMessages`",
    "name": "TopicFilterForAuthMessages"
}
```

2. Either add the dimension to an existing security profile by using [UpdateSecurityProfile](../../../iot/latest/apireference/API_UpdateSecurityProfile.md "../../../iot/latest/apireference/API_UpdateSecurityProfile.md"), or add the dimension to a new
   security profile by using [CreateSecurityProfile](../../../iot/latest/apireference/API_CreateSecurityProfile.md "../../../iot/latest/apireference/API_CreateSecurityProfile.md"). In the following example, we create
   a new security profile that checks if messages to `TopicFilterForAuthMessages`
   are under 128 bytes, and retains the number of messages sent to non-auth topics.

```
aws iot create-security-profile \
  --security-profile-name ProfileForConnectedDevice \
  --security-profile-description "Check to see if messages to TopicFilterForAuthMessages are under 128 bytes and retains the number of messages sent to non-auth topics." \
  --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":10},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]" \
  --additional-metrics-to-retain-v2 "[{\"metric\": \"aws:num-authorization-failures\",\"metricDimension\": {\"dimensionName\": \"TopicFilterForAuthMessages\",\"operator\": \"NOT_IN\"}}]"
```

The output of this command looks like the following:

```
{
    "securityProfileArn": "`arn:aws:iot:us-west-2:1234564789012:securityprofile/ProfileForConnectedDevice`",
    "securityProfileName": "ProfileForConnectedDevice"
}
```

To save time, you can also load a parameter from a file instead of typing it as a
command line parameter value. For more information, see [Loading AWS CLI Parameters
from a File](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md"). The following shows the `behavior` parameter in expanded
JSON format:

```
[
  {
    "criteria": {
      "comparisonOperator": "less-than",
      "consecutiveDatapointsToAlarm": 1,
      "consecutiveDatapointsToClear": 1,
      "value": {
        "count": 128
      }
    },
    "metric": "aws:message-byte-size",
    "metricDimension": {
      "dimensionName:": "TopicFilterForAuthMessages"
    },
    "name": "CellularBandwidth"
  }
]
```

Or use [CreateSecurityProfile](../../../iot/latest/apireference/API_CreateSecurityProfile.md "../../../iot/latest/apireference/API_CreateSecurityProfile.md") using dimension with ML like the following example:

```
aws iot create-security-profile --security-profile-name ProfileForConnectedDeviceML \
   --security-profile-description “Check to see if messages to TopicFilterForAuthMessages are abnormal”  \
   --behaviors “[{\“name\“:\“test1\“,\“metric\“:\“aws:message-byte-size\“,\“metricDimension\“:{\“dimensionName\“: \“TopicFilterForAuthMessages\“,\“operator\“: \“IN\“},\“criteria\“:{\“mlDetectionConfig\“:{\“confidenceLevel\“:\“HIGH\“},\“consecutiveDatapointsToAlarm\“:1,\“consecutiveDatapointsToClear\“:1}}]” \
   --region us-west-2
```

###### To view security profiles with a dimension

- Use the [ListSecurityProfiles](../../../iot/latest/apireference/API_ListSecurityProfiles.md "../../../iot/latest/apireference/API_ListSecurityProfiles.md") command to view security profiles with
  a certain dimension:

```
aws iot list-security-profiles \
  --dimension-name `TopicFilterForAuthMessages`
```

The output of this command looks like the following:

```
{
    "securityProfileIdentifiers": [
        {
            "name": "ProfileForConnectedDevice",
            "arn": "`arn:aws:iot:us-west-2:1234564789012:securityprofile/ProfileForConnectedDevice`"
        }
    ]
}
```

###### To update your dimension

- Use the [UpdateDimension](../../../iot/latest/apireference/API_UpdateDimension.md "../../../iot/latest/apireference/API_UpdateDimension.md") command to update a dimension:

```
aws iot update-dimension \
  --name `TopicFilterForAuthMessages` \
  --string-values `device/${iot:ClientId}/auth`
```

The output of this command looks like the following:

```
{
    "name": "TopicFilterForAuthMessages",
    "lastModifiedDate": `1585866222.317`,
    "stringValues": [
        "device/${iot:ClientId}/auth"
    ],
    "creationDate": `1585854500.474`,
    "type": "TOPIC_FILTER",
    "arn": "`arn:aws:iot:us-west-2:1234564789012:dimension/TopicFilterForAuthMessages`"
}
```

###### To delete a dimension

1. To delete a dimension, first detach it from any security profiles that it's attached
   to. Use the [ListSecurityProfiles](../../../iot/latest/apireference/API_ListSecurityProfiles.md "../../../iot/latest/apireference/API_ListSecurityProfiles.md") command to view security profiles with
   a certain dimension.
2. To remove a dimension from a security profile, use the [UpdateSecurityProfile](../../../iot/latest/apireference/API_UpdateSecurityProfile.md "../../../iot/latest/apireference/API_UpdateSecurityProfile.md") command. Enter all information that
   you want to keep, but exclude the dimension:

```
aws iot update-security-profile \
  --security-profile-name ProfileForConnectedDevice \
  --security-profile-description "Check to see if authorization fails 10 times in 5 minutes or if cellular bandwidth exceeds 128" \
  --behaviors "[{\"name\":\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\comparisonOperator\":\"less-than\",\"value\"{\"count\":10},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"
```

The output of this command looks like the following:

```
{
  "behaviors": [
    {
      "metric": "aws:message-byte-size",
      "name": "CellularBandwidth",
      "criteria": {
        "consecutiveDatapointsToClear": 1,
        "comparisonOperator": "less-than",
        "consecutiveDatapointsToAlarm": 1,
        "value": {
          "count": 128
        }
      }
    },
    {
      "metric": "aws:num-authorization-failures",
      "name": "Authorization",
      "criteria": {
        "durationSeconds": 300,
        "comparisonOperator": "less-than",
        "consecutiveDatapointsToClear": 1,
        "consecutiveDatapointsToAlarm": 1,
        "value": {
          "count": 10
        }
      }
    }
  ],
  "securityProfileName": "ProfileForConnectedDevice",
  "lastModifiedDate": 1585936349.12,
  "securityProfileDescription": "Check to see if authorization fails 10 times in 5 minutes or if cellular bandwidth exceeds 128",
  "version": 2,
  "securityProfileArn": "arn:aws:iot:us-west-2:123456789012:securityprofile/Preo/ProfileForConnectedDevice",
  "creationDate": 1585846909.127
}
```

3. After the dimension is detached, use the [DeleteDimension](../../../iot/latest/apireference/API_DeleteDimension.md "../../../iot/latest/apireference/API_DeleteDimension.md") command to delete the dimension:

```
aws iot delete-dimension \
  --name `TopicFilterForAuthMessages`
```
