# Enabling content quality analysis

and configuring thresholds

You enable content quality analysis for each flow in MediaConnect individually.
You can do this when you create a new flow, or when you update an existing one. For
each flow, you can customize the monitoring experience by configuring thresholds for
individual metrics or disabling specific metrics as needed.

This page guides you through the process of enabling content quality analysis and
configuring its metrics.

## Prerequisites

If you want to enable content quality analysis for an existing
flow, ensure that the flow state is `STANDBY`,
`UPDATING`, or `ACTIVE` before you
start.

## Procedure

You can enable content quality analysis through the AWS Management
Console, the AWS CLI, and the MediaConnect API.

Console

###### To enable content quality analysis when you create a

flow

Follow the instructions for [Creating a flow](flows-create.md "flows-create.md"). In the **Source monitoring
configuration** step, make sure to turn on
**Content quality analysis state.**

When you enable content quality analysis, you can specify
a threshold for the following metrics. For each metric,
you can populate a value between 10 and 60 seconds. The
default threshold is 30 seconds.

| Monitoring type | Metric                                                       | Description                                                                                                                                              | Use case                                                                                                                                           |
| --------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Video           | Black frames                                                 | Detects periods of black video frames in<br>the stream.                                                                                                  | Useful for identifying complete video loss<br>during live events. Helps pinpoint camera failures<br>or transmission interruptions in<br>real-time. |
| Frozen frames   | Detects periods of unchanging video frames<br>in the stream. | Useful for detecting when live video feed<br>stalls or buffers. Helps monitor stream continuity<br>and identify potential network or encoding<br>issues. |
| Audio           | Silent audio                                                 | Detects periods of audio silence in the<br>stream.                                                                                                       | Useful for recognizing audio dropouts in<br>live broadcasts. Helps identify microphone<br>failures or audio mixing problems during<br>streaming.   |

AWS CLI

###### To enable content quality analysis with default

settings

Run the [create-flow](../../../cli/latest/reference/mediaconnect/create-flow.md "../../../cli/latest/reference/mediaconnect/create-flow.md") command as shown in the
following example:

```
aws mediaconnect create-flow
  --flow-name "myFlow" \
  --source-arn "sourceFlowARN" \
  --source-monitoring-config ContentQualityAnalysisState=ENABLED \
  --other-required-parameters
```

MediaConnect automatically enables all individual
metrics with a default value of 30 seconds, as shown
below:

```
{
   "Flow": {
              "FlowArn": <arn>,
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

###### To enable content quality analysis with custom

thresholds

Run the [create-flow](../../../cli/latest/reference/mediaconnect/create-flow.md "../../../cli/latest/reference/mediaconnect/create-flow.md") command with the
`--source-monitoring-config` parameter
configured as shown below.

The following example command enables all three metrics
with custom thresholds:

```
aws mediaconnect create-flow
  --flow-name "myFlow" \
  --source-arn "sourceFlowARN" \
  --source-monitoring-config '{"ContentQualityAnalysisState": "ENABLED", \
   "VideoMonitoringSettings": [{ \
   "FrozenFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`}, \
   "BlackFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}], \
   "AudioMonitoringSettings": [{ \
   "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}]}'
```

Keep in mind the following:

- For each threshold, replace
  `<int>` with a value
  between 10 and 60 seconds.
- If you don't specify a threshold, the default
  value of 30 seconds is used.
- You can enable one or more of the following
  metrics.
  - If you enable video monitoring, you must
    enable at least one of the
    `BlackFrames` or
    `FrozenFrames` metrics.
  - If you enable audio monitoring, you must
    enable the `SilentAudio` metric.

| Monitoring settings type  | Metric                                                       | Description                                                                                                                                              | Use case                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VideoMonitoringSettings` | `BlackFrames`                                                | Detects periods of black video frames in<br>the stream.                                                                                                  | Useful for identifying complete video loss<br>during live events. Helps pinpoint camera failures<br>or transmission interruptions in<br>real-time. |
| `FrozenFrames`            | Detects periods of unchanging video frames<br>in the stream. | Useful for detecting when live video feed<br>stalls or buffers. Helps monitor stream continuity<br>and identify potential network or encoding<br>issues. |
| `AudioMonitoringSettings` | `SilentAudio`                                                | Detects periods of audio silence in the<br>stream.                                                                                                       | Useful for recognizing audio dropouts in<br>live broadcasts. Helps identify microphone<br>failures or audio mixing problems during<br>streaming.   |

Console

###### To enable content quality analysis in an existing

flow

