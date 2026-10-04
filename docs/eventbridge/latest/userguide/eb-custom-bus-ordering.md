

# Ordering and deduplicating events on a Custom Event Bus
<a name="eb-custom-bus-ordering"></a>

Ordering is a property of a subscriber. Deduplication happens when you publish. The two are configured in different places and solve different problems.

## Ordering
<a name="eb-custom-bus-ordering-fifo"></a>

A subscriber's `Type` is `UNORDERED` or `FIFO`. An unordered subscriber delivers events in parallel for the highest throughput. A FIFO subscriber delivers events in the order that they were published within an *event group*. You assign the group when you publish, with `SystemMetadata.EventGroupId` in each entry of either publish API.

An event group belongs to the account that published it. Two accounts that publish to a shared bus with the same `EventGroupId` create two separate groups: their events are not ordered relative to each other, and they do not share a group's throughput. For the group limits, see [Custom Event Bus quotas](eb-quota.md#eb-custom-bus-quotas).

Within a FIFO subscriber, an event that cannot be delivered holds up the later events in its own group while other groups continue. Keep group identifiers bounded, for example a customer identifier or an order identifier, and do not derive them from unbounded input. A FIFO target such as an Amazon SQS FIFO queue enforces its own length and character limits on the group identifier.

A FIFO subscriber accepts `InvocationType` `EVENT` for a Lambda target, but order then holds only up to the hand-off into Lambda's asynchronous queue. Use `REQUEST_RESPONSE` for ordered processing.

## Deduplication at publish time
<a name="eb-custom-bus-ordering-dedup"></a>

You deduplicate either by setting `DeduplicationType=CONTENT_BASED` on the request or by setting `SystemMetadata.DeduplicationId` on each entry.
+ Set `--deduplication-configuration DeduplicationType=CONTENT_BASED` on the request. EventBridge hashes the content of each entry and suppresses an entry whose hash it has already accepted.
+ Omit `DeduplicationConfiguration` and set `SystemMetadata.DeduplicationId` on each entry to a key that you already have, such as an idempotency key from your producer.

EventBridge suppresses a duplicate that arrives within 5 minutes (300 seconds) of the entry it repeats. The check is scoped to your account, and to the event group when the entry carries an `EventGroupId`: an entry with the same key from another account, or in another group, is a different event. An entry without an `EventGroupId` is still deduplicated, across all of your account's ungrouped entries on that bus.

Together, this gives exactly-once ingestion: a duplicate publish within the window is suppressed at the bus, and a FIFO subscriber then hands each accepted event to its target once, in order, within its group.

Either way, a suppressed duplicate returns `SuccessCode: DEDUPLICATED`. Treat it as a success. Code that counts every success as a new event overstates delivery. EventBridge bills content-based deduplication as a separate operation, so prefer a `DeduplicationId` when your producer already has a key. For pricing, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/). For the content types that deduplication applies to, see [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md).