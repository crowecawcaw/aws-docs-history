# Using DynamoDB batch operations in AWS AppSync

AWS AppSync supports using Amazon DynamoDB batch operations across one or more tables in a single Region.
Supported operations are `BatchGetItem`, `BatchPutItem`, and `BatchDeleteItem`.
By using these features in AWS AppSync, you can perform tasks such as:

- Passing a list of keys in a single query and returning the results from a table
- Reading records from one or more tables in a single query
- Writing records in bulk to one or more tables
- Conditionally writing or deleting records in multiple tables that might have a relation
  Batch operations in AWS AppSync have two key differences from non-batched operations:

- The data source role must have permissions to all tables that the resolver will access.
- The table specification for a resolver is part of the request object.

## Single table batches

###### Warning

`BatchPutItem` and `BatchDeleteItem` are not supported when
used with conflict detection and resolution. These settings must be disabled to
prevent possible errors.

To get started, let’s create a new GraphQL API. In the AWS AppSync console, choose **Create
API**, **GraphQL APIs**, and **Design from
scratch**. Name your API `BatchTutorial API`, choose **Next**, and on the **Specify GraphQL resources** step, choose
**Create GraphQL resources later** and click **Next**. Review your details and create the API. Go to the **Schema** page and paste the following schema, noting that for the query, we’ll pass in a list
of IDs:

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
```

Save your schema and choose **Create Resources** at the top of the page.
Choose **Use existing type** and select the `Post` type. Name your
table `Posts`. Make sure the **Primary Key** is set to
`id`, unselect **Automatically generate GraphQL** (you’ll
provide your own code), and select **Create**. To get you started, AWS AppSync
creates a new DynamoDB table and a data source connected to the table with the appropriate roles. However,
there are still a couple of permissions you need to add to the role. Go to the **Data
sources** page and choose the new data source. Under **Select an existing
role**, you'll notice that a role was automatically created for the table. Take note of the
role (should look something like `appsync-ds-ddb-aaabbbcccddd-Posts`) and then go to the IAM
console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")). In the IAM console, choose **Roles**, then choose
your role from the table. In your role, under **Permissions policies**, click
on the "`+`" next to the policy (should have a similar name to the role name). Choose **Edit** at the top of the collapsible when the policy appears. You need to add batch
permissions to your policy, specifically `dynamodb:BatchGetItem` and
`dynamodb:BatchWriteItem`. It'll look something like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem",
 "dynamodb:BatchWriteItem",
 "dynamodb:BatchGetItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:us-east-1:111122223333:table/locationReadings",
 "arn:aws:dynamodb:us-east-1:111122223333:table/locationReadings/*",
 "arn:aws:dynamodb:us-east-1:111122223333:table/temperatureReadings",
 "arn:aws:dynamodb:us-east-1:111122223333:table/temperatureReadings/*"
 ]
 }
 ]
}`

```

Choose **Next**, then **Save changes**. Your
policy should allow batch processing now.

Back in the AWS AppSync console, go to the **Schema** page and select **Attach** next to the `Mutation.batchAdd` field. Create your resolver
using the `Posts` table as the data source. In the code editor, replace the handlers with the
snippet below. This snippet automatically takes each item in the GraphQL `input PostInput` type
and builds a map, which is needed for the `BatchPutItem` operation:

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  return {
    operation: "BatchPutItem",
    tables: {
      Posts: ctx.args.posts.map((post) => util.dynamodb.toMapValues(post)),
    },
  };
}

export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type);
  }
  return ctx.result.data.Posts;
}
```

Navigate to the **Queries** page of the AWS AppSync console and run the
following `batchAdd` mutation:

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

You should see the results printed on the screen; this can be validated by reviewing the DynamoDB console to
scan for the values written to the `Posts` table.

Next, repeat the process of attaching a resolver but for the `Query.batchGet` field using the
`Posts` table as the data source. Replace the handlers with the code below. This
automatically takes each item in the GraphQL `ids:[]` type and builds a map that is needed for
the `BatchGetItem` operation:

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  return {
    operation: "BatchGetItem",
    tables: {
      Posts: {
        keys: ctx.args.ids.map((id) => util.dynamodb.toMapValues({ id })),
        consistentRead: true,
      },
    },
  };
}

