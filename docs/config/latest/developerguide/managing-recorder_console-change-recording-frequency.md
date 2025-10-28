# Changing the recording

frequency for the customer managed configuration recorder

AWS Config supports continuous recording and daily recording:

- _Continuous recording_ allows you to record configuration changes
  continuously whenever a change occurs.
- _Daily recording_ allows you to receive a configuration item (CI)
  representing the most recent state of your resources over the last 24-hour period, only if
  it’s different from the previous CI recorded. For more information see, [Recording
  Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").
  You can use the AWS Config console or the AWS CLI change the recording frequency.

To change the recording frequency for the customer managed configuration recorder
(Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the navigation pane.
3. On the **Customer managed recorder** tab, choose
   **Start recording**.
4. For **Recording method managed recorder**, choose **All
   resource types with customizable overrides**.
5. For **Default settings**, choose a recording frequency.
6. Choose **Save**.

To change the recording frequency (CLI)
Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command to change the recording
frequency for the configuration recorder:

```
$ **aws configservice put-configuration-recorder \
--configuration-recorder `file://configurationRecorder.json`**
```

The `configurationRecorder.json` file specifies `name`
and `roleArn` as well as the default recording frequency for the
configuration recorder (`recordingMode`). You can also use this field
override the recording frequency for specific resource types.

```
`{
 "name": "default",
 "roleARN": "`arn:aws:iam::123456789012:role/config-role`",
 "recordingMode": {
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "recordingModeOverrides": [
 {
 "description": "`Description you provide for the override`",
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "resourceTypes": [ `Comma-separated list of resource types to include in the override` ]
 }
 ]
 }
}`
```

[`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") uses the following fields for the
`--configuration-recorder` parameter:

- `name` – The name of the configuration recorder. AWS Config
  automatically assigns the name of "default" when creating the configuration
  recorder.
- `roleARN` – Amazon Resource Name (ARN) of the IAM role assumed
  by AWS Config and used by the configuration recorder.
- `recordingMode` – Specifies the default recording frequency
  that AWS Config uses to record configuration changes. AWS Config supports _Continuous
  recording_ and _Daily recording_. Continuous
  recording allows you to record configuration changes continuously whenever a change
  occurs. Daily recording allows you to receive a configuration item (CI) representing
  the most recent state of your resources over the last 24-hour period, only if it’s
  different from the previous CI recorded.
  - `recordingFrequency` – The default recording frequency
    that AWS Config uses to record configuration changes.

  ###### Note

  AWS Firewall Manager depends on continuous recording to monitor your resources. If
  you are using Firewall Manager, it is recommended that you set the recording frequency to
  Continuous.
  - `recordingModeOverrides` – This field allows you to
    specify your overrides for the recording mode. It is an array of
    `recordingModeOverride` objects. Each
    `recordingModeOverride` object in the
    `recordingModeOverrides` array consists of three fields:
    - `description` – A description that you provide for the
      override.
    - `recordingFrequency` – The recording frequency that
      will be applied to all the resource types specified in the override.
    - `resourceTypes` – A comma-separated list that
      specifies which resource types AWS Config includes in the override.

###### Note

**Required and optional fields**

The `recordingMode` field for
[`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") is optional. By default, the recording
frequency for the configuration recorder is set to Continuous recording.

###### Note

**Limits**

Daily recording is not supported for the following resource types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`
  For the **Record all current and future supported resource
  types** (`ALL_SUPPORTED_RESOURCE_TYPES`) recording strategy,
  these resource types will be set to Continuous recording.
