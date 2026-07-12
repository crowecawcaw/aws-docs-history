# Developer Tools

###### Topics

- [What are Aurora MCP servers?](#aurora-faq-what-are-aurora-mcp-servers "#aurora-faq-what-are-aurora-mcp-servers")
- [What are Kiro Powers for Aurora PostgreSQL?](#aurora-faq-what-are-kiro-powers-for-aurora-postgresql "#aurora-faq-what-are-kiro-powers-for-aurora-postgresql")
- [What is the Vercel v0 integration with Aurora?](#aurora-faq-what-is-the-vercel-v0-integration-with-aurora "#aurora-faq-what-is-the-vercel-v0-integration-with-aurora")
- [What are Amazon Aurora zero-ETL integrations?](#aurora-faq-what-are-amazon-aurora-zero-etl-integrations "#aurora-faq-what-are-amazon-aurora-zero-etl-integrations")
- [When should I use Aurora zero-ETL integration with Amazon Redshift?](#aurora-faq-when-should-i-use-aurora-zero-etl-integration-with-amazon-re "#aurora-faq-when-should-i-use-aurora-zero-etl-integration-with-amazon-re")
- [When should I use Aurora zero-ETL integration with Amazon SageMaker?](#aurora-faq-when-should-i-use-aurora-zero-etl-integration-with-amazon-sa "#aurora-faq-when-should-i-use-aurora-zero-etl-integration-with-amazon-sa")
- [How do I get started with Aurora zero-ETL integrations?](#aurora-faq-how-do-i-get-started-with-aurora-zero-etl-integrations "#aurora-faq-how-do-i-get-started-with-aurora-zero-etl-integrations")
- [How are Aurora zero-ETL integrations priced?](#aurora-faq-how-are-aurora-zero-etl-integrations-priced "#aurora-faq-how-are-aurora-zero-etl-integrations-priced")
- [What are Amazon RDS blue/green deployments?](#aurora-faq-what-are-amazon-rds-bluegreen-deployments "#aurora-faq-what-are-amazon-rds-bluegreen-deployments")
- [Do blue/green deployments support Aurora Global Database?](#aurora-faq-do-bluegreen-deployments-support-aurora-global-database "#aurora-faq-do-bluegreen-deployments-support-aurora-global-database")
- [How much do blue/green deployments cost?](#aurora-faq-how-much-do-bluegreen-deployments-cost "#aurora-faq-how-much-do-bluegreen-deployments-cost")
- [What are Trusted Language Extensions (TLE) for PostgreSQL?](#aurora-faq-what-are-trusted-language-extensions-tle-for-postgresql "#aurora-faq-what-are-trusted-language-extensions-tle-for-postgresql")

## What are Aurora MCP servers?

[Aurora MCP servers](https://awslabs.github.io/mcp/servers/postgres-mcp-server "https://awslabs.github.io/mcp/servers/postgres-mcp-server") provide the flexibility and ease to build and deploy from the tools and agents of your choice. A critical component in agentic AI architectures, MCP servers provide the standardized interface needed for agents to interact with developer tools and your Aurora databases.

Aurora integrates directly with the developer tools you already use, including AI-enabled IDEs such as [Kiro](https://kiro.dev/ "https://kiro.dev/") and cloud platforms such as [Vercel](https://vercel.com/marketplace/aws "https://vercel.com/marketplace/aws"). Aurora also works with agentic frameworks such as [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/"), Letta, and LangGraph.

## What are Kiro Powers for Aurora PostgreSQL?

[Kiro](https://kiro.dev/ "https://kiro.dev/") is Amazon's AI-powered development environment that can connect directly to Aurora PostgreSQL databases. Developers can use Kiro Powers — guided, reusable workflows — to scaffold full-stack applications with Aurora PostgreSQL as the backend, or to build agentic AI applications that use Aurora as a vector store for [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/"). Combined with the [Vercel v0 marketplace integration](https://vercel.com/marketplace/aws "https://vercel.com/marketplace/aws"), developers can go from idea to deployed application with Aurora PostgreSQL in minutes.

## What is the Vercel v0 integration with Aurora?

Through the [Vercel Marketplace](https://vercel.com/marketplace/aws "https://vercel.com/marketplace/aws"), developers can access Aurora PostgreSQL Serverless directly using only an email address. New AWS customers receive $100 in free credits applied automatically. v0 by Vercel is an AI-coding assistant that can generate full-stack applications with Aurora PostgreSQL as the database backend, enabling rapid prototyping and deployment without manual database configuration.

## What are Amazon Aurora zero-ETL integrations?

[Aurora zero-ETL integrations](https://aws.amazon.com/rds/aurora/zero-etl/ "https://aws.amazon.com/rds/aurora/zero-etl/") remove the need to build and maintain complex data pipelines. You can consolidate data from multiple Aurora database clusters and run near real-time analytics and ML on operational data. Aurora supports zero-ETL integrations with two targets: [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/") for near real-time analytics on transactional data, and [Amazon SageMaker Lakehouse](https://aws.amazon.com/sagemaker/lakehouse/ "https://aws.amazon.com/sagemaker/lakehouse/") for building an open lakehouse on operational data.

Both integrations are compatible with Aurora serverless. When combined with [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/ "https://aws.amazon.com/redshift/redshift-serverless/"), you can generate near real-time analytics without managing any infrastructure. Get started in the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") by specifying the Aurora source and target. Ongoing processing of data changes is offered at no additional charge. See the [Aurora zero-ETL documentation](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") for supported versions and Region availability.

## When should I use Aurora zero-ETL integration with Amazon Redshift?

Use this integration when you need near real-time access to transactional data for analytics. It allows you to take advantage of Amazon Redshift ML with straightforward SQL commands, materialized views, and data sharing.

## When should I use Aurora zero-ETL integration with Amazon SageMaker?

Use this integration to bring data from your operational databases into your lakehouse in near real-time. With the lakehouse architecture of [SageMaker](https://aws.amazon.com/sagemaker/lakehouse/ "https://aws.amazon.com/sagemaker/lakehouse/"), you can build an open lakehouse on your existing data investments without changing your data architecture, and use your preferred analytics tools including SQL, Apache Spark, BI, and AI/ML tools.

## How do I get started with Aurora zero-ETL integrations?

Use the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") to create the zero-ETL integration by specifying the Aurora source and target. Once created, the Aurora database will be replicated to the target and you can start querying the data once initial seeding is completed. You can also manage and automate the configuration and deployment using [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-integration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-integration.md").

## How are Aurora zero-ETL integrations priced?

Ongoing processing of data changes by zero-ETL integration is offered at no additional charge. You pay for existing resources used to create and process the change data, which may include additional I/O and storage for enhanced binlog, snapshot export costs for initial seeding, additional storage and compute for processing data replication, and cross-AZ data transfer costs. For more information, visit the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

## What are Amazon RDS blue/green deployments?

[Amazon RDS blue/green deployments](../../../AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.md "../../../AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.md") allow you to make safer, simpler, and faster database changes. The blue environment is your current production; the green environment is your staging environment that becomes the new production after switchover. Blue/green deployments are ideal for major or minor version upgrades, operating system updates, schema changes, and parameter changes.

During switchover, writes are blocked on both environments until the green catches up, ensuring zero data loss. Guardrails include health checks, replication monitoring, long-running transaction detection, and configurable maximum downtime (as low as 30 seconds). Your old production environment is preserved after switchover for validation — standard billing applies until you delete it. Supports [Aurora Global Database](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-bluegreen.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-bluegreen.md") and [RDS Proxy](../../../AmazonRDS/latest/AuroraUserGuide/rds-proxy.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-proxy.md"). Does not currently support cross-Region read replicas or rollback. [See the blue/green deployments documentation](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.md "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.md") for supported versions. For minor version upgrades only, consider Aurora Zero Downtime Patching (ZDP).

Can I use blue/green deployments when I have a blue database as a subscriber/publisher for a self-managed logical replica?

Switchover will be blocked if your blue environment is a self-managed logical replica, or subscriber. We recommend that you first stop replication to the blue environment, proceed with the switchover, and then resume replication. In contrast, if your blue environment is a source for a self-managed logical replica, or publisher, you can continue to switchover. However, you will need to update the self-managed replica to replicate from the green environment post switchover.

## Do blue/green deployments support Aurora Global Database?

Yes. Amazon RDS blue/green deployments support Aurora Global Database. To learn more, read the [blue/green deployments for Amazon Aurora Global Database User Guide](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-bluegreen.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-bluegreen.md").

## How much do blue/green deployments cost?

You pay the same price for running workloads on green instances as you do for blue instances. Effectively, you are paying approximately 2x the cost of running workloads on db.instances for the lifespan of the blue-green deployment. Costs include [current standard pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/") for db.instances, storage, read/write I/Os, and any enabled features.

## What are Trusted Language Extensions (TLE) for PostgreSQL?

[Trusted Language Extensions (TLE)](../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md "../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md") enables developers to build high-performance PostgreSQL extensions and run them safely on Amazon Aurora. TLE improves time to market by removing the need for database administrators to certify custom and third-party code before production use. For example, with TLE, independent software vendors (ISVs) can provide new PostgreSQL extensions to customers running on Aurora. You can build functions such as bitmap compression and differential privacy using JavaScript, PL/pgSQL, Perl, and SQL.

TLE offers multiple layers of protection: it limits access to system resources, isolates extension defects to a single database connection, and provides fine-grained permission controls via the rds\_superuser role. Deploy extensions using the standard CREATE EXTENSION command from any PostgreSQL client. TLE extensions have access to your PostgreSQL database through the TLE API. TLE is available on supported Aurora PostgreSQL 14.5 or higher versions at no additional cost in all AWS Regions (excluding China) and GovCloud. To learn more, visit the [TLE documentation](../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md "../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md") and [TLE GitHub page](https://github.com/aws/pg_tle "https://github.com/aws/pg_tle").

How is TLE for PostgreSQL different from extensions available on Amazon Aurora and Amazon RDS today?

[TLE for PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md "../../../AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.md") extension is included in the set of over [85 PostgreSQL extensions](../../../AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.md") supported by Aurora and RDS. While AWS manages the security risks for each of these extensions under the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), the extensions you write or obtain from third-party sources and install in TLE are considered part of your application code – you are responsible for their security.
