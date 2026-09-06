

# Disabling content quality analysis for a flow
<a name="disable-content-quality-analysis-flows"></a>

## Prerequisites
<a name="disable-content-quality-analysis-flows-prerequisites"></a>

You must have already enabled content quality analysis for the flow.

## Procedure
<a name="disable-content-quality-analysis-flows-procedure"></a>

You can disable content quality analysis through the AWS Management Console, the AWS CLI, and the MediaConnect API.

------
#### [ Console ]

**To disable content quality analysis**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the **Flows** screen, select the flow for which you want to disable content quality analysis.

1. On the flow details page, choose the **Sources** tab.

1. In the **Source monitoring configuration **section, choose **Edit**.

1. In the **Content quality analysis** section, turn off the metrics you want to disable, or turn off all metrics by turning off **Content quality analysis state**.

1. Choose **Update **to save your changes.

------
#### [ AWS CLI ]

**To disable all metrics**  
Run the [update-flow](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/update-flow.html) command as shown in the following example:

```
aws mediaconnect update-flow \
  --flow-arn "{{flowARN}}" \
  --source-monitoring-config ContentQualityAnalysisState=DISABLED
```

In the following example response, `ContentQualityAnalysisState` is disabled, but individual metric settings remain unchanged:

```
{
    "Flow": {
        "FlowArn": "<arn>",
        ...
        "SourceMonitoringConfig": {
            "ContentQualityAnalysisState": "DISABLED",
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
                        "ThresholdSeconds": 10
                    }
                }
            ]
        }
    }
}
```

**To disable specific metrics**  
Run the [update-flow](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/update-flow.html) command with the `--source-monitoring-config` parameter configured as shown in the following example. This example disables the two video metrics while preserving custom thresholds for future use:

```
aws mediaconnect update-flow \
  --flow-arn "{{flowARN}}" \
  --source-monitoring-config '{"ContentQualityAnalysisState": "ENABLED",
    "VideoMonitoringSettings": [{
      "FrozenFrames": {"State": "DISABLED", "ThresholdSeconds": 10},
      "BlackFrames": {"State": "DISABLED", "ThresholdSeconds": 15}}],
    "AudioMonitoringSettings": [{
      "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": 25}}]}'
```

Note the following:
+ When `ContentQualityAnalysisState` is set to `DISABLED`, it takes precedence over individual metric settings. Individual metrics might show as `ENABLED`, but they are not active until you set `ContentQualityAnalysisState` back to `ENABLED`.
+ Your previously configured thresholds are preserved when you disable metrics. 

------