# AWS AppSync resolver mapping template reference for Lambda

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

You can use AWS AppSync functions and resolvers to invoke Lambda functions located in
your account. You can shape your request payloads and the response from your Lambda functions
before returning them to your clients. You can also use mapping templates to give hints to
AWS AppSync about the nature of the operation to be invoked. This section describes the
different mapping templates for the supported Lambda operations.

## Request mapping template

The Lambda request mapping template handles fields related to your Lambda
function:

```
{
  "version": string,
  "operation": Invoke|BatchInvoke,
  "payload": any type,
  "invocationType": RequestResponse|Event
}
```

This is the JSON schema representation of the Lambda request mapping template when
resolved:

```
{
  "definitions": {},
  "$schema": "https://json-schema.org/draft-06/schema#",
  "$id": "https://aws.amazon.com/appsync/request-mapping-template.json",
  "type": "object",
  "properties": {
    "version": {
      "$id": "/properties/version",
      "type": "string",
      "enum": [
        "2018-05-29"
      ],
      "title": "The Mapping template version.",
      "default": "2018-05-29"
    },
    "operation": {
      "$id": "/properties/operation",
      "type": "string",
      "enum": [
        "Invoke",
        "BatchInvoke"
      ],
      "title": "The Mapping template operation.",
      "description": "What operation to execute.",
      "default": "Invoke"
    },
    "payload": {},
    "invocationType": {
      "$id": "/properties/invocationType",
      "type": "string",
      "enum": [
        "RequestResponse",
        "Event"
      ],
      "title": "The Mapping template invocation type.",
      "description": "What invocation type to execute.",
      "default": "RequestResponse"
    }
  },
  "required": [
    "version",
    "operation"
  ],
  "additionalProperties": false
}
```

Here's an example that uses an `invoke` operation with its payload data
being the `getPost` field from a GraphQL schema along with its arguments from
the context:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
  "payload": {
    "field": "getPost",
    "arguments": $util.toJson($context.arguments)
  }
}
```

The entire mapping document is passed as the input to your Lambda function so that the
previous example now looks like this:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
  "payload": {
    "field": "getPost",
    "arguments": {
      "id": "postId1"
    }
  }
}
```

### Version

Common to all request mapping templates, the `version` defines the
version that the template uses. The `version` is required and is a static
value:

```
"version": "2018-05-29"
```

### Operation

The Lambda data source lets you define two operations in the `operation`
field: `Invoke` and `BatchInvoke`. The `Invoke`
operation lets AWS AppSync know to call your Lambda function for every GraphQL
field resolver. `BatchInvoke` instructs AWS AppSync to batch requests
for the current GraphQL field. The `operation` field is required.

For `Invoke`, the resolved request mapping template matches the input
payload of the Lambda function. Let's modify the example above:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
    "payload": {
      "arguments": $util.toJson($context.arguments)
    }
}
```

This is resolved and passed to the Lambda function, which could look something like
this:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
    "payload": {
      "arguments": {
        "id": "postId1"
      }
    }
}
```

For `BatchInvoke`, the mapping template is applied to every field
resolver in the batch. For conciseness, AWS AppSync merges all the resolved
mapping template `payload` values into a list under a single object
matching the mapping template. The following example template shows the
merge:

```
{
  "version": "2018-05-29",
  "operation": "BatchInvoke",
  "payload": $util.toJson($context)
}
```

This template is resolved into the following mapping document:

```
{
  "version": "2018-05-29",
  "operation": "BatchInvoke",
  "payload": [
    {...}, // context for batch item 1
    {...}, // context for batch item 2
    {...}  // context for batch item 3
  ]
}
```

Each element of the `payload` list corresponds to a single batch item.
The Lambda function is also expected to return a list-shaped response matching the
order of the items sent in the request:

```
[
  { "data": {...}, "errorMessage": null, "errorType": null }, // result for batch item 1
  { "data": {...}, "errorMessage": null, "errorType": null }, // result for batch item 2
  { "data": {...}, "errorMessage": null, "errorType": null }  // result for batch item 3
]
```

### Payload

The `payload` field is a container used to pass any well-formed JSON to
the Lambda function. If the `operation` field is set to
`BatchInvoke`, AWS AppSync wraps the existing `payload`
values into a list. The `payload` field is optional.

### Invocation type

