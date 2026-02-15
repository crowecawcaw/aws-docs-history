# Configuring voice activity detection sensitivity

Voice Activity Detection (VAD) is a technology that determines when speech is present in an audio signal. Amazon Lex V2 uses VAD to optimize speech recognition accuracy by distinguishing between actual speech and background noise. You can configure the VAD sensitivity level to improve your bot's performance in different acoustic environments.

## Understanding VAD sensitivity levels

Amazon Lex V2 provides three VAD sensitivity levels that you can configure for your bot locale:

Default

The standard sensitivity level suitable for most environments with typical background noise levels. This is the recommended setting for general use cases.

HighNoiseTolerance

Increased tolerance for moderate background noise. Use this setting when your bot operates in environments with consistent but moderate noise levels, such as busy offices or retail environments.

MaximumNoiseTolerance

Maximum tolerance for high levels of background noise. Use this setting for very noisy environments such as call centers, manufacturing floors, or outdoor locations with significant ambient noise.

###### Note

Higher noise tolerance levels may result in the system being more permissive about what it considers speech, which could potentially lead to false negatives in very quiet environments. Choose the sensitivity level that best matches your expected acoustic environment.

## Configuring VAD sensitivity

You can configure VAD sensitivity when creating or updating a bot locale using the Amazon Lex V2 console, AWS CLI, or SDKs.

### Using the Amazon Lex V2 console

###### To configure VAD sensitivity in the console

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/](https://console.aws.amazon.com/lexv2/ "https://console.aws.amazon.com/lexv2/").
2. Choose your bot from the list.
3. In the left navigation pane, choose **Bot languages**.
4. Choose the language you want to configure, or choose **Add language** to add a new one.
5. In the **Speech detection sensitivity** section, choose one of the following options:
   - **Default** - Standard sensitivity for typical environments
   - **High noise tolerance** - For moderately noisy environments
   - **Maximum noise tolerance** - For very noisy environments

6. Choose **Save** to apply the changes.

### Using the AWS CLI or SDKs

You can set the VAD sensitivity using the `speechDetectionSensitivity` parameter in the following API operations:

- `CreateBotLocale` - Set VAD sensitivity when creating a new bot locale
- `UpdateBotLocale` - Modify VAD sensitivity for an existing bot locale
- `DescribeBotLocale` - View the current VAD sensitivity setting

###### Example Setting VAD sensitivity with AWS CLI

```

aws lexv2-models create-bot-locale \
    --bot-id "AIDACKCEVSQ6C2EXAMPLE" \
    --bot-version "DRAFT" \
    --locale-id "en_US" \
    --nlu-intent-confidence-threshold 0.40 \
    --speech-detection-sensitivity "HighNoiseTolerance"

```

## Best practices for VAD configuration

- **Test in your target environment** - Configure VAD sensitivity based on the actual acoustic conditions where your bot will be deployed.
- **Start with Default** - Begin with the Default setting and adjust based on performance testing and user feedback.
- **Monitor performance** - Use Amazon Lex V2 analytics and conversation logs to monitor speech recognition accuracy and adjust VAD sensitivity as needed.
- **Consider use case** - Higher sensitivity levels are beneficial for noisy environments but may not be necessary for controlled environments like customer service centers with headsets.
