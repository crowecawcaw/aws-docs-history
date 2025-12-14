# Using Delta

Sync operations on versioned data sources in AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](tutorials-js.md "tutorials-js.md").

Client applications in AWS AppSync store data by caching GraphQL responses locally to disk
in a mobile/web application. Versioned data sources and `Sync` operations give
customers the ability to perform the sync process using a single resolver. This allows clients
to hydrate their local cache with results from one base query that might have a lot of records,
and then receive only the data altered since their last query (the _delta updates_). By allowing clients to perform the base
hydration of the cache with an initial request and incremental updates in another, you can move
the computation from your client application to the backend. This is substantially more
efficient for client applications that frequently switch between online and offline
states.

To implement Delta Sync, the `Sync` query uses the `Sync` operation on
a versioned data source. When an AWS AppSync mutation changes an item in a versioned data source,
a record of that change will be stored in the _Delta_
table as well. You can choose to use different _Delta_
tables (e.g. one per type, one per domain area) for other versioned data sources or a single
_Delta_ table for your API. AWS AppSync recommends
against using a single _Delta_ table for multiple APIs
to avoid the collision of primary keys.

In addition, Delta Sync clients can also receive a subscription as an argument, and then the
client coordinates subscription reconnects and writes between offline to online transitions.
Delta Sync performs this by automatically resuming subscriptions (including exponential backoff
and retry with jitter through different network error scenarios), and storing events in a queue.
The appropriate delta or base query is then run before merging any events from the queue, and
finally processing subscriptions as normal.

