# AWS AppSync JavaScript resolvers overview

AWS AppSync lets you respond to GraphQL requests by performing operations on your data
sources. For each GraphQL field you wish to run a query, mutation, or subscription on, a
resolver must be attached.

Resolvers are the connectors between GraphQL and a data source. They tell AWS AppSync how to translate an
incoming GraphQL request into instructions for your backend data source and how to translate the response from
that data source back into a GraphQL response. With AWS AppSync, you can write your resolvers using JavaScript
and run them in the AWS AppSync (`APPSYNC_JS`) environment.

AWS AppSync allows you to write unit resolvers or pipeline resolvers composed of multiple AWS AppSync functions in
a pipeline.

## Supported runtime features

The AWS AppSync JavaScript runtime provides a subset of JavaScript libraries, utilities, and features. For
a complete list of features and functionality supported by the `APPSYNC_JS` runtime, see [JavaScript runtime
features for resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md").

## Unit resolvers

A unit resolver is composed of code that defines a request and response handler that are executed against a
data source. The request handler takes a context object as an argument and returns the request payload used to
call your data source. The response handler receives a payload back from the data source with the result of the
executed request. The response handler transforms the payload into a GraphQL response to resolve the GraphQL
field. In the example below, a resolver retrieves an item from an DynamoDB data source:

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
  return ddb.get({ key: { id: ctx.args.id } });
}

export const response = (ctx) => ctx.result;
```

## Anatomy of a JavaScript pipeline resolver

A pipeline resolver is composed of code that defines a request and response handler and a list of functions.
Each function has a **request** and **response**
handler that it executes against a data source. As a pipeline resolver delegates runs to a list of functions,
it is therefore not linked to any data source. Unit resolvers and functions are primitives that execute
operation against data sources.

### Pipeline resolver request handler

The request handler of a pipeline resolver (the before step) allows you to perform some preparation logic
before running the defined functions.

### Functions list

The list of functions a pipeline resolver will run in sequence. The pipeline resolver request handler
evaluation result is made available to the first function as `ctx.prev.result`. Each function
evaluation result is available to the next function as `ctx.prev.result`.

### Pipeline resolver response handler

The response handler of a pipeline resolver allows you to perform some final logic from the output of the
last function to the expected GraphQL field type. The output of the last function in the functions list is
available in the pipeline resolver response handler as `ctx.prev.result` or
`ctx.result`.

### Execution flow

Given a pipeline resolver comprised of two functions, the list below represents the
execution flow when the resolver is invoked:

1. Pipeline resolver request handler
2. Function 1: Function request handler
3. Function 1: Data source invocation
4. Function 1: Function response handler
5. Function 2: Function request handler
6. Function 2: Data source invocation
7. Function 2: Function response handler
8. Pipeline resolver response handler

![GraphQL request flow diagram showing interactions between request, data sources, and response components.](images/appsync-js-resolver-logic.png)

### Useful `APPSYNC_JS` runtime built-in

utilities

The following utilities can help you when you’re working with pipeline resolvers.

#### ctx.stash

The stash is an object that is made available inside each resolver and function request and response
handler. The same stash instance lives through a single resolver run. This means that you can use the
stash to pass arbitrary data across request and response handlers and across functions in a pipeline
resolver. You can test the stash like a regular JavaScript object.

#### ctx.prev.result

The `ctx.prev.result` represents the result of the previous operation that was executed in
the pipeline. If the previous operation was the pipeline resolver request handler, then
`ctx.prev.result` is made available to the first function in the chain. If the previous
operation was the first function, then `ctx.prev.result` represents the output of the first
function and is made available to the second function in the pipeline. If the previous operation was the
last function, then `ctx.prev.result` represents the output of the last function and is made
available to the pipeline resolver response handler.

#### util.error

The `util.error` utility is useful to throw a field error. Using `util.error`
inside a function request or response handler throws a field error immediately, which prevents subsequent
functions from being executed. For more details and other `util.error` signatures, visit
[JavaScript
runtime features for resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md").

#### util.appendError

`util.appendError` is similar to `util.error()`, with the major distinction that
it doesn’t interrupt the evaluation of the handler. Instead, it signals there was an error with the
field, but allows the handler to be evaluated and consequently return data. Using
`util.appendError` inside a function will not disrupt the execution flow of the pipeline.
For more details and other `util.error` signatures, visit the [JavaScript runtime features for
resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md").

#### runtime.earlyReturn

The `runtime.earlyReturn` function allows you to prematurely return
from any request function. Using `runtime.earlyReturn` inside of a
resolver request handler will return from the resolver. Calling it from an AWS AppSync
function request handler will return from the function and will continue the run to
either the next function in the pipeline or the resolver response handler.

### Writing pipeline resolvers

A pipeline resolver also has a request and a response handler surrounding the run of the functions in the
pipeline: its request handler is run before the first function’s request, and its response handler is run after
the last function’s response. The resolver request handler can set up data to be used by functions in the
pipeline. The resolver response handler is responsible for returning data that maps to the GraphQL field output
type. In the example below, a resolver request handler, defines `allowedGroups`; the data returned
should belong to one of these groups. This value can be used by the resolver’s functions to request data. The
resolver’s response handler conducts a final check and filters the result to make sure that only items that
belong to the allowed groups are returned.

```
import { util } from '@aws-appsync/utils';

/**
 * Called before the request function of the first AppSync function in the pipeline.
 *  @param ctx the context object holds contextual information about the function invocation.
 */
export function request(ctx) {
  ctx.stash.allowedGroups = ['admin'];
  ctx.stash.startedAt = util.time.nowISO8601();
  return {};
}
/**
 * Called after the response function of the last AppSync function in the pipeline.
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function response(ctx) {
  const result = [];
  for (const item of ctx.prev.result) {
    if (ctx.stash.allowedGroups.indexOf(item.group) > -1) result.push(item);
  }
  return result;
}
```

#### Writing AWS AppSync functions

AWS AppSync functions enable you to write common logic that you can reuse across multiple resolvers in
your schema. For example, you can have one AWS AppSync function called `QUERY_ITEMS` that is
responsible for querying items from an Amazon DynamoDB data source. For resolvers that you'd like to query items
with, simply add the function to the resolver's pipeline and provide the query index to be used. The logic
doesn't have to be re-implemented.

## Supplemental topics

**Topics**

- [Example pipeline resolver with Amazon DynamoDB](writing-code.md "writing-code.md")
- [Configuring utilities for the `APPSYNC_JS` runtime](utility-resolvers.md "utility-resolvers.md")
- [Bundling, TypeScript, and
  source maps for the `APPSYNC_JS` runtime](additional-utilities.md "additional-utilities.md")
- [Testing your resolver and function handlers](test-resolvers.md "test-resolvers.md")
- [Migrating from VTL to JavaScript](migrating-resolvers.md "migrating-resolvers.md")
- [Choosing between direct data source access and proxying via a Lambda data
  source](choosing-data-source.md "choosing-data-source.md")
