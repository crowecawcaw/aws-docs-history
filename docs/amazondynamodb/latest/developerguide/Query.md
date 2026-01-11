# Other aspects of working with the Query operation in

DynamoDB

This section covers additional aspects of the DynamoDB Query operation, including
limiting result size, counting scanned vs. returned items, monitoring read capacity
consumption, and controlling read consistency.

## Limiting the number of items in the result set

With the `Query` operation, you can limit the number of items that it
reads. To do this, set the `Limit` parameter to the maximum number of
items that you want.

For example, suppose that you `Query` a table, with a
`Limit` value of `6`, and without a filter expression. The
`Query` result contains the first six items from the table that match
the key condition expression from the request.

Now suppose that you add a filter expression to the `Query`. In this
case, DynamoDB reads up to six items, and then returns only those that match the filter
expression. The final `Query` result contains six items or fewer, even if
more items would have matched the filter expression if DynamoDB had kept reading more
items.

## Counting the items in the results

In addition to the items that match your criteria, the `Query` response
contains the following elements:

- `ScannedCount` — The number of items that matched the key
  condition expression _before_ a filter
  expression (if present) was applied.
- `Count` — The number of items that remain _after_ a filter expression (if present) was
  applied.

###### Note

If you don't use a filter expression, `ScannedCount` and
`Count` have the same value.

If the size of the `Query` result set is larger than
1 MB, `ScannedCount` and `Count` represent only
a partial count of the total items. You need to perform multiple `Query`
operations to retrieve all the results (see [Paginating table query results in DynamoDB](Query.md "Query.md")).

Each `Query` response contains the `ScannedCount` and
`Count` for the items that were processed by that particular
`Query` request. To obtain grand totals for all of the
`Query` requests, you could keep a running tally of both
`ScannedCount` and `Count`.

## Capacity units consumed by query

You can `Query` any table or secondary index, as long as you provide the name of
the partition key attribute and a single value for that attribute.
`Query` returns all items with that partition key value. Optionally,
you can provide a sort key attribute and use a comparison operator to refine the
search results. `Query` API operations consume read capacity units, as
follows.

| If you `Query` a...    | DynamoDB consumes read capacity units from... |
| ---------------------- | --------------------------------------------- |
| Table                  | The table's provisioned read capacity.        |
| Global secondary index | The index's provisioned read capacity.        |
| Local secondary index  | The base table's provisioned read capacity.   |

By default, a `Query` operation does not return any data on how much
read capacity it consumes. However, you can specify the
`ReturnConsumedCapacity` parameter in a `Query` request to
obtain this information. The following are the valid settings for
`ReturnConsumedCapacity`:

- `NONE` — No consumed capacity data is returned. (This is
  the default.)
- `TOTAL` — The response includes the aggregate number of
  read capacity units consumed.
- `INDEXES` — The response shows the aggregate number of
  read capacity units consumed, together with the consumed capacity for each
  table and index that was accessed.

DynamoDB calculates the number of read capacity units consumed based on the number of
items and the size of those items, not on the amount of data that is returned to an
application. For this reason, the number of capacity units consumed is the same
whether you request all of the attributes (the default behavior) or just some of
them (using a projection expression). The number is also the same whether or not you
use a filter expression. `Query` consumes a minimum read capacity unit to
perform one strongly consistent read per second, or two eventually consistent reads
per second for an item up to 4 KB. If you need to read an item that is larger than 4
KB, DynamoDB needs additional read request units. Empty tables and very large tables
which have a sparse amount of partition keys might see some additional RCUs charged
beyond the amount of data queried. This covers the cost of serving the
`Query` request, even if no data exists.

## Read consistency for query

A `Query` operation performs eventually consistent reads, by default.
This means that the `Query` results might not reflect changes due to
recently completed `PutItem` or `UpdateItem` operations. For
more information, see [DynamoDB read consistency](HowItWorks.md "HowItWorks.md").

If you require strongly consistent reads, set the `ConsistentRead`
parameter to `true` in the `Query` request.
