# Getting started with Watch in Serverless

ElastiCache supports the `WATCH` command, which allows you to monitor keys for changes and execute conditional [transactions](https://valkey.io/topics/transactions/ "https://valkey.io/topics/transactions/").

The `WATCH` command is particularly useful for applications that require optimistic concurrency control, ensuring that transactions are only executed if the monitored keys have not been modified.
This includes modifications made by a client, like write commands, and by Valkey itself, like expiration or eviction.
If keys were modified from the time they were set in `WATCH` and by the time `EXEC` is received, the entire transaction will be aborted.

For ElastiCache Serverless, the following constraints are introduced -

ElastiCache Serverless `WATCH` is scoped to a single hash slot.
That means only keys that map to the same hash slot can be watched at the same time by the same connection, and the transaction that follows the watch commands can only operate on the same hash slot.
When an application attempts to watch keys from different hash slots, or execute transaction commands that operate on keys mapped to a different hash slot than the watched keys', a `CROSSSLOT` error will be returned.
[Hash tags](https://valkey.io/topics/cluster-spec/#hash-tags "https://valkey.io/topics/cluster-spec/#hash-tags") can be used to ensure multiple keys are mapped to the same hash slot.

Additionally, `SCAN` command cannot be executed inside a connection with watched keys and will return `command not supported during watch state` error.

The transaction will be aborted (as if watched keys were touched) when ElastiCache Serverless has no certainty of whether a key was modified.
For example, when a slot has been migrated and the watched keys cannot be found on the same node.

**Code Examples**

In the following example, the watched key and the key specified in the `SET` command map to different hash slots. The execution returns a `CROSSSLOT ERROR`.

```

> WATCH foo:{005119}
OK
> MULTI
OK
> SET bar:{011794} 1234
QUEUED
> EXEC
CROSSSLOT Keys in request don't hash to the same slot

```

The following example shows a successful transaction, as The key set in `WATCH` wasn't changed.

```

> WATCH foo:{005119}
OK
> MULTI
OK
> SET bar:{005119} 1234
QUEUED
> EXEC
1) OK

```

In the following example, an attempt to `WATCH` keys from different slots simultaneously within the same client connection returns a `CROSSSLOT ERROR`.

```

> WATCH foo:{005119}
OK
> WATCH bar:{123455}
CROSSSLOT Keys in request don't hash to the same slot

```

## Watch limit

Every client connection can watch up to 1000 keys at the same time.

## Supported commands related to Watch

[WATCH](https://valkey.io/commands/watch/ "https://valkey.io/commands/watch/") and [UNWATCH](https://valkey.io/commands/unwatch/ "https://valkey.io/commands/unwatch/") commands are documented on the [Valkey.io](https://valkey.io/ "https://valkey.io/") website. It provides a comprehensive overview of the commands, including its syntax, behavior, return values, and potential error conditions.
