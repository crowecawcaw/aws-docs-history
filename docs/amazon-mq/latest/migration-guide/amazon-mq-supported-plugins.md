# Supported plugins for Amazon MQ for ActiveMQ

A plugin in Amazon MQ is a software module that adds a specific
feature to a broker. Amazon MQ for ActiveMQ managed brokers support the
following plugins:

- [authorizationPlugin](https://activemq.apache.org/security.html "https://activemq.apache.org/security.html"):
  Allows you to control access at the granularity level of
  destinations or of individual messages.
- [discardingDLQBrokerPlugin](../developer-guide/permitted-attributes.md#discardingDLQBrokerPlugin.attributes "../developer-guide/permitted-attributes.md#discardingDLQBrokerPlugin.attributes"):
  Provides fine-grained options to discard your dead-letter queue.
- [redeliveryPlugin](../developer-guide/permitted-attributes.md#redeliveryPlugin.attributes "../developer-guide/permitted-attributes.md#redeliveryPlugin.attributes"):
  Enables you to replace the regular DLQ handling with
  re-delivery to the original destination following a delay period.
- [forcePersistencyModeBrokerPlugin](../developer-guide/permitted-attributes.md#forcePersistencyModeBrokerPlugin.attributes "../developer-guide/permitted-attributes.md#forcePersistencyModeBrokerPlugin.attributes"):
  Allows you to force every incoming message to be _persistent_
  or _non-persistent_. This is useful if you've set up a broker usage
  policy to process only persistent or non-persistent messages.
- [statisticsBrokerPlugin](https://activemq.apache.org/statisticsplugin "https://activemq.apache.org/statisticsplugin"):
  Enables you to retrieve statistics from the broker or its
  destinations.
- [timeStampingBrokerPlugin](../developer-guide/permitted-attributes.md#timeStampingBrokerPlugin.attributes "../developer-guide/permitted-attributes.md#timeStampingBrokerPlugin.attributes"):
  Allows you to update a JMS Client's timestamp on a message
  with a broker timestamp. You can trust the timestamp set on your Amazon MQ brokers
  when client-side machine clocks are known to be incorrect.
