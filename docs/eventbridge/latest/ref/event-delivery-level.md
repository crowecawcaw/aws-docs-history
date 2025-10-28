# Delivery level for AWS service events

Each AWS service that generates events sends them to EventBridge as either _best
effort_ or _durable_ delivery attempts.

- _Best effort
  delivery_ means that the service attempts to send all events to EventBridge, but in some
  rare cases an event might not be delivered.
- _Durable delivery_ means the service will successfully attempt to deliver events to EventBridge at least once.
  Once a valid event is delivered to EventBridge, EventBridge matches it against rules and then follows the retry policy and any dead-letter queue specified for the event target(s).
  For more information, see [Retrying event delivery](../userguide/eb-rule-retry-policy.md "../userguide/eb-rule-retry-policy.md") in the _EventBridge User Guide_.
