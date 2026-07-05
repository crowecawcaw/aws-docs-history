# Enabling content quality analysis for a flow

You can enable content quality analysis when you create a new flow or update an
existing one.

## Procedure

You can enable content quality analysis through the AWS Management
Console, the AWS CLI, and the MediaConnect API.

Console

###### To enable content quality analysis when you create a flow

1. Follow the instructions for [Creating a flow](flows-create.md "flows-create.md").
2. In the **Source monitoring configuration** step, turn on
   **Content quality analysis state.**
3. For each metric you want to enable, change the state to **Enabled**
   and specify a threshold value between 10 and 60 seconds.

###### To enable content quality analysis in an existing flow

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the **Flows** screen,
   select the flow for which you want to enable content
   quality analysis.
3. On the flow details page, choose the **Sources** tab.
4. In the **Source monitoring
   configuration** section, choose **Edit**.
5. Turn on **Content quality analysis
   state**.
6. For each metric you want to enable, change the state to
   **Enabled** and specify a threshold value
   between 10 and 60 seconds.
7. Choose **Update** to save
   your changes.

AWS CLI

###### To enable with default settings

Run the [update-flow](../../../cli/latest/reference/mediaconnect/update-flow.md "../../../cli/latest/reference/mediaconnect/update-flow.md") command with the
`--source-monitoring-config` parameter as
shown in the following example:

```
aws mediaconnect update-flow \
  --flow-arn "`flowARN`" \
  --source-monitoring-config ContentQualityAnalysisState=ENABLED
```

MediaConnect automatically enables all individual metrics with
a default threshold of 30 seconds:

```
{
    "Flow": {
        "FlowArn": "<arn>",
        ...
        "SourceMonitoringConfig": {
            "ContentQualityAnalysisState": "ENABLED",
            "AudioMonitoringSettings": [
                {
                    "SilentAudio": {
                        "State": "ENABLED",
                        "ThresholdSeconds": 30
                    }
                }
            ],
            "VideoMonitoringSettings": [
                {
                    "BlackFrames": {
                        "State": "ENABLED",
                        "ThresholdSeconds": 30
                    },
                    "FrozenFrames": {
                        "State": "ENABLED",
                        "ThresholdSeconds": 30
                    }
                }
            ]
        }
    }
}
```

###### To enable with custom thresholds

Run the [update-flow](../../../cli/latest/reference/mediaconnect/update-flow.md "../../../cli/latest/reference/mediaconnect/update-flow.md") command with the
`--source-monitoring-config` parameter
configured as shown in the following example:

```
aws mediaconnect update-flow \
  --flow-arn "`flowARN`" \
  --source-monitoring-config '{"ContentQualityAnalysisState": "ENABLED",
    "VideoMonitoringSettings": [{
      "FrozenFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`},
      "BlackFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}],
    "AudioMonitoringSettings": [{
      "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}]}'
```

Note the following:

- For each threshold, replace
  `<int>` with a value
  between 10 and 60 seconds.
- If you don't specify a threshold, the default
  value of 30 seconds is used. If you're updating a
  previously enabled metric without specifying a
  threshold, the previously set value is
  retained.

###### Note

You can also enable content quality analysis when
you create a new flow by including the
`--source-monitoring-config` parameter in the
[create-flow](../../../cli/latest/reference/mediaconnect/create-flow.md "../../../cli/latest/reference/mediaconnect/create-flow.md") command.
