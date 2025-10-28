# Using DynamoDB batch operations in

AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](tutorials-js.md "tutorials-js.md").

AWS AppSync supports using Amazon DynamoDB batch operations across one or more tables in a
single region. Supported operations are `BatchGetItem`,
`BatchPutItem`, and `BatchDeleteItem`. By using these features in
AWS AppSync, you can perform tasks such as:

- Pass a list of keys in a single query and return the results from a table
- Read records from one or more tables in a single query
- Write records in bulk to one or more tables
- Conditionally write or delete records in multiple tables that might have a
  relation
  Using batch operations with DynamoDB in AWS AppSync is an advanced technique that takes a
  little extra thought and knowledge of your backend operations and table structures.
  Additionally, batch operations in AWS AppSync have two key differences from non-batched
  operations:

- The data source role must have permissions to all tables which the resolver will
  access.
- The table specification for a resolver is part of the mapping template.

## Permissions

Like other resolvers, you need to create a data source in AWS AppSync and either
create a role or use an existing one. Because batch operations require different
permissions on DynamoDB tables, you need to grant the configured role permissions for read
or write actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "dynamodb:BatchGetItem",
 "dynamodb:BatchWriteItem"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:dynamodb:us-east-1:111122223333:table/TABLENAME",
 "arn:aws:dynamodb:us-east-1:111122223333:table/TABLENAME/*"
 ]
 }
 ]
}`

```

**Note**: Roles are tied to data sources in AWS AppSync,
and resolvers on fields are invoked against a data source. Data sources configured to
fetch against DynamoDB only have one table specified, to keep configuration simple.
Therefore, when performing a batch operation against multiple tables in a single
resolver, which is a more advanced task, you must grant the role on that data source
access to any tables the resolver will interact with. This would be done in the
**Resource** field in the IAM policy above.
Configuration of the tables to make batch calls against is done in the resolver
template, which we describe below.

## Data Source

For the sake of simplicity, we’ll use the same data source for all the resolvers used
in this tutorial. On the **Data sources** tab, create a new
DynamoDB data source and name it **BatchTutorial**. The table
name can be anything because table names are specified as part of the request mapping
template for batch operations. We will give the table name `empty`.

For this tutorial, any role with the following inline policy will work:

## Single Table Batch

###### Warning

`BatchPutItem` and `BatchDeleteItem` are not supported when
used with conflict detection and resolution. These settings must be disabled to
prevent possible errors.

For this example, suppose you have a single table named **Posts** to which you want to add and remove items with batch operations.
Use the following schema, noting that for the query, we’ll pass in a list of IDs:

```
type Post {
    id: ID!
    title: String
}

input PostInput {
    id: ID!
    title: String
}

type Query {
    batchGet(ids: [ID]): [Post]
}

type Mutation {
    batchAdd(posts: [PostInput]): [Post]
    batchDelete(ids: [ID]): [Post]
}

schema {
    query: Query
    mutation: Mutation
}
```

Attach a resolver to the `batchAdd()` field with the following **Request Mapping Template**. This automatically takes each item
in the GraphQL `input PostInput` type and builds a map, which is needed for
the `BatchPutItem` operation:

```
#set($postsdata = [])
#foreach($item in ${ctx.args.posts})
    $util.qr($postsdata.add($util.dynamodb.toMapValues($item)))
#end

{
    "version" : "2018-05-29",
    "operation" : "BatchPutItem",
    "tables" : {
        "Posts": $utils.toJson($postsdata)
    }
}
```

In this case, the **Response Mapping Template** is a
simple passthrough, but the table name is appended as `..data.Posts` to the
context object as follows:

```
$util.toJson($ctx.result.data.Posts)
```

Now navigate to the **Queries** page of the AWS AppSync
console and run the following **batchAdd** mutation:

```
mutation add {
    batchAdd(posts:[{
            id: 1 title: "Running in the Park"},{
            id: 2 title: "Playing fetch"
        }]){
            id
            title
    }
}
```

You should see the results printed to the screen, and can independently validate
through the DynamoDB console that both values wrote to the **Posts** table.

