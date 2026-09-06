

# Amazon Transcribe features
<a name="feature-matrix"></a>

To help you decide which Amazon Transcribe solution best fits your use case, the following table offers a feature comparison.

Note that 'batch' and 'post-call' refer to transcribing a file that is located in an Amazon S3 bucket and 'streaming' and 'real-time' refer to transcribing media in real time.

<a name="table-feature-matrix"></a>
<table>
<thead>
  <tr><th>Feature</th><th>Amazon Transcribe</th><th><a href="transcribe-medical.md">Amazon Transcribe Medical</a>1</th><th><a href="call-analytics.md">Amazon Transcribe Call Analytics</a></th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><i>Configuration options</i></td></tr>
  <tr><td><a href="alternatives.md">Alternative transcriptions</a></td><td>batch, streaming</td><td>batch, streaming</td><td>no</td></tr>
  <tr><td><a href="channel-id.md">Channel identification</a></td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td><a href="job-queueing.md">Job queueing</a></td><td>batch</td><td>no</td><td>post-call</td></tr>
  <tr><td><a href="lang-id.md">Language identification</a></td><td>batch, streaming</td><td>no</td><td>post-call</td></tr>
  <tr><td><a href="lang-id-batch.md#lang-id-batch-multi-language">Multi-language identification</a></td><td>batch, streaming</td><td>no</td><td>no</td></tr>
  <tr><td><a href="diarization.md">Speaker diarization</a></td><td>batch, streaming</td><td>batch, streaming</td><td>post-call</td></tr>
  <tr><td><a href="how-numbers.md">Transcribing digits</a>2</td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4"><i>Conversation analytics</i></td></tr>
  <tr><td><a href="call-analytics-batch.md#tca-characteristics-batch">Call characteristics</a></td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td><a href="call-analytics-batch.md#tca-summarization-batch">Call summarization</a>2</td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td><a href="call-analytics-batch.md#tca-categorization-batch">Custom categorization</a></td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td><a href="call-analytics-streaming.md#tca-category-events-stream">Real-time category events</a></td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td><a href="call-analytics-streaming.md#tca-issue-detection-stream">Real-time issue detection</a>2</td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td><a href="call-analytics-streaming.md#tca-sentiment-stream">Real-time speaker sentiment</a></td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td><a href="call-analytics-batch.md#tca-sentiment-batch">Speaker sentiment</a></td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td colspan="4"><i>Language customization</i></td></tr>
  <tr><td><a href="custom-language-models.md">Custom language models</a>2</td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td><a href="custom-vocabulary.md">Custom vocabularies</a></td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4"><i>Resource organization</i></td></tr>
  <tr><td><a href="tagging.md">Tagging</a></td><td>batch</td><td>batch</td><td>post-call</td></tr>
  <tr><td colspan="4"><i>Sensitive data</i></td></tr>
  <tr><td><a href="phi-id.md">Identifying personal health information</a>2</td><td>no</td><td>batch, streaming</td><td>no</td></tr>
  <tr><td><a href="pii-redaction-stream.md">Identifying personally identifiable information</a>2</td><td>streaming</td><td>no</td><td>real-time</td></tr>
  <tr><td><a href="call-analytics-batch.md#tca-pii-redact-batch">Redacting audio</a>2</td><td>no</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td><a href="pii-redaction.md">Redacting transcripts</a>2</td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td><a href="vocabulary-filtering.md">Vocabulary filtering</a></td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4"><i>Video</i></td></tr>
  <tr><td><a href="subtitles.md">Subtitles</a></td><td>batch</td><td>no</td><td>no</td></tr>
</tbody>
</table>


****  
1 Amazon Transcribe Medical is only available in US English.  
2 This feature is not available for all languages; review the [Supported languages and language-specific features](supported-languages.md) table for more details.