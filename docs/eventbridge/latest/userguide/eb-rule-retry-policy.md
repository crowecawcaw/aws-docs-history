# How EventBridge retries delivering events

Sometimes an [event](eb-events.md "eb-events.md") isn't successfully delivered to the
[target](eb-targets.md "eb-targets.md") specified in a [rule](eb-rules.md "eb-rules.md"). This can happen, for example:

- If the target resource is unavailable
- Due to network conditions
  When an event isn't successfully
  delivered to a target because of retriable errors, EventBridge retries sending the event. You set the length of time
  it tries, and number of retry attempts in the **Retry policy** settings for the
  target. By default, EventBridge retries sending the event for 24 hours and up to 185 times with an
  [exponential back off and _jitter_](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/"), or randomized delay.

If an
event isn't delivered after all retry attempts are exhausted, the event is dropped and EventBridge
doesn't continue to process it.

To avoid losing events after they fail to be delivered to a target, configure a dead-letter queue (DLQ) to receive all failed events. For more information, see [Using dead-letter queues to process undelivered events in EventBridge](eb-rule-dlq.md "eb-rule-dlq.md").
