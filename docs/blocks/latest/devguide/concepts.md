

# AWS Blocks concepts
<a name="concepts"></a>

This topic explains the key concepts you need to understand when building applications with AWS Blocks.

## Blocks
<a name="concepts-building-blocks"></a>

A **Block** is an npm package that bundles everything for a single feature: cloud resources, runtime code, and a local implementation. When you create a Block in your code, AWS Blocks sets up the matching AWS resources, wires permissions, and gives you a local implementation for development.

For example, `KVStore` is a Block for key-value storage. A single instantiation gives you:
+ A DynamoDB table (provisioned automatically during deployment)
+  AWS SDK integration (used at runtime in Lambda)
+ A local store (used during local development)

```
import { KVStore, Scope } from '@aws-blocks/blocks';

const scope = new Scope('my-app');
const cache = new KVStore(scope, 'cache', {});

// Same API works locally and in production
await cache.put('user:123', { name: 'Alice' });
const user = await cache.get('user:123');
```

## Scope
<a name="concepts-scope"></a>

A **Scope** is a namespace container for Blocks. Every Block must be instantiated within a scope. The scope provides identity and grouping. Each Block’s full identifier is derived from its scope and the ID you provide.

```
const scope = new Scope('my-app');
const users = new KVStore(scope, 'users', {});   // Full ID: my-app/users
const sessions = new KVStore(scope, 'sessions', {}); // Full ID: my-app/sessions
```

Scopes ensure that resource names are unique and predictable across your application.

**Warning**  
Renaming a Block ID (the second argument to the constructor) causes the corresponding AWS resource to be deleted and recreated on the next deployment. This results in **permanent data loss** for stateful Blocks such as `KVStore`, `DistributedTable`, `Database`, and `FileBucket`. Always treat Block IDs as immutable once deployed.

## The IFC layer
<a name="concepts-ifc-layer"></a>

The **IFC (Infrastructure from Code) layer** is your backend entry point, the `aws-blocks/index.ts` file. This is where you instantiate Blocks and define your API. AWS Blocks derives your infrastructure directly from this code. You don’t need separate infrastructure-as-code files.

```
// aws-blocks/index.ts - the IFC layer
import { ApiNamespace, Scope, KVStore, AuthBasic } from '@aws-blocks/blocks';

const scope = new Scope('my-app');

// Infrastructure is derived from these instantiations
const auth = new AuthBasic(scope, 'auth');
const todos = new KVStore(scope, 'todos', {});

// API methods are callable from the frontend
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createTodo(title: string) {
    const user = await auth.requireAuth(context);
    await todos.put(`${user.username}:${title}`, { title, done: false });
  },
}));

export { auth };
```

The IFC layer serves three purposes simultaneously:
+  **Local development**: Blocks resolve to local implementations
+  **Deployment**: Blocks resolve to CDK constructs that define your infrastructure
+  **Production runtime**: Blocks resolve to AWS SDK integrations running in Lambda

## Conditional exports
<a name="concepts-conditional-exports"></a>

 AWS Blocks uses **Node.js conditional exports** to route the same `import` statement to different implementations depending on the execution context. This is the mechanism that makes a single codebase work across local development, deployment, and production.

When you write `import { KVStore } from '@aws-blocks/blocks'`, the resolved file depends on context:


| Context | Resolved implementation | What happens | 
| --- | --- | --- | 
| Local development | In-memory and filesystem | Your app runs entirely on localhost | 
| CDK synthesis | CDK construct (DynamoDB table) | Infrastructure is defined for CloudFormation | 
| Lambda runtime |  AWS SDK (DynamoDB client) | Real AWS service calls in production | 
| TypeScript/IDE | Type definitions | Full IntelliSense and type checking | 

You never need to configure conditional exports manually. AWS Blocks sets up the build system to select the correct implementation for each context automatically.

## ApiNamespace
<a name="concepts-api-namespace"></a>

An **ApiNamespace** defines type-safe backend methods that your frontend can call directly. It’s the bridge between your backend logic and your client code.