Next, attach a resolver to the `batchGet()` field with the following
**Request Mapping Template**. This automatically takes
each item in the GraphQL `ids:[]` type and builds a map that is needed for
the `BatchGetItem` operation:

```
#set($ids = [])
#foreach($id in ${ctx.args.ids})
    #set($map = {})
    $util.qr($map.put("id", $util.dynamodb.toString($id)))
    $util.qr($ids.add($map))
#end

{
    "version" : "2018-05-29",
    "operation" : "BatchGetItem",
    "tables" : {
        "Posts": {
            "keys": $util.toJson($ids),
            "consistentRead": true,
            "projection" : {
                "expression" : "#id, title",
                "expressionNames" : { "#id" : "id"}
                }
        }
    }
}
```

The **Response Mapping Template** is again a simple
passthrough, with again the table name appended as `..data.Posts` to the
context object:

```
$util.toJson($ctx.result.data.Posts)
```

Now go back to the **Queries** page of the AWS AppSync
console, and run the following **batchGet Query**:

```
query get {
    batchGet(ids:[1,2,3]){
        id
        title
    }
}
```

This should return the results for the two `id` values that you added
earlier. Note that a `null` value returned for the `id` with a
value of `3`. This is because there was no record in your **Posts** table with that value yet. Also note that AWS AppSync
returns the results in the same order as the keys passed in to the query, which is an
additional feature that AWS AppSync does on your behalf. So if you switch to
`batchGet(ids:[1,3,2)`, you’ll see the order changed. You’ll also know
which `id` returned a `null` value.

Finally, attach a resolver to the `batchDelete()` field with the following
**Request Mapping Template**. This automatically takes
each item in the GraphQL `ids:[]` type and builds a map that is needed for
the `BatchGetItem` operation:

```
#set($ids = [])
#foreach($id in ${ctx.args.ids})
    #set($map = {})
    $util.qr($map.put("id", $util.dynamodb.toString($id)))
    $util.qr($ids.add($map))
#end

{
    "version" : "2018-05-29",
    "operation" : "BatchDeleteItem",
    "tables" : {
        "Posts": $util.toJson($ids)
    }
}
```

The **Response Mapping Template** is again a simple
passthrough, with again the table name appended as `..data.Posts` to the
context object:

```
$util.toJson($ctx.result.data.Posts)
```

Now go back to the **Queries** page of the AWS AppSync
console, and run the following **batchDelete**
mutation:

```
mutation delete {
    batchDelete(ids:[1,2]){ id }
}
```

The records with `id`
`1` and `2` should now be deleted. If you re-run the
`batchGet()` query from earlier, these should return
`null`.

## Multi-Table Batch

###### Warning

`BatchPutItem` and `BatchDeleteItem` are not supported when
used with conflict detection and resolution. These settings must be disabled to
prevent possible errors.

AWS AppSync also enables you to perform batch operations across tables. Let’s build
a more complex application. Imagine we are building a Pet Health app, where sensors
report the pet location and body temperature. The sensors are battery powered and
attempt to connect to the network every few minutes. When a sensor establishes
connection, it sends its readings to our AWS AppSync API. Triggers then analyze the
data so a dashboard can be presented to the pet owner. Let’s focus on representing the
interactions between the sensor and the backend data store.

As a prerequisite, let’s first create two DynamoDB tables; **locationReadings** will store sensor location readings and **temperatureReadings** will store sensor temperature readings.
Both tables happen to share the same primary key structure: `sensorId
 (String)` being the partition key, and `timestamp (String)` the
sort key.

Let’s use the following GraphQL schema:

