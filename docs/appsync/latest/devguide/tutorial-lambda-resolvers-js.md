# Using AWS Lambda resolvers in AWS AppSync

You can use AWS Lambda with AWS AppSync to resolve any GraphQL field. For example, a GraphQL
query might send a call to an Amazon Relational Database Service (Amazon RDS) instance, and a GraphQL mutation might write
to an Amazon Kinesis stream. In this section, we'll show you how to write a Lambda function that
performs business logic based on the invocation of a GraphQL field operation.

## Powertools for AWS Lambda

The Powertools for AWS Lambda GraphQL event handler simplifies the routing and
processing of GraphQL events in Lambda functions. It is available for Python and
Typescript. Read more about about the GraphQL API Event Handler on the Powertools for
AWS Lambda documentation, see the following references.

- [Powertools for AWS Lambda GraphQL Event Handler (Python)](../../../powertools/python/latest/core/event_handler/appsync.md "../../../powertools/python/latest/core/event_handler/appsync.md")
- [Powertools for AWS Lambda GraphQL Event Handler (Typescript)](../../../powertools/typescript/latest/features/event-handler/appsync-graphql.md "../../../powertools/typescript/latest/features/event-handler/appsync-graphql.md")

## Create a Lambda function

The following example shows a Lambda function written in `Node.js` (runtime: Node.js 18.x) that
performs different operations on blog posts as part of a blog post application. Note that the code should be
saved in a file name with a .mis extension.

```
export const handler = async (event) => {
console.log('Received event {}', JSON.stringify(event, 3))

  const posts = {
1: { id: '1', title: 'First book', author: 'Author1', url: 'https://amazon.com/', content: 'SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1', ups: '100', downs: '10', },
    2: { id: '2', title: 'Second book', author: 'Author2', url: 'https://amazon.com', content: 'SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT', ups: '100', downs: '10', },
    3: { id: '3', title: 'Third book', author: 'Author3', url: null, content: null, ups: null, downs: null },
    4: { id: '4', title: 'Fourth book', author: 'Author4', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4', ups: '1000', downs: '0', },
    5: { id: '5', title: 'Fifth book', author: 'Author5', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT', ups: '50', downs: '0', },
  }

  const relatedPosts = {
1: [posts['4']],
    2: [posts['3'], posts['5']],
    3: [posts['2'], posts['1']],
    4: [posts['2'], posts['1']],
    5: [],
  }

  console.log('Got an Invoke Request.')
  let result
  switch (event.field) {
case 'getPost':
      return posts[event.arguments.id]
    case 'allPosts':
      return Object.values(posts)
    case 'addPost':
      // return the arguments back
return event.arguments
    case 'addPostErrorWithData':
      result = posts[event.arguments.id]
      // attached additional error information to the post
      result.errorMessage = 'Error with the mutation, data has changed'
      result.errorType = 'MUTATION_ERROR'
return result
    case 'relatedPosts':
      return relatedPosts[event.source.id]
    default:
      throw new Error('Unknown field, unable to resolve ' + event.field)
  }
}
```

This Lambda function retrieves a post by ID, adds a post, retrieves a list of posts, and fetches related
posts for a given post.

###### Note

The Lambda function uses the `switch` statement on `event.field` to determine
which field is currently being resolved.

Create this Lambda function using the AWS Management Console.

## Configure a data source for Lambda

After you create the Lambda function, navigate to your GraphQL API in the AWS AppSync
console, and then choose the **Data Sources** tab.

Choose **Create data source**, enter a friendly **Data source name**
(for example, `Lambda`), and then for **Data source type**, choose
**AWS Lambda function**. For **Region**, choose the same Region as your
function. For **Function ARN**, choose the Amazon Resource Name (ARN) of your Lambda
function.

After choosing your Lambda function, you can either create a new AWS Identity and Access Management (IAM) role
(for which AWS AppSync assigns the appropriate permissions) or choose an existing role
that has the following inline policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:LAMBDA_FUNCTION"
 }
 ]
}`

```

