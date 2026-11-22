

# Ordering and deduplicating events on a Custom Event Bus

Ordering is a property of a subscriber. Deduplication happens when you publish. The two are configured in different places and solve different problems.

## Ordering
<a name="eb-custom-bus-ordering-fifo"></a>

A subscriber's `Type` is `UNORDERED` or `FIFO`. An unordered subscriber delivers events in parallel for the highest throughput. A FIFO subscriber delivers events in the order that they were published within an *event group*. You assign the group when you publish, with `SystemMetadata.EventGroupId` in each entry of either publish API.

An event group belongs to the account that published it. Two accounts that publish to a shared bus with the same `EventGroupId` create two separate groups: their events are not ordered relative to each other, and they do not share a group's throughput. For the group limits, see [Custom Event Bus quotas](eb-quota.md#eb-custom-bus-quotas).

Within a FIFO subscriber, a failed delivery holds up every event group, not only the group of the event that failed. One target call can carry events of several groups. If the call fails, EventBridge retries every event in it. While EventBridge retries, the subscriber reads no further events from the bus. EventBridge can still deliver other events that the subscriber had already read.

Later events of every group wait until the call succeeds or its retries run out. The subscriber's `RetryPolicy` sets those limits. For the limits, and for failures that EventBridge retries without limit, see [Retry limits](eb-custom-bus-retry.md#eb-custom-bus-retry-policy).

Keep group identifiers bounded, for example a customer identifier or an order identifier, and do not derive them from unbounded input. A FIFO target such as an Amazon SQS FIFO queue enforces its own length and character limits on the group identifier.

A FIFO subscriber accepts `InvocationType` `EVENT` for a Lambda target, but order then holds only up to the hand-off into Lambda's asynchronous queue. Use `REQUEST_RESPONSE` for ordered processing.

## Deduplication at publish time
<a name="eb-custom-bus-ordering-dedup"></a>

You deduplicate either by setting `DeduplicationType=CONTENT_BASED` on the request or by setting `SystemMetadata.DeduplicationId` on each entry.
+ Set `--deduplication-configuration DeduplicationType=CONTENT_BASED` on the request. EventBridge hashes the content of each entry and suppresses an entry whose hash it has already accepted.
+ Omit `DeduplicationConfiguration` and set `SystemMetadata.DeduplicationId` on each entry to a key that you already have, such as an idempotency key from your producer.

**Important**  
Content-based deduplication treats two entries as duplicates only when their `Data` payload and their customer `Metadata` map are both identical, not the payload alone. A `Metadata` value that differs on any entry, such as an offset or timestamp for each record, makes every entry unique. Content-based deduplication then never finds a match, and suppresses nothing. When you rely on content-based deduplication, put in `Metadata` only values that are equal across true duplicates. To key deduplication on something other than the full content, set `SystemMetadata.DeduplicationId` instead.

EventBridge suppresses a duplicate that arrives within 5 minutes (300 seconds) of the entry it repeats. The check is scoped to your account, and to the event group when the entry carries an `EventGroupId`: an entry with the same key from another account, or in another group, is a different event. An entry without an `EventGroupId` is still deduplicated, across all of your account's ungrouped entries on that bus.

Together, this gives exactly-once ingestion: a duplicate publish within the window is suppressed at the bus, and a FIFO subscriber then hands each accepted event to its target once, in order, within its group.

Either way, a suppressed duplicate returns `SuccessCode: DEDUPLICATED`. Treat it as a success. Code that counts every success as a new event overstates delivery. EventBridge bills content-based deduplication as a separate operation, so prefer a `DeduplicationId` when your producer already has a key. For pricing, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/). For the content types that deduplication applies to, see [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md).