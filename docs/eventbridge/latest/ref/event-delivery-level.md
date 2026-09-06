

# Delivery level for AWS service events
<a name="event-delivery-level"></a>

Each AWS service that generates events sends them to EventBridge as either *best effort* or *durable* delivery attempts. 
+ *Best effort delivery* means that the service attempts to send all events to EventBridge, but in some rare cases an event might not be delivered.
+ *Durable delivery* means the service will successfully attempt to deliver events to EventBridge at least once.

Once a valid event is delivered to EventBridge, EventBridge matches it against rules and then follows the retry policy and any dead-letter queue specified for the event target(s). For more information, see [Retrying event delivery](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html) in the *EventBridge User Guide*.