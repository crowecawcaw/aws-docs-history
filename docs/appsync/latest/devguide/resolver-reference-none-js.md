# AWS AppSync JavaScript resolver function

reference for `None` data source

The AWS AppSync resolver function request and response with the data source of type
_None_ enables you to shape requests for AWS AppSync local operations.

## Request

The request handler can be simple and enables you to pass as much contextual information as possible via
the `payload` field.

```
type NONERequest = {
  payload: any;
};
```

Here is an example where the field arguments are passed to the payload:

```
export function request(ctx) {
  return {
    payload: context.args
  };
}
```

The value of the `payload` field will be forwarded to the function response handler and is
available in `context.result`.

## Payload

The `payload` field is a container that can be used to pass any data that is then made
available to the function response handler.

The `payload` field is optional.

## Response

Because there is no data source, the value of the `payload` field will be forwarded to the
function response handler and set on the `context.result` property.

If the shape of the `payload` field value exactly matches the shape of the GraphQL type, you
can forward the response using the following response handler:

```
export function response(ctx) {
  return ctx.result;
}
```

There are no required fields or shape restrictions that apply to the return response. However, because
GraphQL is strongly typed, the resolved response must match the expected GraphQL type.
