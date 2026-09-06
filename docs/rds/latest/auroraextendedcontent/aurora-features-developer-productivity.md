

# Developer productivity
<a name="aurora-features-developer-productivity"></a>

**Topics**
+ [MCP servers](#aurora-features-mcp-servers)
+ [Agentic tools](#aurora-features-agentic-tools)
+ [Agent skills](#aurora-features-agent-skills)
+ [Zero-ETL integration with Amazon Redshift](#aurora-features-zero-etl-redshift)
+ [Zero-ETL integration with Amazon SageMaker](#aurora-features-zero-etl-sagemaker)
+ [RDS Proxy](#aurora-features-rds-proxy)
+ [Data API](#aurora-features-data-api)

## MCP servers
<a name="aurora-features-mcp-servers"></a>

[Aurora MCP server](https://awslabs.github.io/mcp/servers/postgres-mcp-server) provides the flexibility and ease to build and deploy from the tools and agents of your choice. A critical component in agentic AI architectures, Aurora MCP server provide the standardized interface needed for agents to interact with developer tools and your Aurora databases. Aurora MCP server is available on Github for [PostgreSQL](https://awslabs.github.io/mcp/servers/postgres-mcp-server/) and [MySQL](https://awslabs.github.io/mcp/servers/mysql-mcp-server).

## Agentic tools
<a name="aurora-features-agentic-tools"></a>

Aurora integrates directly with the developer tools you already use, saving you hours or weeks of time to build, test, and deploy. AI-enabled IDEs (e.g., [Kiro](https://kiro.dev/)) and agentic development platforms (e.g., Vercel) help you build in your preferred environment and significantly shorten the path from idea to working application. Aurora is integrated with agentic frameworks (e.g., [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/), Letta, LangGraph) to persist agent memories using a fully managed database.

## Agent skills
<a name="aurora-features-agent-skills"></a>

[Kiro power for Aurora PostgreSQL](https://github.com/awslabs/mcp/tree/main/src/postgres-mcp-server/kiro_power) provides specialized skills to AI agents that contain specific Aurora knowledge, MCP tools, and best practices to instantly understand how to work with Aurora PostgreSQL. With one-click installation, you can start building database-backed apps in Kiro using natural language – no Aurora expertise required.

## Zero-ETL integration with Amazon Redshift
<a name="aurora-features-zero-etl-redshift"></a>

[Aurora zero-ETL integration with Amazon Redshift](https://aws.amazon.com/rds/aurora/zero-etl/) enables near real-time analytics and ML using Amazon Redshift on petabytes of transactional data from Aurora by removing the need for you to build and maintain complex data pipelines that perform extract, transform, and load (ETL) operations. Transactional data is automatically and continuously replicated within seconds of being written in Aurora and is seamlessly made available in Amazon Redshift.

Once data is available in Amazon Redshift, you can start analyzing it immediately and apply advanced features like data sharing, materialized views, and Amazon Redshift ML to get holistic and predictive insights. You can consolidate multiple tables from various Aurora database clusters and replicate your data into one Amazon Redshift data warehouse to run unified analytics across multiple applications and data sources. When using both [Aurora serverless](https://aws.amazon.com/rds/aurora/serverless/) and [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/), you can generate near real-time analytics on transactional data without having to manage any infrastructure for data pipelines. Additional information is available in [Aurora zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) documentation.

## Zero-ETL integration with Amazon SageMaker
<a name="aurora-features-zero-etl-sagemaker"></a>

Aurora zero-ETL integration with [Amazon SageMaker](https://aws.amazon.com/sagemaker/lakehouse/) enables near real-time access of your data in the lakehouse architecture of SageMaker to run a broad range of analytics. With zero-ETL integration, data from Aurora is automatically extracted and loaded into the lakehouse in SageMaker enabling you to derive near real-time insights from your operational data. The data synced into the lakehouse is compatible with Apache Iceberg open standards, enabling you to use your preferred analytics tools and query engines such as SQL, Apache Spark, BI, and AI/ML tools. Additional information is available in [Aurora zero-ETL integration with Amazon SageMaker](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) documentation.

## RDS Proxy
<a name="aurora-features-rds-proxy"></a>

Aurora works in conjunction with [RDS Proxy](https://aws.amazon.com/rds/proxy/), a fully managed, highly available database proxy that makes applications more scalable, more resilient to database failures, and more secure. RDS Proxy allows applications to pool and share connections established with the database, improving database efficiency and application scalability. It reduces failover times by automatically connecting to a new database instance while preserving application connections. It enhances security through integrations with [AWS IAM](https://aws.amazon.com/iam/) and [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

## Data API
<a name="aurora-features-data-api"></a>

[Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) is an easy-to-use, secure HTTPS API for executing SQL queries against Aurora databases. It eliminates the need for database drivers, client-side connection pools, and VPC networking configuration to securely connect to an Aurora database, which makes accessing Aurora as simple as making an API call. Data API also improves application scalability by automatically pooling and sharing database connections and is integrated with [AWS IAM](https://aws.amazon.com/iam/) and [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). You can call Data API via applications built with an AWS SDK or through [AWS AppSync GraphQL APIs](https://aws.amazon.com/appsync/).