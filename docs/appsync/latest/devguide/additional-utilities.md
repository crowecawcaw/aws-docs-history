# Bundling, TypeScript, and source maps for the `APPSYNC_JS` runtime

TypeScript enhances AWS AppSync development by providing type safety and early error
detection. You can write TypeScript code locally and transpile it to JavaScript before
using it with the `APPSYNC_JS` runtime. The process starts with installing
TypeScript and configuring tsconfig.json for the `APPSYNC_JS` environment. You
can then use bundling tools like esbuild to compile and bundle the code. The Amplify CLI
will generate types from the GraphQL schema, allowing you to use these types in resolver
code.

You can leverage custom and external libraries in your resolver and function code, as
long as they comply with `APPSYNC_JS` requirements. Bundling tools combine code
into a single file for use in AWS AppSync. Source maps can be included to aid debugging.

## Leveraging libraries and bundling your code

In your resolver and function code, you can leverage both custom and external libraries so long as they
comply with the `APPSYNC_JS` requirements. This makes it possible to reuse existing code in your
application. To make use of libraries that are defined by multiple files, you must use a bundling tool, such
as [esbuild](https://esbuild.github.io/ "https://esbuild.github.io/"), to combine your code in a single file that can
then be saved to your AWS AppSync resolver or function.

When bundling your code, keep the following in mind:

- `APPSYNC_JS` only supports ECMAScript modules (ESM).
- `@aws-appsync/*` modules are integrated into `APPSYNC_JS` and should not be
  bundled with your code.
- The `APPSYNC_JS` runtime environment is similar to NodeJS in that code does not run in a
  browser environment.
- You can include an optional source map. However, do not include the source content.

To learn more about source maps, see [Using source maps](#source-maps "#source-maps").

For example, to bundle your resolver code located at `src/appsync/getPost.resolver.js`, you
can use the following esbuild CLI command:

```
$ esbuild --bundle \
--sourcemap=inline \
--sources-content=false \
--target=esnext \
--platform=node \
--format=esm \
--external:@aws-appsync/utils \
--outdir=out/appsync \
 src/appsync/getPost.resolver.js
```

## Building your code and working with TypeScript

[TypeScript](https://www.typescriptlang.org/ "https://www.typescriptlang.org/") is a programming language developed by
Microsoft that offers all of JavaScript’s features along with the TypeScript typing system. You can use
TypeScript to write type-safe code and catch errors and bugs at build time before saving your code to
AWS AppSync. The `@aws-appsync/utils` package is fully typed.

The `APPSYNC_JS` runtime doesn't support TypeScript directly. You must first transpile your
TypeScript code to JavaScript code that the `APPSYNC_JS` runtime supports before saving your code
to AWS AppSync. You can use TypeScript to write your code in your local integrated development environment (IDE),
but note that you cannot create TypeScript code in the AWS AppSync console.

To get started, make sure you have [TypeScript](https://www.typescriptlang.org/download "https://www.typescriptlang.org/download") installed in your project. Then, configure your TypeScript transcompilation settings
to work with the `APPSYNC_JS` runtime using [TSConfig](https://www.typescriptlang.org/tsconfig "https://www.typescriptlang.org/tsconfig"). Here’s an example of a basic `tsconfig.json` file that you can use:

```
// tsconfig.json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
   "noEmit": true,
   "moduleResolution": "node",
  }
}
```

You can then use a bundling tool like esbuild to compile and bundle your code. For example, given a
project with your AWS AppSync code located at `src/appsync`, you can use the following command to
compile and bundle your code:

```
$ esbuild --bundle \
--sourcemap=inline \
--sources-content=false \
--target=esnext \
--platform=node \
--format=esm \
--external:@aws-appsync/utils \
--outdir=out/appsync \
 src/appsync/**/*.ts
```

### Using Amplify codegen

You can use the [Amplify CLI](https://docs.amplify.aws/cli/ "https://docs.amplify.aws/cli/") to generate the types
for your schema. From the directory where your `schema.graphql` file is located, run the
following command and review the prompts to configure your codegen:

```
$  npx @aws-amplify/cli codegen add
```

To regenerate your codegen under certain circumstances (e.g., when your schema is updated), run the
following command:

```
$ npx @aws-amplify/cli codegen
```

You can then use the generated types in your resolver code. For example, given the following
schema:

```
type Todo {
  id: ID!
  title: String!
  description: String
}

type Mutation {
  createTodo(title: String!, description: String): Todo
}

type Query {
  listTodos: Todo
}
```

You could use the generated types in the following example AWS AppSync function:

```
import { Context, util } from '@aws-appsync/utils'
import * as ddb from '@aws-appsync/utils/dynamodb'
import { CreateTodoMutationVariables, Todo } from './API' // codegen

export function request(ctx: Context<CreateTodoMutationVariables>) {
	ctx.args.description = ctx.args.description ?? 'created on ' + util.time.nowISO8601()
	return ddb.put<Todo>({ key: { id: util.autoId() }, item: ctx.args })
}

export function response(ctx) {
	return ctx.result as Todo
}
```

### Using generics in TypeScript

You can use generics with several of the provided types. For example, the snippet below is a
`Todo` type:

```
export type Todo = {
  __typename: "Todo",
  id: string,
  title: string,
  description?: string | null,
};
```

You can write a resolver for a subscription that makes use of `Todo`. In your IDE, type
definitions and auto-complete hints will guide you into properly using the
`toSubscriptionFilter` transform utility:

```
import { util, Context, extensions } from '@aws-appsync/utils'
import { Todo } from './API'

export function request(ctx: Context) {
  return {}
}

export function response(ctx: Context) {
  const filter = util.transform.toSubscriptionFilter<Todo>({
    title: { beginsWith: 'hello' },
    description: { contains: 'created' },
  })
  extensions.setSubscriptionFilter(filter)
  return null
}
```

## Linting your bundles

You can automatically lint your bundles by importing the `esbuild-plugin-eslint` plugin. You
can then enable it by providing a `plugins` value that enables eslint capabilities. Below is a
snippet that uses the esbuild JavaScript API in a file called `build.mjs`:

```
/* eslint-disable */
import { build } from 'esbuild'
import eslint from 'esbuild-plugin-eslint'
import glob from 'glob'
const files = await glob('src/**/*.ts')

await build({
  format: 'esm',
  target: 'esnext',
  platform: 'node',
  external: ['@aws-appsync/utils'],
  outdir: 'dist/',
  entryPoints: files,
  bundle: true,
  plugins: [eslint({ useEslintrc: true })],
})
```

## Using source maps

You can provide an inline source map (`sourcemap`) with your JavaScript code. Source maps are
useful for when you bundle JavaScript or TypeScript code and want to see references to your input source
files in your logs and runtime JavaScript error messages.

Your `sourcemap` must appear at the end of your code. It is defined by a single comment line
that follows the following format:

```
//# sourceMappingURL=data:application/json;base64,<base64 encoded string>
```

Here's an example:

```
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsibGliLmpzIiwgImNvZGUuanMiXSwKICAibWFwcGluZ3MiOiAiO0FBQU8sU0FBUyxRQUFRO0FBQ3RCLFNBQU87QUFDVDs7O0FDRE8sU0FBUyxRQUFRLEtBQUs7QUFDM0IsU0FBTyxNQUFNO0FBQ2Y7IiwKICAibmFtZXMiOiBbXQp9Cg==
```

Source maps can be created with esbuild. The example below shows you how to use the esbuild JavaScript
API to include an inline source map when code is built and bundled:

```
/* eslint-disable */
import { build } from 'esbuild'
import eslint from 'esbuild-plugin-eslint'
import glob from 'glob'
const files = await glob('src/**/*.ts')

await build({
  sourcemap: 'inline',
  sourcesContent: false,

  format: 'esm',
  target: 'esnext',
  platform: 'node',
  external: ['@aws-appsync/utils'],
  outdir: 'dist/',
  entryPoints: files,
  bundle: true,
  plugins: [eslint({ useEslintrc: true })],
})
```

In particular, the `sourcemap` and `sourcesContent` options specify that a source
map should be added in line at the end of each build but should not include the source content. As a
convention, we recommend not including source content in your `sourcemap`. You can disable this
in esbuild by setting `sources-content` to `false`.

To illustrate how source maps work, review the following example in which a resolver code references
helper functions from a helper library. The code contains log statements in the resolver code and in the
helper library:

**./src/default.resolver.ts** (your resolver)

```
import { Context } from '@aws-appsync/utils'
import { hello, logit } from './helper'

export function request(ctx: Context) {
  console.log('start >')
  logit('hello world', 42, true)
  console.log('< end')
  return 'test'
}

export function response(ctx: Context): boolean {
  hello()
  return ctx.prev.result
}
```

**.src/helper.ts** (a helper file)

```
export const logit = (...rest: any[]) => {
  // a special logger
  console.log('[logger]', ...rest.map((r) => `<${r}>`))
}

export const hello = () => {
  // This just returns a simple sentence, but it could do more.
  console.log('i just say hello..')
}
```

When you build and bundle the resolver file, your resolver code will include an inline source map. When
your resolver runs, the following entries appear in the CloudWatch logs:

![CloudWatch log entries showing resolver code execution with inline source map information.](images/cloudwatch-sourcemap.jpeg)

Looking at the entries in the CloudWatch log, you'll notice that the functionality of the two files have been
bundled together and are running concurrently. The original file name of each file is also clearly reflected
in the logs.