Follow the instructions for [Updating a flow](flows-update.md "flows-update.md"). In the
**Source monitoring
configuration** step, make sure to turn
on **Content quality analysis state.**

When you enable content quality analysis, you can
specify a threshold for the following metrics. For each
metric, you can populate a value between 10 and 60
seconds. The default threshold is 30 seconds.

| Monitoring type | Metric                                                       | Description                                                                                                                                              | Use case                                                                                                                                           |
| --------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Video           | Black frames                                                 | Detects periods of black video frames in<br>the stream.                                                                                                  | Useful for identifying complete video loss<br>during live events. Helps pinpoint camera failures<br>or transmission interruptions in<br>real-time. |
| Frozen frames   | Detects periods of unchanging video frames<br>in the stream. | Useful for detecting when live video feed<br>stalls or buffers. Helps monitor stream continuity<br>and identify potential network or encoding<br>issues. |
| Audio           | Silent audio                                                 | Detects periods of audio silence in the<br>stream.                                                                                                       | Useful for recognizing audio dropouts in<br>live broadcasts. Helps identify microphone<br>failures or audio mixing problems during<br>streaming.   |

AWS CLI

###### To enable content quality analysis with default

settings

Run the [update-flow](../../../cli/latest/reference/mediaconnect/update-flow.md "../../../cli/latest/reference/mediaconnect/update-flow.md") command as shown in the
following example:

```
aws mediaconnect update-flow
  --flow-arn "FlowArn" \
  --source-monitoring-config ContentQualityAnalysisState=ENABLED
```

MediaConnect automatically enables all individual
metrics with a default value of 30 seconds, as shown
below:

```
{
   "Flow": {
              "FlowArn": <arn>,
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

###### To enable content quality analysis with custom

thresholds

Run the [update-flow](../../../cli/latest/reference/mediaconnect/update-flow.md "../../../cli/latest/reference/mediaconnect/update-flow.md") command with the
`--source-monitoring-config` parameter
configured as shown below.

This example command enables all three metrics with
custom thresholds.

```
aws mediaconnect update-flow \
 --flow-arn "FlowArn" \
  --source-monitoring-config '{"ContentQualityAnalysisState": "ENABLED", \
   "VideoMonitoringSettings": [{ \
   "FrozenFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`}, \
   "BlackFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}], \
   "AudioMonitoringSettings": [{
   "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": `<int>`}}]}' \
```

Keep in mind the following:

- For each threshold, replace
  `<int>` with a value
  between 10 and 60 seconds.
- If you're enabling a metric for the first time
  and you don't specify a threshold, the default
  value of 30 seconds is used.
- If you're updating a previously enabled metric and
  you don't specify a threshold, the previously set
  value is retained.
- You can enable one or more of the following
  metrics.
  - If you enable video monitoring, you must
    enable at least one of the
    `BlackFrames` or
    `FrozenFrames` metrics.
  - If you enable audio monitoring, you must
    enable the `SilentAudio` metric.

| Monitoring settings type  | Metric                                                       | Description                                                                                                                                              | Use case                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VideoMonitoringSettings` | `BlackFrames`                                                | Detects periods of black video frames in<br>the stream.                                                                                                  | Useful for identifying complete video loss<br>during live events. Helps pinpoint camera failures<br>or transmission interruptions in<br>real-time. |
| `FrozenFrames`            | Detects periods of unchanging video frames<br>in the stream. | Useful for detecting when live video feed<br>stalls or buffers. Helps monitor stream continuity<br>and identify potential network or encoding<br>issues. |
| `AudioMonitoringSettings` | `SilentAudio`                                                | Detects periods of audio silence in the<br>stream.                                                                                                       | Useful for recognizing audio dropouts in<br>live broadcasts. Helps identify microphone<br>failures or audio mixing problems during<br>streaming.   |

## Next steps

- After you enable content quality analysis for a flow, MediaConnect
  starts analyzing the source stream and reporting any detected issues.
  For instructions on how to review these issues, see [Viewing content quality analysis settings and alerts](content-quality-analysis-viewing.md "content-quality-analysis-viewing.md").
- If you no longer want to analyze content quality for your flow, you
  can disable the feature. For instructions, see [Disabling content quality analysis](disable-content-quality-analysis.md "disable-content-quality-analysis.md").

## Additional resources

- [Creating a flow](flows-create.md "flows-create.md")
- [Updating a flow](flows-update.md "flows-update.md")
- [Monitoring and tagging in AWS Elemental MediaConnect](monitor.md "monitor.md")
