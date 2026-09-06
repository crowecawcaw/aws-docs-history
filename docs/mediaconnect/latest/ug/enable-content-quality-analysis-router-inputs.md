

# Enabling content quality analysis for a router input
<a name="enable-content-quality-analysis-router-inputs"></a>

You can enable content quality analysis when you create a new router input or update an existing one.

## Procedure
<a name="enable-content-quality-analysis-router-inputs-procedure"></a>

You can enable content quality analysis through the AWS Management Console, the AWS CLI, and the MediaConnect API.

------
#### [ Console ]

**To enable content quality analysis when you create a router input**

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Choose **Create router input**.

1. In the **Content quality analysis** section, turn on each metric you want to enable and specify a threshold value between 10 and 60 seconds.

1. Complete the remaining fields and choose **Create router input**.

**To enable content quality analysis for an existing router input**

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to update and choose **Edit**.

1. In the **Content quality analysis** section, turn on each metric you want to enable and specify a threshold value between 10 and 60 seconds.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To enable content quality analysis for a router input**  
Run the [update-router-input](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/update-router-input.html) command with the `--content-quality-analysis-configuration` parameter:

```
aws mediaconnect update-router-input \
  --arn "{{routerInputARN}}" \
  --content-quality-analysis-configuration '{
    "ContentLevel": {
      "BlackFrames": {"State": "ENABLED", "ThresholdSeconds": {{<int>}}},
      "FrozenFrames": {"State": "ENABLED", "ThresholdSeconds": {{<int>}}},
      "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": {{<int>}}}
    }
  }'
```

Note the following:
+ For each threshold, replace {{<int>}} with a value between 10 and 60 seconds.
+ If you don't specify a threshold, the default value of 30 seconds is used.
+ Only include the metrics you want to enable.

**Note**  
You can also enable content quality analysis when you create a new router input by including the `--content-quality-analysis-configuration` parameter in the [create-router-input](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/create-router-input.html) command.

------