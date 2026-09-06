

# Viewing content quality analysis for a router input
<a name="content-quality-analysis-viewing-router-inputs"></a>

## Prerequisites
<a name="content-quality-analysis-viewing-router-inputs-prerequisites"></a>

You must have already enabled content quality analysis for the router input.

## Procedure
<a name="content-quality-analysis-viewing-router-inputs-procedure"></a>

You can view content quality analysis status for router inputs through the AWS Management Console, the AWS CLI, and the MediaConnect API.

------
#### [ Console ]

**To check content quality analysis status for a router input**

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to inspect.

1. Choose the **Monitoring** tab. The **Input content health** section displays the real-time status of each content quality analysis metric.

The **Monitoring** tab shows the following indicators:
+ A dash (`-`) indicates that the metric is disabled.
+ **Currently detected** indicates that a quality issue is actively being detected.
+ **Recently detected** indicates that a quality issue was detected within the configured lookback period.
+ **None detected** indicates that a quality issue was not detected within the configured lookback period.

You can configure the lookback period using the dropdown list next to the refresh button. 

The **Router input messages** section displays any active content quality analysis alerts.

------
#### [ AWS CLI ]

To view content quality analysis settings and alerts for a router input, run the [get-router-input](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/get-router-input.html) command:

```
aws mediaconnect get-router-input --arn "{{routerInputARN}}"
```

The response shows the content quality analysis configuration and any active alerts:

```
{
    "RouterInput": {
        "Arn": "{{routerInputARN}}",
        ...
        "ContentQualityAnalysisConfiguration": {
            "ContentLevel": {
                "BlackFrames": {
                    "State": "ENABLED",
                    "ThresholdSeconds": 30
                },
                "FrozenFrames": {
                    "State": "ENABLED",
                    "ThresholdSeconds": 30
                },
                "SilentAudio": {
                    "State": "ENABLED",
                    "ThresholdSeconds": 30
                }
            }
        },
        ...
        "Messages": [
            {
                "Code": "MONITORING_STREAM_ALERT",
                "Message": "Black frames detected for more than 30 seconds."
            }
        ]
    }
}
```

------