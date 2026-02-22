# Using time to live (TTL) in DynamoDB

Time To Live (TTL) for DynamoDB is a cost-effective method for deleting items that are no
longer relevant. TTL allows you to define a per-item expiration timestamp that indicates
when an item is no longer needed. DynamoDB automatically deletes expired items within a few
days of their expiration time, without consuming write throughput.

To use TTL, first enable it on a table and then define a specific attribute to store the
TTL expiration timestamp. The timestamp must be stored as a [Number](HowItWorks.md#HowItWorks.DataTypes "HowItWorks.md#HowItWorks.DataTypes")
data type in [Unix epoch time
format](https://en.wikipedia.org/wiki/Unix_time "https://en.wikipedia.org/wiki/Unix_time") at the seconds granularity. Items with a TTL attribute that is not a
Number type are ignored by the TTL process. Each time an item is created or updated, you
can compute the expiration time and save it in the TTL attribute.

Items with valid, expired TTL attributes may be deleted by the system at any time, typically within a few days of their expiration. You can still update the expired items that are pending deletion, including changing or removing their TTL attributes. While updating an expired item, we recommended that you use a condition expression to make sure the item has not been subsequently deleted. Use filter expressions to remove expired items from [Scan](Scan.md#Scan.FilterExpression "Scan.md#Scan.FilterExpression") and [Query](Query.md "Query.md") results.

Deleted items work similarly to those deleted through typical delete operations. Once
deleted, items go into DynamoDB Streams as service deletions instead of user deletes, and are
removed from local secondary indexes and global secondary indexes just like other delete
operations.

If you are using [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") of
global tables and you also use the TTL feature, DynamoDB replicates TTL deletes to all replica
tables. The initial TTL delete does not consume Write Capacity Units (WCU) in the region in
which the TTL expiry occurs. However, the replicated TTL delete to the replica table(s)
consumes a replicated Write Capacity Unit when using provisioned capacity, or Replicated
Write Unit when using on-demand capacity mode, in each of the replica regions and applicable
charges will apply.

For more information about TTL, see these topics:

###### Topics

- [Enable time to live (TTL) in DynamoDB](time-to-live-ttl-how-to.md "time-to-live-ttl-how-to.md")
- [Computing time to live (TTL) in DynamoDB](time-to-live-ttl-before-you-start.md "time-to-live-ttl-before-you-start.md")
- [Working with expired items and time to live (TTL)](ttl-expired-items.md "ttl-expired-items.md")
