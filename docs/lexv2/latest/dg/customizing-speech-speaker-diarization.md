

# Using speaker diarization to focus on the primary speaker
<a name="customizing-speech-speaker-diarization"></a>

Speaker diarization keeps your bot on the primary (loudest) speaker during a voice conversation. When other voices or background chatter reach the microphone, your bot stays focused on the primary speaker instead of reacting to the surrounding sound. Examples include a television in the next room, a side conversation in an open office, or someone talking near the caller. The result is smoother voice conversations, with fewer turns started by background voices and fewer prompts interrupted by them.

**Note**  
Speaker diarization applies to streaming voice conversations that use the [StartConversation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_StartConversation.html) operation, such as telephony calls. It requires 8 kHz single-channel (mono) audio. Amazon Lex V2 does not apply speaker diarization to text conversations, or to the non-streaming [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) and [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operations. For more information about the streaming API, see [Streaming conversations to an Amazon Lex V2 bot](streaming.md).  
Speaker diarization is available in all AWS Regions where Amazon Lex V2 is available. For the list of Regions, see [Amazon Lex V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lex.html) in the *Amazon Web Services General Reference*.

## How speaker diarization works
<a name="speaker-diarization-how-it-works"></a>

Amazon Lex V2 always uses voice activity detection (VAD) to determine when speech is present in the audio stream. VAD answers the question "is someone speaking?" but not "who is speaking?", so any nearby voice that is loud enough can start a turn. Speaker diarization is an optional setting that you turn on for a bot locale. It adds a second check on top of VAD, so that turns start and end based on the primary speaker's activity. For more information about VAD, see [Configuring voice activity detection sensitivity](customizing-speech-vad-sensitivity.md).

When you enable speaker diarization, Amazon Lex V2 adds a second signal to that decision:
+ **Speaker activity** - A streaming diarization model labels which speakers are active in each 100 millisecond frame of audio. It tracks up to four concurrent speakers.
+ **Primary speaker selection** - Amazon Lex V2 tracks the loudness of each detected speaker and treats the loudest one as the primary speaker. This approach assumes that the caller is closest to the microphone.
+ **Combined decision** - When diarization determines that a speaker other than the primary speaker is talking, Amazon Lex V2 treats that audio as non-speech. This audio does not start a turn, interrupt a prompt, or reach speech recognition. When the primary speaker is talking, and when diarization does not identify a distinct background speaker, Amazon Lex V2 uses the VAD decision. Diarization gates when speech capture starts and ends. It does not filter voices out of audio that Amazon Lex V2 has already captured.

The model distinguishes one speaker from another by voice characteristics rather than by what is said. It therefore works for all bot locales and languages.

Primary speaker changes  
The primary speaker does not change because of a brief loud sound. A different speaker becomes the primary speaker only after being the loudest tracked speaker, while actively speaking, for several consecutive frames. Coughs, door slams, and short exclamations do not take over the conversation.

Warm-up period  
The model needs approximately the first second of audio to establish speaker tracking. During that period, diarization does not suppress any speech, so the beginning of a caller's speech is never dropped while the model warms up.

Before the caller first speaks  
The primary speaker is the loudest speaker so far in the conversation. If a background speaker is the first voice the model tracks, that speaker becomes the primary speaker. The caller takes over after speaking long enough to become the loudest tracked speaker. Speaker diarization does not protect the conversation during this window. Loud background conversation can still start a turn or interrupt a prompt before the caller has spoken.

Automatic fallback  
Amazon Lex V2 monitors diarization throughout each conversation. If diarization begins filtering out nearly all of the speech that VAD detects, Amazon Lex V2 first resets the diarization state. If the condition persists, Amazon Lex V2 stops applying diarization for the rest of the current user turn and continues with VAD alone. Amazon Lex V2 re-enables diarization at the start of the next turn. A diarization problem never causes a conversation to fail or be dropped.

## What speaker diarization does not do
<a name="speaker-diarization-limitations"></a>
+ It does not identify who a speaker is. There is no enrollment, no speaker names, and no association with user accounts. The bot distinguishes only between the primary speaker and other speakers.
+ It does not separate the audio into per-speaker channels, and it does not return speaker labels in the transcript. The only effect is which audio Amazon Lex V2 treats as caller speech.
+ It does not remove overlapping background speech from audio captured while the primary speaker is talking. Speech that overlaps the primary speaker's turn is still transcribed. Diarization ends the capture as soon as the primary speaker stops.
+ It does not track speakers across conversations. Every conversation starts with no speaker history.
+ It is not used without VAD. Diarization refines the VAD decision instead of replacing it.
+ It does not apply to bots that use a generative AI agent or a custom inference endpoint.
+ Accuracy can decrease when more than four people speak at the same time.

## Configuring speaker diarization
<a name="configuring-speaker-diarization"></a>

Speaker diarization is a bot locale setting, so you can enable it for some languages of a bot and leave it turned off for others. You can configure it when creating or updating a bot locale through the Amazon Lex V2 console, or the AWS CLI and SDKs.

------
#### [ Using the console ]

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/](https://console.aws.amazon.com/lexv2/).

1. Choose your bot from the list.

1. In the left navigation pane, choose **Bot languages**.

1. Choose the language you want to configure, or choose **Add language** to add a new one.

1. In the **Speaker Diarization** section, choose **Configure**.

1. Turn on **Enable speaker diarization**.

1. Choose **Save** to apply the changes.

1. Build the language so that the change takes effect at runtime.

The language details page shows the current state of the setting as **Enabled** or **Disabled**.

------
#### [ Using the API ]

You can set speaker diarization using the `speakerDiarizationSettings` parameter in the following API operations:
+ `CreateBotLocale` - Configure speaker diarization for a new bot locale.
+ `UpdateBotLocale` - Modify speaker diarization for an existing bot locale.
+ `DescribeBotLocale` - View the current speaker diarization configuration.

The structure has a single required member:

`enabled`  
Whether Amazon Lex V2 restricts speech detection to the primary speaker for this bot locale. Valid values are `true` and `false`.

You can also include `speakerDiarizationSettings` in the bot locale of an import file, so that the setting travels with the bot when you export and import it.

**Example Enable speaker diarization using the AWS CLI**  

```
aws lexv2-models update-bot-locale \
    --bot-id "ABCDE12345" \
    --bot-version "DRAFT" \
    --locale-id "en_US" \
    --nlu-intent-confidence-threshold 0.40 \
    --speaker-diarization-settings '{
        "enabled": true
    }'
```

**Example View the current setting using the AWS CLI**  

```
aws lexv2-models describe-bot-locale \
    --bot-id "ABCDE12345" \
    --bot-version "DRAFT" \
    --locale-id "en_US" \
    --query "speakerDiarizationSettings"
```

`speakerDiarizationSettings` is returned by `DescribeBotLocale`, and not by `ListBotLocales`. To audit several locales, call `DescribeBotLocale` for each one.

------

**Note**  
After you change the setting, build the bot locale with the `BuildBotLocale` operation. If your alias serves a numbered bot version, create a new version from the `DRAFT` version and update the alias to point to it, as you would for any other bot locale setting. For more information, see [Versioning and aliases with your Lex V2 bot](versions-aliases.md).

## How Amazon Lex V2 interprets the setting
<a name="speaker-diarization-setting-values"></a>

`{"enabled": true}`  
Speech detection is restricted to the primary speaker.

`{"enabled": false}`  
Speaker diarization is turned off. Amazon Lex V2 uses VAD alone.

Not set  
Turned off for bots that have never configured the setting.

`UpdateBotLocale` keeps the stored value when you omit `speakerDiarizationSettings` from the request, so an update that changes other bot locale settings does not turn speaker diarization off. To turn the feature off for a bot locale where it is enabled, send `{"enabled": false}` explicitly instead of omitting the field.

## Best practices for speaker diarization
<a name="speaker-diarization-best-practices"></a>
+ **Enable it where the caller's environment is noisy** - The benefit comes from interference by other speakers, such as callers at home with a television on, callers on speakerphone, open offices, and conference rooms. In quiet one-on-one calls, the feature is designed to have no noticeable effect.
+ **Expect the loudest voice to be treated as the caller** - The primary speaker is chosen by loudness. Two people might share a call, such as a caller and a family member, or a caller and an interpreter. In this case, Amazon Lex V2 treats the quieter person as background until that person becomes the louder speaker for a sustained period. Leave speaker diarization turned off for conversation flows that depend on two people speaking in turn.
+ **Turn off barge-in on a long opening prompt** - Speaker diarization cannot help before the caller has spoken. If your bot opens with a lengthy prompt and your callers are often in constant background conversation, set the `x-amz-lex:allow-interrupt:*:*` session attribute to `false` for that prompt. The prompt then plays through, and speaker diarization takes over once the caller has spoken. For more information, see [How interrupt behavior works in a Lex V2 bot](session-attribs-speech.md#allow-interrupt).
+ **Keep your interruption settings as they are** - Speaker diarization reduces interruptions caused by other voices. It does not change how interruptions from the caller work, so tune barge-in and timeout settings separately.
+ **Test with representative audio** - Validate the change with test calls that contain the background noise your bot actually encounters, such as television, overlapping conversation, and side chatter. Compare the results against the same calls with the setting turned off before you roll it out to production.
+ **Roll out one language at a time** - Because the setting applies to a single bot locale, you can enable it for one language, review your conversation metrics and logs, and then expand to other languages.