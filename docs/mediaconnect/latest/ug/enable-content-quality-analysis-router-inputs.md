# Enabling content quality analysis for a router input

You can enable content quality analysis when you create a new router input or
update an existing one.

## Procedure

You can enable content quality analysis through the AWS Management Console,
the AWS CLI, and the MediaConnect API.

Console

###### To enable content quality analysis when you create a router input

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose
   **Router inputs**.
3. Choose
   **Create router input**.
4. In the **Content quality analysis**
   section, turn on each metric you want to enable and
   specify a threshold value between 10 and 60
   seconds.
5. Complete the remaining fields and choose
   **Create router input**.

###### To enable content quality analysis for an existing router input

1. Open the AWS Elemental MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose
   **Router inputs**.
3. Select the router input that you want to update and
   choose **Edit**.
4. In the **Content quality analysis**
   section, turn on each metric you want to enable and
   specify a threshold value between 10 and 60
   seconds.
5. Choose **Save changes**.

AWS CLI

###### To enable content quality analysis for a router input

Run the [update-router-input](../../../cli/latest/reference/mediaconnect/update-router-input.md "../../../cli/latest/reference/mediaconnect/update-router-input.md") command with the
`--content-quality-analysis-configuration`
parameter:

```
aws mediaconnect update-router-input \
  --arn "`routerInputARN`" \
  --content-quality-analysis-configuration '{
    "ContentLevel": {
      "BlackFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`},
      "FrozenFrames": {"State": "ENABLED", "ThresholdSeconds": `<int>`},
      "SilentAudio": {"State": "ENABLED", "ThresholdSeconds": `<int>`}
    }
  }'
```

Note the following:

- For each threshold, replace
  `<int>` with a value
  between 10 and 60 seconds.
- If you don't specify a threshold, the default value
  of 30 seconds is used.
- Only include the metrics you want to enable.

###### Note

You can also enable content quality analysis when
you create a new router input by including the
`--content-quality-analysis-configuration`
parameter in the [create-router-input](../../../cli/latest/reference/mediaconnect/create-router-input.md "../../../cli/latest/reference/mediaconnect/create-router-input.md") command.