```
type Mutation {
    # Register a batch of readings
    recordReadings(tempReadings: [TemperatureReadingInput], locReadings: [LocationReadingInput]): RecordResult
    # Delete a batch of readings
    deleteReadings(tempReadings: [TemperatureReadingInput], locReadings: [LocationReadingInput]): RecordResult
}

type Query {
    # Retrieve all possible readings recorded by a sensor at a specific time
    getReadings(sensorId: ID!, timestamp: String!): [SensorReading]
}

type RecordResult {
    temperatureReadings: [TemperatureReading]
    locationReadings: [LocationReading]
}

interface SensorReading {
    sensorId: ID!
    timestamp: String!
}

# Sensor reading representing the sensor temperature (in Fahrenheit)
type TemperatureReading implements SensorReading {
    sensorId: ID!
    timestamp: String!
    value: Float
}

# Sensor reading representing the sensor location (lat,long)
type LocationReading implements SensorReading {
    sensorId: ID!
    timestamp: String!
    lat: Float
    long: Float
}

input TemperatureReadingInput {
    sensorId: ID!
    timestamp: String
    value: Float
}

input LocationReadingInput {
    sensorId: ID!
    timestamp: String
    lat: Float
    long: Float
}
```

### BatchPutItem - Recording

Sensor Readings

Our sensors need to be able to send their readings once they connect to the
internet. The GraphQL field `Mutation.recordReadings` is the API they
will use to do so. Let’s attach a resolver to bring our API to life.

Select **Attach** next to the
`Mutation.recordReadings` field. On the next screen, pick the same
`BatchTutorial` data source created at the beginning of the
tutorial.

Let’s add the following request mapping template:

**Request Mapping Template**

```
## Convert tempReadings arguments to DynamoDB objects
#set($tempReadings = [])
#foreach($reading in ${ctx.args.tempReadings})
    $util.qr($tempReadings.add($util.dynamodb.toMapValues($reading)))
#end

## Convert locReadings arguments to DynamoDB objects
#set($locReadings = [])
#foreach($reading in ${ctx.args.locReadings})
    $util.qr($locReadings.add($util.dynamodb.toMapValues($reading)))
#end

{
    "version" : "2018-05-29",
    "operation" : "BatchPutItem",
    "tables" : {
        "locationReadings": $utils.toJson($locReadings),
        "temperatureReadings": $utils.toJson($tempReadings)
    }
}
```

As you can see, the `BatchPutItem` operation allows us to specify
multiple tables.

Let’s use the following response mapping template.

**Response Mapping Template**

```
## If there was an error with the invocation
## there might have been partial results
#if($ctx.error)
    ## Append a GraphQL error for that field in the GraphQL response
    $utils.appendError($ctx.error.message, $ctx.error.message)
#end
## Also returns data for the field in the GraphQL response
$utils.toJson($ctx.result.data)
```

With batch operations, there can be both errors and results returned from the
invocation. In that case, we’re free to do some extra error handling.

**Note**: The use of `$utils.appendError()`
is similar to the `$util.error()`, with the major distinction that it
doesn’t interrupt the evaluation of the mapping template. Instead, it signals there
was an error with the field, but allows the template to be evaluated and
consequently return data back to the caller. We recommend you use
`$utils.appendError()` when your application needs to return partial
results.

Save the resolver and navigate to the **Queries**
page of the AWS AppSync console. Let’s send some sensor readings!

Execute the following mutation:

```
mutation sendReadings {
  recordReadings(
    tempReadings: [
      {sensorId: 1, value: 85.5, timestamp: "2018-02-01T17:21:05.000+08:00"},
      {sensorId: 1, value: 85.7, timestamp: "2018-02-01T17:21:06.000+08:00"},
      {sensorId: 1, value: 85.8, timestamp: "2018-02-01T17:21:07.000+08:00"},
      {sensorId: 1, value: 84.2, timestamp: "2018-02-01T17:21:08.000+08:00"},
      {sensorId: 1, value: 81.5, timestamp: "2018-02-01T17:21:09.000+08:00"}
    ]
    locReadings: [
      {sensorId: 1, lat: 47.615063, long: -122.333551, timestamp: "2018-02-01T17:21:05.000+08:00"},
      {sensorId: 1, lat: 47.615163, long: -122.333552, timestamp: "2018-02-01T17:21:06.000+08:00"}
      {sensorId: 1, lat: 47.615263, long: -122.333553, timestamp: "2018-02-01T17:21:07.000+08:00"}
      {sensorId: 1, lat: 47.615363, long: -122.333554, timestamp: "2018-02-01T17:21:08.000+08:00"}
      {sensorId: 1, lat: 47.615463, long: -122.333555, timestamp: "2018-02-01T17:21:09.000+08:00"}
    ]) {
    locationReadings {
      sensorId
      timestamp
      lat
      long
    }
    temperatureReadings {
      sensorId
      timestamp
      value
    }
  }
}
```

