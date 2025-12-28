# DynamoDB read consistency

Amazon DynamoDB reads data from tables, local secondary indexes (LSIs), global secondary
indexes (GSIs), and streams. For more information, see [Core components of Amazon DynamoDB](HowItWorks.md "HowItWorks.md").
Both tables and LSIs provide two read consistency options: _eventually consistent_ (default) and _strongly
consistent_ reads. All reads from GSIs and streams are eventually
consistent.

When your application writes data to a DynamoDB table and receives an HTTP 200 response
(OK), that means the write completed successfully and has been durably persisted. DynamoDB
provides _read-committed_ isolation and ensures that
read operations always return committed values for an item. The read will never present
a view to the item from a write which did not ultimately succeed. Read-committed
isolation does not prevent modifications of the item immediately after the read
operation.

## Eventually consistent

reads

Eventually consistent is the default read consistent model for all read
operations. When issuing eventually consistent reads to a DynamoDB table or an index,
the responses may not reflect the results of a recently completed write operation.
If you repeat your read request after a short time, the response should eventually
return the more recent item. Eventually consistent reads are supported on tables,
local secondary indexes, and global secondary indexes. Also note that all reads from
a DynamoDB stream are also eventually consistent.

Eventually consistent reads are half the cost of strongly consistent reads. For
more information, see [Amazon DynamoDB](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/") pricing.

## Strongly consistent

reads

Read operations such as `GetItem`, `Query`, and
`Scan` provide an optional `ConsistentRead` parameter. If
you set `ConsistentRead` to true, DynamoDB returns a response with the most
up-to-date data, reflecting the updates from all prior write operations that were
successful. Strongly consistent reads are only supported on tables and local
secondary indexes. Strongly consistent reads from a global secondary index or a
DynamoDB stream are not supported.

## Global tables read

consistency

DynamoDB also supports [global tables](GlobalTables.md "GlobalTables.md") for
multi-active and multi-Region replication. A global table is composed of multiple
replica tables in different AWS Regions. Any change made to any item in any
replica table is replicated to all the other replicas within the same global table,
typically within a second, and are eventually consistent. For more information, see
[Consistency modes](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes "V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes").