export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type);
  }
  return ctx.result.data.Posts;
}
```

Now, go back to the **Queries** page of the AWS AppSync console and run the
following `batchGet` query:

```
query get {
    batchGet(ids:[1,2,3]){
        id
        title
    }
}
```

This should return the results for the two `id` values that you added earlier. Note that a
`null` value was returned for the `id` with a value of `3`. This is
because there was no record in your `Posts` table with that value yet. Also note that
AWS AppSync returns the results in the same order as the keys passed to the query, which is an additional
feature that AWS AppSync performs on your behalf. So, if you switch to `batchGet(ids:[1,3,2])`,
you’ll see that the order changed. You’ll also know which `id` returned a `null`
value.

Finally, attach one more resolver to the `Mutation.batchDelete` field using the
`Posts` table as the data source. Replace the handlers with the code below. This
automatically takes each item in the GraphQL `ids:[]` type and builds a map that is needed for
the `BatchGetItem` operation:

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  return {
    operation: "BatchDeleteItem",
    tables: {
      Posts: ctx.args.ids.map((id) => util.dynamodb.toMapValues({ id })),
    },
  };
}

export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type);
  }
  return ctx.result.data.Posts;
}
```

Now, go back to the **Queries** page of the AWS AppSync console and run the
following `batchDelete` mutation:

```
mutation delete {
    batchDelete(ids:[1,2]){ id }
}
```

The records with `id`
`1` and `2` should now be deleted. If you re-run the
`batchGet()` query from earlier, these should return
`null`.

## Multi-table batch

###### Warning

`BatchPutItem` and `BatchDeleteItem` are not supported when
used with conflict detection and resolution. These settings must be disabled to
prevent possible errors.

AWS AppSync also enables you to perform batch operations across tables. Let’s build
a more complex application. Imagine we are building a pet health app wherein sensors
report the pet's location and body temperature. The sensors are battery powered and
attempt to connect to the network every few minutes. When a sensor establishes a
connection, it sends its readings to our AWS AppSync API. Triggers then analyze the
data so a dashboard can be presented to the pet owner. Let’s focus on representing the
interactions between the sensor and the backend data store.

In the AWS AppSync console, choose **Create API**, **GraphQL
APIs**, and **Design from scratch**. Name your API
`MultiBatchTutorial API`, choose **Next**, and on the **Specify GraphQL resources** step, choose **Create GraphQL
resources later** and click **Next**. Review your details and
create the API. Go to the **Schema** page and paste and save the following
schema:

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

We need to create two DynamoDB tables:

- `locationReadings` will store sensor location readings.
- `temperatureReadings` will store sensor temperature readings.

Both tables will share the same primary key structure: `sensorId (String)` as the partition key
and `timestamp (String)` as the sort key.

Choose **Create Resources** at the top of the page. Choose **Use existing type** and select the `locationReadings` type. Name your
table `locationReadings`. Make sure the **Primary Key** is set to
`sensorId` and the sort key to `timestamp`. Unselect **Automatically generate GraphQL** (you’ll provide your own code), and select **Create**. Repeat this process for `temperatureReadings` using the
`temperatureReadings` as the type and table name. Use the same keys as above.