We sent 10 sensor readings in one mutation, with readings split up across two
tables. Use the DynamoDB console to validate that data shows up in both the **locationReadings** and **temperatureReadings** tables.

### BatchDeleteItem -

Deleting Sensor Readings

Similarly, we would also need to delete batches of sensor readings. Let’s use the
`Mutation.deleteReadings` GraphQL field for this purpose. Select
**Attach** next to the
`Mutation.recordReadings` field. On the next screen, pick the same
`BatchTutorial` data source created at the beginning of the
tutorial.

Let’s use the following request mapping template.

**Request Mapping Template**

```
## Convert tempReadings arguments to DynamoDB primary keys
#set($tempReadings = [])
#foreach($reading in ${ctx.args.tempReadings})
    #set($pkey = {})
    $util.qr($pkey.put("sensorId", $reading.sensorId))
    $util.qr($pkey.put("timestamp", $reading.timestamp))
    $util.qr($tempReadings.add($util.dynamodb.toMapValues($pkey)))
#end

## Convert locReadings arguments to DynamoDB primary keys
#set($locReadings = [])
#foreach($reading in ${ctx.args.locReadings})
    #set($pkey = {})
    $util.qr($pkey.put("sensorId", $reading.sensorId))
    $util.qr($pkey.put("timestamp", $reading.timestamp))
    $util.qr($locReadings.add($util.dynamodb.toMapValues($pkey)))
#end

{
    "version" : "2018-05-29",
    "operation" : "BatchDeleteItem",
    "tables" : {
        "locationReadings": $utils.toJson($locReadings),
        "temperatureReadings": $utils.toJson($tempReadings)
    }
}
```

The response mapping template is the same as the one we used for
`Mutation.recordReadings`.

**Response Mapping Template**

```
## If there was an error with the invocation
## there might have been partial results
#if($ctx.error)
    ## Append a GraphQL error for that field in the GraphQL response
    $utils.appendError($ctx.error.message, $ctx.error.message)
#end
## Also return data for the field in the GraphQL response
$utils.toJson($ctx.result.data)
```

Save the resolver and navigate to the **Queries**
page of the AWS AppSync console. Now, let’s delete a couple of sensor
readings!

Execute the following mutation:

```
mutation deleteReadings {
  # Let's delete the first two readings we recorded
  deleteReadings(
    tempReadings: [{sensorId: 1, timestamp: "2018-02-01T17:21:05.000+08:00"}]
    locReadings: [{sensorId: 1, timestamp: "2018-02-01T17:21:05.000+08:00"}]) {
    locationReadings {
      sensorId
      timestamp
      lat
      long
    }
    temperatureReadings {
      sensorId
      timestamp
      value
    }
  }
}
```

Validate through the DynamoDB console that these two readings have been deleted from
the **locationReadings** and **temperatureReadings** tables.

### BatchGetItem - Retrieve

Readings

Another common operation for our Pet Health app would be to retrieve the readings
for a sensor at a specific point in time. Let’s attach a resolver to the
`Query.getReadings` GraphQL field on our schema. Select **Attach**, and on the next screen pick the same
`BatchTutorial` data source created at the beginning of the
tutorial.

Let’s add the following request mapping template.

**Request Mapping Template**

```
## Build a single DynamoDB primary key,
## as both locationReadings and tempReadings tables
## share the same primary key structure
#set($pkey = {})
$util.qr($pkey.put("sensorId", $ctx.args.sensorId))
$util.qr($pkey.put("timestamp", $ctx.args.timestamp))

{
    "version" : "2018-05-29",
    "operation" : "BatchGetItem",
    "tables" : {
        "locationReadings": {
            "keys": [$util.dynamodb.toMapValuesJson($pkey)],
            "consistentRead": true
        },
        "temperatureReadings": {
            "keys": [$util.dynamodb.toMapValuesJson($pkey)],
            "consistentRead": true
        }
    }
}
```

