# Conflict detection and resolution in AWS AppSync

When concurrent writes happen with AWS AppSync, you can configure Conflict Detection and
Conflict Resolution strategies to handle updates appropriately. Conflict Detection
determines if the mutation is in conflict with the actual written item in the data source.
Conflict Detection is enabled by setting the value in the SyncConfig for the
`conflictDetection` field to `VERSION`.

Conflict Resolution is the action that is taken in the event that a conflict is
detected. This is determined by setting the Conflict Handler field in the SyncConfig. There
are three Conflict Resolution strategies:

- OPTIMISTIC_CONCURRENCY
- AUTOMERGE
- LAMBDA
  Versions are automatically incremented by AWS AppSync during write operations and should
  not be modified by clients or outside of a resolver configured with a version-enabled data
  source. Doing so will change the consistency behavior of the system and could result in
  data loss.

## Optimistic concurrency

Optimistic Concurrency is a conflict resolution strategy that AWS AppSync provides for
versioned data sources. When the conflict resolver is set to Optimistic Concurrency, if
an incoming mutation is detected to have a version that differs from the actual version
of the object, the conflict handler will simply reject the incoming request. Inside the
GraphQL response, the existing item on the server that has the latest version will be
provided. The client is then expected to handle this conflict locally and retry the
mutation with the updated version of the item.

## Automerges

Automerge provides developers an easy way to configure a conflict resolution strategy
without writing client-side logic to manually merge conflicts that were unable to be
handled by other strategies. Automerge adheres to a strict rule set when merging data to
resolve conflicts. The tenets of Automerge revolve around the underlying data type of
the GraphQL field. They are as follows:

- Conflict on a scalar field: GraphQL scalar or any field that is not a
  collection (i.e. List, Set, Map). Reject the incoming value for the scalar field
  and select the value existing in the server.
- Conflict on a list: GraphQL type and database type are lists. Concatenate the
  incoming list with the existing list in the server. The list values in the
  incoming mutation will be appended to the end of the list in the server. Duplicate
  values will be retained.
- Conflict on a set: GraphQL type is a list and database type is a Set. Apply a
  set union using incoming the set and the existing set in the server. This adheres
  to the properties of a Set, meaning no duplicate entries.
- When an incoming mutation adds a new field to the item or is made against a
  field with the value of `null`, merge that on to the existing
  item.
- Conflict on a map: When the underlying data type in the database is a Map (i.e.
  key-value document), apply the above rules as it parses and processes each
  property of the Map.

Automerge is designed to automatically detect, merge, and retry requests with an
updated version, absolving the client from needing to manually merge any conflicting
data.

To show an example of how Automerge handles a Conflict on a Scalar type. We will use
the following record as our starting point.

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "_version" : 4
}
```

Now an incoming mutation might be attempting to update the item but with an older
version since the client has not synchronized with the server yet. That looks like
this:

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 55,
  "_version" : 2
}
```

Notice the outdated version of 2 in the incoming request. During this flow, Automerge
will merge the data by rejecting the ‘jersey’ field update to ‘55’ and keep the value at
‘5’ resulting in the following image of the item being saved in the server.

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "_version" : 5 # version is incremented every time automerge performs a merge that is stored on the server.
}
```

Given the state of the item shown above at version 5, now suppose an incoming
mutation that attempts to mutate the item with the following image:

```
{
  "id" : 1,
  "name" : "Shaggy",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "dinner"] # underlying data type is a Set
  "points": [24, 30, 27] # underlying data type is a List
  "_version" : 3
}
```

There are three points of interest in the incoming mutation. The name, a scalar, has
been changed but two new fields “interests”, a Set, and “points”, a List, have been
added. In this scenario, a conflict will be detected due to the version mismatch.
Automerge adheres to its properties and rejects the name change due to it being a scalar
and add on the non-conflicting fields. This results in the item that is saved in the
server to appear as follows.

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "dinner"] # underlying data type is a Set
  "points": [24, 30, 27] # underlying data type is a List
  "_version" : 6
}
```

