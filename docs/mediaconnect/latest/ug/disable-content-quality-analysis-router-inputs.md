

# Disabling content quality analysis for a router input
<a name="disable-content-quality-analysis-router-inputs"></a>

## Prerequisites
<a name="disable-content-quality-analysis-router-inputs-prerequisites"></a>

You must have already enabled content quality analysis for the router input.

## Procedure
<a name="disable-content-quality-analysis-router-inputs-procedure"></a>

You can disable content quality analysis for a router input through the AWS Management Console, the AWS CLI, and the MediaConnect API.

------
#### [ Console ]

**To disable content quality analysis for a router input**

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to update and choose **Edit**.

1. In the **Content quality analysis** section, turn off the metrics you want to disable, or turn off all metrics.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To disable all metrics for a router input**  
Run the [update-router-input](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/update-router-input.html) command with all metrics set to `DISABLED`:

```
aws mediaconnect update-router-input \
  --arn "{{routerInputARN}}" \
  --content-quality-analysis-configuration '{
    "ContentLevel": {
      "BlackFrames": {"State": "DISABLED", "ThresholdSeconds": 30},
      "FrozenFrames": {"State": "DISABLED", "ThresholdSeconds": 30},
      "SilentAudio": {"State": "DISABLED", "ThresholdSeconds": 30}
    }
  }'
```

**To disable specific metrics for a router input**  
Run the [update-router-input](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/update-router-input.html) command and include all metrics. Set the metrics you want to disable to `DISABLED` and the metrics you want to keep to `ENABLED`. The following example disables video metrics while keeping audio monitoring active:

```
aws mediaconnect update-router-input \
  --arn "{{routerInputARN}}" \
  --content-quality-analysis-configuration '{
    "ContentLevel": {
      "BlackFrames": {"State": "DISABLED", "ThresholdSeconds": 30},
      "FrozenFrames": {"State": "DISABLED", "ThresholdSeconds": 30},
      "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": 30}
    }
  }'
```

------