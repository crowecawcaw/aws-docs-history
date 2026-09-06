

# Blocks reference
<a name="building-blocks-reference"></a>

 AWS Blocks ships with built-in Blocks covering authentication, data storage, real-time messaging, AI, observability, and more. Each Block provides a typed API, automatic resource provisioning, and a local implementation for offline development.

For more information about source code and advanced configuration, see [AWS Blocks on GitHub](https://github.com/aws-devtools-labs/aws-blocks).

## Authentication
<a name="authentication"></a>

Blocks for user identity and session management.
+  **AuthBasic**: Username/password with JWT sessions. Use for prototypes and internal tools.
+  **AuthOIDC**: OIDC sign-in with Google, GitHub, Okta, or any compliant provider. Use for social login.
+  **AuthCognito**: Production-grade auth with MFA, social sign-in, SAML, and passkeys. Use for production applications.

For more information, see [Authentication](bb-authentication.md).

## Data storage
<a name="data-storage"></a>

Blocks for persisting and retrieving data.
+  **KVStore**: Simple key-value storage backed by DynamoDB. Use for caches, session stores, and feature flags.
+  **DistributedTable**: Structured data with schema validation, secondary indexes, and rich queries. Use for entities with multiple access patterns.
+  **Database**: Full PostgreSQL with Kysely query builder, migrations, transactions, and Row Level Security. Use for relational data.
+  **DistributedDatabase**: Serverless SQL with scale-to-zero and multi-region writes. Use for globally distributed relational data.
+  **FileBucket**: File storage for uploads and downloads with presigned URLs. Use for user-generated content.

For more information, see [Data storage](bb-data-storage.md).

## Real-time and async
<a name="real-time-and-async"></a>

Blocks for real-time communication and background processing.
+  **Realtime**: Typed WebSocket pub/sub channels. Use for live updates, chat, and notifications.
+  **AsyncJob**: Fire-and-forget background work via SQS and Lambda. Use for tasks that don’t need immediate results.
+  **CronJob**: Scheduled task execution via EventBridge. Use for periodic maintenance and batch processing.

For more information, see [Real-time and async](bb-realtime-async.md).

## AI
<a name="ai"></a>

Blocks for AI-powered features.
+  **Agent**: AI agent with streaming, tool calling, HITL approval, and conversation persistence. Locally, uses a canned keyword-based provider (no real model needed). On AWS, connects to Amazon Bedrock.
+  **KnowledgeBase**: Semantic document retrieval via Amazon Bedrock Knowledge Bases. Use for RAG and contextual search.

For more information, see [AI](bb-ai.md).

## Communication
<a name="communication"></a>

Blocks for sending messages to users.
+  **EmailClient**: Transactional email sending via Amazon SES. Locally, captures emails for testing.

For more information, see [Communication](bb-communication.md).

## Configuration
<a name="configuration"></a>

Blocks for application settings and secrets.
+  **AppSetting**: A single configuration value or secret backed by SSM Parameter Store.

For more information, see [Configuration](bb-configuration.md).

## Observability
<a name="observability"></a>

Blocks for monitoring, logging, and tracing.
+  **Metrics**: Custom application metrics via CloudWatch Embedded Metric Format.
+  **Logger**: Structured JSON logging with levels and contextual metadata.
+  **Tracer**: Distributed tracing via AWS X-Ray.
+  **Dashboard**: Auto-generated observability dashboard from your metrics definitions.

For more information, see [Observability](bb-observability.md).

## Hosting
<a name="hosting"></a>

Frontend deployment (CDK layer only, import from `@aws-blocks/blocks/cdk`).
+  **Hosting**: Frontend deployment with SSR support. Auto-detects framework (Next.js, Nuxt, Astro, SPA).

For more information, see [Hosting](bb-hosting.md).