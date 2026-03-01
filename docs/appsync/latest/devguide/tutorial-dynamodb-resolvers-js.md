# Creating a simple post application using DynamoDB JavaScript resolvers

In this tutorial, you will import your Amazon DynamoDB tables to AWS AppSync and connect them to build a fully-functional
GraphQL API using JavaScript pipeline resolvers that you can leverage in your own application.

You will use the AWS AppSync console to provision your Amazon DynamoDB resources, create your resolvers, and connect them
to your data sources. You will also be able to read and write to your Amazon DynamoDB database through GraphQL
statements and subscribe to real-time data.

There are specific steps that must be completed in order for GraphQL statements to be translated to Amazon DynamoDB
operations and for responses to be translated back into GraphQL. This tutorial outlines the configuration
process through several real-world scenarios and data access patterns.

## Creating your GraphQL API

**To create a GraphQL API in AWS AppSync**

1. Open the AppSync console and choose **Create API**.
2. Select **Design from scratch** and choose **Next**.
3. Name your API `PostTutorialAPI`, then choose **Next**.
   Skip to the review page while keeping the rest of the options set to their default values and choose
   `Create`.

The AWS AppSync console creates a new GraphQL API for you. By detault, it's using the API key authentication
mode. You can use the console to set up the rest of the GraphQL API and run queries against it for the rest
of this tutorial.

## Defining a basic post API

Now that you have your GraphQL API, you can set up a basic schema that allows the basic creation,
retrieval, and deletion of post data.

**To add data to your schema**

1. In your API, choose the **Schema** tab.
2. We will create a schema that defines a `Post` type and an operation
   `addPost` to add and get `Post` objects. In the **Schema** pane, replace the contents with the following code:

```
schema {
    query: Query
    mutation: Mutation
}

type Query {
    getPost(id: ID): Post
}

type Mutation {
    addPost(
        id: ID!
        author: String!
        title: String!
        content: String!
        url: String!
    ): Post!
}

type Post {
    id: ID!
    author: String
    title: String
    content: String
    url: String
    ups: Int!
    downs: Int!
    version: Int!
}
```

3. Choose **Save Schema**.

## Setting up your Amazon DynamoDB table

The AWS AppSync console can help provision the AWS resources needed to store your own resources in an
Amazon DynamoDB table. In this step, you’ll create an Amazon DynamoDB table to store your posts. You’ll also set up a
[secondary
index](../../../amazondynamodb/latest/developerguide/SecondaryIndexes.md "../../../amazondynamodb/latest/developerguide/SecondaryIndexes.md") that we’ll use later.

**To create your Amazon DynamoDB table**

1. On the **Schema** page, choose **Create
   Resources**.
2. Choose **Use existing type**, then choose the `Post`
   type.
3. In the **Additional Indexes** section, choose **Add Index**.
4. Name the index `author-index`.
5. Set the `Primary key` to `author` and the `Sort` key to
   `None`.
6. Disable **Automatically generate GraphQL**. In this example, we'll
   create the resolver ourselves.
7. Choose **Create**.

You now have a new data source called `PostTable`, which you can see by visiting **Data sources** in the side tab. You will use this data source to link your queries
and mutations to your Amazon DynamoDB table.

## Setting up an addPost resolver (Amazon DynamoDB PutItem)

Now that AWS AppSync is aware of the Amazon DynamoDB table, you can link it to individual queries and mutations by
defining resolvers. The first resolver you create is the `addPost` pipeline resolver using
JavaScript, which enables you to create a post in your Amazon DynamoDB table. A pipeline resolver has the
following components:

- The location in the GraphQL schema to attach the resolver. In this case, you are setting up a
  resolver on the `createPost` field on the `Mutation` type. This resolver will
  be invoked when the caller calls mutation `{ addPost(...){...} }`.
- The data source to use for this resolver. In this case, you want to use the DynamoDB data source you
  defined earlier, so you can add entries into the `post-table-for-tutorial` DynamoDB
  table.
- The request handler. The request handler is a function that handles the incoming request from the
  caller and translates it into instructions for AWS AppSync to perform against DynamoDB.
- The response handler. The job of the response handler is to handle the response from DynamoDB and
  translate it back into something that GraphQL expects. This is useful if the shape of the data in
  DynamoDB is different to the `Post` type in GraphQL, but in this case they have the same
  shape, so you just pass the data through.

**To set up your resolver**

1. In your API, choose the **Schema** tab.
2. In the **Resolvers** pane, find the `addPost` field under
   the `Mutation` type, then choose **Attach**.
3. Choose your data source, then choose **Create**.
4. In your code editor, replace the code with this snippet:

```
import { util } from '@aws-appsync/utils'
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	const item = { ...ctx.arguments, ups: 1, downs: 0, version: 1 }
	const key = { id: ctx.args.id ?? util.autoId() }
	return ddb.put({ key, item })
}

export function response(ctx) {
	return ctx.result
}
```