Documentation for client configuration options, including the Amplify DataStore, is
available on the [Amplify Framework website](https://aws-amplify.github.io/ "https://aws-amplify.github.io/").
This documentation outlines how to set up versioned DynamoDB data sources and `Sync`
operations to work with the Delta Sync client for optimal data access.

## One-Click Setup

To automatically set up the GraphQL endpoint in AWS AppSync with all the resolvers
configured and the necessary AWS resources, use this AWS CloudFormation template:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/deltasync/deltasync-v2-full.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/deltasync/deltasync-v2-full.yaml")

This stack creates the following resources in your account:

- 2 DynamoDB tables (Base and Delta)
- 1 AWS AppSync API with API key
- 1 IAM Role with policy for DynamoDB tables

Two tables are used to partition your sync queries into a second table that acts as a
journal of missed events when the clients were offline. To keep the queries efficient on the
delta table, [Amazon
DynamoDB TTLs](../../../amazondynamodb/latest/developerguide/TTL.md "../../../amazondynamodb/latest/developerguide/TTL.md") are used to automatically groom the events as necessary. The TTL time
is configurable for your needs on the data source (you might want this as 1hour, 1day,
etc.).

## Schema

To demonstrate Delta Sync, the sample application creates a _Posts_ schema backed by a _Base_ and _Delta_ table in DynamoDB.
AWS AppSync automatically writes the mutations to both tables. The sync query pulls records from
the _Base_ or _Delta_ table as appropriate, and a single subscription is defined to show how
clients can leverage this in their reconnection logic.

```
input CreatePostInput {
    author: String!
    title: String!
    content: String!
    url: String
    ups: Int
    downs: Int
    _version: Int
}

interface Connection {
  nextToken: String
  startedAt: AWSTimestamp!
}

type Mutation {
    createPost(input: CreatePostInput!): Post
    updatePost(input: UpdatePostInput!): Post
    deletePost(input: DeletePostInput!): Post
}

type Post {
    id: ID!
    author: String!
    title: String!
    content: String!
    url: AWSURL
    ups: Int
    downs: Int
    _version: Int
    _deleted: Boolean
    _lastChangedAt: AWSTimestamp!
}

type PostConnection implements Connection {
    items: [Post!]!
    nextToken: String
    startedAt: AWSTimestamp!
}

type Query {
    getPost(id: ID!): Post
    syncPosts(limit: Int, nextToken: String, lastSync: AWSTimestamp): PostConnection!
}

type Subscription {
    onCreatePost: Post
        @aws_subscribe(mutations: ["createPost"])
    onUpdatePost: Post
        @aws_subscribe(mutations: ["updatePost"])
    onDeletePost: Post
        @aws_subscribe(mutations: ["deletePost"])
}

input DeletePostInput {
    id: ID!
    _version: Int!
}

input UpdatePostInput {
    id: ID!
    author: String
    title: String
    content: String
    url: String
    ups: Int
    downs: Int
    _version: Int!
}

schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}
```

The GraphQL schema is standard, but a couple things are worth calling out before moving
forward. First, all of the mutations automatically first write to the _Base_ table and then to the _Delta_ table. The _Base_ table is the central source of truth for state while the _Delta_ table is your journal. If you don’t pass in the
`lastSync: AWSTimestamp`, the `syncPosts` query runs against the
_Base_ table and hydrates the cache as well as
running at periodic times as a _global catchup
process_ for edge cases when clients are offline longer than your configured TTL
time in the _Delta_ table. If you do pass in the
`lastSync: AWSTimestamp`, the `syncPosts` query runs against your
_Delta_ table and is used by clients to retrieve
changed events since they were last offline. Amplify clients automatically pass the
`lastSync: AWSTimestamp` value, and persist to disk appropriately.

The _\_deleted_ field on _Post_ is used for **DELETE**
operations. When clients are offline and records are removed from the _Base_ table, this attribute notifies clients performing
synchronization to evict items from their local cache. In cases where clients are offline for
longer periods of time and the item has been removed before the client can retrieve this value
with a Delta Sync query, the global catch-up event in the base query (configurable in the
client) runs and removes the item from the cache. This field is marked optional because it
only returns a value when running a sync query that has deleted items present.

## Mutations

For all of the mutations, AWS AppSync does a standard Create/Update/Delete operation in the
_Base_ table and also records the change in the
_Delta_ table automatically. You can reduce or
extend the time to keep records by modifying the `DeltaSyncTableTTL` value on the
data source. For organizations with a high velocity of data, it may make sense to keep this
short. Alternatively, if your clients are offline for longer periods of time, it might be
prudent to keep this longer.

## Sync Queries

The _base query_ is a DynamoDB Sync operation
without a `lastSync` value specified. For many organizations, this works because
the base query only runs on startup and at a periodic basis thereafter.

The _delta query_ is a DynamoDB Sync operation with
a `lastSync` value specified. The _delta
query_ executes whenever the client comes back online from an offline state (as
long as the base query periodic time hasn’t triggered to run). Clients automatically track the
last time they successfully ran a query to sync data.

When a delta query is run, the query’s resolver uses the `ds_pk` and
`ds_sk` to query only for the records that have changed since the last time the
client performed a sync. The client stores the appropriate GraphQL response.

For more information on executing Sync Queries, see the [Sync Operation
documentation](aws-appsync-conflict-detection-and-sync-sync-operations.md "aws-appsync-conflict-detection-and-sync-sync-operations.md").

## Example

Let’s start first by calling a `createPost` mutation to create an item:

```
mutation create {
  createPost(input: {author: "Nadia", title: "My First Post", content: "Hello World"}) {
    id
    author
    title
    content
    _version
    _lastChangedAt
    _deleted
  }
}
```

The return value of this mutation will look as follows:

```
{
  "data": {
    "createPost": {
      "id": "81d36bbb-1579-4efe-92b8-2e3f679f628b",
      "author": "Nadia",
      "title": "My First Post",
      "content": "Hello World",
      "_version": 1,
      "_lastChangedAt": 1574469356331,
      "_deleted": null
    }
  }
}
```

If you examine the contents of the _Base_ table,
you will see a record that looks like:

```
{
  "_lastChangedAt": {
    "N": "1574469356331"
  },
  "_version": {
    "N": "1"
  },
  "author": {
    "S": "Nadia"
  },
  "content": {
    "S": "Hello World"
  },
  "id": {
    "S": "81d36bbb-1579-4efe-92b8-2e3f679f628b"
  },
  "title": {
    "S": "My First Post"
  }
}
```

If you examine the contents of the _Delta_
table, you will see a record that looks like:

```
{
  "_lastChangedAt": {
    "N": "1574469356331"
  },
  "_ttl": {
    "N": "1574472956"
  },
  "_version": {
    "N": "1"
  },
  "author": {
    "S": "Nadia"
  },
  "content": {
    "S": "Hello World"
  },
  "ds_pk": {
    "S": "AppSync-delta-sync-post:2019-11-23"
  },
  "ds_sk": {
    "S": "00:35:56.331:81d36bbb-1579-4efe-92b8-2e3f679f628b:1"
  },
  "id": {
    "S": "81d36bbb-1579-4efe-92b8-2e3f679f628b"
  },
  "title": {
    "S": "My First Post"
  }
}
```

Now we can simulate a _Base_ query that a client
will run to hydrate its local data store using a `syncPosts` query like:

```
query baseQuery {
  syncPosts(limit: 100, lastSync: null, nextToken: null) {
    items {
      id
      author
      title
      content
      _version
      _lastChangedAt
    }
    startedAt
    nextToken
  }
}
```

The return value of this _Base_ query will look
as follows:

```
{
  "data": {
    "syncPosts": {
      "items": [
        {
          "id": "81d36bbb-1579-4efe-92b8-2e3f679f628b",
          "author": "Nadia",
          "title": "My First Post",
          "content": "Hello World",
          "_version": 1,
          "_lastChangedAt": 1574469356331
        }
      ],
      "startedAt": 1574469602238,
      "nextToken": null
    }
  }
}
```

We’ll save the `startedAt` value later to simulate a _Delta_ query, but first we need to make a change to our
table. Let’s use the `updatePost` mutation to modify our existing Post:

```
mutation updatePost {
  updatePost(input: {id: "81d36bbb-1579-4efe-92b8-2e3f679f628b", _version: 1, title: "Actually this is my Second Post"}) {
    id
    author
    title
    content
    _version
    _lastChangedAt
    _deleted
  }
}
```

The return value of this mutation will look as follows:

```
{
  "data": {
    "updatePost": {
      "id": "81d36bbb-1579-4efe-92b8-2e3f679f628b",
      "author": "Nadia",
      "title": "Actually this is my Second Post",
      "content": "Hello World",
      "_version": 2,
      "_lastChangedAt": 1574469851417,
      "_deleted": null
    }
  }
}
```

If you examine the contents of the _Base_ table
now, you should see the updated item:

```
{
  "_lastChangedAt": {
    "N": "1574469851417"
  },
  "_version": {
    "N": "2"
  },
  "author": {
    "S": "Nadia"
  },
  "content": {
    "S": "Hello World"
  },
  "id": {
    "S": "81d36bbb-1579-4efe-92b8-2e3f679f628b"
  },
  "title": {
    "S": "Actually this is my Second Post"
  }
}
```

If you examine the contents of the _Delta_ table
now, you should see two records:

1. A record when the item was created
2. A record for when the item was updated.

The new item will look like:

```
{
  "_lastChangedAt": {
    "N": "1574469851417"
  },
  "_ttl": {
    "N": "1574473451"
  },
  "_version": {
    "N": "2"
  },
  "author": {
    "S": "Nadia"
  },
  "content": {
    "S": "Hello World"
  },
  "ds_pk": {
    "S": "AppSync-delta-sync-post:2019-11-23"
  },
  "ds_sk": {
    "S": "00:44:11.417:81d36bbb-1579-4efe-92b8-2e3f679f628b:2"
  },
  "id": {
    "S": "81d36bbb-1579-4efe-92b8-2e3f679f628b"
  },
  "title": {
    "S": "Actually this is my Second Post"
  }
}
```

Now we can simulate a _Delta_ query to retrieve
modifications that occurred when a client was offline. We will use the `startedAt`
value returned from our _Base_ query to make the
request:

```
query delta {
  syncPosts(limit: 100, lastSync: 1574469602238, nextToken: null) {
    items {
      id
      author
      title
      content
      _version
    }
    startedAt
    nextToken
  }
}
```

The return value of this _Delta_ query will look
as follows:

```
{
  "data": {
    "syncPosts": {
      "items": [
        {
          "id": "81d36bbb-1579-4efe-92b8-2e3f679f628b",
          "author": "Nadia",
          "title": "Actually this is my Second Post",
          "content": "Hello World",
          "_version": 2
        }
      ],
      "startedAt": 1574470400808,
      "nextToken": null
    }
  }
}
```
