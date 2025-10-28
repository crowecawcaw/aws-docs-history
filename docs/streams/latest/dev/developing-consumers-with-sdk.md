# Develop shared-throughput consumers with the

AWS SDK for Java

One of the methods for developing custom Kinesis Data Streams consumers with shared throughout is to use
the Amazon Kinesis Data Streams APIs with the AWS SDK for Java. This section describes using the Kinesis Data Streams APIs with
the AWS SDK for Java. You can call the Kinesis Data Streams APIs using other different programming languages.
For more information about all available AWS SDKs, see [Start Developing with Amazon Web
Services](https://aws.amazon.com/developers/getting-started/ "https://aws.amazon.com/developers/getting-started/").

The Java sample code in this section demonstrates how to perform basic Kinesis Data Streams API
operations, and is divided up logically by operation type. These examples don't
represent production-ready code. They don't check for all possible exceptions or account
for all possible security or performance considerations.

###### Topics

- [Get data from a stream](#kinesis-using-sdk-java-get-data "#kinesis-using-sdk-java-get-data")
- [Use shard
  iterators](#kinesis-using-sdk-java-get-data-shard-iterators "#kinesis-using-sdk-java-get-data-shard-iterators")
- [Use GetRecords](#kinesis-using-sdk-java-get-data-getrecords "#kinesis-using-sdk-java-get-data-getrecords")
- [Adapt to a reshard](#kinesis-using-sdk-java-get-data-reshard "#kinesis-using-sdk-java-get-data-reshard")

## Get data from a stream

The Kinesis Data Streams APIs include the `getShardIterator` and `getRecords`
methods that you can invoke to retrieve records from a data stream. This is the pull
model, where your code draws data records directly from the shards of the data
stream.

###### Important

We recommend that you use the record processor support provided by KCL to
retrieve records from your data streams. This is the push model, where you implement
the code that processes the data. The KCL retrieves data records from the
data stream and delivers them to your application code. In addition, the
KCL provides failover, recovery, and load balancing functionality. For more
information, see [Developing Custom Consumers with Shared Throughput Using KCL](shared-throughput-kcl-consumers.md "shared-throughput-kcl-consumers.md").

However, in some cases you might prefer to use the Kinesis Data Streams APIs. For example, to
implement custom tools for monitoring or debugging your data streams.

###### Important

Kinesis Data Streams supports changes to the data record retention period of your data stream.
For more information, see [Change the data retention period](kinesis-extended-retention.md "kinesis-extended-retention.md").

## Use shard

iterators

You retrieve records from the stream on a per-shard basis. For each shard, and for
each batch of records that you retrieve from that shard, you must obtain a
_shard iterator_. The shard iterator is used in the
`getRecordsRequest` object to specify the shard from which records are to
be retrieved. The type associated with the shard iterator determines the point in the
shard from which the records should be retrieved (see later in this section for more
details). Before you can work with the shard iterator, you must retrieve the shard.
For more information, see [List shards](kinesis-using-sdk-java-list-shards.md "kinesis-using-sdk-java-list-shards.md").

Obtain the initial shard iterator using the `getShardIterator` method.
Obtain shard iterators for additional batches of records using the
`getNextShardIterator` method of the `getRecordsResult` object
returned by the `getRecords` method. A shard iterator is valid for 5 minutes.
If you use a shard iterator while it is valid, you get a new one. Each shard iterator
remains valid for 5 minutes, even after it is used.

To obtain the initial shard iterator, instantiate `GetShardIteratorRequest`
and pass it to the `getShardIterator` method. To configure the request,
specify the stream and the shard ID. For information about how to obtain the streams in
your AWS account, see [List streams](kinesis-using-sdk-java-list-streams.md "kinesis-using-sdk-java-list-streams.md"). For information about how to
obtain the shards in a stream, see [List shards](kinesis-using-sdk-java-list-shards.md "kinesis-using-sdk-java-list-shards.md").

```
String shardIterator;
GetShardIteratorRequest getShardIteratorRequest = new GetShardIteratorRequest();
getShardIteratorRequest.setStreamName(myStreamName);
getShardIteratorRequest.setShardId(shard.getShardId());
getShardIteratorRequest.setShardIteratorType("TRIM_HORIZON");

GetShardIteratorResult getShardIteratorResult = client.getShardIterator(getShardIteratorRequest);
shardIterator = getShardIteratorResult.getShardIterator();
```

This sample code specifies `TRIM_HORIZON` as the iterator type when
obtaining the initial shard iterator. This iterator type means that records should be
returned beginning with the first record added to the shard—rather than beginning
with the most recently added record, also known as the _tip_. The
following are possible iterator types:

- `AT_SEQUENCE_NUMBER`
- `AFTER_SEQUENCE_NUMBER`
- `AT_TIMESTAMP`
- `TRIM_HORIZON`
- `LATEST`

For more information, see [ShardIteratorType](../../../kinesis/latest/APIReference/API_GetShardIterator.md#Kinesis-GetShardIterator-request-ShardIteratorType "../../../kinesis/latest/APIReference/API_GetShardIterator.md#Kinesis-GetShardIterator-request-ShardIteratorType").

Some iterator types require that you specify a sequence number in addition to the
type; for example:

```
getShardIteratorRequest.setShardIteratorType("AT_SEQUENCE_NUMBER");
getShardIteratorRequest.setStartingSequenceNumber(specialSequenceNumber);
```

After you obtain a record using `getRecords`, you can get the sequence
number for the record by calling the record's `getSequenceNumber` method.

```
record.getSequenceNumber()
```

In addition, the code that adds records to the data stream can get the sequence number
for an added record by calling `getSequenceNumber` on the result of
`putRecord`.

```
lastSequenceNumber = putRecordResult.getSequenceNumber();
```

You can use sequence numbers to guarantee strictly increasing ordering of records. For
more information, see the code example in [PutRecord
example](developing-producers-with-sdk.md#kinesis-using-sdk-java-putrecord-example "developing-producers-with-sdk.md#kinesis-using-sdk-java-putrecord-example").

## Use GetRecords

After you obtain the shard iterator, instantiate a `GetRecordsRequest`
object. Specify the iterator for the request using the `setShardIterator`
method.

Optionally, you can also set the number of records to retrieve using the
`setLimit` method. The number of records returned by
`getRecords` is always equal to or less than this limit. If you do not
specify this limit, `getRecords` returns 10 MB of retrieved
records. The sample code below sets this limit to 25 records.

If no records are returned, that means no data records are currently available from
this shard at the sequence number referenced by the shard iterator. In this situation,
your application should wait for an amount of time that's appropriate for the data
sources for the stream. Then try to get data from the shard again
using the shard iterator returned by the preceding call to `getRecords`.

Pass the `getRecordsRequest` to the `getRecords` method, and
capture the returned value as a `getRecordsResult` object. To get the data
records, call the `getRecords` method on the `getRecordsResult`
object.

```

GetRecordsRequest getRecordsRequest = new GetRecordsRequest();
getRecordsRequest.setShardIterator(shardIterator);
getRecordsRequest.setLimit(25);

GetRecordsResult getRecordsResult = client.getRecords(getRecordsRequest);
List<Record> records = getRecordsResult.getRecords();

```

To prepare for another call to `getRecords`, obtain the next shard iterator
from `getRecordsResult`.

```

shardIterator = getRecordsResult.getNextShardIterator();

```

For best results, sleep for at least 1 second (1,000 milliseconds) between calls to
`getRecords` to avoid exceeding the limit on `getRecords`
frequency.

```

try {
  Thread.sleep(1000);
}
catch (InterruptedException e) {}

```

Typically, you should call `getRecords` in a loop, even when you're
retrieving a single record in a test scenario. A single call to `getRecords`
might return an empty record list, even when the shard contains more records at later
sequence numbers. When this occurs, the `NextShardIterator` returned along
with the empty record list references a later sequence number in the shard, and
successive `getRecords` calls eventually returns the records. The following
sample demonstrates the use of a loop.

###### Example: getRecords

The following code example reflects the `getRecords` tips in this
section, including making calls in a loop.

```

// Continuously read data records from a shard
List<Record> records;

while (true) {

  // Create a new getRecordsRequest with an existing shardIterator
  // Set the maximum records to return to 25

  GetRecordsRequest getRecordsRequest = new GetRecordsRequest();
  getRecordsRequest.setShardIterator(shardIterator);
  getRecordsRequest.setLimit(25);

  GetRecordsResult result = client.getRecords(getRecordsRequest);

  // Put the result into record list. The result can be empty.
  records = result.getRecords();

  try {
    Thread.sleep(1000);
  }
  catch (InterruptedException exception) {
    throw new RuntimeException(exception);
  }

  shardIterator = result.getNextShardIterator();
}

```

If you are using the Kinesis Client Library, it might make multiple calls before returning
data. This behavior is by design and does not indicate a problem with the KCL
or your data.

## Adapt to a reshard

If `getRecordsResult.getNextShardIterator` returns `null`, it
indicates that a shard split or merge has occurred that involved this shard.
This shard is now in a `CLOSED` state and you have read all available data
records from this shard.

In this scenario, you can use `getRecordsResult.childShards` to learn
about the new child shards of the shard that is being processed that were created by the
split or merge. For more information, see [ChildShard](../../../kinesis/latest/APIReference/API_ChildShard.md "../../../kinesis/latest/APIReference/API_ChildShard.md").

In the case of a split, the two new shards both have `parentShardId` equal
to the shard ID of the shard that you were processing previously. The value of
`adjacentParentShardId` for both of these shards is `null`.

In the case of a merge, the single new shard created by the merge has
`parentShardId` equal to shard ID of one of the parent shards and
`adjacentParentShardId` equal to the shard ID of the other parent shard.
Your application has already read all the data from one of these shards. This is the
shard for which `getRecordsResult.getNextShardIterator` returned
`null`. If the order of the data is important to your application, ensure
that it also reads all the data from the other parent shard before reading any new data
from the child shard created by the merge.

If you are using multiple processors to retrieve data from the stream (say, one
processor per shard), and a shard split or merge occurs, adjust the number of processors
up or down to adapt to the change in the number of shards.

For more information about resharding, including a discussion of shards
states—such as `CLOSED`—see [Reshard a stream](kinesis-using-sdk-java-resharding.md "kinesis-using-sdk-java-resharding.md").