Note that we are now using the **BatchGetItem**
operation.

Our response mapping template is going to be a little different because we chose
to return a `SensorReading` list. Let’s map the invocation result to the
desired shape.

**Response Mapping Template**

```
## Merge locationReadings and temperatureReadings
## into a single list
## __typename needed as schema uses an interface
#set($sensorReadings = [])

#foreach($locReading in $ctx.result.data.locationReadings)
    $util.qr($locReading.put("__typename", "LocationReading"))
    $util.qr($sensorReadings.add($locReading))
#end

#foreach($tempReading in $ctx.result.data.temperatureReadings)
    $util.qr($tempReading.put("__typename", "TemperatureReading"))
    $util.qr($sensorReadings.add($tempReading))
#end

$util.toJson($sensorReadings)
```

Save the resolver and navigate to the **Queries**
page of the AWS AppSync console. Now, let’s retrieve sensor readings!

Execute the following query:

```
query getReadingsForSensorAndTime {
  # Let's retrieve the very first two readings
  getReadings(sensorId: 1, timestamp: "2018-02-01T17:21:06.000+08:00") {
    sensorId
    timestamp
    ...on TemperatureReading {
      value
    }
    ...on LocationReading {
      lat
      long
    }
  }
}
```

We have successfully demonstrated the use of DynamoDB batch operations using
AWS AppSync.

## Error Handling

In AWS AppSync, data source operations can sometimes return partial results. Partial
results is the term we will use to denote when the output of an operation is comprised
of some data and an error. Because error handling is inherently application specific,
AWS AppSync gives you the opportunity to handle errors in the response mapping
template. The resolver invocation error, if present, is available from the context as
`$ctx.error`. Invocation errors always include a message and a type,
accessible as properties `$ctx.error.message` and
`$ctx.error.type`. During the response mapping template invocation, you
can handle partial results in three ways:

1. swallow the invocation error by just returning data
2. raise an error (using `$util.error(...)`) by stopping the response
   mapping template evaluation, which won’t return any data.
3. append an error (using `$util.appendError(...)`) and also return
   data

Let’s demonstrate each of the three points above with DynamoDB batch
operations!

### DynamoDB Batch operations

With DynamoDB batch operations, it is possible that a batch partially completes.
That is, it is possible that some of the requested items or keys are left
unprocessed. If AWS AppSync is unable to complete a batch, unprocessed items and
an invocation error will be set on the context.

We will implement error handling using the `Query.getReadings` field
configuration from the `BatchGetItem` operation from the previous section
of this tutorial. This time, let’s pretend that while executing the
`Query.getReadings` field, the `temperatureReadings`
DynamoDB table ran out of provisioned throughput. DynamoDB raised a **ProvisionedThroughputExceededException** at the second
attempt by AWS AppSync to process the remaining elements in the batch.

The following JSON represents the serialized context after the DynamoDB batch
invocation but before the response mapping template was evaluated.

```
{
  "arguments": {
    "sensorId": "1",
    "timestamp": "2018-02-01T17:21:05.000+08:00"
  },
  "source": null,
  "result": {
    "data": {
      "temperatureReadings": [
        null
      ],
      "locationReadings": [
        {
          "lat": 47.615063,
          "long": -122.333551,
          "sensorId": "1",
          "timestamp": "2018-02-01T17:21:05.000+08:00"
        }
      ]
    },
    "unprocessedKeys": {
      "temperatureReadings": [
        {
          "sensorId": "1",
          "timestamp": "2018-02-01T17:21:05.000+08:00"
        }
      ],
      "locationReadings": []
    }
  },
  "error": {
    "type": "DynamoDB:ProvisionedThroughputExceededException",
    "message": "You exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. (...)"
  },
  "outErrors": []
}
```

A few things to note on the context:

- the invocation error has been set on the context at
  `$ctx.error` by AWS AppSync, and the error type has been
  set to **DynamoDB:ProvisionedThroughputExceededException**.
- results are mapped per table under `$ctx.result.data`, even
  though an error is present
