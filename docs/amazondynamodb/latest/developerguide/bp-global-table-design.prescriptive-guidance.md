# Write modes with DynamoDB global tables

Global tables are always active-active at the table level. However, especially for MREC
tables, you might want to treat them as active-passive by controlling how you route write
requests. For example, you might decide to route write requests to a single Region to avoid
potential write conflicts that can happen with MREC tables.

There are three main managed write patterns, as explained in the next three sections.
You should consider which write pattern fits your use case. This choice affects how you route
requests, evacuate a Region, and handle disaster recovery. The guidance in later sections
depends on your application’s write mode.

## Write to any Region mode (no primary)

The _write to any Region_ mode, illustrated in the
following diagram, is fully active-active and doesn’t impose restrictions on where a write
may occur. Any Region may accept a write at any time. This is the simplest mode, but it can
only be used with some types of applications. This mode is suitable for all MRSC tables.
It’s also suitable for MREC tables when all writers are idempotent, and therefore safely
repeatable so that concurrent or repeated write operations across Regions are not in
conflict. For example, when a user updates their contact data. This mode also works well for
a special case of being idempotent, an append-only dataset where all writes are unique
inserts under a deterministic primary key. Lastly, this mode is suitable for MREC where the
risk of conflicting writes would be acceptable.

![Diagram of how client writes to any region works.](images/gt-client-read-write-to-any-region2.png)

The _write to any Region_ mode is the most
straightforward architecture to implement. Routing is easier because any Region can be the
write target at any time. Failover is easier, because with MRSC tables, the items are always
synchronized, and with MRSC tables, any recent writes can be replayed any number of times to
any secondary Region. Where possible, you should design for this write mode.

For example, several video streaming services use global tables for tracking bookmarks,
reviews, watch status flags, and so on. These deployments use MREC tables because they need
replicas scattered around the world, with each replica providing low-latency read and write
operations. These deployments can use the _write to any
Region_ mode as long as they ensure that every write operation is idempotent.
This will be the case if every update―for example, setting a new latest time code, assigning
a new review, or setting a new watch status―assigns the user’s new state directly, and the
next correct value for an item doesn’t depend on its current value. If, by chance, the
user’s write requests are routed to different Regions, the last write operation will persist
and the global state will settle according to the last assignment. Read operations in this
mode will eventually become consistent, delayed by the latest
`ReplicationLatency` value.

In another example, a financial services firm uses global tables as part of a system
to maintain a running tally of debit card purchases for each customer, to calculate that
customer’s cash-back rewards. They want to keep a `RunningBalance` item per
customer. This write mode is not naturally idempotent because as transactions stream in,
they modify the balance by using an `ADD` expression where the new correct value
depends on the current value. By using MRSC tables they can still _write to any Region_, because every `ADD` call always operates
against the very latest value of the item.

A third example involves a company that provides online ad placement services. This
company decided that a low risk of data loss would be acceptable to achieve the design
simplifications of the _write to any Region_ mode. When
they serve ads, they have just a few milliseconds to retrieve enough metadata to determine
which ad to show, and then to record the ad impression so they don’t repeat the same ad
soon. They use global tables to get both low-latency read operations for end users across
the world and low-latency write operations. They record all ad impressions for a user within
a single item, which is represented as a growing list. They use one item instead of
appending to an item collection, so they can remove older ad impressions as part of each
write operation without paying for a delete operation. This write operation is not
idempotent; if the same end user sees ads served out of multiple Regions at approximately
the same time, there’s a chance that one write operation for an ad impression could
overwrite another. The risk is that a user might see an ad repeated once in a while. They
decided that this is acceptable.

## Write to one Region (single primary)

The _write to one Region_ mode, illustrated in the
following diagram, is active-passive and routes all table writes to a single active region.
Note that DynamoDB doesn’t have a notion of a single active region; the application routing
outside DynamoDB manages this. The _write to one Region_ mode
works well for MREC tables that need to avoid write conflicts by ensuring that write
operations flow only to one Region at a time. This write mode helps when you want to use
conditional expressions and can't use MRSC for some reason, or when you need to perform
transactions. These expressions aren’t possible unless you know that you’re acting against
the latest data, so they require sending all write requests to a single Region that has the
latest data.

