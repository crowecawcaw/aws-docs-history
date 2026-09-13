

# Local development
<a name="local-development"></a>

 AWS Blocks is local-first. When you run `npm run dev`, your entire application runs on your local machine: backend, frontend, database, authentication, and background jobs. You don’t need an AWS account, AWS credentials, an internet connection, or a running container daemon. Every Block ships with a local implementation that exposes the same typed API as its AWS counterpart, so no emulator or additional tooling is required. The only prerequisite is Node.js version 22 or later.

This page explains how local development works, what each Block maps to locally, and how to use local implementations to test your application.

## How local development works
<a name="local-development-how-it-works"></a>

### Conditional exports
<a name="local-development-conditional-exports"></a>

Every Block is an npm package with several implementations behind a single import. AWS Blocks uses [Node.js conditional exports](https://nodejs.org/api/packages.html#conditional-exports) to route the same `import` statement to the right implementation for the execution context:

```
{
  "exports": {
    ".": {
      "browser": "./dist/index.browser.js",
      "cdk": "./dist/index.cdk.js",
      "aws-runtime": "./dist/index.aws.js",
      "default": "./dist/index.local.js"
    }
  }
}
```


| Context | Export condition | What resolves | 
| --- | --- | --- | 
| Local development |  `default`  | The local implementation. Your code runs in-process on your machine, backed by the filesystem, in-memory state, or an embedded engine. | 
| Deployment (CDK synthesis) |  `cdk`  | CDK constructs that define the Block’s AWS infrastructure. | 
| Production runtime (Lambda) |  `aws-runtime`  | The AWS SDK implementation that calls real AWS services. | 
| Browser |  `browser`  | The client-side code bundled into your frontend. | 

The local implementation is the default resolution, so any Node.js process that imports your backend gets the local implementations automatically. This includes the dev server, your test runner, and any script you run. You don’t turn on a local mode. The local implementation is used whenever no deployment context applies. AWS Blocks applies the `aws-runtime` condition only when it bundles your backend for Lambda, so the AWS SDK is never loaded during local development.

You never configure this yourself. AWS Blocks sets up the build system to select the correct implementation for each context automatically.

### The dev server
<a name="local-development-dev-server"></a>

 `npm run dev` starts a local dev server in watch mode:
+ Your backend runs in-process. There is no separate compute to provision, and code changes reload automatically.
+ Your frontend is served at `http://localhost:3000`.
+  `ApiNamespace` calls route through the local HTTP server with the same request and response semantics as Amazon API Gateway in production, including `BlocksContext`, cookies, and headers.
+  `Realtime` channels connect over a WebSocket served by the dev server.
+  `CronJob` schedules fire while the dev server is running.

### Where local state lives
<a name="local-development-state"></a>

Blocks that persist data write to a `.bb-data/` directory at your project root. Each Block instance gets its own subdirectory, named after the Block’s scope ID.

This has three practical benefits:
+ Data persists across restarts. Stop and restart the dev server, and your users, files, and table rows are still there.
+ You can inspect the state directly. The data is stored as plain files, so you can open your `EmailClient` outbox or a `KVStore’s contents in your editor.
+ You can reset at any time. Delete `.bb-data/`, or a single Block’s subdirectory, to start from a clean state.

Keep `.bb-data/` out of version control. Scaffolded AWS Blocks applications add it to `.gitignore` for you.

## What each Block maps to locally
<a name="local-development-block-mapping"></a>

Every Block exposes the same typed API locally and on AWS. The following table shows what backs that API in each environment.


| Block | Locally | On AWS  | 
| --- | --- | --- | 
|  `AuthBasic`  | Signed JWT sessions in HTTP-only cookies, with user records in a local store | Same JWT sessions, with user records in a DynamoDB table | 
|  `AuthOIDC`  | An in-process stub identity provider, so you can complete full sign-in flows without registering an external provider | Real OIDC redirect flow with your configured provider (Google, GitHub, Okta, or any compliant provider) | 
|  `AuthCognito`  | An in-process simulation of the Cognito user pool. Sign-up, sign-in, MFA, and passkey flows work without any AWS calls | An Amazon Cognito user pool with your configured options | 
|  `KVStore`  | File-backed store in `.bb-data/`  | DynamoDB table | 
|  `DistributedTable`  | File-backed store in `.bb-data/` with the same key and index query semantics | DynamoDB table with Global Secondary Indexes | 
|  `Database`  | PGlite, an embedded WebAssembly PostgreSQL engine, running in-process with data in `.bb-data/`. Supports migrations, transactions, and Row Level Security | Aurora Serverless v2 (PostgreSQL) | 
|  `DistributedDatabase`  | PGlite with a validation layer that enforces Amazon Aurora DSQL compatibility, so unsupported SQL fails locally instead of at deploy time | Aurora DSQL | 
|  `FileBucket`  | A directory in `.bb-data/`, mirroring S3 API behavior including presigned upload/download URLs | S3 bucket | 
|  `Realtime`  | Typed pub/sub over a WebSocket served by the local dev server | API Gateway WebSocket API with DynamoDB connection management | 
|  `AsyncJob`  | In-process queue. Handlers execute inside the dev server, and job status transitions (`queued`, `processing`, `complete`) behave as they do in production | SQS queue with a Lambda consumer | 
|  `CronJob`  | In-process scheduler. `rate` and `cron` schedules fire on Node.js timers while the dev server runs, and each trigger is logged to the terminal | EventBridge rule triggering a Lambda function | 
|  `Agent`  | A canned, keyword-based provider that returns predictable responses without a real model, API key, or cloud cost. You can alternatively point an `openai-api` provider at Ollama or any OpenAI-compatible endpoint | Amazon Bedrock | 
|  `KnowledgeBase`  | A local text index built over your documents in `.bb-data/`, so retrieval works offline | Amazon Bedrock Knowledge Bases with automatic ingestion, chunking, and embedding | 
|  `EmailClient`  | Emails are captured to a local outbox (`.bb-data/…​/emails.json`) instead of being sent, so you can inspect what your application tried to send | Amazon SES | 
|  `AppSetting`  | File-backed values in `.bb-data/`  | SSM Parameter Store (SecureString for secrets) | 
|  `Logger`  | Structured logs to your terminal, using the same code path as production | Same output, captured by CloudWatch Logs with request correlation | 
|  `Metrics`  | EMF-formatted JSON to your terminal, using the same code path as production | Same output, captured as CloudWatch metrics | 
|  `Tracer`  | Traces recorded to files in `.bb-data/` for local inspection |  AWS X-Ray distributed tracing | 
|  `Dashboard`  | Not available locally. The dashboard route responds with a message directing you to deploy, because there is no CloudWatch dashboard to render | CloudWatch dashboard with widgets for your metrics | 

Note two things about this table:
+  `Logger` and `Metrics` run the same code in both environments. Only the destination of the output differs: what you see in your terminal locally is what CloudWatch captures in production.
+ The data Blocks use real database engines locally. `Database` runs actual PostgreSQL through PGlite, and `DistributedDatabase` additionally validates your SQL against Aurora DSQL restrictions, so incompatible SQL fails on your machine instead of during a deployment.

## Testing with local implementations
<a name="local-development-testing"></a>

Local implementations also form the basis for testing. A typical AWS Blocks test setup has three levels: unit tests for your business logic, integration tests against local implementations, and end-to-end tests against a sandbox. The first two levels run entirely on your machine.

### Unit test business logic with Blocks as parameters
<a name="local-development-testing-unit"></a>

Extract business logic from your API handlers into pure functions that accept Block instances as parameters. The functions depend only on the Block’s typed interface, so you can test them with a standard test runner such as Vitest, without starting the dev server:

```
// orders.ts - testable without the full framework
export async function createOrder(store: KVStore, userId: string, input: OrderInput) {
  if (!input.title) throw new Error('Title required');
  const order = { id: crypto.randomUUID(), ...input, userId };
  await store.put(`${userId}:${order.id}`, order);
  return order;
}
```

```
// orders.test.ts
import { it, expect, vi } from 'vitest';
import { createOrder } from './orders.js';

it('creates an order', async () => {
  const testStore = { put: vi.fn(), get: vi.fn() };
  const result = await createOrder(testStore, 'user-1', { title: 'Test' });
  expect(result.title).toBe('Test');
  expect(testStore.put).toHaveBeenCalled();
});
```

For more information about structuring your application this way, see [Testing](best-practices.md#bp-testing) in Best practices.

### Integration test against local implementations
<a name="local-development-testing-fast"></a>

For tests that cover Block behavior itself, run your application with `npm run dev` and test against it. Blocks resolve to their local implementations automatically.
+ Tests run in milliseconds because everything is in-process.
+ Stateful Blocks behave realistically: conditional writes on `KVStore` fail when they should, `Database` enforces your migrations and Row Level Security, and `AsyncJob` moves jobs through its status transitions.
+ Tests run anywhere Node.js runs, including CI, without AWS credentials.

### Control and inspect state through `.bb-data/`
<a name="local-development-testing-state"></a>

Because local state is plain files, your tests can seed and assert on it directly:
+ Reset between tests or runs by deleting `.bb-data/` or one Block’s subdirectory.
+ Assert on side effects that are hard to observe in the cloud. For example, `EmailClient` writes every email to a local outbox file. A test can trigger a password reset and then read the outbox to verify the message content.

### Test against a sandbox
<a name="local-development-testing-sandbox"></a>

Local implementations match the behavior of their AWS counterparts at the API level, but some things can only be verified against real services: IAM permission boundaries, service quotas and throttling, DynamoDB query performance at scale, or real model output from Amazon Bedrock.

For those cases, deploy a [sandbox](concepts.md#concepts-sandbox) with `npm run sandbox` and run the same tests against it. A sandbox is a fast, ephemeral deployment to AWS that each developer gets in isolation. A useful pattern is to parameterize your end-to-end tests by target environment, so the same test suite runs against `localhost` during development and against a sandbox URL before you ship:


| Run against | Use for | 
| --- | --- | 
| Local dev server | Day-to-day development, fast feedback, CI on every commit | 
| Sandbox deployment | IAM and permission verification, performance characteristics, service-specific behavior, real AI model responses | 
| Production deployment | Smoke tests after release | 

Do most of your development and testing against local implementations, and use a sandbox when you need to verify the behavior of the AWS services themselves.

For more information about how Blocks are structured, see [Conditional exports](concepts.md#concepts-conditional-exports). For deploying to AWS, see [Deploy to AWS](deploy-to-aws.md).