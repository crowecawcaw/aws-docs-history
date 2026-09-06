

# Using audio filler to improve bot responsiveness
<a name="customizing-speech-audio-filler"></a>

Audio filler plays brief background audio, such as a light melody or soft keystrokes, during the pause between the end of a user's utterance and the start of the bot's response. This masks processing delays and keeps voice conversations feeling natural.

**Note**  
At launch, audio filler is available for bot locales that support speech-to-speech interactions and have `unifiedSpeechSettings` configured. Support for additional conversation modes will roll out over the next several months.

## Available audio filler types
<a name="audio-filler-types"></a>

Amazon Lex V2 provides seven built-in filler sounds, organized into two families:
+ Melody - Chipper Chime
+ Melody - Curious Crawl
+ Melody - Rising Ripple
+ Melody - Patient Ping
+ Melody - Pondering Pong
+ Typing - Kinetic Keys
+ Typing - Quiet Qwerty

Use the **Play audio preview** button in the Amazon Lex V2 console to hear each option before you save it to a bot locale.

## Timing parameters
<a name="audio-filler-timing"></a>

You can tune three timing parameters to control when audio filler plays and how it transitions into the bot response:

`startDelayInMilliseconds`  
Time to wait after the end of the user's utterance before starting audio filler playback. Valid range is `500` to `5000` milliseconds. Default is `1000`.

`minimumPlayDurationInMilliseconds`  
Minimum time audio filler plays after it has started, even if the bot response becomes ready sooner. Valid range is `1000` to `5000` milliseconds. Default is `3000`.

`responseDeliveryDelayInMilliseconds`  
Silent delay inserted between the end of audio filler playback and the start of the bot's response. Valid range is `200` to `1000` milliseconds. Default is `500`.

## Configuring audio filler
<a name="configuring-audio-filler"></a>

You can configure audio filler when creating or updating a bot locale through the Amazon Lex V2 console, the Amazon Connect Conversational AI designer, or the AWS CLI and SDKs.

------
#### [ Using the console ]

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/](https://console.aws.amazon.com/lexv2/).

1. Choose your bot from the list.

1. In the left navigation pane, choose **Bot languages**.

1. Choose the language you want to configure, or choose **Add language** to add a new one.

1. In the **Audio Filler** section, choose **Enable audio filler**.

1. Choose an **Audio type** from the melody or typing options. Use **Play audio preview** to hear the selected filler.

1. Adjust the timing sliders for **Start delay**, **Minimum play duration**, and **Response buffer** as needed.

1. Choose **Save** to apply the changes.

------
#### [ Using the Amazon Connect Conversational AI designer ]

1. Open the Amazon Connect admin website and navigate to the Conversational AI designer for your bot.

1. Open the language (locale) you want to configure.

1. In the **Audio Filler** section, enable audio filler and choose an audio type.

1. Adjust the **Start delay**, **Minimum play duration**, and **Response buffer** values.

1. Save your changes. The designer applies the same `audioFillerSettings` to the underlying Amazon Lex V2 bot locale.

------
#### [ Using the API ]

You can set audio filler using the `audioFillerSettings` parameter in the following API operations:
+ `CreateBotLocale` - Configure audio filler for a new bot locale.
+ `UpdateBotLocale` - Modify audio filler for an existing bot locale.
+ `DescribeBotLocale` - View the current audio filler configuration.

**Example Configure audio filler using the AWS CLI**  

```
aws lexv2-models update-bot-locale \
    --bot-id "bot-1234567890abcdef0" \
    --bot-version "DRAFT" \
    --locale-id "en_US" \
    --nlu-intent-confidence-threshold 0.40 \
    --audio-filler-settings '{
        "enabled": true,
        "audioType": "MELODY_CHIPPER_CHIME",
        "startDelayInMilliseconds": 1000,
        "minimumPlayDurationInMilliseconds": 3000,
        "responseDeliveryDelayInMilliseconds": 500
    }'
```

------

## Audio filler with AI agent interim messages
<a name="audio-filler-interim-messages"></a>

Audio filler works alongside AI agent interim messages. When an AI agent sends an interim message to the caller (for example, "Let me look that up for you"), the start delay timer is measured from the end of that interim message rather than from the original invocation. This prevents audio filler from overlapping with the agent's speech and ensures the delay the caller experiences is measured from the most recent audio they heard.

## Audio filler with dialog and fulfillment code hooks
<a name="audio-filler-dialog-code-hooks"></a>

Audio filler also plays during the processing gap introduced by Lambda dialog code hooks and fulfillment code hooks. The same timing parameters apply, so callers hear a consistent experience whether your bot delegates processing to an AI agent, a code hook, or both in the same turn.

## Best practices for audio filler
<a name="audio-filler-best-practices"></a>
+ Match the filler to your brand voice. Use melody fillers for consumer or retail experiences, and typing fillers when users expect the bot to be actively working on a task.
+ Tune the start delay to your latency profile. If most bot responses are faster than `startDelayInMilliseconds`, the filler will rarely play. Lower the delay for latency-heavy workloads and raise it for fast-responding bots.
+ Keep the minimum play duration short for fast bots. A long `minimumPlayDurationInMilliseconds` on a fast bot adds perceived latency by holding the filler after the response is ready.
+ Test with representative traffic. Validate the filler choice and timing in realistic conversations before rolling out to production.