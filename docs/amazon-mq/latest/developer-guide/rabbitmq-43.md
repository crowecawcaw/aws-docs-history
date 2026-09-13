

# RabbitMQ 4.3
<a name="rabbitmq-43"></a>

 Amazon MQ now supports RabbitMQ 4.3 in the RabbitMQ 4 release series on the mq.m7g instance type across all supported instance sizes. RabbitMQ 4.3 introduces quorum queue enhancements, new exchange types, and completes the removal of several features that were deprecated in earlier 4.x releases. For more information about this release, see the [RabbitMQ 4.3.0 release notes](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.0) on the GitHub website. 

**Important**  
 Amazon MQ only supports upgrading to RabbitMQ 4.3 from RabbitMQ 4.2. You cannot upgrade directly from RabbitMQ 3.13 to 4.3. If your broker is running RabbitMQ 3.13, you must first upgrade to RabbitMQ 4.2 before upgrading to 4.3. 

## Breaking changes in RabbitMQ 4.3 on Amazon MQ
<a name="rabbitmq-43-breaking-changes"></a>

The following open-source changes might impact your applications when upgrading to RabbitMQ 4.3. Review these changes before upgrading your broker.
+ **Transient non-exclusive queues are rejected:** Declaring a queue that is both non-durable and non-exclusive now returns an error. Amazon MQ for RabbitMQ 4.3 removed support for this feature. Use durable queues, exclusive queues, or durable queues with [queue TTL](https://www.rabbitmq.com/docs/ttl#queue-ttl) on the RabbitMQ website instead.
+ **Global QoS is rejected:** Calling `basic.qos` with `global=true` now returns a channel error. Amazon MQ for RabbitMQ 4.3 removed support for this feature. Use per-consumer prefetch (`global=false`) instead. For more information about this change, see [Removal of global QoS](https://www.rabbitmq.com/blog/2021/08/21/4.0-deprecation-announcements#removal-of-global-qos) on the RabbitMQ website.
+ **Classic queue v1 storage is removed:** Declaring a queue with `x-queue-version=1` now returns an error. Classic queue v2 is the only supported storage engine. Amazon MQ has enforced v2 since RabbitMQ 3.12, so existing queues are not affected.
+ **Consumer timeout no longer applies to classic queues:** Classic queues no longer evaluate consumer timeouts. If a consumer becomes stuck at the application level, RabbitMQ does not automatically redeliver messages. The `consumer_timeout` setting continues to apply to quorum queues. If your application relies on consumer timeout for classic queues, consider migrating to quorum queues or implementing application-level heartbeat checks. For more information about this change, see the [RabbitMQ 4.3.0 release notes](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.0) on the GitHub website.

## New features and enhancements in RabbitMQ 4.3 on Amazon MQ
<a name="rabbitmq-43-new-features"></a>
+ **Quorum queue strict priority:** Quorum queues now support strict priority ordering with up to 32 levels (0–31), enabled with the `x-max-priority` queue argument. Higher-priority messages are always delivered before lower-priority messages. This replaces the 2-level ratio-based delivery introduced in RabbitMQ 4.2. For more information about quorum queue priorities, see [Quorum queue priorities](https://www.rabbitmq.com/docs/quorum-queues#priorities) on the RabbitMQ website.
+ **Quorum queue delayed retry:** Quorum queues support delayed retry with configurable increasing backoff. You can configure retry behavior by using queue arguments or policy keys (`delayed-retry-type`, `delayed-retry-min`, `delayed-retry-max`). For more information about quorum queues, see [Quorum queues](https://www.rabbitmq.com/docs/quorum-queues) on the RabbitMQ website.
+ **Granular consumer timeout for quorum queues:** Consumer timeout can now be set per-consumer, per-queue, or by using a policy. This provides finer control than the previous broker-wide `consumer_timeout` setting.
+ **Delivery limit changeable by using a policy:** The quorum queue delivery limit can now be updated by using a policy without requiring queue redeclaration.
+ **Consistent hash exchange (x-modulus-hash):** The `x-modulus-hash` exchange type is now built into RabbitMQ core. This exchange type distributes messages across bound queues by using consistent hashing of the routing key, enabling workload sharding without client-side logic. For more information about consistent hash exchanges, see [Consistent hash exchange](https://www.rabbitmq.com/docs/consistent-hash-exchange) on the RabbitMQ website.

**Important**  
 If you are upgrading from RabbitMQ 4.2, note the following change to message delivery. Existing messages with priorities previously mapped to high (≥5) or normal (0–4) are now delivered using strict ordering. As a result, lower-priority messages might be starved while higher-priority messages remain in the queue. RabbitMQ 4.2 used 2:1 ratio-based delivery, which guaranteed progress on normal-priority messages. 