Your new tables will contain automatically generated roles. There are still a couple of permissions you
need to add to those roles. Go to the **Data sources** page and choose
`locationReadings`. Under **Select an existing role**, you can
see the role. Take note of the role (should look something like
`appsync-ds-ddb-aaabbbcccddd-locationReadings`) and then go to the IAM console
([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")). In the IAM console, choose **Roles**, then choose your
role from the table. In your role, under **Permissions policies**, click on the
"`+`" next to the policy (should have a similar name to the role name). Choose **Edit** at the top of the collapsible when the policy appears. You need to add
permissions to this policy. It'll look something like this:

Choose **Next**, then **Save changes**. Repeat
this process for the `temperatureReadings` data source using the same policy snippet
above.

### BatchPutItem - Recording sensor readings

Our sensors need to be able to send their readings once they connect to the internet. The GraphQL
field `Mutation.recordReadings` is the API they will use to do so. We'll need to add a
resolver to this field.

In the AWS AppSync console's **Schema** page, select **Attach** next to the `Mutation.recordReadings` field. On the next screen,
create your resolver using the `locationReadings` table as the data source.

After creating your resolver, replace the handlers with the following code in the editor. This
`BatchPutItem` operation allows us to specify multiple tables:

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { locReadings, tempReadings } = ctx.args
	const locationReadings = locReadings.map((loc) => util.dynamodb.toMapValues(loc))
	const temperatureReadings = tempReadings.map((tmp) => util.dynamodb.toMapValues(tmp))

	return {
		operation: 'BatchPutItem',
		tables: {
			locationReadings,
			temperatureReadings,
		},
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.appendError(ctx.error.message, ctx.error.type)
	}
	return ctx.result.data
}
```

With batch operations, there can be both errors and results returned from the
invocation. In that case, we’re free to do some extra error handling.

###### Note

The use of `utils.appendError()` is similar to the `util.error()`, with the
major distinction that it doesn’t interrupt the evaluation of the request or response handler.
Instead, it signals there was an error with the field but allows the handler to be evaluated and
consequently return data back to the caller. We recommend that you use
`utils.appendError()` when your application needs to return partial results.

Save the resolver and navigate to the **Queries** page in the
AWS AppSync console. We can now send some sensor readings.

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
      {sensorId: 1, lat: 47.615163, long: -122.333552, timestamp: "2018-02-01T17:21:06.000+08:00"},
      {sensorId: 1, lat: 47.615263, long: -122.333553, timestamp: "2018-02-01T17:21:07.000+08:00"},
      {sensorId: 1, lat: 47.615363, long: -122.333554, timestamp: "2018-02-01T17:21:08.000+08:00"},
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

We sent ten sensor readings in one mutation with readings split up across two tables. Use the DynamoDB
console to validate that the data shows up in both the `locationReadings` and
`temperatureReadings` tables.

### BatchDeleteItem - Deleting sensor readings

Similarly, we would also need to be able to delete batches of sensor readings. Let’s use the
`Mutation.deleteReadings` GraphQL field for this purpose. In the AWS AppSync console's
**Schema** page, select **Attach** next to
the `Mutation.deleteReadings` field. On the next screen, create your resolver using the
`locationReadings` table as the data source.

After creating your resolver, replace the handlers in the code editor with the snippet below. In this
resolver, we use a helper function mapper that extracts the `sensorId` and the
`timestamp` from the provided inputs.

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { locReadings, tempReadings } = ctx.args
	const mapper = ({ sensorId, timestamp }) => util.dynamodb.toMapValues({ sensorId, timestamp })

	return {
		operation: 'BatchDeleteItem',
		tables: {
			locationReadings: locReadings.map(mapper),
			temperatureReadings: tempReadings.map(mapper),
		},
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.appendError(ctx.error.message, ctx.error.type)
	}
	return ctx.result.data
}
```

Save the resolver and navigate to the **Queries** page in the
AWS AppSync console. Now, let’s delete a couple of sensor readings.

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

###### Note

Contrary to the `DeleteItem` operation, the fully deleted item isn’t returned in the
response. Only the passed key is returned. To learn more, see the [BatchDeleteItem in JavaScript resolver function reference for DynamoDB](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-batch-delete-item "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-batch-delete-item") .

Validate through the DynamoDB console that these two readings have been deleted from the
`locationReadings` and `temperatureReadings` tables.

### BatchGetItem - Retrieve readings

Another common operation for our app would be to retrieve the readings for a sensor at a specific
point in time. Let’s attach a resolver to the `Query.getReadings` GraphQL field on our
schema. In the AWS AppSync console's **Schema** page, select **Attach** next to the `Query.getReadings` field. On the next screen,
create your resolver using the `locationReadings` table as the data source.

Let’s use the following code:

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const keys = [util.dynamodb.toMapValues(ctx.args)]
	const consistentRead = true
	return {
		operation: 'BatchGetItem',
		tables: {
			locationReadings: { keys, consistentRead },
			temperatureReadings: { keys, consistentRead },
		},
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.appendError(ctx.error.message, ctx.error.type)
	}
	const { locationReadings: locs, temperatureReadings: temps } = ctx.result.data

	return [
		...locs.map((l) => ({ ...l, __typename: 'LocationReading' })),
		...temps.map((t) => ({ ...t, __typename: 'TemperatureReading' })),
	]
}
```

Save the resolver and navigate to the **Queries** page in the
AWS AppSync console. Now, let’s retrieve our sensor readings.

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

## Error handling

In AWS AppSync, data source operations can sometimes return partial results. Partial results is the term
we will use to denote when the output of an operation is comprised of some data and an error. Because error
handling is inherently application specific, AWS AppSync gives you the opportunity to handle errors in the
response handler. The resolver invocation error, if present, is available from the context as
`ctx.error`. Invocation errors always include a message and a type, accessible as properties
`ctx.error.message` and `ctx.error.type`. In the response handler, you can handle
partial results in three ways:

1. Swallow the invocation error by just returning data.
2. Raise an error (using `util.error(...)`) by stopping the handler evaluation, which
   won’t return any data.
3. Append an error (using `util.appendError(...)`) and also return data.

Let’s demonstrate each of the three points above with DynamoDB batch operations.

### DynamoDB Batch operations

With DynamoDB batch operations, it is possible that a batch partially completes. That is, it is possible
that some of the requested items or keys are left unprocessed. If AWS AppSync is unable to complete a
batch, unprocessed items and an invocation error will be set on the context.

We will implement error handling using the `Query.getReadings` field configuration from the
`BatchGetItem` operation from the previous section of this tutorial. This time, let’s
pretend that while executing the `Query.getReadings` field, the
`temperatureReadings` DynamoDB table ran out of provisioned throughput. DynamoDB raised a
`ProvisionedThroughputExceededException` during the second attempt by AWS AppSync to
process the remaining elements in the batch.

The following JSON represents the serialized context after the DynamoDB batch invocation but before the
response handler was called:

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

- The invocation error has been set on the context at `ctx.error` by AWS AppSync,
  and the error type has been set to
  `DynamoDB:ProvisionedThroughputExceededException`.
- Results are mapped per table under `ctx.result.data` even though an error is
  present.
- Keys that were left unprocessed are available at `ctx.result.data.unprocessedKeys`.
  Here, AWS AppSync was unable to retrieve the item with key (sensorId:1,
  timestamp:2018-02-01T17:21:05.000+08:00) because of insufficient table throughput.

###### Note

For `BatchPutItem`, it is `ctx.result.data.unprocessedItems`. For
`BatchDeleteItem`, it is `ctx.result.data.unprocessedKeys`.

Let’s handle this error in three different ways.

#### 1. Swallowing the invocation error

Returning data without handling the invocation error effectively swallows the
error, making the result for the given GraphQL field always successful.

The code we write is familiar and only focuses on the result data.

**Response handler**

```
export function response(ctx) {
  return ctx.result.data
}
```

**GraphQL response**

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

#### 2. Raising an error to abort the response handler execution

When partial failures should be treated as complete failures from the client’s perspective, you
can abort the response handler execution to prevent returning data. The `util.error(...)`
utility method achieves exactly this behavior.

**Response handler code**

```
export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type, null, ctx.result.data.unprocessedKeys);
  }
  return ctx.result.data;
}
```

**GraphQL response**

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

#### 3. Appending an error to return both data and errors

In certain cases, to provide a better user experience, applications can return partial results and
notify their clients of the unprocessed items. The clients can decide to either implement a retry or
translate the error back to the end user. The `util.appendError(...)` is the utility
method that enables this behavior by letting the application designer append errors on the context
without interfering with the evaluation of the response handler. After evaluating the response
handler, AWS AppSync will process any context errors by appending them to the errors block of the
GraphQL response.

**Response handler code**

```
export function response(ctx) {
  if (ctx.error) {
    util.appendError(ctx.error.message, ctx.error.type, null, ctx.result.data.unprocessedKeys);
  }
  return ctx.result.data;
}
```

We forwarded both the invocation error and `unprocessedKeys` element inside the errors
block of the GraphQL response. The `getReadings` field also return partial data from the
`locationReadings` table as you can see in the response below.

**GraphQL response**

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
