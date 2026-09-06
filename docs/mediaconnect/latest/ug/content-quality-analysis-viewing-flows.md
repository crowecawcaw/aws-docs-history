

# Viewing content quality analysis for a flow
<a name="content-quality-analysis-viewing-flows"></a>

## Prerequisites
<a name="content-quality-analysis-viewing-flows-prerequisites"></a>

You must have already enabled content quality analysis for the flow.

## Procedure
<a name="content-quality-analysis-viewing-flows-procedure"></a>

You can view content quality warnings and alerts through the AWS Management Console, the AWS CLI, and the MediaConnect API.

------
#### [ Console ]

**To check if content quality analysis is enabled**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the **Flows** screen, select the flow you want to inspect.

1. On the flow details page, choose the **Configuration** tab.

1. Under **Source monitoring configuration**, you can find the content quality analysis state.

**To check if quality alerts are present**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the **Flows** screen, select the flow you want to inspect.

1. On the **Alerts** tab, alerts appear when content quality problems are detected in the flow source.

------
#### [ AWS CLI ]

To confirm if quality analysis metrics are enabled for a given flow, run the [describe-flow](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/describe-flow.html) command:

```
aws mediaconnect describe-flow --flow-arn {{flowARN}}
```

The response shows which content quality analysis metrics are enabled:

```
{
    "Flow": {
        "FlowArn": "flowARN",
        ...
        "SourceMonitoringConfig": {
            "ContentQualityAnalysisState": "ENABLED",
            "AudioMonitoringSettings": [
                {
                    "SilentAudio": {
                        "State": "DISABLED",
                        "ThresholdSeconds": 15
                    }
                }
            ],
            "VideoMonitoringSettings": [
                {
                    "BlackFrames": {
                        "State": "DISABLED",
                        "ThresholdSeconds": 10
                    },
                    "FrozenFrames": {
                        "State": "ENABLED",
                        "ThresholdSeconds": 5
                    }
                }
            ]
        },
        ...
    }
}
```

The response also shows messages about any warnings or alerts that need your attention:

```
{
    ...
    "Messages": {
        "Errors": [
            "Monitoring Stream Alert: Audio Stream Missing. Please investigate the flow source.",
            "Monitoring Stream Alert: Video Stream Missing. Please investigate the flow source."
        ]
    }
}
```

Alternatively, if both audio and video streams are present but experiencing issues, you might see something like this:

```
{
    ...
    "Messages": {
        "Errors": [
            "Monitoring Stream Alert: Black frames detected for more than 30 seconds. Please investigate the flow source.",
            "Monitoring Stream Alert: Frozen frames detected for more than 30 seconds. Please investigate the flow source.",
            "Monitoring Stream Alert: Silent audio detected for more than 30 seconds. Please investigate the flow source."
        ]
}
```

**Note**  
These error messages are context-dependent. If an audio or video stream is missing, related quality alerts for that stream (such as silent audio or black/frozen frames) won't be triggered.

------