5. Choose **Save**.

###### Note

In this code, you use the DynamoDB module utils that allow you to easily create DynamoDB
requests.

AWS AppSync comes with a utility for automatic ID generation called `util.autoId()`, which is used
to generate an ID for your new post. If you do not specify an ID, the utility will automatically generate it
for you.

```
const key = { id: ctx.args.id ?? util.autoId() }
```

For more information about the utilities available for JavaScript, see [JavaScript
runtime features for resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md").

### Call the API to add a post

Now that the resolver has been configured, AWS AppSync can translate an incoming `addPost`
mutation to an Amazon DynamoDB `PutItem` operation. You can now run a mutation to put something in
the table.

**To run the operation**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation:

```
mutation addPost {
  addPost(
    id: 123,
    author: "AUTHORNAME"
    title: "Our first post!"
    content: "This is our first post."
    url: "https://aws.amazon.com/appsync/"
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `addPost`. The results of the newly created post should appear in the **Results** pane to the right of the **Queries** pane. It should look similar to the following:

```
{
  "data": {
    "addPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our first post!",
      "content": "This is our first post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

The following explanation shows what occurred:

1. AWS AppSync received an `addPost` mutation request.
2. AWS AppSync executes the request handler of the resolver. The `ddb.put` function creates
   a `PutItem` request that looks like this:

```
{
  operation: 'PutItem',
  key: { id: { S: '123' } },
  attributeValues: {
    downs: { N: 0 },
    author: { S: 'AUTHORNAME' },
    ups: { N: 1 },
    title: { S: 'Our first post!' },
    version: { N: 1 },
    content: { S: 'This is our first post.' },
    url: { S: 'https://aws.amazon.com/appsync/' }
  }
}
```

3. AWS AppSync uses this value to generate and execute a Amazon DynamoDB `PutItem`
   request.
4. AWS AppSync took the results of the `PutItem` request and converted them back to GraphQL
   types.

```
{
    "id" : "123",
    "author": "AUTHORNAME",
    "title": "Our first post!",
    "content": "This is our first post.",
    "url": "https://aws.amazon.com/appsync/",
    "ups" : 1,
    "downs" : 0,
    "version" : 1
}
```

5. The response handler returns the result immediately (`return ctx.result`).
6. The final result is visible in the GraphQL response.

## Setting up the getPost resolver (Amazon DynamoDB GetItem)

Now that you’re able to add data to the Amazon DynamoDB table, you need to set up the `getPost` query
so it can retrieve that data from the table. To do this, you set up another resolver.

**To add your resolver**

1. In your API, choose the **Schema** tab.
2. In the **Resolvers** pane on the right, find the `getPost`
   field on the `Query` type and then choose **Attach**.
3. Choose your data source, then choose **Create**.
4. In the code editor, replace the code with this snippet:

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	return ddb.get({ key: { id: ctx.args.id } })
}

export const response = (ctx) => ctx.result
```

5. Save your resolver.

###### Note

In this resolver, we use an arrow function expression for the response handler.

### Call the API to get a post

Now that the resolver has been set up, AWS AppSync knows how to translate an incoming `getPost`
query to an Amazon DynamoDB `GetItem` operation. You can now run a query to retrieve the post you
created earlier.

**To run your query**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following code, and use the id
   that you copied after creating your post:

```
query getPost {
  getPost(id: "123") {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `getPost`. The results of the newly created post should appear in the **Results** pane to the right of the **Queries** pane.
4. The post retrieved from Amazon DynamoDB should appear in the **Results** pane to the right of the **Queries** pane.
   It should look similar to the following:

```
{
  "data": {
    "getPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our first post!",
      "content": "This is our first post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

Alternatively, take the following example:

```
query getPost {
  getPost(id: "123") {
    id
    author
    title
  }
}
```

If your `getPost` query only needs the `id`, `author`, and
`title`, you can change your request function to use projection expressions to specify only
the attributes that you want from your DynamoDB table to avoid unnecessary data transfer from DynamoDB to AWS AppSync.
For example, the request function may look like the snippet below:

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	return ddb.get({
		key: { id: ctx.args.id },
		projection: ['author', 'id', 'title'],
	})
}

export const response = (ctx) => ctx.result
```

You can also use a [selectionSetList](resolver-context-reference-js.md#aws-appsync-resolver-context-reference-info-js "resolver-context-reference-js.md#aws-appsync-resolver-context-reference-info-js") with `getPost` to represent the `expression`:

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	const projection = ctx.info.selectionSetList.map((field) => field.replace('/', '.'))
	return ddb.get({ key: { id: ctx.args.id }, projection })
}

export const response = (ctx) => ctx.result
```

## Create an updatePost mutation (Amazon DynamoDB UpdateItem)

So far, you can create and retrieve `Post` objects in Amazon DynamoDB. Next, you’ll set up a new
mutation to update an object. Compared to the `addPost` mutation that requires all fields to be
specified, this mutation allows you to only specify the fields that you want to change. It also introduced a
new `expectedVersion` argument that allows you to specify the version that you want to modify.
You’ll set up a condition that makes sure that you are modifying the latest version of the object. You’ll do
this using the `UpdateItem` Amazon DynamoDB operation.sc

**To update your resolver**

1. In your API, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Mutation` type to add
   a new `updatePost` mutation as follows:

```
type Mutation {
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post

    addPost(
        id: ID
        author: String!
        title: String!
        content: String!
        url: String!
    ): Post!
}
```

3. Choose **Save Schema**.
4. In the **Resolvers** pane on the right, find the newly created
   `updatePost` field on the `Mutation` type, then choose **Attach**. Create your new resolver using the snippet below:

```
import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  const { id, expectedVersion, ...rest } = ctx.args;
  const values = Object.entries(rest).reduce((obj, [key, value]) => {
    obj[key] = value ?? ddb.operations.remove();
    return obj;
  }, {});

  return ddb.update({
    key: { id },
    condition: { version: { eq: expectedVersion } },
    update: { ...values, version: ddb.operations.increment(1) },
  });
}

export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    util.appendError(error.message, error.type);
  }
  return result;
```

5. Save any changes you made.

This resolver uses `ddb.update` to create an Amazon DynamoDB `UpdateItem` request. Instead
of writing the entire item, you’re just asking Amazon DynamoDB to update certain attributes. This is done using
Amazon DynamoDB update expressions.

The `ddb.update` function takes a key and an update object as arguments. Then, you check the
values of the incoming arguments. When a value is set to `null`, use the DynamoDB
`remove` operation to signal that the value should be removed from the DynamoDB item.

There is also a new `condition` section. A condition expression allows you tell AWS AppSync and
Amazon DynamoDB whether or not the request should succeed based on the state of the object already in Amazon DynamoDB
before the operation is performed. In this case, you only want the `UpdateItem` request to
succeed if the `version` field of the item currently in Amazon DynamoDB matches the
`expectedVersion` argument exactly. When the item is updated, we want to increment the value
of the `version`. This is easy to do with the operation function `increment`.

For more information about condition expressions, see the [Condition expressions](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions") documentation.

For more info about the `UpdateItem` request, see the [UpdateItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-updateitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-updateitem") documentation and the [DynamoDB
module](built-in-modules-js.md "built-in-modules-js.md") documentation.

For more information about how to write update expressions, see the [DynamoDB
UpdateExpressions](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md") documentation.

### Call the API to update a post

Let’s try updating the `Post` object with the new resolver.

**To update your object**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation. You’ll also
   need to update the `id` argument to the value you noted down earlier:

```
mutation updatePost {
  updatePost(
    id:123
    title: "An empty story"
    content: null
    expectedVersion: 1
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `updatePost`.
4. The updated post in Amazon DynamoDB should appear in the **Results**
   pane to the right of the **Queries** pane. It should look similar
   to the following:

```
{
  "data": {
    "updatePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 2
    }
  }
}
```

In this request, you asked AWS AppSync and Amazon DynamoDB to update the `title` and
`content` fields only. All of the other fields were left alone (other than incrementing
the `version` field). You set the `title` attribute to a new value and removed the
`content` attribute from the post. The `author`, `url`,
`ups`, and `downs` fields were left untouched. Try executing the mutation
request again while leaving the request exactly as is. You should see a response similar to the
following:

```
{
  "data": {
    "updatePost": null
  },
  "errors": [
    {
      "path": [
        "updatePost"
      ],
      "data": null,
      "errorType": "DynamoDB:ConditionalCheckFailedException",
      "errorInfo": null,
      "locations": [
        {
          "line": 2,
          "column": 3,
          "sourceName": null
        }
      ],
      "message": "The conditional request failed (Service: DynamoDb, Status Code: 400, Request ID: 1RR3QN5F35CS8IV5VR4OQO9NNBVV4KQNSO5AEMVJF66Q9ASUAAJG)"
    }
  ]
}
```

The request fails because the condition expression evaluates to `false`:

1. The first time you ran the request, the value of the `version` field of the post in
   Amazon DynamoDB was `1`, which matched the `expectedVersion` argument. The
   request succeeded, which meant the `version` field was incremented in Amazon DynamoDB to
   `2`.
2. The second time you ran the request, the value of the `version` field of the post
   in Amazon DynamoDB was `2`, which did not match the `expectedVersion`
   argument.

This pattern is typically called _optimistic locking_.

## Create vote mutations (Amazon DynamoDB UpdateItem)

The `Post` type contains `ups` and `downs` fields to enable the recording
of upvotes and downvotes. However, at this moment, the API doesn’t let us do anything with them. Let’s add a
mutation to let us upvote and downvote the posts.

**To add your mutation**

1. In your API, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Mutation` type and add
   the `DIRECTION` enum to add new vote mutations:

```
type Mutation {
    vote(id: ID!, direction: DIRECTION!): Post
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post
    addPost(
        id: ID,
        author: String!,
        title: String!,
        content: String!,
        url: String!
    ): Post!
}

enum DIRECTION {
  UP
  DOWN
}
```

3. Choose **Save Schema**.
4. In the **Resolvers** pane on the right, find the newly created
   `vote` field on the `Mutation` type, and then choose **Attach**. Create a new resolver by creating and replacing the code with the following
   snippet:

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  const field = ctx.args.direction === 'UP' ? 'ups' : 'downs';
  return ddb.update({
    key: { id: ctx.args.id },
    update: {
      [field]: ddb.operations.increment(1),
      version: ddb.operations.increment(1),
    },
  });
}

export const response = (ctx) => ctx.result;
```

5. Save any changes you made.

### Call the API to upvote or downvote a post

Now that the new resolvers have been set up, AWS AppSync knows how to translate an incoming
`upvotePost` or `downvote` mutation to an Amazon DynamoDB `UpdateItem`
operation. You can now run mutations to upvote or downvote the post you created earlier.

**To run your mutation**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation. You’ll also
   need to update the `id` argument to the value you noted down earlier:

```
mutation votePost {
  vote(id:123, direction: UP) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `votePost`.
4. The updated post in Amazon DynamoDB should appear in the **Results**
   pane to the right of the **Queries** pane. It should look similar
   to the following:

```
{
  "data": {
    "vote": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 6,
      "downs": 0,
      "version": 4
    }
  }
}
```

5. Choose **Run** a few more times. You should see the
   `ups` and `version` fields incrementing by `1` each time
   you execute the query.
6. Change the query to call it with a different `DIRECTION`.

```
mutation votePost {
  vote(id:123, direction: DOWN) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

7. Choose **Run** (the orange play button), then choose
   `votePost`.

This time, you should see the `downs` and `version` fields incrementing
by `1` each time you run the query.

## Setting up a deletePost resolver (Amazon DynamoDB DeleteItem)

Next, you'll want to create a mutation to delete a post. You’ll do this using the `DeleteItem`
Amazon DynamoDB operation.

**To add your mutation**

1. In your schema, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Mutation` type to add
   a new `deletePost` mutation:

```
type Mutation {
    deletePost(id: ID!, expectedVersion: Int): Post
    vote(id: ID!, direction: DIRECTION!): Post
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post
    addPost(
        id: ID
        author: String!,
        title: String!,
        content: String!,
        url: String!
    ): Post!
}
```

3. This time, you made the `expectedVersion` field optional. Next, choose **Save Schema**.
4. In the **Resolvers** pane on the right, find the newly created
   `delete` field in the `Mutation` type, then choose **Attach**. Create a new resolver using the following code:

```
import { util } from '@aws-appsync/utils'

import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  let condition = null;
  if (ctx.args.expectedVersion) {
    condition = {
      or: [
        { id: { attributeExists: false } },
        { version: { eq: ctx.args.expectedVersion } },
      ],
    };
  }
  return ddb.remove({ key: { id: ctx.args.id }, condition });
}

export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    util.appendError(error.message, error.type);
  }
  return result;
}
```

###### Note

The `expectedVersion` argument is an optional argument. If the caller set an
`expectedVersion` argument in the request, the request handler adds a condition
that only allows the `DeleteItem` request to succeed if the item is already deleted
or if the `version` attribute of the post in Amazon DynamoDB exactly matches the
`expectedVersion`. If left out, no condition expression is specified on the
`DeleteItem` request. It succeeds regardless of the value of `version`
or whether or not the item exists in Amazon DynamoDB.

Even though you’re deleting an item, you can return the item that was deleted, if it was not
already deleted.

For more info about the `DeleteItem` request, see the [DeleteItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-deleteitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-deleteitem") documentation.

### Call the API to delete a post

Now that the resolver has been set up, AWS AppSync knows how to translate an incoming `delete`
mutation to an Amazon DynamoDB `DeleteItem` operation. You can now run a mutation to delete
something in the table.

**To run your mutation**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation. You’ll also
   need to update the `id` argument to the value you noted down earlier:

```
mutation deletePost {
  deletePost(id:123) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `deletePost`.
4. The post is deleted from Amazon DynamoDB. Note that AWS AppSync returns the value of the item that was
   deleted from Amazon DynamoDB, which should appear in the **Results** pane
   to the right of the **Queries** pane. It should look similar to the
   following:

```
{
  "data": {
    "deletePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 6,
      "downs": 4,
      "version": 12
    }
  }
}
```

5. The value is only returned if this call to `deletePost` is the one that actually
   deletes it from Amazon DynamoDB. Choose **Run** again.
6. The call still succeeds, but no value is returned:

```
{
  "data": {
    "deletePost": null
  }
}
```

7. Now, let’s try deleting a post, but this time specifying an `expectedValue`. First,
   you’ll need to create a new post because you’ve just deleted the one you’ve been working with so
   far.
8. In the **Queries** pane, add the following mutation:

```
mutation addPost {
  addPost(
    id:123
    author: "AUTHORNAME"
    title: "Our second post!"
    content: "A new post."
    url: "https://aws.amazon.com/appsync/"
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

9. Choose **Run** (the orange play button), then choose
   `addPost`.
10. The results of the newly created post should appear in the **Results** pane to the right of the **Queries** pane.
    Record the `id` of the newly created object because you'll need it in just a moment.
    It should look similar to the following:

```
{
  "data": {
    "addPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our second post!",
      "content": "A new post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

11. Now, let’s try to delete that post with an illegal value for **expectedVersion**. In the **Queries** pane, add the
    following mutation. You’ll also need to update the `id` argument to the value you
    noted down earlier:

```
mutation deletePost {
  deletePost(
    id:123
    expectedVersion: 9999
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

12. Choose **Run** (the orange play button), then choose
    `deletePost`. The following result is returned:

```
{
  "data": {
    "deletePost": null
  },
  "errors": [
    {
      "path": [
        "deletePost"
      ],
      "data": null,
      "errorType": "DynamoDB:ConditionalCheckFailedException",
      "errorInfo": null,
      "locations": [
        {
          "line": 2,
          "column": 3,
          "sourceName": null
        }
      ],
      "message": "The conditional request failed (Service: DynamoDb, Status Code: 400, Request ID: 7083O037M1FTFRK038A4CI9H43VV4KQNSO5AEMVJF66Q9ASUAAJG)"
    }
  ]
}
```

13. The request failed because the condition expression evaluates to `false`. The value
    for `version` of the post in Amazon DynamoDB doesn't match the `expectedValue`
    specified in the arguments. The current value of the object is returned in the `data`
    field in the `errors` section of the GraphQL response. Retry the request, but correct
    the `expectedVersion`:

```
mutation deletePost {
  deletePost(
    id:123
    expectedVersion: 1
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

14. Choose **Run** (the orange play button), then choose
    `deletePost`.

This time the request succeeds, and the value that was deleted from Amazon DynamoDB is
returned:

```
{
  "data": {
    "deletePost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our second post!",
      "content": "A new post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

15. Choose **Run** again. The call still succeeds, but this time no
    value is returned because the post was already deleted in Amazon DynamoDB.

```
{ "data": { "deletePost": null } }
```

## Setting up an allPost resolver (Amazon DynamoDB Scan)

So far, the API is only useful if you know the `id` of each post you want to look at. Let’s add
a new resolver that returns all the posts in the table.

**To add your mutation**

1. In your API, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Query` type to add a
   new `allPost` query as follows:

```
type Query {
    allPost(limit: Int, nextToken: String): PaginatedPosts!
    getPost(id: ID): Post
}
```

3. Add a new `PaginationPosts` type:

```
type PaginatedPosts {
    posts: [Post!]!
    nextToken: String
}
```

4. Choose **Save Schema**.
5. In the **Resolvers** pane on the right, find the newly created
   `allPost` field in the `Query` type, then choose **Attach**. Create a new resolver with the following code:

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  const { limit = 20, nextToken } = ctx.arguments;
  return ddb.scan({ limit, nextToken });
}

export function response(ctx) {
  const { items: posts = [], nextToken } = ctx.result;
  return { posts, nextToken };
}
```

This resolver's request handler expects two optional arguments:

    * `limit` - Specifies the maximum number of items to return in a single
     call.
    * `nextToken` - Used to retrieve the next set of results (we’ll show where the
     value for `nextToken` comes from later).

6. Save any changes made to your resolver.

For more information about `Scan` request, see the [Scan](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-scan "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-scan") reference documentation.

### Call the API to scan all posts

Now that the resolver has been set up, AWS AppSync knows how to translate an incoming `allPost`
query to an Amazon DynamoDB `Scan` operation. You can now scan the table to retrieve all the posts.
Before you can try it out though, you need to populate the table with some data because you’ve deleted
everything you’ve worked with so far.

**To add and query data**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation:

```
mutation addPost {
  post1: addPost(id:1 author: "AUTHORNAME" title: "A series of posts, Volume 1" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post2: addPost(id:2 author: "AUTHORNAME" title: "A series of posts, Volume 2" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post3: addPost(id:3 author: "AUTHORNAME" title: "A series of posts, Volume 3" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post4: addPost(id:4 author: "AUTHORNAME" title: "A series of posts, Volume 4" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post5: addPost(id:5 author: "AUTHORNAME" title: "A series of posts, Volume 5" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post6: addPost(id:6 author: "AUTHORNAME" title: "A series of posts, Volume 6" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post7: addPost(id:7 author: "AUTHORNAME" title: "A series of posts, Volume 7" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post8: addPost(id:8 author: "AUTHORNAME" title: "A series of posts, Volume 8" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post9: addPost(id:9 author: "AUTHORNAME" title: "A series of posts, Volume 9" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
}
```

3. Choose **Run** (the orange play button).
4. Now, let’s scan the table, returning five results at a time. In the **Queries** pane, add the following query:

```
query allPost {
  allPost(limit: 5) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

5. Choose **Run** (the orange play button), then choose
   `allPost`.

The first five posts should appear in the **Results** pane to the
right of the **Queries** pane. It should look similar to the
following:

```
{
  "data": {
    "allPost": {
      "posts": [
        {
          "id": "5",
          "title": "A series of posts, Volume 5"
        },
        {
          "id": "1",
          "title": "A series of posts, Volume 1"
        },
        {
          "id": "6",
          "title": "A series of posts, Volume 6"
        },
        {
          "id": "9",
          "title": "A series of posts, Volume 9"
        },
        {
          "id": "7",
          "title": "A series of posts, Volume 7"
        }
      ],
      "nextToken": "<token>"
    }
  }
}
```

6. You received five results and a `nextToken` that you can use to get the next set of
   results. Update the `allPost` query to include the `nextToken` from the
   previous set of results:

```
query allPost {
  allPost(
    limit: 5
    nextToken: "<token>"
  ) {
    posts {
      id
      author
    }
    nextToken
  }
}
```

7. Choose **Run** (the orange play button), then choose
   `allPost`.

The remaining four posts should appear in the **Results** pane to
the right of the **Queries** pane. There is no
`nextToken` in this set of results because you’ve paged through all nine posts
with none remaining. It should look similar to the following:

```
{
  "data": {
    "allPost": {
      "posts": [
        {
          "id": "2",
          "title": "A series of posts, Volume 2"
        },
        {
          "id": "3",
          "title": "A series of posts, Volume 3"
        },
        {
          "id": "4",
          "title": "A series of posts, Volume 4"
        },
        {
          "id": "8",
          "title": "A series of posts, Volume 8"
        }
      ],
      "nextToken": null
    }
  }
}
```

## Setting up an allPostsByAuthor resolver(Amazon DynamoDB Query)

In addition to scanning Amazon DynamoDB for all posts, you can also query Amazon DynamoDB to retrieve posts created by
a specific author. The Amazon DynamoDB table you created earlier already has a `GlobalSecondaryIndex`
called `author-index` that you can use with an Amazon DynamoDB `Query` operation to retrieve
all posts created by a specific author.

**To add your query**

1. In your API, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Query` type to add a
   new `allPostsByAuthor` query as follows:

```
type Query {
    allPostsByAuthor(author: String!, limit: Int, nextToken: String): PaginatedPosts!
    allPost(limit: Int, nextToken: String): PaginatedPosts!
    getPost(id: ID): Post
}
```

Note that this uses the same `PaginatedPosts` type that you used with the
`allPost` query. 3. Choose **Save Schema**. 4. In the **Resolvers** pane on the right, find the newly created
`allPostsByAuthor` field on the `Query` type, and then choose **Attach**. Create a resolver using the snippet below:

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  const { limit = 20, nextToken, author } = ctx.arguments;
  return ddb.query({
    index: 'author-index',
    query: { author: { eq: author } },
    limit,
    nextToken,
  });
}

export function response(ctx) {
  const { items: posts = [], nextToken } = ctx.result;
  return { posts, nextToken };
}
```

Like the `allPost` resolver, this resolver has two optional arguments:

    * `limit` - Specifies the maximum number of items to return in a single
     call.
    * `nextToken` - Retrieves the next set of results (the value for
     `nextToken` can be obtained from a previous call).

5. Save any changes made to your resolver.

For more information about the `Query` request, see the [Query](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-query "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-query") reference documentation.

### Call the API to query all posts by author

Now that the resolver has been set up, AWS AppSync knows how to translate an incoming
`allPostsByAuthor` mutation to a DynamoDB `Query` operation against the
`author-index` index. You can now query the table to retrieve all the posts by a specific
author.

Before this, however, let’s populate the table with some more posts, because every post so far has the
same author.

**To add data and query**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following mutation:

```
mutation addPost {
  post1: addPost(id:10 author: "Nadia" title: "The cutest dog in the world" content: "So cute. So very, very cute." url: "https://aws.amazon.com/appsync/" ) { author, title }
  post2: addPost(id:11 author: "Nadia" title: "Did you know...?" content: "AppSync works offline?" url: "https://aws.amazon.com/appsync/" ) { author, title }
  post3: addPost(id:12 author: "Steve" title: "I like GraphQL" content: "It's great" url: "https://aws.amazon.com/appsync/" ) { author, title }
}
```

3. Choose **Run** (the orange play button), then choose
   `addPost`.
4. Now, let’s query the table, returning all posts authored by `Nadia`. In the
   **Queries** pane, add the following query:

```
query allPostsByAuthor {
  allPostsByAuthor(author: "Nadia") {
    posts {
      id
      title
    }
    nextToken
  }
}
```

5. Choose **Run** (the orange play button), then choose
   `allPostsByAuthor`. All posts authored by `Nadia` should appear in the
   **Results** pane to the right of the **Queries** pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world"
        },
        {
          "id": "11",
          "title": "Did you know...?"
        }
      ],
      "nextToken": null
    }
  }
}
```

6. Pagination works for `Query` just the same as it does for `Scan`. For
   example, let’s look for all posts by `AUTHORNAME`, getting five at a time.
7. In the **Queries** pane, add the following query:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "AUTHORNAME"
    limit: 5
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

8. Choose **Run** (the orange play button), then choose
   `allPostsByAuthor`. All posts authored by `AUTHORNAME` should appear
   in the **Results** pane to the right of the **Queries** pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "6",
          "title": "A series of posts, Volume 6"
        },
        {
          "id": "4",
          "title": "A series of posts, Volume 4"
        },
        {
          "id": "2",
          "title": "A series of posts, Volume 2"
        },
        {
          "id": "7",
          "title": "A series of posts, Volume 7"
        },
        {
          "id": "1",
          "title": "A series of posts, Volume 1"
        }
      ],
      "nextToken": "<token>"
    }
  }
}
```

9. Update the `nextToken` argument with the value returned from the previous query as
   follows:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "AUTHORNAME"
    limit: 5
    nextToken: "<token>"
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

10. Choose **Run** (the orange play button), then choose
    `allPostsByAuthor`. The remaining posts authored by `AUTHORNAME`
    should appear in the **Results** pane to the right of the **Queries** pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "8",
          "title": "A series of posts, Volume 8"
        },
        {
          "id": "5",
          "title": "A series of posts, Volume 5"
        },
        {
          "id": "3",
          "title": "A series of posts, Volume 3"
        },
        {
          "id": "9",
          "title": "A series of posts, Volume 9"
        }
      ],
      "nextToken": null
    }
  }
}
```

## Using sets

Up to this point, the `Post` type has been a flat key/value object. You can also model complex
objects with your resolver, such as sets, lists, and maps. Let’s update the `Post` type to
include tags. A post can have zero or more tags, which are stored in DynamoDB as a String Set. You’ll also set
up some mutations to add and remove tags, and a new query to scan for posts with a specific tag.

**To set up your data**

1. In your API, choose the **Schema** tab.
2. In the **Schema** pane, modify the `Post` type to add a
   new `tags` field as follows:

```
type Post {
  id: ID!
  author: String
  title: String
  content: String
  url: String
  ups: Int!
  downs: Int!
  version: Int!
  tags: [String!]
}
```

3. In the **Schema** pane, modify the `Query` type to add a
   new `allPostsByTag` query as follows:

```
type Query {
  allPostsByTag(tag: String!, limit: Int, nextToken: String): PaginatedPosts!
  allPostsByAuthor(author: String!, limit: Int, nextToken: String): PaginatedPosts!
  allPost(limit: Int, nextToken: String): PaginatedPosts!
  getPost(id: ID): Post
}
```

4. In the **Schema** pane, modify the `Mutation` type to add
   new `addTag` and `removeTag` mutations as follows:

```
type Mutation {
  addTag(id: ID!, tag: String!): Post
  removeTag(id: ID!, tag: String!): Post
  deletePost(id: ID!, expectedVersion: Int): Post
  upvotePost(id: ID!): Post
  downvotePost(id: ID!): Post
  updatePost(
    id: ID!,
    author: String,
    title: String,
    content: String,
    url: String,
    expectedVersion: Int!
  ): Post
  addPost(
    author: String!,
    title: String!,
    content: String!,
    url: String!
  ): Post!
}
```

5. Choose **Save Schema**.
6. In the **Resolvers** pane on the right, find the newly created
   `allPostsByTag` field on the `Query` type, and then choose **Attach**. Create your resolver using the snippet below:

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
  const { limit = 20, nextToken, tag } = ctx.arguments;
  return ddb.scan({ limit, nextToken, filter: { tags: { contains: tag } } });
}

export function response(ctx) {
  const { items: posts = [], nextToken } = ctx.result;
  return { posts, nextToken };
}
```

7. Save any changes you've made to your resolver.
8. Now, do the same for the `Mutation` field `addTag` using the snippet
   below:

###### Note

Though the DynamoDB utils currently don't support set operations, you can still interact with
sets by building the request yourself.

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { id, tag } = ctx.arguments
	const expressionValues = util.dynamodb.toMapValues({ ':plusOne': 1 })
	expressionValues[':tags'] = util.dynamodb.toStringSet([tag])

	return {
		operation: 'UpdateItem',
		key: util.dynamodb.toMapValues({ id }),
		update: {
			expression: `ADD tags :tags, version :plusOne`,
			expressionValues,
		},
	}
}

export const response = (ctx) => ctx.result
```

9. Save any changes made to your resolver.
10. Repeat this one more time for the `Mutation` field `removeTag` using the
    snippet below:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
	  const { id, tag } = ctx.arguments;
	  const expressionValues = util.dynamodb.toMapValues({ ':plusOne': 1 });
	  expressionValues[':tags'] = util.dynamodb.toStringSet([tag]);

	  return {
	    operation: 'UpdateItem',
	    key: util.dynamodb.toMapValues({ id }),
	    update: {
	      expression: `DELETE tags :tags ADD version :plusOne`,
	      expressionValues,
	    },
	  };
	}

	export const response = (ctx) => ctx.resultexport
```

11. Save any changes made to your resolver.

### Call the API to work with tags

Now that you’ve set up the resolvers, AWS AppSync knows how to translate incoming `addTag`,
`removeTag`, and `allPostsByTag` requests into DynamoDB `UpdateItem`
and `Scan` operations. To try it out, let’s select one of the posts you created earlier. For
example, let’s use a post authored by `Nadia`.

**To use tags**

1. In your API, choose the **Queries** tab.
2. In the **Queries** pane, add the following query:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "Nadia"
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

3. Choose **Run** (the orange play button), then choose
   `allPostsByAuthor`.
4. All of Nadia’s posts should appear in the **Results** pane to the
   right of the **Queries** pane. It should look similar to the
   following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world"
        },
        {
          "id": "11",
          "title": "Did you known...?"
        }
      ],
      "nextToken": null
    }
  }
}
```

5. Let’s use the one with the title _The cutest dog in the
   world_. Record its `id` because you’ll use it later. Now, let’s try
   adding a `dog` tag.
6. In the **Queries** pane, add the following mutation. You’ll also
   need to update the `id` argument to the value you noted down earlier.

```
mutation addTag {
  addTag(id:10 tag: "dog") {
    id
    title
    tags
  }
}
```

7. Choose **Run** (the orange play button), then choose
   `addTag`. The post is updated with the new tag:

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog"
      ]
    }
  }
}
```

8. You can add more tags. Update the mutation to change the `tag` argument to
   `puppy`:

```
mutation addTag {
  addTag(id:10 tag: "puppy") {
    id
    title
    tags
  }
}
```

9. Choose **Run** (the orange play button), then choose
   `addTag`. The post is updated with the new tag:

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog",
        "puppy"
      ]
    }
  }
}
```

