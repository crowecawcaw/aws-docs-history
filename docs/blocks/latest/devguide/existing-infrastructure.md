# Integrating with existing infrastructure

AWS Blocks is designed to work with existing AWS infrastructure. Whether you have an existing CDK application, pre-deployed resources, or a mix of both, you can adopt AWS Blocks incrementally without rewriting your infrastructure.

## Choosing a pattern

AWS Blocks provides four patterns for integrating with existing infrastructure. Choose based on your situation:

| Pattern           | Effort | Use when                                                      | Local support |
| ----------------- | ------ | ------------------------------------------------------------- | ------------- |
| CDK in AWS Blocks | Low    | No Block exists for the resource you need                     | ❌ Manual     |
| `fromExisting`    | Lowest | A Block exists and you have a pre-deployed resource           | ✅ Automatic  |
| Custom Block      | Medium | You’re repeating the same resource pattern in multiple places | ✅ Automatic  |
| Vendorize         | Low    | A first-party Block is almost right but needs CDK changes     | ✅ Automatic  |

## Pattern 1: CDK in AWS Blocks

Use raw CDK constructs alongside Blocks. AWS Blocks gives you two shapes for this:

**`BlocksStack`**: A standalone CloudFormation stack containing the AWS Blocks Lambda and API Gateway. Use for new projects or when you want Blocks isolated in its own deployment unit.

**`BlocksBackend`**: A CDK Construct you drop into an existing stack. Use when you already have stacks and want Blocks to live alongside your other resources.

Both expose a `.handler` (the Lambda function) that you can grant permissions to and inject environment variables into.

### Example: BlocksStack with an SQS queue

```
// aws-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { BlocksStack } from '@aws-blocks/blocks/cdk';

const app = new cdk.App();
const stack = await BlocksStack.create(app, 'my-app', {
  backendHandlerPath: './index.handler.ts',
  backendCDKPath: './index.ts',
});

const queue = new sqs.Queue(stack, 'work-queue');
queue.grantSendMessages(stack.handler);
stack.handler.addEnvironment('QUEUE_URL', queue.queueUrl);
```

```
// aws-blocks/index.ts
import { Scope, ApiNamespace } from '@aws-blocks/blocks';
import { SQSClient, SendMessageCommand } from '@aws-sdk/client-sqs';

const scope = new Scope('my-app');
const sqs = new SQSClient({});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async enqueue(payload: Record<string, unknown>) {
    await sqs.send(new SendMessageCommand({
      QueueUrl: process.env.QUEUE_URL!,
      MessageBody: JSON.stringify(payload),
    }));
    return { ok: true };
  },
}));
```

### Example: BlocksBackend inside an existing stack

Use a static factory method because `BlocksBackend.create()` is asynchronous and constructors cannot use `await`:

```
// my-existing-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { BlocksBackend } from '@aws-blocks/blocks/cdk';

export class MyApiStack extends cdk.Stack {
  static async create(scope: cdk.App, id: string, props?: cdk.StackProps) {
    const stack = new MyApiStack(scope, id, props);

    // Your existing resources
    const queue = new sqs.Queue(stack, 'work-queue');

    // Drop Blocks in as a Construct
    const blocks = await BlocksBackend.create(stack, 'BlocksApi', {
      backendHandlerPath: './aws-blocks/index.handler.ts',
      backendCDKPath: './aws-blocks/index.ts',
    });

    queue.grantSendMessages(blocks.handler);
    blocks.handler.addEnvironment('QUEUE_URL', queue.queueUrl);
    return stack;
  }
}
```

### Tradeoffs

- ✅ Full access to any AWS resource with plain CDK and SDK
- ❌ No local implementation. `npm run dev` will call real AWS unless you stub the SDK yourself
- ❌ No type-level guarantee that environment variables exist

If you find yourself repeating this pattern, consider creating a [custom Block](custom-building-blocks.md "custom-building-blocks.md") instead.

## Pattern 2: fromExisting

Some Blocks can wrap a pre-deployed AWS resource. The Block provides its typed API and local implementation, but skips provisioning. You keep ownership of the resource.

Supported Blocks:

| Block              | Factory method                             | Wraps                      |
| ------------------ | ------------------------------------------ | -------------------------- |
| `KVStore`          | `KVStore.fromExisting(tableName)`          | Existing DynamoDB table    |
| `DistributedTable` | `DistributedTable.fromExisting(tableName)` | Existing DynamoDB table    |
| `FileBucket`       | `FileBucket.fromExisting(bucketName)`      | Existing S3 bucket         |
| `Database`         | `Database.fromExisting({ …​ })`            | Existing RDS instance      |
| `AuthCognito`      | `AuthCognito.fromExisting(userPoolId)`     | Existing Cognito User Pool |

### Example

```
// aws-blocks/index.ts
import { Scope, KVStore, ApiNamespace } from '@aws-blocks/blocks';

const scope = new Scope('my-app');

const sessions = new KVStore(scope, 'sessions', {
  table: KVStore.fromExisting('my-legacy-sessions-table'),
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async getSession(token: string) {
    return sessions.get(token);
  },
}));
```

### Tradeoffs

- ✅ Local development still works. `npm run dev` uses in-memory storage, not the real table
- ✅ IAM permissions are granted automatically to the AWS Blocks Lambda
- ✅ Same typed API as a AWS Blocks-managed resource
- ❌ Limited to the Block’s API surface. If you need features the BB doesn’t expose, use Pattern 1
- ❌ Cross-account resources require manual IAM (fall back to Pattern 1)

## Pattern 3: Custom Block

When you’re repeating Pattern 1 for the same resource type, wrap it in a custom Block. This gives you a typed API, a local implementation, and reusability.

See [Creating custom Blocks](custom-building-blocks.md "custom-building-blocks.md") for a complete guide to authoring Blocks.

### When to use

- You have ≥2 callers using the same resource pattern
- You want `npm run dev` to work without AWS for this resource
- You want type-safe call sites instead of raw `process.env` + SDK

## Pattern 4: Vendorize

If a first-party Block is _almost_ right but needs CDK changes you can’t get upstream quickly, you can eject its source into your project:

```
npm run vendorize -- @aws-blocks/bb-kv-store
```

This copies the Block source into your monorepo. You now own it. Modify the CDK, runtime, or local implementation as needed.

### Tradeoffs

- ✅ Full control over the Block implementation
- ✅ Local implementations, types, and API surface all still work
- ❌ You’re responsible for maintenance. Upstream updates require manual re-sync
- ❌ Only use when a custom wrapping BB (Pattern 3) or upstream PR won’t solve the problem
