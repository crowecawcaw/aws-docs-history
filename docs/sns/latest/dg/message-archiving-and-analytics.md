# Amazon SNS message archiving, replay, and

analytics

Amazon SNS standard topics support message archiving through . You can fan out
notifications to Firehose delivery streams, which allows you to send notifications to storage
and analytics destinations that Firehose supports, including Amazon Simple Storage Service (Amazon S3), Amazon Redshift, and
more.

Amazon SNS FIFO topics support an in-place, no-code, message archive that lets topic owners
store (or _archive_) messages published to a topic for up
to 365 days. For topics with an active `ArchivePolicy`, subscribers can then
create a `ReplayPolicy` to retrieve (or _replay_) the archived messages back to a subscribed endpoint. To learn more about
this feature, see [Amazon SNS message archiving and replay for FIFO
topics](fifo-message-archiving-replay.md "fifo-message-archiving-replay.md").

| Features          | Standard Topics                                                                                                      | FIFO Topics                                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Message archiving | [Fanout to Firehose delivery streams](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md")                 | [Amazon SNS message archiving for FIFO topic owners](message-archiving-and-replay-topic-owner.md "message-archiving-and-replay-topic-owner.md") |
| Message replay    | Replay for standard topics is not a built in feature. Many customers build their own based on their message archive. | [Amazon SNS message replay for FIFO topic subscribers](message-archiving-and-replay-subscriber.md "message-archiving-and-replay-subscriber.md") |