10. You can also delete tags. In the **Queries** pane, add the
    following mutation. You’ll also need to update the `id` argument to the value you
    noted down earlier:

```
mutation removeTag {
  removeTag(id:10 tag: "puppy") {
    id
    title
    tags
  }
}
```

11. Choose **Run** (the orange play button), then choose
    `removeTag`. The post is updated and the `puppy` tag is
    deleted.

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog"
      ]
    }
  }
}
```

12. You can also search for all posts that have a tag. In the **Queries** pane, add the following query:

```
query allPostsByTag {
  allPostsByTag(tag: "dog") {
    posts {
      id
      title
      tags
    }
    nextToken
  }
}
```

13. Choose **Run** (the orange play button), then choose
    `allPostsByTag`. All posts that have the `dog` tag are returned as
    follows:

```
{
  "data": {
    "allPostsByTag": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world",
          "tags": [
            "dog",
            "puppy"
          ]
        }
      ],
      "nextToken": null
    }
  }
}
```

## Conclusion

In this tutorial, you’ve built an API that lets you manipulate `Post` objects in DynamoDB using
AWS AppSync and GraphQL.

To clean up, you can delete the AWS AppSync GraphQL API from the console.

To delete the role associated with your DynamoDB table, select your data source in the **Data Sources** table and click **edit**. Note the value of the
role under **Create or use an existing role**. Go to the IAM console to delete
the role.

To delete your DynamoDB table, click on the name of the table in the data sources list. This takes you to the
DynamoDB console where you can delete the table.
