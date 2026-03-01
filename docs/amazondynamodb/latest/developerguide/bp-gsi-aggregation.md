# Using Global Secondary Indexes for materialized aggregation queries in DynamoDB

Maintaining near real-time aggregations and key metrics on top of rapidly changing data is
becoming increasingly valuable to businesses for making rapid decisions. For example, a music
library might want to showcase its most downloaded songs in near-real time, or an e-commerce
platform might need to display trending products by category.

Because DynamoDB doesn't natively support aggregation operations like `SUM` or
`COUNT` across items, computing these values at read time would require scanning
large numbers of items—which may be slow and expensive. Instead, you can
_pre-compute_ aggregations as data changes and store the results as
regular items in your table. This pattern is called _materialized
aggregation_.

###### Topics

- [Example scenario and access patterns](#bp-gsi-aggregation-scenario "#bp-gsi-aggregation-scenario")
- [Why pre-compute aggregations](#bp-gsi-aggregation-why "#bp-gsi-aggregation-why")
- [Table design](#bp-gsi-aggregation-table-design "#bp-gsi-aggregation-table-design")
- [Aggregation pipeline with Streams and AWS Lambda](#bp-gsi-aggregation-pipeline "#bp-gsi-aggregation-pipeline")
- [Sparse GSI design](#bp-gsi-aggregation-sparse-gsi "#bp-gsi-aggregation-sparse-gsi")
- [Querying the GSI](#bp-gsi-aggregation-querying "#bp-gsi-aggregation-querying")
- [Considerations](#bp-gsi-aggregation-considerations "#bp-gsi-aggregation-considerations")

## Example scenario and access patterns

Consider a music library application with the following requirements:

- The application records individual song downloads at high volume (thousands
  per second).
- Users need to see the most downloaded songs for a given month with
  single-digit millisecond latency.
- The application also needs to support queries like "top 10 songs this month"
  and "all songs downloaded in a given month."

Computing download counts at read time by scanning all download records may be expensive at this scale. Instead, you can maintain a running count that updates
as each download occurs, and store it in a way that supports efficient querying.

## Why pre-compute aggregations

There are several approaches to computing aggregations. The following table compares
common alternatives and explains why materialized aggregation in DynamoDB is often the best
fit for this type of use case.

| Approach                                                     | Tradeoffs                                                                                                                                                                         | When to use                                                                                                                                                        |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scan and count at read time                                  | Requires reading all download records for every query. Latency grows with data<br>volume and consumes significant read capacity.                                                  | Only suitable for very small datasets where latency isn't a concern.                                                                                               |
| External aggregation store (for example, Amazon ElastiCache) | Adds operational complexity with a separate service to manage. Requires<br>synchronization logic between DynamoDB and the cache.                                                  | When you need sub-millisecond reads or complex aggregation logic that goes<br>beyond simple counts.                                                                |
| Application-level aggregation on write                       | Couples the aggregation logic to the write path. If the application fails<br>after recording the download but before updating the count, the aggregation<br>becomes inconsistent. | When you need synchronous, strongly consistent aggregation and can tolerate<br>added write latency.                                                                |
| **Materialized aggregation with Streams and<br>Lambda**      | Decouples aggregation from the write path. Aggregation is eventually<br>consistent (typically seconds behind). Adds Lambda invocation costs.                                      | \*_When you need near real-time aggregations with low<br>read latency and can tolerate eventual consistency._<br>• This is the<br>approach described on this page. |

The materialized aggregation approach keeps the write path simple (just record the
download), offloads the aggregation to an asynchronous process, and stores the result in
DynamoDB where it can be queried with single-digit millisecond latency.

## Table design

This design uses a single table with two item types that share the same partition key
(`songID`) but use different sort key patterns to distinguish between them:

- **Download records** – Individual download
  events. The sort key is the `DownloadID` (a unique identifier for each
  download).
- **Monthly aggregation items** –
  Pre-computed download counts per song per month. The sort key is the month in
  `YYYY-MM` format (for example, `2018-01`). These items also contain
  a `DownloadCount` attribute with the running total.

Only the monthly aggregation items contain the `Month` attribute. This
distinction is important for the sparse GSI design described later.

The following diagram shows the table layout with both item types:

![Music library table layout showing download records and monthly aggregation items sharing the same partition key (songID).](images/AggregationQueries.png)

| Item type           | Partition key (songID) | Sort key          | Additional attributes                             |
| ------------------- | ---------------------- | ----------------- | ------------------------------------------------- |
| Download record     | `song1`                | `download-abc123` | `UserID`, `Timestamp`                             |
| Monthly aggregation | `song1`                | `2018-01`         | `Month`=`2018-01`,<br>`DownloadCount`=`1,746,992` |

## Aggregation pipeline with Streams and AWS Lambda

The aggregation pipeline works as follows:

1. When a song is downloaded, the application writes a new item to the table
   with `Partition-Key=songID` and `Sort-Key=DownloadID`.
2. DynamoDB Streams captures this write as a stream record.
3. A Lambda function, attached to the stream, processes the new record. It
   identifies the `songID` and the current month, then updates the corresponding
   monthly aggregation item by incrementing the `DownloadCount`
   attribute.
4. The updated aggregation item is then available for querying through the
   sparse GSI.

The Lambda function uses an `UpdateItem` call with an `ADD`
expression to atomically increment the download count. This avoids read-modify-write
race conditions:

```
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicLibrary')

def handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_image = record['dynamodb']['NewImage']
            song_id = new_image['songID']['S']
            # Derive the month from the download timestamp
            timestamp = new_image['Timestamp']['S']
            month = timestamp[:7]  # Extract YYYY-MM

            table.update_item(
                Key={
                    'songID': song_id,
                    'SK': month
                },
                UpdateExpression='ADD DownloadCount :inc SET #m = :month',
                ExpressionAttributeNames={
                    '#m': 'Month'
                },
                ExpressionAttributeValues={
                    ':inc': 1,
                    ':month': month
                }
            )
```

###### Note

If a Lambda execution fails after writing the updated aggregation value, the stream
record may be retried. Because the `ADD` operation increments the count each
time it runs, a retry would increment the count more than once for the same download,
leaving you with an _approximate_ value. For most analytics and
leaderboard use cases, this small margin of error is acceptable. If you need exact counts,
consider adding idempotency logic—for example, by using a condition expression that
checks whether the specific `DownloadID` has already been processed.

## Sparse GSI design

To efficiently query the aggregated results, create a global secondary index with the
following key schema:

- **GSI partition key:**
  `Month` (String)
- **GSI sort key:**
  `DownloadCount` (Number)

This GSI is _sparse_ because only the monthly aggregation items
contain the `Month` attribute. The individual download records don't have this
attribute, so they are automatically excluded from the index. This means the GSI contains
only the pre-computed aggregation items—a small fraction of the total items in the
table.

A sparse GSI provides two key benefits:

- **Lower cost** – Because only aggregation
  items are replicated to the index, you consume far less write capacity and storage compared
  to an index that includes every item in the table.
- **Faster queries** – The index contains
  only the data you need to query, so reads are efficient and return results with single-digit
  millisecond latency.

For more information about how sparse indexes work, see
[Take advantage of sparse indexes](bp-indexes-general-sparse-indexes.md "bp-indexes-general-sparse-indexes.md").

## Querying the GSI

With the sparse GSI in place, you can efficiently answer several types of queries:

**Get the most downloaded song for a given month:**

```
aws dynamodb query \
    --table-name "MusicLibrary" \
    --index-name "MonthDownloadsIndex" \
    --key-condition-expression "#m = :month" \
    --expression-attribute-names '{"#m": "Month"}' \
    --expression-attribute-values '{":month": {"S": "2018-01"}}' \
    --scan-index-forward false \
    --limit 1
```

Setting `ScanIndexForward` to `false` sorts results by
`DownloadCount` in descending order, and `Limit=1` returns only the
top song.

**Get the top 10 songs for a given month:**

```
aws dynamodb query \
    --table-name "MusicLibrary" \
    --index-name "MonthDownloadsIndex" \
    --key-condition-expression "#m = :month" \
    --expression-attribute-names '{"#m": "Month"}' \
    --expression-attribute-values '{":month": {"S": "2018-01"}}' \
    --scan-index-forward false \
    --limit 10
```

**Get all songs downloaded in a given month** (sorted by
download count):

```
aws dynamodb query \
    --table-name "MusicLibrary" \
    --index-name "MonthDownloadsIndex" \
    --key-condition-expression "#m = :month" \
    --expression-attribute-names '{"#m": "Month"}' \
    --expression-attribute-values '{":month": {"S": "2018-01"}}' \
    --scan-index-forward false
```

## Considerations

Keep the following in mind when implementing this pattern:

- **Eventual consistency** – The aggregation
  values are updated asynchronously through DynamoDB Streams and Lambda. There is typically a
  delay of a few seconds between a download being recorded and the aggregation being updated.
  This means the GSI reflects near real-time data, not real-time data.
- **Lambda concurrency** – If your table has
  a high write volume, multiple Lambda invocations may attempt to update the same aggregation
  item concurrently. The atomic `ADD` operation handles this safely, but you should
  monitor Lambda concurrency and throttling metrics to ensure your function can keep up with
  the stream.
- **GSI write capacity** – Because the
  sparse GSI only contains aggregation items, it requires significantly less write capacity
  than the base table. However, you should still provision enough capacity (or use on-demand
  mode) to handle the rate of aggregation updates.
- **Approximate counts** – As noted earlier,
  Lambda retries can cause counts to be slightly over-counted. For use cases that require
  exact counts, implement idempotency checks in the Lambda function.