With the updated image of the item with version 6, now suppose an incoming mutation
(with another version mismatch) tries to transform the item to the following:

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "brunch"] # underlying data type is a Set
  "points": [30, 35] # underlying data type is a List
  "_version" : 5
}
```

Here we observe that the incoming field for “interests” has one duplicate value that
exists in the server and two new values. In this case, since the underlying data type is
a Set, Automerge will combine the values existing in the server with the ones in the
incoming request and strip out any duplicates. Similarly there is a conflict on the
“points” field where there is one duplicate value and one new value. But since the
underlying data type here is a List, Automerge will simply append all values in the
incoming request to the end of the values already existing in the server. The resulting
merged image stored on the server would appear as follows:

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "dinner", "brunch"] # underlying data type is a Set
  "points": [24, 30, 27, 30, 35] # underlying data type is a List
  "_version" : 7
}
```

Now let’s assume the item stored in the server appears as follows, at version 8.

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "dinner", "brunch"] # underlying data type is a Set
  "points": [24, 30, 27, 30, 35] # underlying data type is a List
  "stats": {
      "ppg": "35.4",
      "apg": "6.3"
  }
  "_version" : 8
}
```

But an incoming request tries to update the item with the following image, once again
with a version mismatch:

```
{
  "id" : 1,
  "name" : "Nadia",
  "stats": {
      "ppg": "25.7",
      "rpg": "6.9"
  }
  "_version" : 3
}
```

Now in this scenario, we can see that the fields that already exist in the server are
missing (interests, points, jersey). In addition, the value for “ppg” within the map
“stats” is being edited, a new value “rpg” is being added, and “apg” is omitted.
Automerge preserve the fields that have been omitted (note: if fields are intended to be
removed, then the request must be tried again with the matching version), and so they
will not be lost. It will also apply the same rules to fields within maps and therefore
the change to “ppg” will be rejected whereas “apg” is preserved and “rpg”, a new field”,
is added on. The resulting item stored in the server will now appear as:

```
{
  "id" : 1,
  "name" : "Nadia",
  "jersey" : 5,
  "interests" : ["breakfast", "lunch", "dinner", "brunch"] # underlying data type is a Set
  "points": [24, 30, 27, 30, 35] # underlying data type is a List
  "stats": {
      "ppg": "35.4",
      "apg": "6.3",
      "rpg": "6.9"
  }
  "_version" : 9
}
```

## Lambdas

There are several Lambda resolution strategies to choose from:

- `RESOLVE`: Replaces the existing item with new item supplied in
  response payload. You can only retry the same operation on a single item at a
  time. Currently supported for DynamoDB `PutItem` &
  `UpdateItem`.
- `REJECT`: Rejects the mutation and returns an error with the existing
  item in the GraphQL response. Currently supported for DynamoDB
  `PutItem`, `UpdateItem`, &
  `DeleteItem`.
- `REMOVE`: Removes the existing item. Currently supported for DynamoDB
  `DeleteItem`.

**The Lambda Invocation Request**

The AWS AppSync DynamoDB resolver invokes the Lambda function specified in the
`LambdaConflictHandlerArn`. It uses the same `service-role-arn`
configured on the data source. The payload of the invocation has the following
structure:

```
{
    "newItem": { ... },
    "existingItem": {... },
    "arguments": { ... },
    "resolver": { ... },
    "identity": { ... }
}
```

The fields are defined as follows:

**`newItem`**

The preview item, if the mutation succeeded.

**`existingItem`**

The item currently resided in DynamoDB table.

**`arguments`**

The arguments from the GraphQL mutation.

**`resolver`**

Information about the AWS AppSync resolver.

**`identity`**

Information about the caller. This field is set to null, if access with API
key.

Example payload:

```
{
    "newItem": {
        "id": "1",
        "author": "Jeff",
        "title": "Foo Bar",
        "rating": 5,
        "comments": ["hello world"],
    },
    "existingItem": {
        "id": "1",
        "author": "Foo",
        "rating": 5,
        "comments": ["old comment"]
    },
    "arguments": {
        "id": "1",
        "author": "Jeff",
        "title": "Foo Bar",
        "comments": ["hello world"]
    },
    "resolver": {
        "tableName": "post-table",
        "awsRegion": "us-west-2",
        "parentType": "Mutation",
        "field": "updatePost"
    },
    "identity": {
         "accountId": "123456789012",
         "sourceIp": "x.x.x.x",
         "username": "AIDAAAAAAAAAAAAAAAAAA",
         "userArn": "arn:aws:iam::123456789012:user/appsync"
    }
}
```

**The Lambda Invocation Response**

For `PutItem` and `UpdateItem` conflict resolution

`RESOLVE` the mutation. The response must be in the following format.

```
{
    "action": "RESOLVE",
    "item": { ... }
}
```

The `item` field represents an object that will be used to replace the
existing item in the underlying data source. The primary key and sync metadata will be
ignored if included in `item`.

`REJECT` the mutation. The response must be in the following format.

```
{
    "action": "REJECT"
}
```

For `DeleteItem` conflict resolution

`REMOVE` the item. The response must be in the following format.

```
{
    "action": "REMOVE"
}
```

`REJECT` the mutation. The response must be in the following format.

```
{
    "action": "REJECT"
}
```

The example Lambda function below checks who makes the call and the resolver name. If
it is made by `jeffTheAdmin`, `REMOVE` the object for DeletePost
resolver or `RESOLVE` the conflict with new item for Update/Put resolvers. If
not, the mutation is `REJECT`.

```
exports.handler = async (event, context, callback) => {
    console.log("Event: "+ JSON.stringify(event));

    // Business logic goes here.
    var response;
    if ( event.identity.user == "jeffTheAdmin" ) {
        let resolver = event.resolver.field;

        switch(resolver) {
            case "deletePost":
                response = {
                    "action" : "REMOVE"
                }
                break;

            case "updatePost":
            case "createPost":
                response = {
                    "action" : "RESOLVE",
                    "item": event.newItem
                }
                break;
            default:
                response = { "action" : "REJECT" };
        }
    } else {
        response = { "action" : "REJECT" };
    }

    console.log("Response: "+ JSON.stringify(response));
    return response;
}
```

## Errors

Below is a list of possible errors that may occur during a Conflict Resolution
process:

**`ConflictUnhandled`**

Conflict detection finds a version mismatch and the conflict handler rejects
the mutation.

Example: Conflict resolution with an Optimistic Concurrency conflict
handler. Or, Lambda conflict handler returned with `REJECT`.

**`ConflictError`**

An internal error occurs when trying to resolve a conflict.

Example: Lambda conflict handler returned a malformed response. Or, cannot
invoke Lambda conflict handler because the supplied resource
`LambdaConflictHandlerArn` is not found.

**`MaxConflicts`**

Max retry attempts were reached for conflict resolution.

Example: Too many concurrent requests on the same object. Before the
conflict is resolved, the object is updated to a new version by another
client.

**`BadRequest`**

Client tries to update metadata fields (`_version`,
`_ttl`, `_lastChangedAt`,
`_deleted`).

Example: Client tries to update `_version` of an object with an
update mutation.

**`DeltaSyncWriteError`**

Failed to write delta sync record.

Example: Mutation succeeded, but an internal error occurred when trying to
write to the delta sync table.

**`InternalFailure`**

An internal error occurred.

**`UnsupportedOperation`**

Unsupported operation '`X`'. Datasource Versioning
only supports the following operations
(TransactGetItems,PutItem,BatchGetItem,Scan,Query,GetItem,DeleteItem,UpdateItem,Sync).

Example: Using certain transaction and batch operations with conflict
detection/resolution enabled. These operations are not currently
supported.

## CloudWatch Logs

If an AWS AppSync API has enabled CloudWatch Logs with the logging settings set to Field-Level
Logs `enabled` and log-level for the Field-Level Logs set to
`ALL`, then AWS AppSync will emit Conflict Detection and Resolution information
to the log group. For information about the format of the log messages, see the [documentation
for Conflict Detection and Sync Logging](monitoring.md#aws-appsync-monitoring-conflict-detection-and-sync-logging "monitoring.md#aws-appsync-monitoring-conflict-detection-and-sync-logging").