When you use an MRSC table, you might choose to generally write to one Region for
convenience. For example, this can help minimize your infrastructure build-out beyond DynamoDB.
The write mode would still be write to any Region because with MRSC you could safely write
to any Region at any time without concern of conflict resolution that would cause MREC
tables to choose to _write to one Region_.

Eventually consistent reads can go to any replica Regions to achieve lower latencies.
Strongly consistent reads must go to the single primary Region.

![Diagram of how writing to one Region works.](images/gt-client-writes-one-region2.png)

It’s sometimes necessary to change the active Region in response to a Regional failure.
Some users change the currently active Region on a regular schedule, such as implementing a
follow-the-sun deployment. This places the active Region near the geography that has the
most activity (usually where it’s daytime, thus the name), which results in the lowest
latency read and write operations. It also has the side benefit of calling the
Region-changing code daily and making sure that it’s well tested before any disaster
recovery.

The passive Region(s) may keep a downscaled set of infrastructure surrounding DynamoDB that
gets built up only if it becomes the active Region. This guide doesn’t cover pilot light and
warm standby designs. For a more information, see [Disaster Recovery (DR) Architecture on AWS, Part III: Pilot Light and Warm
Standby](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/ "https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/").

Using the _write to one Region_ mode works well when
you use global tables for low-latency globally distributed read operations. An example is a
large social media company that needs to have the same reference data available in every
Region around the world. They don’t update the data often, but when they do, they write to
only one Region to avoid any potential write conflicts. Read operations are always allowed
from any Region.

As another example, consider the financial services company discussed earlier that
implemented the daily cash-back calculation. They used _write to any
Region_ mode to calculate the balance but _write to one
Region_ mode to track payments. This work requires transactions, which aren't
supported in MRSC tables, so it works better with a separate MREC table and _write to one Region_ mode.

## Write to your Region (mixed primary)

The _write to your Region_ write mode, illustrated in
the following diagram, works with MREC tables. It assigns different data subsets to
different home Regions and allows write operations to an item only through its home Region.
This mode is active-passive but assigns the active Region based on the item. Every Region is
primary for its own non-overlapping dataset, and write operations must be guarded to ensure
proper locality.

This mode is similar to _write to one Region_ except
that it enables lower-latency write operations, because the data associated with each user
can be placed in closer network proximity to that user. It also spreads the surrounding
infrastructure more evenly between Regions and requires less work to build out
infrastructure during a failover scenario, because all Regions have a portion of their
infrastructure already active.

![Diagram of how client writes to each item in a single Region works.](images/get-client-writes-each-item-single-region2.png)

You can determine the home Region for items in several ways:

- **Intrinsic:** Some aspect of the data, such as a special
  attribute or a value embedded within its partition key, makes its home Region clear.
  This technique is described in the blog post [Use Region pinning to set a home Region for items in an Amazon DynamoDB global
  table](https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/ "https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/").
- **Negotiated:** The home Region of each dataset is
  negotiated in some external manner, such as with a separate global service that
  maintains assignments. The assignment may have a finite duration after which it’s
  subject to renegotiation.
- **Table-oriented:** Instead of creating a single
  replicating global table, you create the same number of global tables as replicating
  Regions. Each table’s name indicates its home Region. In standard operations, all data
  is written to the home Region while other Regions keep a read-only copy. During a
  failover, another Region temporarily adopts write duties for that table.

For example, imagine that you’re working for a gaming company. You need low-latency read
and write operations for all gamers around the world. You assign each gamer to the Region
that’s closest to them. That Region takes all their read and write operations, ensuring
strong read-after-write consistency. However, when a gamer travels or if their home Region
suffers an outage, a complete copy of their data is available in alternative Regions, and
the gamer can be assigned to a different home Region.

As another example, imagine that you’re working at a video conferencing company. Each
conference call’s metadata is assigned to a particular Region. Callers can use the Region
that’s closest to them for lowest latency. If there’s a Region outage, using global tables
allows quick recovery because the system can move the processing of the call to a different
Region where a replicated copy of the data already exists.

###### To summarize

- Write to any Region mode is suitable for MRSC tables and idempotent calls to MREC
  tables.
- Write to one Region mode is suitable for non-idempotent calls to MREC tables.
- Write to your Region mode is suitable for non-idempotent calls to MREC tables, where
  it's important to have clients write to a Region that’s close to them.