You must also set up a trust relationship with AWS AppSync for the IAM role as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appsync.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Create a GraphQL schema

Now that the data source is connected to your Lambda function, create a GraphQL
schema.

From the schema editor in the AWS AppSync console, make sure that your schema matches
the following schema:

```
schema {
    query: Query
    mutation: Mutation
}
type Query {
    getPost(id:ID!): Post
    allPosts: [Post]
}
type Mutation {
    addPost(id: ID!, author: String!, title: String, content: String, url: String): Post!
}
type Post {
    id: ID!
    author: String!
    title: String
    content: String
    url: String
    ups: Int
    downs: Int
    relatedPosts: [Post]
}
```

## Configure resolvers

Now that you've registered a Lambda data source and a valid GraphQL schema, you can
connect your GraphQL fields to your Lambda data source using resolvers.

You will create a resolver that uses the AWS AppSync JavaScript (`APPSYNC_JS`) runtime and
interact with your Lambda functions. To learn more about writing AWS AppSync resolvers and functions with
JavaScript, see [JavaScript runtime features for resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md").

For more information about Lambda mapping templates, see [JavaScript resolver function reference for Lambda](resolver-reference-lambda-js.md "resolver-reference-lambda-js.md").

In this step, you attach a resolver to the Lambda function for the following fields: `getPost(id:ID!):
 Post`, `allPosts: [Post]`, `addPost(id: ID!, author: String!, title: String,
 content: String, url: String): Post!`, and `Post.relatedPosts: [Post]`. From the
**Schema** editor in the AWS AppSync console, in the **Resolvers** pane, choose **Attach** next to the
`getPost(id:ID!): Post` field. Choose your Lambda data source. Next, provide the following
code:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const {source, args} = ctx
  return {
    operation: 'Invoke',
    payload: { field: ctx.info.fieldName, arguments: args, source },
  };
}