```
// Backend: define the API
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async greet(name: string) {
    return { message: `Hello, ${name}!` };
  },
}));
```

```
// Frontend: call the API directly
import { api } from 'aws-blocks';

const result = await api.greet('World');
// result.message === 'Hello, World!'
// TypeScript knows the return type
```

There is no code generation, no API client initialization, and no URL configuration. The frontend import is type-safe. If you change the backend method signature, TypeScript reports errors in the frontend immediately.

Locally, `ApiNamespace` routes calls through a local HTTP server. In production, calls go through API Gateway to Lambda.

## BlocksContext
<a name="concepts-context"></a>

The **BlocksContext** is the request/response object provided to `ApiNamespace` handlers. Blocks that need HTTP-level access (such as authentication blocks reading cookies or setting headers) accept `BlocksContext` as a parameter.

```
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async protectedAction() {
    // Auth blocks use context to read headers/cookies
    const user = await auth.requireAuth(context);
    return { username: user.username };
  },
}));
```

You don’t construct `BlocksContext` yourself. It’s provided automatically by the framework for each incoming request.

## The CDK layer
<a name="concepts-cdk-layer"></a>

The **CDK layer** is an optional file (`aws-blocks/index.cdk.ts`) that gives you direct access to CDK constructs. Use it when you need to:
+ Add AWS resources that don’t have a Block (such as SQS queues or SNS topics)
+ Configure custom domains or other environment-specific settings
+ Integrate AWS Blocks into an existing CDK application

```
// aws-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import { BlocksStack } from '@aws-blocks/blocks/cdk';

const app = new cdk.App();
const stack = await BlocksStack.create(app, 'my-stack', {
  backendHandlerPath: './index.handler.ts',
  backendCDKPath: './index.ts',
});

// Add any CDK construct alongside your Blocks
const queue = new sqs.Queue(stack, 'my-queue');
queue.grantSendMessages(stack.handler);
stack.handler.addEnvironment('QUEUE_URL', queue.queueUrl);
```

The CDK layer is optional. If you don’t create one, AWS Blocks generates a default CDK application from your IFC layer automatically.

## Local development
<a name="concepts-local-development"></a>

When you run `npm run dev`, AWS Blocks starts your entire application locally:
+ Blocks use local implementations (in-memory stores, local JWT tokens, embedded databases)
+ The application runs on `http://localhost:3000` with hot reload
+ No AWS account, no internet connection, and no cloud costs required

Local data persists in a `.bb-data/` directory at your project root. Each Block gets its own subdirectory.

## Sandbox deployments
<a name="concepts-sandbox"></a>

A **sandbox** is a fast, ephemeral deployment to AWS for testing against real services. When you run `npm run sandbox`:
+  AWS Blocks deploys your backend to Lambda with hot-swapping (seconds, not minutes)
+ Blocks resolve to real AWS services (DynamoDB, API Gateway, etc.)
+ Each developer gets an isolated sandbox identified by a unique ID
+ Remove it with `npm run sandbox:destroy` 

Sandboxes are useful when you need to test behavior that differs between local implementations and real services, such as DynamoDB query performance or IAM permission boundaries.

## Terminology reference
<a name="concepts-terminology"></a>


| Term | Definition | 
| --- | --- | 
| Block | A self-contained npm package that bundles infrastructure, runtime, and local development code for a single capability. | 
| Scope | A namespace container that provides identity to Blocks. | 
| IFC layer | The backend entry point (`aws-blocks/index.ts`) where Blocks are instantiated and APIs are defined. Infrastructure is derived from this code. | 
| CDK layer | An optional file (`aws-blocks/index.cdk.ts`) for direct CDK access and custom infrastructure. | 
| ApiNamespace | A Block that defines type-safe RPC methods callable from the frontend. | 
| BlocksContext | The request/response context object provided to API handlers. | 
| Conditional exports | Node.js mechanism that routes imports to different files based on execution context. | 
| Sandbox | A fast, ephemeral AWS deployment for testing against real services. | 
| Local implementation | An in-memory or filesystem-based version of a Block that runs without AWS. | 