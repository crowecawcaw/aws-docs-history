# Evacuation processes

Evacuating a Region is the process of migrating activity, usually read and write
activity or read activity, away from that Region.

## Evacuating a live Region

You might decide to evacuate a live Region for a number of reasons: as part of usual
business activity (for example, if you’re using a follow-the-sun, write to one Region mode),
due to a business decision to change the currently active Region, in response to failures in
the software stack outside DynamoDB, or because you’re encountering general issues such as
higher than usual latencies within the Region.

With _write to any Region_ mode, evacuating a live
Region is straightforward. You can route traffic to alternative Regions by using any routing
system and let the write operations in the evacuated Region replicate over as usual.

The write to one Region and write to your Region modes are usually used with MREC
tables. Therefore, you must make sure that all write operations to the active Region have
been fully recorded, stream processed, and globally propagated before starting write
operations in the new active Region, to ensure that future write operations are processed
against the latest version of the data.

Let’s say that Region A is active and Region B is passive (either for the full table
or for items that are homed in Region A). The typical mechanism to perform an evacuation is
to pause write operations to A, wait long enough for those operations to have fully
propagated to B, update the architecture stack to recognize B as active, and then resume
write operations to B. There is no metric to indicate with absolute certainty that Region A
has fully replicated its data to Region B. If Region A is healthy, pausing write operations
to Region A and waiting 10 times the recent maximum value of the
`ReplicationLatency` metric would typically be sufficient to determine that
replication is complete. If Region A is unhealthy and shows other areas of increased
latencies, you would choose a larger multiple for the wait time.

## Evacuating an offline Region

There’s a special case to consider: What if Region A goes fully offline without
notice? This is extremely unlikely but should be considered nevertheless.

Evacuating an offline MRSC table

If this happens with an MRSC table, there is nothing special you need to do. MRSC
tables support a recovery point objective (RPO) of zero. All successful write
operations made to the MRSC table in the offline Region will be available in all other
Region tables, so there's no potential gap in data even if the Region goes fully
offline without notice. Business can continue using replicas located in the other
Regions.

Evacuating an offline MREC table

If this happens with an MREC table, any write operations in Region A that were not
yet propagated are held and propagated after Region A comes back online. The write
operations aren’t lost, but their propagation is indefinitely delayed.

How to proceed in this event is the application’s decision. For business
continuity, write operations might need to proceed to the new primary Region B.
However, if an item in Region B receives an update while there is a pending
propagation of a write operation for that item from Region A, the propagation is
suppressed under the _last writer wins_ model. Any
update in Region B might suppress an incoming write request.

With the _write to any Region_ mode, read and
write operations can continue in Region B, trusting that the items in Region A will
propagate to Region B eventually and recognizing the potential for missing items until
Region A comes back online. When possible, such as with idempotent write operations,
you should consider replaying recent write traffic (for example, by using an upstream
event source) to fill in the gap of any potentially missing write operations and let
the last writer wins conflict resolution suppress the eventual propagation of the
incoming write operation.

With the other write modes, you have to consider the degree to which work can
continue with a slightly out-of-date view of the world. Some small duration of write
operations, as tracked by `ReplicationLatency`, will be missing until
Region A comes back online. Can business move forward? In some use cases it can, but
in others it might not without additional mitigation mechanisms.

For example, imagine that you have to maintain an available credit balance without
interruption even after a full outage of a Region. You could split the balance into
two different items, one homed in Region A and one in Region B, and start each with
half the available balance. This would use the _write to your
Region_ mode. Transactional updates processed in each Region would write
against the local copy of the balance. If Region A goes fully offline, work could
still proceed with transaction processing in Region B, and write operations would be
limited to the balance portion held in Region B. Splitting the balance like this
introduces complexities when the balance gets low or the credit has to be rebalanced,
but it does provide one example of safe business recovery even with uncertain pending
write operations.

As another example, imagine that you’re capturing web form data. You can use
[Optimistic Concurrency
Control (OCC)](DynamoDBMapper.md "DynamoDBMapper.md") (OCC) to assign versions to data items and embed the
latest version into the web form as a hidden field. On each submit, the write
operation succeeds only if the version in the database still matches the version that
the form was built against. If the versions don’t match, the web form can be refreshed
(or carefully merged) based on the current version in the database, and the user can
proceed again. The OCC model usually protects against another client overwriting and
producing a new version of the data, but it can also help during failover where a
client might encounter older versions of data. Let’s imagine that you’re using the
timestamp as the version. The form was first built against Region A at 12:00 but
(after failover) tries to write to Region B and notices that the latest version in the
database is 11:59. In this scenario, the client can either wait for the 12:00 version
to propagate to Region B and then write on top of that version, or build on 11:59 and
create a new 12:01 version (which, after writing, would suppress the incoming version
after Region A recovers).

As a third example, a financial services company holds data about customer
accounts and their financial transactions in a DynamoDB database. In the event of a
complete Region A outage, they want to make sure that any write activity related to
their accounts is either fully available in Region B, or they want to quarantine their
accounts as known partial until Region A comes back online. Instead of pausing all
business, they decided to pause business only to the tiny fraction of accounts that
they determined had unpropagated transactions. To achieve this, they used a third
Region, which we will call Region C. Before they processed any write operations in
Region A, they placed a succinct summary of those pending operations (for example, a
new transaction count for an account) in Region C. This summary was sufficient for
Region B to determine if its view was fully up to date. This action effectively locked
the account from the time of writing in Region C until Region A accepted the write
operations and Region B received them. The data in Region C wasn’t used except as part
of a failover process, after which Region B could cross-check its data with Region C
to check if any of its accounts were out of date. Those accounts would be marked as
quarantined until the Region A recovery propagated the partial data to Region B. If
Region C were to fail, a new Region D could be spun up for use instead. The data in
Region C was very transient, and after a few minutes Region D would have a
sufficiently up-to-date record of the in-flight write operations to be fully useful.
If Region B were to fail, Region A could continue accepting write requests in
cooperation with Region C. This company was willing to accept higher latency writes
(to two Regions: C and then A) and was fortunate to have a data model where the state
of an account could be succinctly summarized.