The Lambda data source allows you to define two invocation types:
`RequestResponse` and `Event`. The invocation types are
synonymous with the invocation types defined in the [Lambda API](../../../lambda/latest/api/API_Invoke.md "../../../lambda/latest/api/API_Invoke.md"). The
`RequestResponse` invocation type lets AWS AppSync call your Lambda
function synchronously to wait for a response. The `Event` invocation
allows you to invoke your Lambda function asynchronously. For more information on how
Lambda handles `Event` invocation type requests, see [Asynchronous
invocation](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md"). The `invocationType` field is optional. If this
field is not included in the request, AWS AppSync will default to the
`RequestResponse` invocation type.

For any `invocationType` field, the resolved request matches the input
payload of the Lambda function. Let's modify the example above:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
  "invocationType": "Event"
  "payload": {
    "arguments": $util.toJson($context.arguments)
  }
}
```

This is resolved and passed to the Lambda function, which could look something like
this:

```
{
  "version": "2018-05-29",
  "operation": "Invoke",
  "invocationType": "Event",
  "payload": {
    "arguments": {
      "id": "postId1"
    }
  }
}
```

When the `BatchInvoke` operation is used in conjunction with the
`Event` invocation type field, AWS AppSync merges the field
resolver in the same way mentioned above, and the request is passed to your Lambda
function as an asynchronous event with the `payload` being a list of
values. We recommend that you disable resolver caching for `Event`
invocation type resolvers because these would not be sent to Lambda if there were a
cache hit.

## Response mapping template

As with other data sources, your Lambda function sends a response to AWS AppSync that
must be converted to a GraphQL type.

The result of the Lambda function is set on the `context` object that is
available via the Velocity Template Language (VTL) `$context.result`
property.

If the shape of your Lambda function response exactly matches the shape of the GraphQL
type, you can forward the response using the following response mapping template:

```
$util.toJson($context.result)
```

There are no required fields or shape restrictions that apply to the response mapping
template. However, because GraphQL is strongly typed, the resolved mapping template must
match the expected GraphQL type.

## Lambda function batched response

If the `operation` field is set to `BatchInvoke`, AWS AppSync
expects a list of items back from the Lambda function. In order for AWS AppSync to map
each result back to the original request item, the response list must match in size and
order. It's valid to have `null` items in the response list;
`$ctx.result` is set to _null_ accordingly.

## Direct Lambda Resolvers

If you wish to circumvent the use of mapping templates entirely, AWS AppSync can
provide a default payload to your Lambda function and a default Lambda function response
to a GraphQL type. You can choose to provide a request template, a response template, or
neither, and AWS AppSync handles it accordingly.

### Direct Lambda request mapping template

When the request mapping template is not provided, AWS AppSync will send the
`Context` object directly to your Lambda function as an
`Invoke` operation. For more information about the structure of the
`Context` object, see [AWS AppSync resolver mapping template context reference](resolver-context-reference.md "resolver-context-reference.md").

### Direct Lambda response mapping template

When the response mapping template is not provided, AWS AppSync does one of two
things upon receiving your Lambda function's response. If you did not provide a
request mapping template or if you provided a request mapping template with the
version `2018-05-29`, the response will be equivalent to the following
response mapping template:

```
#if($ctx.error)
     $util.error($ctx.error.message, $ctx.error.type, $ctx.result)
 #end
 $util.toJson($ctx.result)
```

If you provided a template with the version `2017-02-28`, the response
logic functions equivalently to the following response mapping template:

```
$util.toJson($ctx.result)
```

Superficially, the mapping template bypass operates similarly to using certain
mapping templates as shown in the preceding examples. However, behind the scenes,
the evaluation of the mapping templates is circumvented entirely. Because the
template evaluation step is bypassed, applications might experience less overhead
and latency during the response in some scenarios compared to a Lambda function with
a response mapping template that needs to be evaluated.

### Custom error handling in Direct Lambda Resolver responses

You can customize error responses from Lambda functions that Direct Lambda Resolvers
invoke by raising a custom exception. The following example demonstrates how to
create a custom exception using JavaScript:

```
class CustomException extends Error {
  constructor(message) {
    super(message);
    this.name = "CustomException";
  }
}

throw new CustomException("Custom message");
```

When exceptions are raised, the `errorType` and
`errorMessage` are the `name` and `message`,
respectively, of the custom error that is thrown.

If `errorType` is `UnauthorizedException`, AWS AppSync
returns the default message (`"You are not authorized to make this
 call."`) instead of a custom message.

The following snippet is an example GraphQL response that demonstrates a custom
`errorType`:

```
{
  "data": {
    "query": null
  },
  "errors": [
    {
      "path": [
        "query"
      ],
      "data": null,
      "errorType": "CustomException",
      "errorInfo": null,
      "locations": [
        {
          "line": 5,
          "column": 10,
          "sourceName": null
        }
      ],
      "message": "Custom Message"
    }
  ]
}
```

### Direct Lambda Resolvers: Batching enabled

You can enable batching for your Direct Lambda Resolver by configuring the
`maxBatchSize` on your resolver. When `maxBatchSize` is
set to a value greater than `0` for a Direct Lambda resolver,
AWS AppSync sends requests in batches to your Lambda function in sizes up to
`maxBatchSize`.

Setting `maxBatchSize` to `0` on a Direct Lambda resolver
turns off batching.

For more information on how batching with Lambda resolvers works, see [Advanced use case: Batching](tutorial-lambda-resolvers.md#advanced-use-case-batching "tutorial-lambda-resolvers.md#advanced-use-case-batching").

#### Request mapping template

When batching is enabled and the request mapping template is not provided,
AWS AppSync sends a list of `Context` objects as a
`BatchInvoke` operation directly to your Lambda function.

#### Response mapping template

When batching is enabled and the response mapping template is not provided,
the response logic is equivalent to the following response mapping
template:

```
#if( $context.result && $context.result.errorMessage )
      $utils.error($context.result.errorMessage, $context.result.errorType,
      $context.result.data)
#else
      $utils.toJson($context.result.data)
#end
```

The Lambda function must return a list of results in the same order as the list
of `Context` objects that were sent. You can return individual
errors by providing an `errorMessage` and `errorType` for
a specific result. Each result in the list has the following format:

```
{
   "data" : { ... }, // your data
   "errorMessage" : { ... }, // optional, if included an error entry is added to the "errors" object in the AppSync response
   "errorType" : { ... } // optional, the error type
}
```

###### Note

Other fields in the result object are currently ignored.

#### Handling errors from Lambda

You can return an error for all results by throwing an exception or an error
in your Lambda function. If the payload request or response size for your batch
request is too large, Lambda returns an error. In that case, you should consider
reducing your `maxBatchSize` or reducing the size of the response
payload.

For information on handling individual errors, see [Returning individual errors](tutorial-lambda-resolvers.md#returning-individual-errors "tutorial-lambda-resolvers.md#returning-individual-errors").

#### Sample Lambda functions

Using the schema below, you can create a Direct Lambda Resolver for the
`Post.relatedPosts` field resolver and enable batching by setting
`maxBatchSize` above `0`:

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

In the following query, the Lambda function will be called with batches of
requests to resolve `relatedPosts`:

```
query getAllPosts {
  allPosts {
    id
    relatedPosts {
      id
    }
  }
}
```

A simple implementation of a Lambda function is provided below:

```
const posts = {
  1: {
    id: '1',
    title: 'First book',
    author: 'Author1',
    url: 'https://amazon.com/',
    content:
      'SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1',
    ups: '100',
    downs: '10',
  },
  2: {
    id: '2',
    title: 'Second book',
    author: 'Author2',
    url: 'https://amazon.com',
    content: 'SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT',
    ups: '100',
    downs: '10',
  },
  3: { id: '3', title: 'Third book', author: 'Author3', url: null, content: null, ups: null, downs: null },
  4: {
    id: '4',
    title: 'Fourth book',
    author: 'Author4',
    url: 'https://www.amazon.com/',
    content:
      'SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4',
    ups: '1000',
    downs: '0',
  },
  5: {
    id: '5',
    title: 'Fifth book',
    author: 'Author5',
    url: 'https://www.amazon.com/',
    content: 'SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT',
    ups: '50',
    downs: '0',
  },
}

const relatedPosts = {
  1: [posts['4']],
  2: [posts['3'], posts['5']],
  3: [posts['2'], posts['1']],
  4: [posts['2'], posts['1']],
  5: [],
}
exports.handler = async (event) => {
  console.log('event ->', event)
  // retrieve the ID of each post
  const ids = event.map((context) => context.source.id)
  // fetch the related posts for each post id
  const related = ids.map((id) => relatedPosts[id])

  // return the related posts; or an error if none were found
  return related.map((r) => {
    if (r.length > 0) {
      return { data: r }
    } else {
      return { data: null, errorMessage: 'Not found', errorType: 'ERROR' }
    }
  })
}
```