- keys that were left unprocessed are available at
  `$ctx.result.data.unprocessedKeys`. Here, AWS AppSync was
  unable to retrieve the item with key (sensorId:1,
  timestamp:2018-02-01T17:21:05.000+08:00) because of insufficient table
  throughput.

**Note**: For `BatchPutItem`, it is
`$ctx.result.data.unprocessedItems`. For
`BatchDeleteItem`, it is
`$ctx.result.data.unprocessedKeys`.

Let’s handle this error in three different ways.

#### 1. Swallowing the invocation

error

Returning data without handling the invocation error effectively swallows the
error, making the result for the given GraphQL field always successful.

The response mapping template we write is familiar and only focuses on the
result data.

Response mapping template:

```
$util.toJson($ctx.result.data)
```

GraphQL response:

```
{
  "data": {
    "getReadings": [
      {
        "sensorId": "1",
        "timestamp": "2018-02-01T17:21:05.000+08:00",
        "lat": 47.615063,
        "long": -122.333551
      },
      {
        "sensorId": "1",
        "timestamp": "2018-02-01T17:21:05.000+08:00",
        "value": 85.5
      }
    ]
  }
}
```

No errors will be added to the error response as only data was acted
on.

#### 2. Raising an

error to abort the template execution

When partial failures should be treated as complete failures from the client’s
perspective, you can abort the template execution to prevent returning data. The
`$util.error(...)` utility method achieves exactly this
behavior.

Response mapping template:

```
## there was an error let's mark the entire field
## as failed and do not return any data back in the response
#if ($ctx.error)
    $util.error($ctx.error.message, $ctx.error.type, null, $ctx.result.data.unprocessedKeys)
#end

$util.toJson($ctx.result.data)
```

GraphQL response:

```
{
  "data": {
    "getReadings": null
  },
  "errors": [
    {
      "path": [
        "getReadings"
      ],
      "data": null,
      "errorType": "DynamoDB:ProvisionedThroughputExceededException",
      "errorInfo": {
        "temperatureReadings": [
          {
            "sensorId": "1",
            "timestamp": "2018-02-01T17:21:05.000+08:00"
          }
        ],
        "locationReadings": []
      },
      "locations": [
        {
          "line": 58,
          "column": 3
        }
      ],
      "message": "You exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. (...)"
    }
  ]
}
```

Even though some results might have been returned from the DynamoDB batch
operation, we chose to raise an error such that the `getReadings`
GraphQL field is null and the error has been added to the GraphQL response
_errors_ block.

#### 3. Appending

an error to return both data and errors

In certain cases, to provide a better user experience, applications can return
partial results and notify their clients of the unprocessed items. The clients
can decide to either implement a retry or translate the error back to the end
user. The `$util.appendError(...)` is the utility method that enables
this behavior by letting the application designer append errors on the context
without interfering with the evaluation of the template. After evaluating the
template, AWS AppSync will process any context errors by appending them to the
errors block of the GraphQL response.

Response mapping template:

```
#if ($ctx.error)
    ## pass the unprocessed keys back to the caller via the `errorInfo` field
    $util.appendError($ctx.error.message, $ctx.error.type, null, $ctx.result.data.unprocessedKeys)
#end

$util.toJson($ctx.result.data)
```

We forwarded both the invocation error and unprocessedKeys element inside the
errors block of the GraphQL response. The `getReadings` field also
return partial data from the **locationReadings**
table as you can see in the response below.

GraphQL response:

```
{
  "data": {
    "getReadings": [
      null,
      {
        "sensorId": "1",
        "timestamp": "2018-02-01T17:21:05.000+08:00",
        "value": 85.5
      }
    ]
  },
  "errors": [
    {
      "path": [
        "getReadings"
      ],
      "data": null,
      "errorType": "DynamoDB:ProvisionedThroughputExceededException",
      "errorInfo": {
        "temperatureReadings": [
          {
            "sensorId": "1",
            "timestamp": "2018-02-01T17:21:05.000+08:00"
          }
        ],
        "locationReadings": []
      },
      "locations": [
        {
          "line": 58,
          "column": 3
        }
      ],
      "message": "You exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. (...)"
    }
  ]
}
```
