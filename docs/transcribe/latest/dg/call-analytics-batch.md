# Post-call analytics

Call Analytics provides post-call analyses, which are useful for monitoring customer
service trends.

Post-call transcriptions offer the following insights:

- [Call characteristics](#tca-characteristics-batch "#tca-characteristics-batch"), including talk
  time, non-talk time, speaker loudness, interruptions, talk speed, issues, outcomes, and action items
- [Generative call summarization](#tca-summarization-batch "#tca-summarization-batch"), which creates a concise summary of the entire call
- [Custom categorization](#tca-categorization-batch "#tca-categorization-batch") with rules that
  you can use to hone in on specific keywords and criteria
- [PII redaction](#tca-pii-redact-batch "#tca-pii-redact-batch") of your text transcript
  and your audio file
- [Speaker sentiment](#tca-sentiment-batch "#tca-sentiment-batch") for each
  caller at various points in a call

## Post-call insights

This section details the insights available for post-call analytics transcriptions.

### Call characteristics

The call characteristics feature measures the quality of agent-customer interactions using
these criteria:

- **Interruption**: Measures if and when one participant cuts off
  the other participant mid-sentence. Frequent interruptions may be associated with rudeness or
  anger, and could correlate to negative sentiment for one or both participants.
- **Loudness**: Measures the volume at which each participant is
  speaking. Use this metric to see if the caller or the agent is speaking loudly or yelling,
  which is often indicative of being upset. This metric is represented as a normalized value
  (speech level per second of speech in a given segment) on a scale from 0 to 100, where a
  higher value indicates a louder voice.
- **Non-talk time**: Measures periods of time that do not
  contain speech. Use this metric to see if there are long periods of silence, such as an agent
  keeping a customer on hold for an excessive amount of time.
- **Talk speed**: Measures the speed at which both participants
  are speaking. Comprehension can be affected if one participant speaks too quickly. This metric
  is measured in words per minute.
- **Talk time**: Measures the amount of time (in milliseconds)
  each participant spoke during the call. Use this metric to help identify if one participant is
  dominating the call or if the dialogue is balanced.
- **Issues, Outcomes, and Action Items**: Identifies issues, outcomes and action items from the call transcript.

Here's an [output example](tca-output-batch.md#tca-output-characteristics-batch "tca-output-batch.md#tca-output-characteristics-batch").

### Generative call summarization

Generative call summarization creates a concise summary of the entire call,
capturing key components such as reason for the call, steps taken to resolve issue, and
next steps.

Using generative call summarization, you can:

- Reduce the need for manual note-taking during and after calls.
- Improve agent efficiency as they can spend more time talking to callers waiting in queue rather than engaging in after-call work.
- Speed up supervisor reviews as call summaries are much quicker to review than entire transcripts.

To use generative call summarization with a post-call analytics job, see [Enabling generative call summarization](tca-enable-summarization.md "tca-enable-summarization.md").
For example output, see [Generative call summarization output example](tca-output-batch.md#tca-output-summarization-batch "tca-output-batch.md#tca-output-summarization-batch").
Generative call summarization is priced separately (please refer to [pricing page](https://aws.amazon.com/transcribe/pricing "https://aws.amazon.com/transcribe/pricing")).

###### Note

Generative call summarization is currently available in `us-east-1` and `us-west-2`.
This capability is supported with these English language dialects: Australian (`en-AU`),
British (`en-GB`), Indian (`en-IN`), Irish (`en-IE`),
Scottish (`en-AB`), US (`en-US`), and Welsh (`en-WL`).

### Custom categorization

Use call categorization to flag keywords, phrases, sentiment, or actions within a call. Our
categorization options can help you triage escalations, such as negative-sentiment calls with many
interruptions, or organize calls into specific categories, such as company departments.

The criteria you can add to a category include:

- **Non-talk time**: Periods of time when neither the customer
  nor the agent is talking.
- **Interruptions**: When the customer or the agent is interrupting
  the other person.
- **Customer or agent sentiment**: How the customer or the
  agent is feeling during a specified time period. If at least 50 percent of the conversation
  turns (the back-and-forth between two speakers) in a specified time period match the
  specified sentiment, Amazon Transcribe considers the sentiment a match.
- **Keywords or phrases**: Matches part of the transcription based on an
  exact phrase. For example, if you set a filter for the phrase "I want to speak to the manager",
  Amazon Transcribe filters for that _exact_ phrase.

You can also flag the inverse of the previous criteria (talk time, lack of
interruptions, a sentiment not being present, and the lack of a specific phrase).

Here's an [output example](tca-output-batch.md#tca-output-categorization-batch "tca-output-batch.md#tca-output-categorization-batch").

For more information on categories or to learn how to create a new category, see
[Creating categories for post-call transcriptions](tca-categories-batch.md "tca-categories-batch.md").

### Sensitive data redaction

Sensitive data redaction replaces personally identifiable information (PII) in the text transcript
and the audio file. A redacted transcript replaces the original text with `[PII]`; a
redacted audio file replaces spoken personal information with silence. This parameter is useful for
protecting customer information.

###### Note

Post-call PII redaction is supported with US English (`en-US`) and US Spanish (`es-US`).

To view the list of PII that is redacted using this feature, or to learn more about redaction with
Amazon Transcribe, see [Redacting or identifying personally identifiable information](pii-redaction.md "pii-redaction.md").

Here is an [output example](tca-output-batch.md#tca-output-pii-redact-batch "tca-output-batch.md#tca-output-pii-redact-batch").

### Sentiment analysis

Sentiment analysis estimates how the customer and agent are feeling throughout the call. This
metric is represented as both a quantitative value (with a range from `5` to
`-5`) and a qualitative value (`positive`, `neutral`,
`mixed`, or `negative`). Quantitative values are provided per quarter
and per call; qualitative values are provided per turn.

This metric can help identify if your agent is able to delight an upset customer by the time the
call ends.

Sentiment analysis works out-of-the-box and thus doesn't support customization, such as model
training or custom categories.

Here's an [output example](tca-output-batch.md#tca-output-sentiment-batch "tca-output-batch.md#tca-output-sentiment-batch").
