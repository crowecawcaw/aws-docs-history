# What is AWS Blocks?

AWS Blocks is a backend toolkit for building full-stack applications on AWS. Each Block is a self-contained backend capability. It bundles your application code, a local development setup, and the infrastructure to run it. Every Block works with every other Block, so any combination produces a functioning backend. Pick the ones you need, combine them, and AWS Blocks automatically defines the infrastructure for you following AWS best practices.

Your entire application runs locally without an AWS account. When you’re ready, deploy the same code to AWS without changing anything.

## Why AWS Blocks

**Start building in seconds**

Run one command to get a working application on your machine. You don’t need an AWS account until you’re ready to deploy.

**End-to-end type safety**

Define your backend once. Your frontend types update on their own. No code generation, no type mismatches. TypeScript carries types from your database to your UI.

**AI agents get it right on first attempt**

Steering files ship in the npm package. They guide AI coding agents to build correct code from the start. No plugins needed.

**No ceiling on what you can build**

Every Block uses production AWS services. When you need more control, drop into CDK and configure resources directly. You’re never stuck in an abstraction.

**Compose with what you already use**

Add AWS features to your existing backend. Adopt one Block at a time. A built-in migration path lets you move at your own pace.

## Blocks

A Block is a module that gives you a complete feature: cloud resources, a runtime API, and a local implementation. Each Block is an npm package. You import it and use it in your backend code.

The following table lists all available Blocks.

### Data and storage

| Block                 | Description                                      | AWS service                 |
| --------------------- | ------------------------------------------------ | --------------------------- |
| `KVStore`             | Key-value storage with conditional writes        | Amazon DynamoDB             |
| `DistributedTable`    | Structured data with indexes and queries         | Amazon DynamoDB             |
| `Database`            | SQL with Kysely query builder (managed Postgres) | Amazon Aurora Serverless v2 |
| `DistributedDatabase` | Serverless SQL with zero idle cost               | Amazon Aurora DSQL          |
| `FileBucket`          | File storage with presigned URLs                 | Amazon S3                   |

### Authentication

| Block         | Description                              | AWS service           |
| ------------- | ---------------------------------------- | --------------------- |
| `AuthBasic`   | Username/password with state machine API | Amazon DynamoDB + JWT |
| `AuthCognito` | Managed auth with MFA, groups, passkeys  | Amazon Cognito        |
| `AuthOIDC`    | OIDC sign-in (Google, GitHub, Okta)      | OAuth redirect flow   |

### Compute and background

| Block      | Description                     | AWS service                     |
| ---------- | ------------------------------- | ------------------------------- |
| `AsyncJob` | Fire-and-forget background work | Amazon SQS + AWS Lambda         |
| `CronJob`  | Scheduled task execution        | Amazon EventBridge + AWS Lambda |

### AI

| Block           | Description                                                  | AWS service                    |
| --------------- | ------------------------------------------------------------ | ------------------------------ |
| `Agent`         | AI agent with tools, HITL approval, conversation persistence | Amazon Bedrock                 |
| `KnowledgeBase` | Semantic document retrieval and RAG                          | Amazon Bedrock Knowledge Bases |

### Communication

| Block         | Description                | AWS service                  |
| ------------- | -------------------------- | ---------------------------- |
| `Realtime`    | WebSocket pub/sub channels | Amazon API Gateway WebSocket |
| `EmailClient` | Transactional email        | Amazon SES                   |

### Configuration

| Block        | Description                      | AWS service                         |
| ------------ | -------------------------------- | ----------------------------------- |
| `AppSetting` | Configuration values and secrets | AWS Systems Manager Parameter Store |

### Observability

| Block       | Description                             | AWS service            |
| ----------- | --------------------------------------- | ---------------------- |
| `Logger`    | Structured logging with correlation IDs | Amazon CloudWatch Logs |
| `Metrics`   | Custom application metrics              | Amazon CloudWatch      |
| `Tracer`    | Distributed request tracing             | AWS X-Ray              |
| `Dashboard` | Auto-generated observability dashboard  | Amazon CloudWatch      |

### Hosting and deployment

| Component | Description                                                                            | AWS service                   |
| --------- | -------------------------------------------------------------------------------------- | ----------------------------- |
| `Hosting` | Frontend deployment with SSR support (CDK layer, import from `@aws-blocks/blocks/cdk`) | Amazon CloudFront + Amazon S3 |

For detailed API references for each Block, see [Blocks reference](building-blocks-reference.md "building-blocks-reference.md").

## How AWS Blocks works

AWS Blocks uses Node.js conditional exports to load different code for each context:

- **Local development**: Blocks use in-memory and filesystem storage. Your app runs on your machine.
- **CDK synthesis**: Blocks produce CDK constructs. AWS Blocks creates a CloudFormation template.
- **AWS Lambda runtime**: Blocks call AWS services through the SDK.

The same `new KVStore(scope, 'todos')` line becomes a local store in development, a DynamoDB table at deploy time, and SDK calls in production. You don’t change any code.

## Supported platforms

AWS Blocks supports web frameworks (Next.js, Nuxt, Astro, React, Vue, Svelte, Angular), native mobile (Swift, Kotlin, Dart/Flutter), and desktop applications. Type safety extends from your backend all the way to your client, regardless of platform.

For the full list of supported frameworks and versions, see [Supported platforms](supported-platforms.md "supported-platforms.md").

## Related services and tools

The following are some of the AWS services and tools that AWS Blocks works with. This is not an exhaustive list.

**AWS Cloud Development Kit (AWS CDK)**

AWS Blocks applications are CDK applications. The AWS CDK is an open-source framework that lets you define cloud infrastructure as code. You can use any CDK construct alongside Blocks, and you can embed AWS Blocks into an existing CDK stack. For more information, see the [AWS CDK Developer Guide](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md").

**AWS Amplify**

AWS Amplify is a set of tools and services for building full-stack applications. AWS Blocks and Amplify are complementary. Amplify provides hosting, CI/CD, and a managed backend experience, while AWS Blocks focuses on type-safe infrastructure-from-code with local-first development. For more information, see the [Amplify documentation](https://docs.amplify.aws/ "https://docs.amplify.aws/").

**AWS Lambda**

AWS Blocks deploys your backend code to AWS Lambda. For more information, see the [AWS Lambda Developer Guide](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md").

**Amazon API Gateway**

AWS Blocks uses API Gateway to expose your backend APIs and WebSocket channels. For more information, see the [API Gateway Developer Guide](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md").

**Amazon DynamoDB**

Several Blocks use DynamoDB for data persistence. For more information, see the [Amazon DynamoDB Developer Guide](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md").

**Amazon Aurora**

The Database and DistributedDatabase Blocks use Aurora for managed PostgreSQL. For more information, see the [Amazon Aurora User Guide](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md").

**Amazon Bedrock**

The Agent and KnowledgeBase Blocks use Amazon Bedrock for AI capabilities. For more information, see the [Amazon Bedrock User Guide](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md").

## Next steps

- [Getting started with AWS Blocks](getting-started.md "getting-started.md"): Set up your environment and build your first application.
- [AWS Blocks concepts](concepts.md "concepts.md"): Learn about Blocks, scopes, and the IFC layer.
- [Blocks reference](building-blocks-reference.md "building-blocks-reference.md"): Browse all available Blocks and their APIs.
