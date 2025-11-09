# Elements and Their Attributes Permitted in Amazon MQ

Configurations

The following is a detailed listing of the elements and their attributes permitted in
Amazon MQ configurations. For more information, see [XML Configuration](http://activemq.apache.org/xml-configuration.html "http://activemq.apache.org/xml-configuration.html") in the
Apache ActiveMQ documentation.

Use the scroll bars to see the rest of the table.

| Element                                                                                 | Attribute                           |
| --------------------------------------------------------------------------------------- | ----------------------------------- |
| `abortSlowAckConsumerStrategy`                                                          | `abortConnection`                   |
| `checkPeriod`                                                                           |
| `ignoreIdleConsumers`                                                                   |
| `ignoreNetworkConsumers`                                                                |
| `maxSlowCount`                                                                          |
| `maxSlowDuration`                                                                       |
| `maxTimeSinceLastAck`                                                                   |
| `name`                                                                                  |
| `abortSlowConsumerStrategy`                                                             | `abortConnection`                   |
| `checkPeriod`                                                                           |
| `ignoreNetworkConsumers`                                                                |
| `maxSlowCount`                                                                          |
| `maxSlowDuration`                                                                       |
| `name`                                                                                  |
| `authorizationEntry`                                                                    | `admin`                             |
| `queue`                                                                                 |
| `read`                                                                                  |
| `tempQueue`                                                                             |
| `tempTopic`                                                                             |
| `topic`                                                                                 |
| `write`                                                                                 |
| `broker`                                                                                | `advisorySupport`                   |
| `allowTempAutoCreationOnSend`                                                           |
| `cacheTempDestinations`                                                                 |
| `consumerSystemUsagePortion`                                                            |
| `dedicatedTaskRunner`                                                                   |
| `deleteAllMessagesOnStartup`                                                            |
| `keepDurableSubsActive`                                                                 |
| `enableMessageExpirationOnActiveDurableSubs`                                            |
| `maxPurgedDestinationsPerSweep`                                                         |
| `maxSchedulerRepeatAllowed`                                                             |
| `monitorConnectionSplits`                                                               |
| [networkConnectorStartAsync](#networkConnectorStartAsync "#networkConnectorStartAsync") |
| `offlineDurableSubscriberTaskSchedule`                                                  |
| `offlineDurableSubscriberTimeout`                                                       |
| `persistenceThreadPriority`                                                             |
| `persistent`                                                                            |
| `populateJMSXUserID`                                                                    |
| `producerSystemUsagePortion`                                                            |
| `rejectDurableConsumers`                                                                |
| `rollbackOnlyOnAsyncException`                                                          |
| `schedulePeriodForDestinationPurge`                                                     |
| `schedulerSupport`                                                                      |
| `splitSystemUsageForProducersConsumers`                                                 |
| `taskRunnerPriority`                                                                    |
| `timeBeforePurgeTempDestinations`                                                       |
| `useAuthenticatedPrincipalForJMSXUserID`                                                |
| `useMirroredQueues`                                                                     |
| `useTempMirroredQueues`                                                                 |
| `useVirtualDestSubs`                                                                    |
| `useVirtualDestSubsOnCreation`                                                          |
| `useVirtualTopics`                                                                      |
| `cachedMessageGroupMapFactory`                                                          | `cacheSize`                         |
| `compositeQueue`                                                                        | `concurrentSend`                    |
| `copyMessage`                                                                           |
| `forwardOnly`                                                                           |
| `name`                                                                                  |
| `sendWhenNotMatched`                                                                    |
| `compositeTopic`                                                                        | `concurrentSend`                    |
| `copyMessage`                                                                           |
| `forwardOnly`                                                                           |
| `name`                                                                                  |
| `sendWhenNotMatched`                                                                    |
| conditionalNetworkBridgeFilterFactory                                                   | `rateDuration`                      |
| `rateLimit`                                                                             |
| `replayDelay`                                                                           |
| `replayWhenNoConsumers`                                                                 |
| `selectorAware`<br>Supported inApache ActiveMQ 5.16.x                                   |
| `constantPendingMessageLimitStrategy`                                                   | `limit`                             |
| `discarding`                                                                            | `deadLetterQueue`                   |
| `enableAudit`                                                                           |
| `expiration`                                                                            |
| `maxAuditDepth`                                                                         |
| `maxProducersToAudit`                                                                   |
| `processExpired`                                                                        |
| `processNonPersistent`                                                                  |
| `discardingDLQBrokerPlugin`                                                             | `dropAll`                           |
| `dropOnly`                                                                              |
| `dropTemporaryQueues`                                                                   |
| `dropTemporaryTopics`                                                                   |
| `reportInterval`                                                                        |
| `filteredDestination`                                                                   | `queue`                             |
| `selector`                                                                              |
| `topic`                                                                                 |
| `fixedCountSubscriptionRecoveryPolicy`                                                  | `maximumSize`                       |
| `fixedSizedSubscriptionRecoveryPolicy`                                                  | `maximumSize`                       |
| `useSharedBuffer`                                                                       |
| `forcePersistencyModeBrokerPlugin`                                                      | `persistenceFlag`                   |
| `individualDeadLetterStrategy`                                                          | `destinationPerDurableSubscriber`   |
| `enableAudit`                                                                           |
| `expiration`                                                                            |
| `maxAuditDepth`                                                                         |
| `maxProducersToAudit`                                                                   |
| `processExpired`                                                                        |
| `processNonPersistent`                                                                  |
| `queuePrefix`                                                                           |
| `queueSuffix`                                                                           |
| `topicPrefix`                                                                           |
| `topicSuffix`                                                                           |
| `useQueueForQueueMessages`                                                              |
| `useQueueForTopicMessages`                                                              |
| `messageGroupHashBucketFactory`                                                         | `bucketCount`                       |
| `cacheSize`                                                                             |
| `mirroredQueue`                                                                         | `copyMessage`                       |
| `postfix`                                                                               |
| `prefix`                                                                                |
| `oldestMessageEvictionStrategy`                                                         | `evictExpiredMessagesHighWatermark` |
| `oldestMessageWithLowestPriorityEvictionStrategy`                                       | `evictExpiredMessagesHighWatermark` |
| `policyEntry`                                                                           | `advisoryForConsumed`               |
| `advisoryForDelivery`                                                                   |
| `advisoryForDiscardingMessages`                                                         |
| `advisoryForFastProducers`                                                              |
| `advisoryForSlowConsumers`                                                              |
| `advisoryWhenFull`                                                                      |
| `allConsumersExclusiveByDefault`                                                        |
| `alwaysRetroactive`                                                                     |
| `blockedProducerWarningInterval`                                                        |
| `consumersBeforeDispatchStarts`                                                         |
| `cursorMemoryHighWaterMark`                                                             |
| `doOptimzeMessageStorage`                                                               |
| `durableTopicPrefetch`                                                                  |
| `enableAudit`                                                                           |
| `expireMessagesPeriod`                                                                  |
| `gcInactiveDestinations`                                                                |
| `gcWithNetworkConsumers`                                                                |
| `inactiveTimeoutBeforeGC`                                                               |
| `inactiveTimoutBeforeGC`                                                                |
| `includeBodyForAdvisory`                                                                |
| `lazyDispatch`                                                                          |
| `maxAuditDepth`                                                                         |
| `maxBrowsePageSize`                                                                     |
| `maxDestinations`                                                                       |
| `maxExpirePageSize`                                                                     |
| `maxPageSize`                                                                           |
| `maxProducersToAudit`                                                                   |
| `maxQueueAuditDepth`                                                                    |
| `memoryLimit`                                                                           |
| `messageGroupMapFactoryType`                                                            |
| `minimumMessageSize`                                                                    |
| `optimizedDispatch`                                                                     |
| `optimizeMessageStoreInFlightLimit`                                                     |
| `persistJMSRedelivered`                                                                 |
| `prioritizedMessages`                                                                   |
| `producerFlowControl`                                                                   |
| `queue`                                                                                 |
| `queueBrowserPrefetch`                                                                  |
| `queuePrefetch`                                                                         |
| `reduceMemoryFootprint`                                                                 |
| `sendAdvisoryIfNoConsumers`                                                             |
| `sendFailIfNoSpace`                                                                     |
| `sendFailIfNoSpaceAfterTimeout`<br>Supported in Apache ActiveMQ 5.16.4 and above        |
| `sendDuplicateFromStoreToDLQ`                                                           |
| `storeUsageHighWaterMark`                                                               |
| `strictOrderDispatch`                                                                   |
| `tempQueue`                                                                             |
| `tempTopic`                                                                             |
| `timeBeforeDispatchStarts`                                                              |
| `topic`                                                                                 |
| `topicPrefetch`                                                                         |
| `useCache`                                                                              |
| `useConsumerPriority`                                                                   |
| `usePrefetchExtension`                                                                  |
| `prefetchRatePendingMessageLimitStrategy`                                               | `multiplier`                        |
| `queryBasedSubscriptionRecoveryPolicy`                                                  | `query`                             |
| `queue`                                                                                 | `DLQ`                               |
| `physicalName`                                                                          |
| `redeliveryPlugin`                                                                      | `fallbackToDeadLetter`              |
| `sendToDlqIfMaxRetriesExceeded`                                                         |
| `redeliveryPolicy`                                                                      | `backOffMultiplier`                 |
| `collisionAvoidancePercent`                                                             |
| `initialRedeliveryDelay`                                                                |
| `maximumRedeliveries`                                                                   |
| `maximumRedeliveryDelay`                                                                |
| `preDispatchCheck`                                                                      |
| `queue`                                                                                 |
| `redeliveryDelay`                                                                       |
| `tempQueue`                                                                             |
| `tempTopic`                                                                             |
| `topic`                                                                                 |
| `useCollisionAvoidance`                                                                 |
| `useExponentialBackOff`                                                                 |
| `sharedDeadLetterStrategy`                                                              | `enableAudit`                       |
| `expiration`                                                                            |
| `maxAuditDepth`                                                                         |
| `maxProducersToAudit`                                                                   |
| `processExpired`                                                                        |
| `processNonPersistent`                                                                  |
| `storeDurableSubscriberCursor`                                                          | `immediatePriorityDispatch`         |
| `useCache`                                                                              |
| `tempDestinationAuthorizationEntry`                                                     | `admin`                             |
| `queue`                                                                                 |
| `read`                                                                                  |
| `tempQueue`                                                                             |
| `tempTopic`                                                                             |
| `topic`                                                                                 |
| `write`                                                                                 |
| `tempQueue`                                                                             | `DLQ`                               |
| `physicalName`                                                                          |
| `tempTopic`                                                                             | `DLQ`                               |
| `physicalName`                                                                          |
| `timedSubscriptionRecoveryPolicy`                                                       | `zeroExpirationOverride`            |
| `timeStampingBrokerPlugin`                                                              | `recoverDuration`                   |
| `futureOnly`                                                                            |
| `processNetworkMessages`                                                                |
| `ttlCeiling`                                                                            |
| `topic`                                                                                 | `DLQ`                               |
| `physicalName`                                                                          |
| `transportConnector`                                                                    | `name`                              |
| `updateClusterClients`                                                                  |
| `rebalanceClusterClients`                                                               |
| `updateClusterClientsOnRemove`                                                          |
| `uniquePropertyMessageEvictionStrategy`                                                 | `evictExpiredMessagesHighWatermark` |
| `propertyName`                                                                          |
| `virtualTopic`                                                                          | `concurrentSend`                    |
| `local`                                                                                 |
| `dropOnResourceLimit`                                                                   |
| `name`                                                                                  |
| `postfix`                                                                               |
| `prefix`                                                                                |
| `selectorAware`                                                                         |
| `setOriginalDestination`                                                                |
| `transactedSend`                                                                        |

## Amazon MQ Parent Element Attributes

The following is a detailed explanation of parent element attributes. For more
information, see [XML
Configuration](http://activemq.apache.org/xml-configuration.html "http://activemq.apache.org/xml-configuration.html") in the Apache ActiveMQ documentation.

###### Topics

- [broker](#broker-element "#broker-element")

### broker

`broker` is a parent collection element.

#### Attributes

##### networkConnectionStartAsync

To mitigate network latency and to allow other networks to start in a
timely manner, use the `<networkConnectionStartAsync>` tag.
The tag instructs the broker to use an executor to start network connections
in parallel, asynchronous to a broker start.

**Default:**
`false`

#### Example Configuration

```
<broker networkConnectorStartAsync="false"/>
```
