# AWS AppSync JavaScript resolver function reference for Lambda

You can use AWS AppSync functions and resolvers to invoke Lambda functions located in
your account. You can shape your request payloads and the response from your Lambda functions
before returning them to your clients. You can also specify the type of operation to perform
in your request object. This section describes the requests for the supported Lambda
operations.

## Request object

The Lambda request object handles fields related to your Lambda function:

```
export type LambdaRequest = {
  operation: 'Invoke' | 'BatchInvoke';
  invocationType?: 'RequestResponse' | 'Event';
  payload: unknown;
};
```

Here's an example that uses an `invoke` operation with its payload data
being the `getPost` field from a GraphQL schema along with its arguments from
the context:

```
export function request(ctx) {
  return {
    operation: 'Invoke',
    payload: { field: 'getPost', arguments: ctx.args },
  };
}
```

The entire mapping document is passed as the input to your Lambda function so that the
previous example now looks like this:

```
{
  "operation": "Invoke",
  "payload": {
    "field": "getPost",
    "arguments": {
      "input": {
        "id": "postId1",
      }
    }
  }
}
```

### Operation

The Lambda data source lets you define two operations in the `operation`
field: `Invoke` and `BatchInvoke`. The `Invoke`
operation lets AWS AppSync know to call your Lambda function for every GraphQL
field resolver. `BatchInvoke` instructs AWS AppSync to batch requests
for the current GraphQL field. The `operation` field is required.

For `Invoke`, the resolved request matches the input payload of the
Lambda function. Let's modify the example above:

```
export function request(ctx) {
  return {
    operation: 'Invoke',
    payload: { field: 'getPost', arguments: ctx.args },
  };
}
```

This is resolved and passed to the Lambda function, which could look something like
this:

```
{
  "operation": "Invoke",
  "payload": {
    "arguments": {
      "id": "postId1"
    }
  }
}
```

For `BatchInvoke`, the request is applied to every field resolver in
the batch. For conciseness, AWS AppSync merges all the request
`payload` values into a list under a single object matching the
request object. The following example request handler shows the merge:

```
export function request(ctx) {
  return {
    operation: 'Invoke',
    payload: ctx,
  };
}
```

This request is evaluated and resolved into the following mapping document:

```
{
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

The `payload` field is a container used to pass any data to the Lambda
function. If the `operation` field is set to `BatchInvoke`,
AWS AppSync wraps the existing `payload` values into a list. The
`payload` field is optional.

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
export function request(ctx) {
  return {
    operation: 'Invoke',
    invocationType: 'Event',
    payload: { field: 'getPost', arguments: ctx.args },
  };
}
```

This is resolved and passed to the Lambda function, which could look something like
this:

```
{
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
values. The response from an `Event` invocation type request results in a
`null` value without a response handler:

```
{
  "data": {
    "field": null
  }
}
```

We recommend that you disable resolver caching for `Event` invocation
type resolvers because these would not be sent to Lambda if there were a cache
hit.

## Response object

As with other data sources, your Lambda function sends a response to AWS AppSync that
must be converted to a GraphQL type. The result of the Lambda function is contained in
the `context` result property (`context.result`).

If the shape of your Lambda function response matches the shape of the GraphQL type,
you can forward the response using the following function response handler:

```
export function response(ctx) {
  return ctx.result
}
```

There are no required fields or shape restrictions that apply to the response object.
However, because GraphQL is strongly typed, the resolved response must match the
expected GraphQL type.

## Lambda function batched response

If the `operation` field is set to `BatchInvoke`, AWS AppSync
expects a list of items back from the Lambda function. In order for AWS AppSync to map
each result back to the original request item, the response list must match in size and
order. It's valid to have `null` items in the response list;
`ctx.result` is set to _null_ accordingly.
