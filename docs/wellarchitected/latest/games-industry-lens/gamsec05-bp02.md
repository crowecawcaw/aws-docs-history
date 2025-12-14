# GAMESEC05-BP02 Collect, store, and analyze player usage logs to

detect inappropriate behavior

Instrument your game to collect logs to understand how players use
the features of your game and how they interact with other players.
You can then block unauthorized activities that can degrade the
player experience. 

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Send structured log events to
the [Game
Analytics Pipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/ "https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/"), by using a logging solution such as
[Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") or
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/"), or through a solution from an AWS
Partner such
as [Datadog](https://www.datadoghq.com/ "https://www.datadoghq.com/"),
[Sumo Logic](https://www.sumologic.com/ "https://www.sumologic.com/"),
[New Relic](https://newrelic.com/ "https://newrelic.com/"),
[Honeycomb.io](https://www.honeycomb.io/ "https://www.honeycomb.io/"),
or [Splunk](https://www.splunk.com/ "https://www.splunk.com/").
Structure these player usage logs so that they can be used to
detect when specific actions by players need to be investigated.

After you have captured the data, consider implementing tools to
detect inappropriate usage behavior. For example, if your game has
social features such as in-game player messaging, voice chat, or
online forums, save logs from these player engagements in a format
that can be analyzed for moderation purposes.

Configure your game's voice chat feature to export recordings to
Amazon S3 and
use [Amazon Transcribe](https://aws.amazon.com/transcribe "https://aws.amazon.com/transcribe") to convert the audio speech to text format which
can be stored for processing. Alternatively, you can perform
real-time streaming transcription by integrating your game backend
voice chat service directly with the Transcribe API
to [transcribe
streaming audio](../../../transcribe/latest/dg/streaming.md "../../../transcribe/latest/dg/streaming.md") in real time. Moderation teams can manually
review the content, and once the content is in a standard format,
you can also use AWS AI/ML services to perform moderation
automatically.
[Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/") can be used to perform natural language
processing (NLP) to uncover information from the unstructured
text, which can classify and organize the conversations into
relevant topics and identify inappropriate behavior such as
profanity.

### Implementation steps

- Collect, store, and analyze player usage logs.
- Use AWS services for artificial intelligence and machine
  learning to more efficiently review and gain insights into
  your player usage logs.