export function response(ctx) {
  return ctx.result;
}
```

This resolver code passes the field name, list of arguments, and context about the source object to the
Lambda function when it invokes it. Choose **Save**.

You have successfully attached your first resolver. Repeat this operation for the remaining fields.

## Test your GraphQL API

Now that your Lambda function is connected to GraphQL resolvers, you can run some
mutations and queries using the console or a client application.

On the left side of the AWS AppSync console, choose **Queries**, and then paste in the following code:

### addPost Mutation

```
mutation AddPost {
    addPost(
        id: 6
        author: "Author6"
        title: "Sixth book"
        url: "https://www.amazon.com/"
        content: "This is the book is a tutorial for using GraphQL with AWS AppSync."
    ) {
        id
        author
        title
        content
        url
        ups
        downs
    }
}
```

### getPost Query

```
query GetPost {
    getPost(id: "2") {
        id
        author
        title
        content
        url
        ups
        downs
    }
}
```

### allPosts Query

```
query AllPosts {
    allPosts {
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {
            id
            title
        }
    }
}
```

## Returning errors

Any given field resolution can result in an error. With AWS AppSync, you can raise
errors from the following sources:

- Resolver response handler
- Lambda function

### From the resolver response handler

To raise intentional errors, you can use the `util.error` utility method. It takes an
argument an `errorMessage`, an `errorType`, and an optional `data`
value. The `data` is useful for returning extra data back to the client when an error occurs.
The `data` object is added to the `errors` in the GraphQL final response.

The following example shows how to use it in the `Post.relatedPosts: [Post]` resolver
response handler.

```
// the Post.relatedPosts response handler
export function response(ctx) {
    util.error("Failed to fetch relatedPosts", "LambdaFailure", ctx.result)
    return ctx.result;
}
```

This yields a GraphQL response similar to the following:

```
{
    "data": {
        "allPosts": [
            {
                "id": "2",
                "title": "Second book",
                "relatedPosts": null
            },
            ...
        ]
    },
    "errors": [
        {
            "path": [
                "allPosts",
                0,
                "relatedPosts"
            ],
            "errorType": "LambdaFailure",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ],
            "message": "Failed to fetch relatedPosts",
            "data": [
                {
                  "id": "2",
                  "title": "Second book"
                },
                {
                  "id": "1",
                  "title": "First book"
                }
            ]
        }
    ]
}
```

Where `allPosts[0].relatedPosts` is _null_ because of the error and the `errorMessage`,
`errorType`, and `data` are present in the
`data.errors[0]` object.

### From the Lambda function

AWS AppSync also understands errors that the Lambda function throws. The Lambda programming model lets you
raise _handled_ errors. If the Lambda function throws an error,
AWS AppSync fails to resolve the current field. Only the error message returned from Lambda is set in the
response. Currently, you can't pass any extraneous data back to the client by raising an error from the
Lambda function.

###### Note

If your Lambda function raises an _unhandled_ error,
AWS AppSync uses the error message that Lambda set.

The following Lambda function raises an error:

```
export const handler = async (event) => {
  console.log('Received event {}', JSON.stringify(event, 3))
  throw new Error('I always fail.')
}
```

The error is received in your response handler. You can send it back in the GraphQL response by
appending the error to the response with `util.appendError`. To do so, change your AWS AppSync
function response handler to this:

```
// the lambdaInvoke response handler
export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    util.appendError(error.message, error.type, result);
  }
  return result;
}
```

This returns a GraphQL response similar to the following:

```
{
  "data": {
    "allPosts": null
  },
  "errors": [
    {
      "path": [
        "allPosts"
      ],
      "data": null,
      "errorType": "Lambda:Unhandled",
      "errorInfo": null,
      "locations": [
        {
          "line": 2,
          "column": 3,
          "sourceName": null
        }
      ],
      "message": "I fail. always"
    }
  ]
}
```

## Advanced use case: Batching

The Lambda function in this example has a `relatedPosts` field that returns
a list of related posts for a given post. In the example queries, the
`allPosts` field invocation from the Lambda function returns five posts.
Because we specified that we also want to resolve `relatedPosts` for each
returned post, the `relatedPosts` field operation is invoked five
times.

```
query {
    allPosts {   // 1 Lambda invocation - yields 5 Posts
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {   // 5 Lambda invocations - each yields 5 posts
            id
            title
        }
    }
}
```

While this might not sound substantial in this specific example, this compounded
over-fetching can quickly undermine the application.

If you were to fetch `relatedPosts` again on the returned related
`Posts` in the same query, the number of invocations would increase
dramatically.

```
query {
    allPosts {   // 1 Lambda invocation - yields 5 Posts
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {   // 5 Lambda invocations - each yield 5 posts = 5 x 5 Posts
            id
            title
            relatedPosts {  // 5 x 5 Lambda invocations - each yield 5 posts = 25 x 5 Posts
                id
                title
                author
            }
        }
    }
}
```

In this relatively simple query, AWS AppSync would invoke the Lambda function 1 + 5 + 25
= 31 times.

This is a fairly common challenge and is often called the N+1 problem (in this case, N
= 5), and it can incur increased latency and cost to the application.

One approach to solving this issue is to batch similar field resolver requests
together. In this example, instead of having the Lambda function resolve a list of
related posts for a single given post, it could instead resolve a list of related posts
for a given batch of posts.

To demonstrate this, let's update the resolver for `relatedPosts` to handle batching.

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const {source, args} = ctx
  return {
    operation: ctx.info.fieldName === 'relatedPosts' ? 'BatchInvoke' : 'Invoke',
    payload: { field: ctx.info.fieldName, arguments: args, source },
  };
}

export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    util.appendError(error.message, error.type, result);
  }
  return result;
}
```

The code now changes the operation from `Invoke` to `BatchInvoke` when the
`fieldName` being resolved is `relatedPosts`. Now, enable batching on the function
in the **Configure Batching** section. Set the maximum batching size set to
`5`. Choose **Save**.

With this change, when resolving `relatedPosts`, the Lambda function receives the following as
input:

```
[
    {
        "field": "relatedPosts",
        "source": {
            "id": 1
        }
    },
    {
        "field": "relatedPosts",
        "source": {
            "id": 2
        }
    },
    ...
]
```

When `BatchInvoke` is specified in the request, the Lambda function receives a list of requests
and returns a list of results.

Specifically, the list of results must match the size and order of the request payload
entries so that AWS AppSync can match the results accordingly.

In this batching example, the Lambda function returns a batch of results as
follows:

```
[
    [{"id":"2","title":"Second book"}, {"id":"3","title":"Third book"}],   // relatedPosts for id=1
    [{"id":"3","title":"Third book"}]                                     // relatedPosts for id=2
]
```

You can update your Lambda code to handle batching for `relatedPosts`:

```
export const handler = async (event) => {
  console.log('Received event {}', JSON.stringify(event, 3))
  //throw new Error('I fail. always')

  const posts = {
    1: { id: '1', title: 'First book', author: 'Author1', url: 'https://amazon.com/', content: 'SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1', ups: '100', downs: '10', },
    2: { id: '2', title: 'Second book', author: 'Author2', url: 'https://amazon.com', content: 'SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT', ups: '100', downs: '10', },
    3: { id: '3', title: 'Third book', author: 'Author3', url: null, content: null, ups: null, downs: null },
    4: { id: '4', title: 'Fourth book', author: 'Author4', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4', ups: '1000', downs: '0', },
    5: { id: '5', title: 'Fifth book', author: 'Author5', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT', ups: '50', downs: '0', },
  }

  const relatedPosts = {
    1: [posts['4']],
    2: [posts['3'], posts['5']],
    3: [posts['2'], posts['1']],
    4: [posts['2'], posts['1']],
    5: [],
  }

  if (!event.field && event.length){
    console.log(`Got a BatchInvoke Request. The payload has ${event.length} items to resolve.`);
    return event.map(e => relatedPosts[e.source.id])
  }

  console.log('Got an Invoke Request.')
  let result
  switch (event.field) {
    case 'getPost':
      return posts[event.arguments.id]
    case 'allPosts':
      return Object.values(posts)
    case 'addPost':
      // return the arguments back
      return event.arguments
    case 'addPostErrorWithData':
      result = posts[event.arguments.id]
      // attached additional error information to the post
      result.errorMessage = 'Error with the mutation, data has changed'
      result.errorType = 'MUTATION_ERROR'
      return result
    case 'relatedPosts':
      return relatedPosts[event.source.id]
    default:
      throw new Error('Unknown field, unable to resolve ' + event.field)
  }
}
```

### Returning individual errors

The previous examples show that it's possible to return a single error from the Lambda function or
raise an error from your response handler. For batched invocations, raising an error from the Lambda
function flags an entire batch as failed. This might be acceptable for specific scenarios where an
irrecoverable error occurs, such as a failed connection to a data store. However, in cases where some
items in the batch succeed and others fail, it's possible to return both errors and valid data. Because
AWS AppSync requires the batch response to list elements matching the original size of the batch, you must
define a data structure that can differentiate valid data from an error.

For example, if the Lambda function is expected to return a batch of related posts,
you could choose to return a list of `Response` objects where each object
has optional _data_, _errorMessage_, and _errorType_ fields. If the _errorMessage_ field is present, it means that
an error occurred.

The following code shows how you could update the Lambda function:

```
export const handler = async (event) => {
console.log('Received event {}', JSON.stringify(event, 3))
  // throw new Error('I fail. always')
const posts = {
1: { id: '1', title: 'First book', author: 'Author1', url: 'https://amazon.com/', content: 'SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1', ups: '100', downs: '10', },
    2: { id: '2', title: 'Second book', author: 'Author2', url: 'https://amazon.com', content: 'SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT', ups: '100', downs: '10', },
    3: { id: '3', title: 'Third book', author: 'Author3', url: null, content: null, ups: null, downs: null },
    4: { id: '4', title: 'Fourth book', author: 'Author4', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4', ups: '1000', downs: '0', },
    5: { id: '5', title: 'Fifth book', author: 'Author5', url: 'https://www.amazon.com/', content: 'SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT', ups: '50', downs: '0', },
  }

  const relatedPosts = {
1: [posts['4']],
    2: [posts['3'], posts['5']],
    3: [posts['2'], posts['1']],
    4: [posts['2'], posts['1']],
    5: [],
  }

  if (!event.field && event.length){
console.log(`Got a BatchInvoke Request. The payload has ${event.length} items to resolve.`);
    return event.map(e => {
// return an error for post 2
if (e.source.id === '2') {
return { 'data': null, 'errorMessage': 'Error Happened', 'errorType': 'ERROR' }
      }
      return {data: relatedPosts[e.source.id]}
      })
  }

  console.log('Got an Invoke Request.')
  let result
  switch (event.field) {
case 'getPost':
      return posts[event.arguments.id]
    case 'allPosts':
      return Object.values(posts)
    case 'addPost':
      // return the arguments back
return event.arguments
    case 'addPostErrorWithData':
      result = posts[event.arguments.id]
      // attached additional error information to the post
      result.errorMessage = 'Error with the mutation, data has changed'
      result.errorType = 'MUTATION_ERROR'
return result
    case 'relatedPosts':
      return relatedPosts[event.source.id]
    default:
      throw new Error('Unknown field, unable to resolve ' + event.field)
  }
}
```

Update the `relatedPosts` resolver code:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const {source, args} = ctx
  return {
    operation: ctx.info.fieldName === 'relatedPosts' ? 'BatchInvoke' : 'Invoke',
    payload: { field: ctx.info.fieldName, arguments: args, source },
  };
}

export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    util.appendError(error.message, error.type, result);
  } else if (result.errorMessage) {
    util.appendError(result.errorMessage, result.errorType, result.data)
  } else if (ctx.info.fieldName === 'relatedPosts') {
      return result.data
  } else {
      return result
  }
}
```

The response handler now checks for errors returned by the Lambda function on `Invoke`
operations, checks for errors returned for individual items for `BatchInvoke` operations, and
finally checks the `fieldName`. For `relatedPosts`, the function returns
`result.data`. For all other fields, the function just returns `result`. For
example, see the query below:

```
query AllPosts {
  allPosts {
    id
    title
    content
    url
    ups
    downs
    relatedPosts {
      id
    }
    author
  }
}
```

This query returns a GraphQL response similar to the following:

```
{
  "data": {
    "allPosts": [
      {
        "id": "1",
        "relatedPosts": [
          {
            "id": "4"
          }
        ]
      },
      {
        "id": "2",
        "relatedPosts": null
      },
      {
        "id": "3",
        "relatedPosts": [
          {
            "id": "2"
          },
          {
            "id": "1"
          }
        ]
      },
      {
        "id": "4",
        "relatedPosts": [
          {
            "id": "2"
          },
          {
            "id": "1"
          }
        ]
      },
      {
        "id": "5",
        "relatedPosts": []
      }
    ]
  },
  "errors": [
    {
      "path": [
        "allPosts",
        1,
        "relatedPosts"
      ],
      "data": null,
      "errorType": "ERROR",
      "errorInfo": null,
      "locations": [
        {
          "line": 4,
          "column": 5,
          "sourceName": null
        }
      ],
      "message": "Error Happened"
    }
  ]
}
```

### Configuring the maximum batching size

To configure the maximum batching size on a resolver, use the following command in
the AWS Command Line Interface (AWS CLI):

```
$ aws appsync create-resolver --api-id <api-id> --type-name Query --field-name relatedPosts \
 --code "<code-goes-here>" \
 --runtime name=APPSYNC_JS,runtimeVersion=1.0.0 \
 --data-source-name "<lambda-datasource>" \
 --max-batch-size X
```

###### Note

When providing a request mapping template, you must use the
`BatchInvoke` operation to use batching.
