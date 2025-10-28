# Using change streams with Amazon DocumentDB

The change streams feature in Amazon DocumentDB (with MongoDB compatibility) provides
a time-ordered sequence of change events that occur within your cluster’s
collections. You can read events from a change stream to implement many
different use cases, including the following:

- Change notification
- Full-text search with Amazon OpenSearch Service (OpenSearch Service)
- Analytics with Amazon Redshift
  Applications can use change streams to subscribe to data changes on individual collections. Change streams events are ordered as they occur on the cluster and are stored for 3 hours (by default) after the event has been recorded. The retention period can be extended up to 7 days using the `change_stream_log_retention_duration` parameter. To modify the change stream retention period, please see [Modifying the Change Stream Log Retention Duration](change_streams.md#change_streams-modifying_log_retention "change_streams.md#change_streams-modifying_log_retention") .

###### Topics

- [Supported operations](#change_streams-supported_ops "#change_streams-supported_ops")
- [Billing](#change_streams-billing "#change_streams-billing")
- [Limitations](#change_streams-limitations "#change_streams-limitations")
- [Enabling change streams](#change_streams-enabling "#change_streams-enabling")
- [Example: using change
  streams with Python](#change_streams-using_example "#change_streams-using_example")
- [Full document lookup](#change_streams-lookup "#change_streams-lookup")
- [Resuming a change stream](#change_streams-resuming "#change_streams-resuming")
- [Resuming a change stream with startAtOperationTime](#change_streams-startAtOperation "#change_streams-startAtOperation")
- [Resuming a change stream with postBatchResumeToken](#change_streams-postBatchResumeToken "#change_streams-postBatchResumeToken")
- [Transactions in change streams](#change_streams-transactions "#change_streams-transactions")
- [Modifying the
  change stream log retention duration](#change_streams-modifying_log_retention "#change_streams-modifying_log_retention")
- [Using change streams on secondary instances](#change-streams-secondary-instances "#change-streams-secondary-instances")

## Supported operations

Amazon DocumentDB supports the following operations for change streams:

- All change events supported in the MongoDB `db.collection.watch()`, `db.watch()` and `client.watch()` API.
- Full document lookup for updates.
- Aggregation stages: `$match`, `$project`, `$redact`, and `$addFields`and `$replaceRoot`.
- Resuming a change stream from a resume token
- Resuming a change stream from a timestamp using `startAtOperation` (applicable to Amazon DocumentDB 4.0+)

## Billing

The Amazon DocumentDB change streams feature is disabled by default and does not incur any additional charges until the feature is enabled. Using change streams in a cluster incurs additional read and write IOs and storage costs. You can use the `modifyChangeStreams` API operation to enable this feature for your cluster. For more information on pricing, see [Amazon DocumentDB pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

## Limitations

Change streams have the following limitations in Amazon DocumentDB:

- On Amazon DocumentDB 3.6. and Amazon DocumentDB 4.0, change streams can only be opened from a connection to the primary instance of an Amazon DocumentDB cluster.
  Reading from change streams on a replica instance is not supported on Amazon DocumentDB 3.6. and Amazon DocumentDB 4.0.
  When invoking the `watch()` API operation, you must specify a `primary` read preference to ensure that all reads are directed to the primary instance (see the [Example](#change_streams-using_example "#change_streams-using_example") section).
- On Amazon DocumentDB 5.0, change streams can be opened from both primary instance and secondary instances, including global clusters.
  You can specify a secondary read preference to redirect the change streams to secondary instances.
  See [Using change streams on secondary instances](#change-streams-secondary-instances "#change-streams-secondary-instances") for additional best practices and limitations.
- Events written to a change stream for a collection are available for up to 7 days (the default is 3 hours). Change streams data is deleted after the log retention duration window, even if no new changes have occurred.
- A long-running write operation on a collection like
  `updateMany` or `deleteMany` can temporarily
  stall the writing of change streams events until the long running
  write operation is complete.
- Amazon DocumentDB does not support the MongoDB operations log
  (`oplog`).
- With Amazon DocumentDB, you must explicitly enable change streams on a given
  collection.
- If the total size of a change streams event (including the change
  data and full document, if requested) is greater than
  `16 MB`, the client will experience a read failure on the
  change streams.
- The Ruby driver is currently not supported when using `db.watch()` and `client.watch()` with Amazon DocumentDB 3.6.
- The output from the `updateDescription` command in change streams is different in Amazon DocumentDB than in MongoDB when the updated value of the field is the same as the previous one:
  - Amazon DocumentDB doesn't return a field in the `updateDescription` output if the provided field is specified in the `$set` command and its target value is already equal to the source value.
  - MongoDB returns the field in the output, even if the specified value is equal to the current value.

## Enabling change streams

You can enable Amazon DocumentDB change streams for all collections within a
given database, or only for selected collections. The following are
examples of how to enable change streams for different use cases using the
mongo shell. Empty strings are treated as wildcards when specifying
database and collection names.

```
//Enable change streams for the collection "foo" in database "bar"
db.adminCommand({modifyChangeStreams: 1,
    database: "bar",
    collection: "foo",
    enable: true});
```

```
//Disable change streams on collection "foo" in database "bar"
db.adminCommand({modifyChangeStreams: 1,
    database: "bar",
    collection: "foo",
    enable: false});
```

```
//Enable change streams for all collections in database "bar"
db.adminCommand({modifyChangeStreams: 1,
    database: "bar",
    collection: "",
    enable: true});
```

```
//Enable change streams for all collections in all databases in a cluster
db.adminCommand({modifyChangeStreams: 1,
    database: "",
    collection: "",
    enable: true});
```

Change streams will be enabled for a collection if any of the
following are true:

- Both the database and collection are explicitly enabled.
- The database containing the collection is enabled.
- All databases are enabled.

Dropping a collection from a database does not disable change streams for that collection if the parent database also has change streams enabled, or if all databases in the cluster are enabled. If a new collection is created with the same name as the deleted collection, change streams will be enabled for that collection.

You can list all of your cluster’s enabled change streams by using the `$listChangeStreams` aggregation pipeline stage. All aggregation stages supported by Amazon DocumentDB can be used in the pipeline for additional processing. If a previously enabled collection has been disabled, it will not appear in the `$listChangeStreams` output.

```
//List all databases and collections with change streams enabled
cursor = new DBCommandCursor(db,
    db.runCommand(
        {aggregate: 1,
        pipeline: [{$listChangeStreams: 1}],
        cursor:{}}));
```

```
//List of all databases and collections with change streams enabled
{ "database" : "test", "collection" : "foo" }
{ "database" : "bar", "collection" : "" }
{ "database" : "", "collection" : "" }
```

```
//Determine if the database “bar” or collection “bar.foo” have change streams enabled
cursor = new DBCommandCursor(db,
  db.runCommand(
      {aggregate: 1,
       pipeline: [{$listChangeStreams: 1},
                  {$match: {$or: [{database: "bar", collection: "foo"},
                                  {database: "bar", collection: ""},
                                  {database: "", collection: ""}]}}
                 ],
      cursor:{}}));
```

## Example: using change

streams with Python

The following is an example of using an Amazon DocumentDB change stream with
Python at the collection level.

```
import os
import sys
from pymongo import MongoClient, ReadPreference

username = "DocumentDBusername"
password = <Insert your password>

clusterendpoint = "DocumentDBClusterEndpoint”
client = MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='global-bundle.pem')

db = client['bar']

#While ‘Primary’ is the default read preference, here we give an example of
#how to specify the required read preference when reading the change streams
coll = db.get_collection('foo', read_preference=ReadPreference.PRIMARY)
#Create a stream object
stream = coll.watch()
#Write a new document to the collection to generate a change event
coll.insert_one({'x': 1})
#Read the next change event from the stream (if any)
print(stream.try_next())

"""
Expected Output:
{'_id': {'_data': '015daf94f600000002010000000200009025'},
'clusterTime': Timestamp(1571788022, 2),
'documentKey': {'_id': ObjectId('5daf94f6ea258751778163d6')},
'fullDocument': {'_id': ObjectId('5daf94f6ea258751778163d6'), 'x': 1},
'ns': {'coll': 'foo', 'db': 'bar'},
'operationType': 'insert'}
"""

#A subsequent attempt to read the next change event returns nothing, as there are no new changes
print(stream.try_next())

"""
Expected Output:
None
"""

#Generate a new change event by updating a document
result = coll.update_one({'x': 1}, {'$set': {'x': 2}})
print(stream.try_next())

"""
Expected Output:
{'_id': {'_data': '015daf99d400000001010000000100009025'},
'clusterTime': Timestamp(1571789268, 1),
'documentKey': {'_id': ObjectId('5daf9502ea258751778163d7')},
'ns': {'coll': 'foo', 'db': 'bar'},
'operationType': 'update',
'updateDescription': {'removedFields': [], 'updatedFields': {'x': 2}}}
"""
```

The following is an example of using an Amazon DocumentDB change stream with Python at the database level.

```
import os
import sys
from pymongo import MongoClient

username = "DocumentDBusername"
password = <Insert your password>
clusterendpoint = "DocumentDBClusterEndpoint”
client = MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='global-bundle.pem')

db = client['bar']
#Create a stream object
stream = db.watch()
coll = db.get_collection('foo')
#Write a new document to the collection foo to generate a change event
coll.insert_one({'x': 1})

#Read the next change event from the stream (if any)
print(stream.try_next())

"""
Expected Output:
{'_id': {'_data': '015daf94f600000002010000000200009025'},
'clusterTime': Timestamp(1571788022, 2),
'documentKey': {'_id': ObjectId('5daf94f6ea258751778163d6')},
'fullDocument': {'_id': ObjectId('5daf94f6ea258751778163d6'), 'x': 1},
'ns': {'coll': 'foo', 'db': 'bar'},
'operationType': 'insert'}
"""
#A subsequent attempt to read the next change event returns nothing, as there are no new changes
print(stream.try_next())

"""
Expected Output:
None
"""

coll = db.get_collection('foo1')

#Write a new document to another collection to generate a change event
coll.insert_one({'x': 1})
print(stream.try_next())

"""
Expected Output: Since the change stream cursor was the database level you can see change events from different collections in the same database
{'_id': {'_data': '015daf94f600000002010000000200009025'},
'clusterTime': Timestamp(1571788022, 2),
'documentKey': {'_id': ObjectId('5daf94f6ea258751778163d6')},
'fullDocument': {'_id': ObjectId('5daf94f6ea258751778163d6'), 'x': 1},
'ns': {'coll': 'foo1', 'db': 'bar'},
'operationType': 'insert'}
"""
```

## Full document lookup

The update change event does not include the full document; it includes only the change that was made. If your use case requires the complete document affected by an update, you can enable full document lookup when opening the stream.

The `fullDocument` document for an update change streams
event represents the most current version of the updated document at the
time of document lookup. If changes occurred between the update operation
and the `fullDocument` lookup, the `fullDocument`
document might not represent the document state at update time.

To create a stream object with update lookup enabled, use this example:

```
stream = coll.watch(full_document='updateLookup')

#Generate a new change event by updating a document
result = coll.update_one({'x': 2}, {'$set': {'x': 3}})

stream.try_next()
```

The output of the stream object will look something like this:

```
{'_id': {'_data': '015daf9b7c00000001010000000100009025'},
'clusterTime': Timestamp(1571789692, 1),
'documentKey': {'_id': ObjectId('5daf9502ea258751778163d7')},
'fullDocument': {'_id': ObjectId('5daf9502ea258751778163d7'), 'x': 3},
'ns': {'coll': 'foo', 'db': 'bar'},
'operationType': 'update',
'updateDescription': {'removedFields': [], 'updatedFields': {'x': 3}}}
```

## Resuming a change stream

You can resume a change stream later by using a resume token, which is equal to the `_id` field of the last retrieved change event document.

```
import os
import sys
from pymongo import MongoClient

username = "DocumentDBusername"
password = <Insert your password>
clusterendpoint = "DocumentDBClusterEndpoint”
client = MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='global-bundle.pem', retryWrites='false')

db = client['bar']
coll = db.get_collection('foo')
#Create a stream object
stream = db.watch()
coll.update_one({'x': 1}, {'$set': {'x': 4}})
event = stream.try_next()
token = event['_id']
print(token)

"""
Output: This is the resume token that we will later us to resume the change stream
{'_data': '015daf9c5b00000001010000000100009025'}
"""
#Python provides a nice shortcut for getting a stream’s resume token
print(stream.resume_token)

"""
Output
{'_data': '015daf9c5b00000001010000000100009025'}
"""
#Generate a new change event by updating a document
result = coll.update_one({'x': 4}, {'$set': {'x': 5}})
#Generate another change event by inserting a document
result = coll.insert_one({'y': 5})
#Open a stream starting after the selected resume token
stream = db.watch(full_document='updateLookup', resume_after=token)
#Our first change event is the update with the specified _id
print(stream.try_next())

"""
#Output: Since we are resuming the change stream from the resume token, we will see all events after the first update operation. In our case, the change stream will resume from the update operation {x:5}

{'_id': {'_data': '015f7e8f0c000000060100000006000fe038'},
'operationType': 'update',
'clusterTime': Timestamp(1602129676, 6),
'ns': {'db': 'bar', 'coll': 'foo'},
'documentKey': {'_id': ObjectId('5f7e8f0ac423bafbfd9adba2')},
'fullDocument': {'_id': ObjectId('5f7e8f0ac423bafbfd9adba2'), 'x': 5},
'updateDescription': {'updatedFields': {'x': 5}, 'removedFields': []}}
"""
#Followed by the insert
print(stream.try_next())

"""
#Output:
{'_id': {'_data': '015f7e8f0c000000070100000007000fe038'},
'operationType': 'insert',
'clusterTime': Timestamp(1602129676, 7),
'ns': {'db': 'bar', 'coll': 'foo'},
'documentKey': {'_id': ObjectId('5f7e8f0cbf8c233ed577eb94')},
'fullDocument': {'_id': ObjectId('5f7e8f0cbf8c233ed577eb94'), 'y': 5}}
"""
```

## Resuming a change stream with `startAtOperationTime`

You can resume a change stream later from a particular time stamp by using `startAtOperationTime`.

###### Note

The ability to use `startAtOperationTime` is available in Amazon DocumentDB 4.0+. When using `startAtOperationTime`, the change stream cursor will only return changes that occurred at or after the specified Timestamp. The `startAtOperationTime` and `resumeAfter` commands are mutually exclusive and thus cannot be used together.

```
import os
import sys
from pymongo import MongoClient

username = "DocumentDBusername"
password = <Insert your password>
clusterendpoint = "DocumentDBClusterEndpoint”
client = MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='rds-root-ca-2020.pem',retryWrites='false')
db = client['bar']
coll = db.get_collection('foo')
#Create a stream object
stream = db.watch()
coll.update_one({'x': 1}, {'$set': {'x': 4}})
event = stream.try_next()
timestamp = event['clusterTime']
print(timestamp)
"""
Output
Timestamp(1602129114, 4)
"""
#Generate a new change event by updating a document
result = coll.update_one({'x': 4}, {'$set': {'x': 5}})
result = coll.insert_one({'y': 5})
#Generate another change event by inserting a document
#Open a stream starting after specified time stamp

stream = db.watch(start_at_operation_time=timestamp)
print(stream.try_next())

"""
#Output: Since we are resuming the change stream at the time stamp of our first update operation (x:4), the change stream cursor will point to that event
{'_id': {'_data': '015f7e941a000000030100000003000fe038'},
'operationType': 'update',
'clusterTime': Timestamp(1602130970, 3),
'ns': {'db': 'bar', 'coll': 'foo'},
'documentKey': {'_id': ObjectId('5f7e9417c423bafbfd9adbb1')},
'updateDescription': {'updatedFields': {'x': 4}, 'removedFields': []}}
"""

print(stream.try_next())
"""
#Output: The second event will be the subsequent update operation (x:5)
{'_id': {'_data': '015f7e9502000000050100000005000fe038'},
'operationType': 'update',
'clusterTime': Timestamp(1602131202, 5),
'ns': {'db': 'bar', 'coll': 'foo'},
'documentKey': {'_id': ObjectId('5f7e94ffc423bafbfd9adbb2')},
'updateDescription': {'updatedFields': {'x': 5}, 'removedFields': []}}
"""

print(stream.try_next())

"""
#Output: And finally the last event will be the insert operation (y:5)
{'_id': {'_data': '015f7e9502000000060100000006000fe038'},
'operationType': 'insert',
'clusterTime': Timestamp(1602131202, 6),
'ns': {'db': 'bar', 'coll': 'foo'},
'documentKey': {'_id': ObjectId('5f7e95025c4a569e0f6dde92')},
'fullDocument': {'_id': ObjectId('5f7e95025c4a569e0f6dde92'), 'y': 5}}
"""
```

## Resuming a change stream with `postBatchResumeToken`

Amazon DocumentDB change stream now returns an additional field called `postBatchResumeToken`.
This field is returned from the `$changestream` command and `getMore` command.

Example of the `$changestream` command in Python:

```
db.command({"aggregate": "sales", "pipeline": [{ "$changeStream": {}}], "cursor": {"batchSize": 1}})
```

Expected output:

```
cursor" : {
   "firstBatch" : [ ],
   "postBatchResumeToken" : {"_data" : "0167c8cbe60000000004"},
   "id" : NumberLong("9660788144470"),
   "ns" : "test.sales"
}
```

Example of the `getMore` command in Python:

```
db.command({"getMore": NumberLong(<cursor id>), "collection": "sales", "batchSize": 1 })
```

Expected output

```
cursor" : {
   "nextBatch" : [ ],
   "postBatchResumeToken" : {"_data" : "0167c8cbe60000000004"},
   "id" : NumberLong("9660788144470"),
   "ns" : "test.sales"
}
```

The `postBatchResumeToken` field can be used to open new change stream cursors in the `resumeAfter` field, similar to how the resume token is used.

Open a stream starting after the selected `postBatchResumeToken`:

```
post_batch_resume_token = output['cursor']['postBatchResumeToken']
stream = db.watch(full_document='updateLookup', resume_after=post_batch_resume_token)
```

Unlike a regular resume token that always corresponds to an operations log (oplog) entry that reflects an actual event, `postBatchResumeToken` corresponds to an oplog entry the change stream has scanned up to on the server, which is not necessarily a matching change.

Attempting to resume with an old regular resume token will force the database to scan all the oplog entries between the specified time stamp and the current time.
This may generate a lot of queries internally with each sub-query scanning for a small period of time.
This will cause a spike in CPU usage and degrade the database performance.
Resuming with the last `postBatchResumeToken` skips the scanning of unmatched oplog entries.

## Transactions in change streams

Change stream events will not contain events from uncommitted and/or aborted transactions. For example, if you start a transaction with one `INSERT` operation and one `UPDATE` operation, and if your `INSERT` operation succeeds, but the `UPDATE` operation fails, the transaction will be rolled back. Since this transaction was rolled back, your change stream will not contain any events for this transaction.

## Modifying the

change stream log retention duration

You can modify the change stream log retention duration to be between 1 hour and 7 days using the AWS Management Console or the AWS CLI.

Using the AWS Management Console

###### To modify the change stream log retention duration

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Parameter groups** .

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the **Parameter groups** pane, choose the
cluster parameter group that is associated with your cluster. To
identify the cluster parameter group that is associated with your
cluster, see [Determining an Amazon DocumentDB cluster's parameter group](cluster_parameter_groups-describe.md#cluster_parameter_groups-determine "cluster_parameter_groups-describe.md#cluster_parameter_groups-determine"). 4. The resulting page shows the parameters and their corresponding details for your cluster parameter group. Select the parameter `change_stream_log_retention_duration`. 5. On the top right of the page, choose **Edit** to change the value of the parameter.
The `change_stream_log_retention_duration` parameter can be modified to be between 1 hour and 7 days. 6. Make your change, and then choose **Modify cluster
parameter** to save the changes. To discard your changes,
choose **Cancel**.

Using the AWS CLI
To modify your cluster parameter group's
`change_stream_log_retention_duration` parameter, use the
`modify-db-cluster-parameter-group` operation with the
following parameters:

- `--db-cluster-parameter-group-name`
  — Required. The name of the cluster parameter group that
  you are modifying. To identify the cluster parameter group that
  is associated with your cluster, see [Determining an Amazon DocumentDB cluster's parameter group](cluster_parameter_groups-describe.md#cluster_parameter_groups-determine "cluster_parameter_groups-describe.md#cluster_parameter_groups-determine").
- `--parameters` —
  Required. The parameter that you are modifying. Each parameter
  entry must include the following:
  - `ParameterName`
    — The name of the parameter that you are modifying.
    In this case, it is `change_stream_log_retention_duration`
  - `ParameterValue`
    — The new value for this parameter.
  - `ApplyMethod`
    — How you want changes to this parameter applied.
    Permitted values are `immediate` and
    `pending-reboot`.

  ###### Note

  Parameters with the `ApplyType` of `static` must have an `ApplyMethod` of `pending-reboot`.

1. To change the values of the parameter
   `change_stream_log_retention_duration`, run the
   following command and replace `parameter-value` with
   the value you want to modify the parameter to.

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name sample-parameter-group \
    --parameters "ParameterName=change_stream_log_retention_duration,ParameterValue=<parameter-value>,ApplyMethod=immediate"
```

For Windows:

```
aws docdb modify-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name sample-parameter-group ^
    --parameters "ParameterName=change_stream_log_retention_duration,ParameterValue=<parameter-value>,ApplyMethod=immediate"
```

Output from this operation looks something like the following (JSON format).

```
{
    "DBClusterParameterGroupName": "sample-parameter-group"
}
```

2. Wait at least 5 minutes.
3. List the parameter values of `sample-parameter-group`
   to ensure that your changes have been made.

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameters \
    --db-cluster-parameter-group-name sample-parameter-group
```

For Windows:

```
aws docdb describe-db-cluster-parameters ^
    --db-cluster-parameter-group-name sample-parameter-group
```

Output from this operation looks something like the following (JSON format).

```
{
    "Parameters": [
        {
            "ParameterName": "audit_logs",
            "ParameterValue": "disabled",
            "Description": "Enables auditing on cluster.",
            "Source": "system",
            "ApplyType": "dynamic",
            "DataType": "string",
            "AllowedValues": "enabled,disabled",
            "IsModifiable": true,
            "ApplyMethod": "pending-reboot"
        },
        {
            `"ParameterName": "change_stream_log_retention_duration"`,
            `"ParameterValue": "12345"`,
            "Description": "Duration of time in seconds that the change stream log is retained and can be consumed.",
            "Source": "user",
            "ApplyType": "dynamic",
            "DataType": "integer",
            "AllowedValues": "3600-86400",
            "IsModifiable": true,
            "ApplyMethod": "immediate"
        }
    ]
}
```

###### Note

Change stream log retention will not delete logs older than the configured `change_stream_log_retention_duration` value until log size is greater than (>) 51,200MB.

## Using change streams on secondary instances

To get started on using change stream on secondary instances, open the change stream cursor with `readPreference` as the secondary.

You can open a change stream cursor to watch for change events on a specific collection or all collections in a cluster or database.
You can open a change stream cursor on any Amazon DocumentDB instance and fetch change stream documents from both writer and reader instances.
You can share change stream tokens (such as `resumeToken` or `startOperationTime`) across different change stream cursors opened on a writer and reader instance.

**Example**

```
import os
import sys
from pymongo import MongoClient, ReadPreference

username = "DocumentDBusername"
password = <Your password>

clusterendpoint = "DocumentDBClusterEndpoint"

client = MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='global-bundle.pem')

db = client['bar']

# Make sure to use SECONDARY to redirect cursor reads from secondary instances
coll = db.get_collection('foo', read_preference=ReadPreference.SECONDARY)

# Create a stream object on RO. The token needs to generated from PRIMARY.
stream = coll.watch(resumeAfter=token)

for event in stream:
   print(event)
```

**Guidelines and limitations for change streams on secondary instances**

- Change stream events need to be replicated from the primary instance to the secondary instances.
  You can monitor the lag from the `DBInstanceReplicaLag` metric in Amazon CloudWatch.
- Timestamps on secondary instances may not always be in sync with the primary instance.
  In this case, expect delays on the secondary instance timestamp so it can catch up.
  As a best practice, we recommend using `startAtOperationTime` or `resumeToken` to start the watch on the secondary instance.
- You might experience lower throughput on secondary instances compared to the primary instance if your document size is large, you are doing `fullDocumentLookup`, and there is high concurrent write workload on the primary instance.
  As a best practice, we recommend you monitor your buffer cache hit ratio on the secondary and make sure that buffer cache hit ratio is high.
