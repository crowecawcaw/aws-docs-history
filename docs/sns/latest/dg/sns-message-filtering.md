# Amazon SNS message filtering

By default, an Amazon SNS topic subscriber receives every message that's published to the
topic. To receive only a subset of the messages, a subscriber must assign a _filter
policy_ to the topic subscription.

A filter policy is a JSON object containing properties that define which messages the
subscriber receives. Amazon SNS supports policies that act on the message attributes or on the
message body, according to the filter policy scope that you set for the subscription. Filter
policies for the message body assume that the message payload is a well-formed JSON
object.

If a subscription doesn't have a filter policy, the subscriber receives every message
published to its topic. When you publish a message to a topic with a filter policy in place,
Amazon SNS compares the message attributes or the message body to the properties in the filter
policy for each of the topic's subscriptions. If all of the message attributes or message
body properties satisfy the conditions specified in the filter policy, Amazon SNS sends the
message to the subscriber. Otherwise, Amazon SNS doesn't send the message to that subscriber.

For more information, see [Filter Messages
Published to Topics](https://aws.amazon.com/getting-started/tutorials/filter-messages-published-to-topics/ "https://aws.amazon.com/getting-started/tutorials/filter-messages-published-to-topics/").
