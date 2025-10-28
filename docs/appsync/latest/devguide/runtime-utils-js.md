# Runtime utilities

The `runtime` library provides utilities to control or modify the runtime
properties of your resolvers and functions.

## Runtime utils list

**`runtime.earlyReturn(obj?: unknown, returnOptions?:
 {skipTo: 'END' | 'NEXT'}): never`**

Invoking this function will halt the execution of the current
handler, AWS AppSync function or resolver (Unit or Pipeline Resolver) depending on
the current context. The specified object is returned as the result.

- When called in an AWS AppSync function request handler, the data
  source and response handler are skipped, and the next function
  request handler (or the pipeline resolver response handler if this
  was the last AWS AppSync function) is called.
- When called in an AWS AppSync pipeline resolver request handler, the
  pipeline execution is skipped, and the pipeline resolver response
  handler is called immediately.
- When `returnOptions` is given with `skipTo` set to "END", the pipeline execution is skipped, and the pipeline resolver response handler is called immediately.
- When `returnOptions` is given with `skipTo` set to "NEXT", the function execution is skipped, and the next pipeline handler is called.

**Example**

```
import { runtime } from '@aws-appsync/utils'

export function request(ctx) {
  runtime.earlyReturn({ hello: 'world' })
  // code below is not executed
  return ctx.args
}

// never called because request returned early
export function response(ctx) {
  return ctx.result
}
```
