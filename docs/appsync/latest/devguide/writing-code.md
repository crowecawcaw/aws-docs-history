# Example pipeline resolver with Amazon DynamoDB

Suppose you wanted to attach a pipeline resolver on a field named `getPost(id:ID!)` that returns
a `Post` type from an Amazon DynamoDB data source with the following GraphQL query:

```
getPost(id:1){
    id
    title
    content
}
```

First, attach a simple resolver to `Query.getPost` with the code below. This is an example of
simple resolver code. There is no logic defined in the request handler, and the response handler simply returns
the result of the last function.

```
/**
 * Invoked **before** the request handler of the first AppSync function in the pipeline.
 * The resolver `request` handler allows to perform some preparation logic
 * before executing the defined functions in your pipeline.
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function request(ctx) {
  return {}
}

/**
 * Invoked **after** the response handler of the last AppSync function in the pipeline.
 * The resolver `response` handler allows to perform some final evaluation logic
 * from the output of the last function to the expected GraphQL field type.
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function response(ctx) {
  return ctx.prev.result
}
```

Next, define function `GET_ITEM` that retrieves a postitem from your data source:

```
import { util } from '@aws-appsync/utils'
import * as ddb from '@aws-appsync/utils/dynamodb'

/**
 * Request a single item from the attached DynamoDB table datasource
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function request(ctx) {
	const { id } = ctx.args
	return ddb.get({ key: { id } })
}

/**
 * Returns the result
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function response(ctx) {
	const { error, result } = ctx
	if (error) {
		return util.appendError(error.message, error.type, result)
	}
	return ctx.result
}
```

If there is an error during the request, the function’s response handler appends an error that will be
returned to the calling client in the GraphQL response. Add the `GET_ITEM` function to your resolver
functions list. When you execute the query, the `GET_ITEM` function’s request handler uses the utils
provided by AWS AppSync's DynamoDB module to create a `DynamoDBGetItem` request using the `id` as
the key. `ddb.get({ key: { id } })` generates the appropriate `GetItem` operation:

```
{
    "operation" : "GetItem",
    "key" : {
        "id" : { "S" : "1" }
    }
}
```

AWS AppSync uses the request to fetch the data from Amazon DynamoDB. Once the data is returned, it is handled by the
`GET_ITEM` function’s response handler, which checks for errors and then returns the result.

```
{
  "result" : {
    "id": 1,
    "title": "hello world",
    "content": "<long story>"
  }
}
```

Finally, the resolver’s response handler returns the result directly.

## Working with errors

If an error occurs in your function during a request, the error will be made available in your function
response handler in `ctx.error`. You can append the error to your GraphQL response using the
`util.appendError` utility. You can make the error available to other functions in the
pipeline by using the stash. See the example below:

```
/**
 * Returns the result
 * @param ctx the context object holds contextual information about the function invocation.
 */
export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    if (!ctx.stash.errors) ctx.stash.errors = []
    ctx.stash.errors.push(ctx.error)
    return util.appendError(error.message, error.type, result);
  }
  return ctx.result;
}
```
