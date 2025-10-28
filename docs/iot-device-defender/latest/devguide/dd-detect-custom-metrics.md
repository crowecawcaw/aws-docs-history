# Custom metrics

With AWS IoT Device Defender custom metrics, you can define and monitor metrics that are unique to your
fleet or use case, such as number of devices connected to Wi-Fi gateways, charge levels for
batteries, or number of power cycles for smart plugs. Custom metric behaviors are defined in
Security Profiles, which specify expected behaviors for a group of devices (a thing group)
or for all devices. You can monitor behaviors by setting up alarms, which you can use to
detect and respond to issues that are specific to the devices.

###### This chapter contains the following sections:

- [How to use custom metrics in the console](#dd-detect-custom-metrics-how-to-console "#dd-detect-custom-metrics-how-to-console")
- [How to use custom metrics from the
  CLI](#dd-detect-custom-metrics-how-to-cli "#dd-detect-custom-metrics-how-to-cli")
- [Custom metrics CLI commands](#dd-detect-custom-metrics-cli-commands "#dd-detect-custom-metrics-cli-commands")
- [Custom metrics APIs](#dd-detect-custom-metrics-apis "#dd-detect-custom-metrics-apis")

## How to use custom metrics in the console

###### Tutorials

- [AWS IoT Device Defender Agent SDK (Python)](#dd-detect-custom-metrics-device-agent "#dd-detect-custom-metrics-device-agent")
- [Create a custom metric and add it to a
  Security Profile](#dd-detect-console-create "#dd-detect-console-create")
- [View custom metric details](#dd-detect-console-read "#dd-detect-console-read")
- [Update a custom metric](#dd-detect-console-edit "#dd-detect-console-edit")
- [Delete a custom metric](#dd-detect-console-delete "#dd-detect-console-delete")

### AWS IoT Device Defender Agent SDK (Python)

To get started, download the AWS IoT Device Defender Agent SDK (Python) sample agent. The agent
gathers the metrics and publishes reports. Once your device-side metrics are
publishing, you can view the metrics being collected and determine thresholds for
setting up alarms. Instructions for setting up the device agent are available on the
[AWS IoT Device Defender Agent SDK (Python) Readme](https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python/blob/master/README.rst "https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python/blob/master/README.rst"). For more information,
see [AWS IoT Device Defender Agent SDK (Python)](https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python "https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python").

### Create a custom metric and add it to a

Security Profile

The following procedure shows you how to create a custom metric in the
console.

1.  In the [AWS IoT
    console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"), in the navigation pane, expand
    **Defend**, and then choose
    **Detect**, **Metrics**.
2.  On the **Custom metrics** page, choose
    **Create**.
3.  On the **Create custom metric** page, do the
    following.

        1. Under **Name**, enter a name for your custom
         metric. You can't modify this name after you create the custom
         metric.
        2. Under **Display name (optional)**, you can enter
         a friendly name for your custom metric. It doesn't have to be unique
         and it can be modified after creation.
        3. Under **Type**, choose the type of metric you'd
         like to monitor. Metric types include
         **string-list**,
         **ip-address-list**,
         **number-list**, and
         **number**. The type can't be modified after
         creation.


        ###### Note

        ML Detect only allows the **number** type.
        4. Under **Tags**, you can select tags to be
         associated with the resource.

    When you're done, choose **Confirm**.

4.  After you've created your custom metric, the **Custom
    metrics** page appears, where you can see your newly created
    custom metric.
5.  Next, you need to add your custom metric to a Security Profile. In the
    [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"),
    in the navigation pane, expand **Defend**, and then choose
    **Detect**, **Security
    profiles**.
6.  Choose the Security Profile you'd like to add your custom metric
    to.
7.  Choose **Actions**, **Edit**.
8.  Choose **Additional Metrics to retain**, and then choose
    your custom metric. Choose **Next** on the following
    screens until you reach the **Confirm** page. Choose
    **Save** and **Continue**. After
    your custom metric has been successfully added, the Security Profile details
    page appears.

###### Note

Percentile statistics are not available for metrics when any of the
metric values are negative numbers.

### View custom metric details

The following procedure shows you how to view a custom metric's details in the
console.

1. In the [AWS IoT
   console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"), in the navigation pane, expand
   **Defend**, and then choose
   **Detect**, **Metrics**.
2. Choose the **Metric name** of the custom metric you'd
   like to view the details of.

### Update a custom metric

The following procedure shows you how to update a custom metric in the
console.

1. In the [AWS IoT
   console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"), in the navigation pane, expand
   **Defend**, and then choose
   **Detect**, **Metrics**.
2. Choose the option button next to the custom metric you'd like to update.
   Then, for **Actions**, choose
   **Edit**.
3. On the **Update custom metric** page, you can edit the
   display name and remove or add tags.
4. After you're done, choose **Update**. The
   **Custom metrics** page.

### Delete a custom metric

The following procedure shows you how to delete a custom metric in the
console.

1. First, remove your custom metric from any Security Profile it's referenced
   in. You can view which Security Profiles contain your custom metric on your
   custom metric details page. In the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"), in the
   navigation pane, expand **Defend**, and then choose
   **Detect**, **Metrics**.
2. Choose the custom metric you'd like to remove. Remove the custom metric
   from any Security Profile listed under **Security
   Profiles** on the custom metric details page.
3. In the [AWS IoT
   console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"), in the navigation pane, expand
   **Defend**, and then choose
   **Detect**, **Metrics**.
4. Choose the option button next to the custom metric you'd like to delete.
   Then, for **Actions**, choose
   **Delete**.
5. On the **Are you sure you want to delete custom metric?**
   message, choose **Delete custom metric**.

###### Warning

After you've deleted a custom metric, you lose all data associated
with the metric. This action can't be undone.

## How to use custom metrics from the

CLI

###### Tutorials

- [AWS IoT Device Defender Agent SDK (Python)](#dd-detec-custom-metrics-cli-sdk "#dd-detec-custom-metrics-cli-sdk")
- [Create a custom metric and add it to a
  Security Profile](#dd-detect-custom-cli-create "#dd-detect-custom-cli-create")
- [View custom metric details](#dd-detect-custom-cli-read "#dd-detect-custom-cli-read")
- [Update a custom metric](#dd-detect-custom-cli-edit "#dd-detect-custom-cli-edit")
- [Delete a custom metric](#dd-detect-custom-cli-delete "#dd-detect-custom-cli-delete")

### AWS IoT Device Defender Agent SDK (Python)

To get started, download the AWS IoT Device Defender Agent SDK (Python) sample agent. The agent
gathers the metrics and publishes reports. After your device-side metrics are
publishing, you can view the metrics being collected and determine thresholds for
setting up alarms. Instructions for setting up the device agent are available on the
[AWS IoT Device Defender Agent SDK (Python) Readme](https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python/blob/master/README.rst "https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python/blob/master/README.rst"). For more information,
see [AWS IoT Device Defender Agent SDK (Python)](https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python "https://github.com/aws-samples/aws-iot-device-defender-agent-sdk-python").

### Create a custom metric and add it to a

Security Profile

The following procedure shows you how to create a custom metric and add it to a
Security Profile from the CLI.

1. Use the `create-custom-metric` command to create your custom
   metric. The following example creates a custom metric that measures battery
   percentage.

```
aws iot create-custom-metric \
    --metric-name "`batteryPercentage`" \
    --metric-type "`number`" \
    --display-name "`Remaining battery percentage.`" \
    --region `us-east-1`
    --client-request-token "`02ccb92b-33e8-4dfa-a0c1-35b181ed26b0`" \
```

Output:

```
{
    "metricName": "`batteryPercentage`",
    "metricArn": "arn:aws:iot:`us-east-1`:`1234564789012`:custommetric/`batteryPercentage`"
}

```

2. After you've created your custom metric, you can either add the custom
   metric to an existing profile using `update-security-profile` or create a new security
   profile to add the custom metric to using `create-security-profile`. Here, we create a new
   security profile called `batteryUsage` to add our
   new `batteryPercentage` custom metric to. We also
   add a Rules Detect metric called
   `cellularBandwidth`.

```
aws iot create-security-profile \
    --security-profile-name `batteryUsage` \
    --security-profile-description "`Shows how much battery is left in percentile.`"  \
    --behaviors "[{\"name\":\"great-than-75\",\"metric\":\"`batteryPercentage`\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"number\":75},\"consecutiveDatapointsToAlarm\":5,\"consecutiveDatapointsToClear\":1}},{\"name\":\"`cellularBandwidth`\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]" \
    --region `us-east-1`
```

Output:

```
{
    "securityProfileArn": "`arn:aws:iot:us-east-1:1234564789012:securityprofile/batteryUsage`",
    "securityProfileName": "`batteryUsage`"
}
```

###### Note

Percentile statistics are not available for metrics when any of the metric
values are negative numbers.

### View custom metric details

The following procedure shows you how to view the details for a custom metric from
the CLI.

- Use the `list-custom-metrics` command to view all of your
  custom metrics.

```
aws iot list-custom-metrics \
    --region `us-east-1`
```

The output of this command looks like the following.

```
{
    "metricNames": [
        "`batteryPercentage`"
    ]
}

```

### Update a custom metric

The following procedure shows you how to update a custom metric from the
CLI.

- Use the `update-custom-metric` command to update a custom
  metric. The following example updates the `display-name`.

```
aws iot update-custom-metric \
    --metric-name `batteryPercentage` \
    --display-name '`remaining battery percentage on device`' \
    --region `us-east-1`
```

The output of this command looks like the following.

```
{
    "metricName": "`batteryPercentage`",
    "metricArn": "arn:aws:iot:`us-east-1`:`1234564789012`:custommetric/`batteryPercentage`",
    "metricType": "number",
    "displayName": "`remaining battery percentage on device`",
    "creationDate": "2020-11-17T23:01:35.110000-08:00",
    "lastModifiedDate": "2020-11-17T23:02:12.879000-08:00"
}

```

### Delete a custom metric

The following procedure shows you how to delete a custom metric from the
CLI.

1. To delete a custom metric, first remove it from any Security Profiles that
   it's attached to. Use the `list-security-profiles` command to view Security
   Profiles with a certain custom metric.
2. To remove a custom metric from a Security Profile, use the `update-security-profiles` command. Enter all
   information that you want to keep, but exclude the custom metric.

```
aws iot update-security-profile \
  --security-profile-name `batteryUsage` \
  --behaviors "[{\"name\":\"`cellularBandwidth`\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"
```

The output of this command looks like the following.

```
{
  "behaviors": [{\"name\":\"`cellularBandwidth`\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}],
  "securityProfileName": "`batteryUsage`",
  "lastModifiedDate": 2020-11-17T23:02:12.879000-09:00,
  "securityProfileDescription": "`Shows how much battery is left in percentile.`",
  "version": 2,
  "securityProfileArn": "`arn:aws:iot:us-east-1:1234564789012:securityprofile/batteryUsage`",
  "creationDate": 2020-11-17T23:02:12.879000-09:00
}
```

3. After the custom metric is detached, use the `delete-custom-metric` command to delete the custom
   metric.

```
aws iot delete-custom-metric  \
  --metric-name `batteryPercentage` \
  --region `us-east-1`
```

The output of this command looks like the following

```
HTTP 200
```

## Custom metrics CLI commands

You can use the following CLI commands to create and manage custom metrics.

- [create-custom-metric](../../../cli/latest/reference/iot/create-custom-metric.md "../../../cli/latest/reference/iot/create-custom-metric.md")
- [describe-custom-metric](../../../cli/latest/reference/iot/describe-custom-metric.md "../../../cli/latest/reference/iot/describe-custom-metric.md")
- [list-custom-metrics](../../../cli/latest/reference/iot/list-custom-metrics.md "../../../cli/latest/reference/iot/list-custom-metrics.md")
- [update-custom-metric](../../../cli/latest/reference/iot/update-custom-metric.md "../../../cli/latest/reference/iot/update-custom-metric.md")
- [delete-custom-metric](../../../cli/latest/reference/iot/delete-custom-metric.md "../../../cli/latest/reference/iot/delete-custom-metric.md")
- [list-security-profiles](../../../cli/latest/reference/iot/list-security-profiles.md "../../../cli/latest/reference/iot/list-security-profiles.md")

## Custom metrics APIs

The following APIs can be used to create and manage custom metrics.

- [CreateCustomMetric](../../../iot/latest/apireference/API_CreateCustomMetric.md "../../../iot/latest/apireference/API_CreateCustomMetric.md")
- [DescribeCustomMetric](../../../iot/latest/apireference/API_DescribeCustomMetric.md "../../../iot/latest/apireference/API_DescribeCustomMetric.md")
- [ListCustomMetrics](../../../iot/latest/apireference/API_ListCustomMetrics.md "../../../iot/latest/apireference/API_ListCustomMetrics.md")
- [UpdateCustomMetric](../../../iot/latest/apireference/API_UpdateCustomMetric.md "../../../iot/latest/apireference/API_UpdateCustomMetric.md")
- [DeleteCustomMetric](../../../iot/latest/apireference/API_DeleteCustomMetric.md "../../../iot/latest/apireference/API_DeleteCustomMetric.md")
- [ListSecurityProfiles](../../../iot/latest/apireference/API_ListSecurityProfiles.md "../../../iot/latest/apireference/API_ListSecurityProfiles.md")
