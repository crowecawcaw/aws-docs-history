

# Elements, Child Collection Elements, and Their Child Elements Permitted in Amazon MQ Configurations
<a name="permitted-collections"></a>

The following is a detailed listing of the elements, child collection elements, and their child elements permitted in Amazon MQ configurations. For more information, see [XML Configuration](https://activemq.apache.org/xml-configuration.html) in the Apache ActiveMQ documentation.

Use the scroll bars to see the rest of the table.



- **`authorizationMap`**
  - **Child Collection Element:** authorizationEntries / **Child Element:** [`authorizationEntry`](child-element-details.md#authorizationEntry)
  - **Child Element:** tempDestinationAuthorizationEntry
  - **Child Collection Element:** defaultEntry / **Child Element:** authorizationEntry
  - **Child Element:** tempDestinationAuthorizationEntry
  - **Child Collection Element:** tempDestinationAuthorizationEntry / **Child Element:** tempDestinationAuthorizationEntry

- **`authorizationPlugin`**
  - **Child Collection Element:** map
  - **Child Element:** authorizationMap

- **`broker`**
  - **Child Collection Element:** destinationInterceptors / **Child Element:** mirroredQueue
  - **Child Element:** virtualDestinationInterceptor
  - **Child Collection Element:** destinationPolicy / **Child Element:** policyMap
  - **Child Collection Element:** destinations / **Child Element:** queue
  - **Child Element:** tempQueue
  - **Child Element:** tempTopic
  - **Child Element:** topic
  - **Child Collection Element:** networkConnectors / **Child Element:** [`networkConnector`](child-element-details.md#networkConnector)
  - **Child Collection Element:** persistenceAdapter / **Child Element:** [`kahaDB`](child-element-details.md#kahaDB)
  - **Child Collection Element:** plugins / **Child Element:** authorizationPlugin
  - **Child Element:** discardingDLQBrokerPlugin
  - **Child Element:** forcePersistencyModeBrokerPlugin
  - **Child Element:** redeliveryPlugin
  - **Child Element:** statisticsBrokerPlugin
  - **Child Element:** timeStampingBrokerPlugin
  - **Child Collection Element:** systemUsage / **Child Element:** [`systemUsage`](child-element-details.md#systemUsage)

- **`compositeQueue`**
  - **Child Collection Element:** forwardTo
  - **Child Element:**
    - queue
    - tempQueue
    - tempTopic
    - topic
    - filteredDestination

- **`compositeTopic`**
  - **Child Collection Element:** forwardTo
  - **Child Element:**
    - queue
    - tempQueue
    - tempTopic
    - topic
    - filteredDestination

- **`policyEntry`**
  - **Child Collection Element:** deadLetterStrategy / **Child Element:** discarding
  - **Child Element:** individualDeadLetterStrategy
  - **Child Element:** sharedDeadLetterStrategy
  - **Child Collection Element:** destination / **Child Element:** queue
  - **Child Element:** tempQueue
  - **Child Element:** tempTopic
  - **Child Element:** topic
  - **Child Collection Element:** dispatchPolicy / **Child Element:** priorityDispatchPolicy
  - **Child Element:** priorityNetworkDispatchPolicy
  - **Child Element:** roundRobinDispatchPolicy
  - **Child Element:** simpleDispatchPolicy
  - **Child Element:** strictOrderDispatchPolicy
  - **Child Element:** clientIdFilterDispatchPolicy
  - **Child Collection Element:** messageEvictionStrategy / **Child Element:** oldestMessageEvictionStrategy
  - **Child Element:** oldestMessageWithLowestPriorityEvictionStrategy
  - **Child Element:** uniquePropertyMessageEvictionStrategy
  - **Child Collection Element:** messageGroupMapFactory / **Child Element:** cachedMessageGroupMapFactory
  - **Child Element:** messageGroupHashBucketFactory
  - **Child Element:** simpleMessageGroupMapFactory
  - **Child Collection Element:** pendingDurableSubscriberPolicy / **Child Element:** fileDurableSubscriberCursor
  - **Child Element:** storeDurableSubscriberCursor
  - **Child Element:** vmDurableCursor
  - **Child Collection Element:** pendingMessageLimitStrategy / **Child Element:** constantPendingMessageLimitStrategy
  - **Child Element:** prefetchRatePendingMessageLimitStrategy
  - **Child Collection Element:** pendingQueuePolicy / **Child Element:** fileQueueCursor
  - **Child Element:** storeCursor
  - **Child Element:** vmQueueCursor
  - **Child Collection Element:** pendingSubscriberPolicy / **Child Element:** fileCursor
  - **Child Element:** vmCursor
  - **Child Collection Element:** slowConsumerStrategy / **Child Element:** abortSlowAckConsumerStrategy
  - **Child Element:** abortSlowConsumerStrategy
  - **Child Collection Element:** subscriptionRecoveryPolicy / **Child Element:** fixedCountSubscriptionRecoveryPolicy
  - **Child Element:** fixedSizedSubscriptionRecoveryPolicy
  - **Child Element:** lastImageSubscriptionRecoveryPolicy
  - **Child Element:** noSubscriptionRecoveryPolicy
  - **Child Element:** queryBasedSubscriptionRecoveryPolicy
  - **Child Element:** retainedMessageSubscriptionRecoveryPolicy

- **`timedSubscriptionRecoveryPolicy`**

- **`policyMap`**
  - **Child Collection Element:** defaultEntry / **Child Element:** policyEntry
  - **Child Collection Element:** policyEntries / **Child Element:** policyEntry

- **`redeliveryPlugin`**
  - **Child Collection Element:** redeliveryPolicyMap
  - **Child Element:** redeliveryPolicyMap

- **`redeliveryPolicyMap`**
  - **Child Collection Element:** defaultEntry / **Child Element:** redeliveryPolicy
  - **Child Collection Element:** redeliveryPolicyEntries / **Child Element:** redeliveryPolicy

- **`retainedMessageSubscriptionRecoveryPolicy`**
  - **Child Collection Element:** wrapped
  - **Child Element:**
    - fixedCountSubscriptionRecoveryPolicy
    - fixedSizedSubscriptionRecoveryPolicy
    - lastImageSubscriptionRecoveryPolicy
    - noSubscriptionRecoveryPolicy
    - queryBasedSubscriptionRecoveryPolicy
    - retainedMessageSubscriptionRecoveryPolicy
    - timedSubscriptionRecoveryPolicy

- **`sharedDeadLetterStrategy`**
  - **Child Collection Element:** deadLetterQueue
  - **Child Element:**
    - queue
    - tempQueue
    - tempTopic
    - topic

- **`virtualDestinationInterceptor`**
  - **Child Collection Element:** virtualDestinations
  - **Child Element:**
    - compositeQueue
    - compositeTopic
    - virtualTopic

