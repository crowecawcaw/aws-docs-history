# Real-time Call Analytics

Real-time Call Analytics provides real-time insights that can be used for addressing
issues and mitigating escalations as they happen.

The following insights are available with real-time Call Analytics:

- [Category events](#tca-category-events-stream "#tca-category-events-stream") that use rules to flag
  specific keywords and phrases; category events can be used to create
  [real-time alerts](tca-start-stream.md#tca-create-alert-stream "tca-start-stream.md#tca-create-alert-stream")
- [Issue detection](#tca-issue-detection-stream "#tca-issue-detection-stream") identifies the
  issues spoken within each audio segment
- [PII (sensitive data) identification](#tca-pii-id-stream "#tca-pii-id-stream") in your text
  transcript
- [PII (sensitive data) redaction](#tca-pii-redact-stream "#tca-pii-redact-stream") of your text
  transcript
- [Sentiment analysis](#tca-sentiment-stream "#tca-sentiment-stream") for each speech segment
- [Language identification](#tca-language-id-stream "#tca-language-id-stream") detects the primary language spoken in each audio channel
  In addition to real-time Call Analytics, Amazon Transcribe can also perform
  [post-call analytics](tca-post-call.md "tca-post-call.md") on your media stream. You can include
  post-call analytics in your real-time Call Analytics request using the [`PostCallAnalyticsSettings`](../APIReference/API_streaming_PostCallAnalyticsSettings.md "../APIReference/API_streaming_PostCallAnalyticsSettings.md")
  parameter.

## Real-time insights

This section details the insights available for real-time Call Analytics transcriptions.

### Category events

Using category events, you can match your transcription based on an exact keyword or
phrase. For example, if you set a filter for the phrase "I want to speak to the
manager", Amazon Transcribe filters for that _exact_ phrase.

Here's an [output example](tca-output-streaming.md#tca-output-category-event-stream "tca-output-streaming.md#tca-output-category-event-stream").

For more information on creating real-time Call Analytics categories, see
[Creating categories for real-time transcriptions](tca-categories-stream.md "tca-categories-stream.md").

###### Tip

Category events allow you to set real-time alerts; see
[Creating real-time alerts for category
matches](tca-start-stream.md#tca-create-alert-stream "tca-start-stream.md#tca-create-alert-stream") for
more information.

### Issue detection

Issue detection provides succinct summaries of detected issues within each audio
segment. Using the issue detection feature, you can:

- Reduce the need for manual note-taking during and after calls
- Improve agent efficiency, allowing them to respond faster to customers

###### Note

Issue detection is supported with these English language dialects: Australian
(`en-AU`), British (`en-GB`), and US
(`en-US`).

The issue detection feature works across all industries and business sectors, and is
context-based. It works out-of-the-box and thus doesn't support customization, such
as model training or custom categories.

Issue detection with real-time Call Analytics is performed on each complete audio
segment.

Here's an [output example](tca-output-streaming.md#tca-output-issue-detection-stream "tca-output-streaming.md#tca-output-issue-detection-stream").

### PII (sensitive data) identification

Sensitive data identification labels personally identifiable information (PII) in the text transcript.
This parameter is useful for protecting customer information.

###### Note

Real-time PII identification is supported with these English language dialects: Australian
(`en-AU`), British (`en-GB`), US
(`en-US`) and with Spanish language dialect (`es-US`).

PII identification with real-time Call Analytics is performed on each complete audio
segment.

To view the list of PII that is identified using this feature, or to learn more about PII identification
with Amazon Transcribe, see [Redacting or identifying personally identifiable information](pii-redaction.md "pii-redaction.md").

Here is an [output example](tca-output-streaming.md#tca-output-pii-id-stream "tca-output-streaming.md#tca-output-pii-id-stream").

### PII (sensitive data) redaction

Sensitive data redaction replaces personally identifiable information (PII) in your text transcript
with the type of PII (for example, `[NAME]`). This parameter is useful for
protecting customer information.

###### Note

Real-time PII redaction is supported with these English language dialects: Australian
(`en-AU`), British (`en-GB`), US
(`en-US`) and with Spanish language dialect (`es-US`).

PII redaction with real-time Call Analytics is performed on each complete audio
segment.

To view the list of PII that is redacted using this feature, or to learn more about redaction with
Amazon Transcribe, see [Redacting or identifying personally identifiable information](pii-redaction.md "pii-redaction.md").

Here is an [output example](tca-output-streaming.md#tca-output-pii-redact-stream "tca-output-streaming.md#tca-output-pii-redact-stream").

### Sentiment analysis

Sentiment analysis estimates how the customer and agent are feeling throughout the call.
This metric is provided for every speech segment and is represented as a qualitative value
(`positive`, `neutral`, `mixed`, or
`negative`).

Using this parameter, you can qualitatively evaluate the overall sentiment for each call
participant and the sentiment for each participant during each speech segment. This metric can
help identify if your agent is able to delight an upset customer by the time the call ends.

Sentiment analysis with real-time Call Analytics is performed on each complete audio
segment.

Sentiment analysis works out-of-the-box and thus doesn't support customization, such as model
training or custom categories.

Here's an [output example](tca-output-streaming.md#tca-output-sentiment-stream "tca-output-streaming.md#tca-output-sentiment-stream").

### Language identification

Language identification automatically recognizes and determines the primary language being spoken within each channel of your audio streams during real-time Call Analytics. Once identified, Call Analytics will process and return the most suitable transcription based on the detected language, delivering this information back through the stream in real-time.

This feature allows you to automatically recognize and identify the dominant language spoken in each channel of your audio stream. Once the language is detected, Call Analytics processes and delivers the appropriate transcription for the identified language in real-time.

Automatic language identification is supported for all [Call Analytics streaming supported languages](supported-languages.md "supported-languages.md") that are currently supported for streaming transcriptions at no additional cost, and is available in the Call Analytics streaming supported [AWS Regions](../../../general/latest/gr/transcribe.md#transcribe_region "../../../general/latest/gr/transcribe.md#transcribe_region").

###### Important

Call Analytics supports single-language identification only, which identifies the dominant language spoken in your audio channel. Multi-language identification is not supported, meaning each channel can only be transcribed in one language.

To use language identification, you must provide at least two language codes and at most five language codes, and you can select only one language dialect per language per stream from [supported Call Analytics streaming languages](supported-languages.md "supported-languages.md"). This means that you cannot select en-US and en-AU as language options for the same transcription. When utilizing this feature, the LanguageCode parameter must remain null in the request, as LanguageCode and IdentifyLanguage are mutually exclusive options.

###### Warning

If your specified language codes don't match the actual spoken language, the system will select the most similar language from your options, which may result in inaccurate transcriptions.

Using the language identification feature, you can:

- Automatically detect the dominant language in real-time
- Process different languages across separate channels
- Receive confidence scores for language detection
- Apply language-specific custom vocabularies

To use language identification, you must configure the following parameters:

**Required parameters:**

- `identifyLanguage` - Set to true to enable language identification.
- `languageOptions` - A list of possible language codes to use when identifyLanguage is set to true. You must provide a minimum of two language selections, as single-language selection is not supported.

**Optional parameters:**

- `preferredLanguage` - Your expected primary language from provided languageOptions. Adding a preferred language can help Call Analytics identify the language faster.
- `vocabularyNames` - Custom vocabulary names for improved accuracy. Note that vocabulary names are case-sensitive, and if the custom vocabulary's language doesn't match the identified media language, it won't be applied to the transcription.
- `vocabularyFilterNames` - Vocabulary filter names to customize the transcript output.

Here's an [output example](tca-output-streaming.md#tca-output-language-id-stream "tca-output-streaming.md#tca-output-language-id-stream").
