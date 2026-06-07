# Creating value and personalized experiences with vehicle data

Publication date: _January 2026 ([last update](revisions.md "revisions.md"): January 2026)_

Automotive manufacturers face a critical challenge: customer and vehicle data is fragmented across disconnected systems—CRM platforms, dealer management systems, connected vehicle telemetry, service records, and contact center interactions—preventing holistic customer understanding and proactive service delivery. This data fragmentation makes it nearly impossible to answer fundamental business questions like "Which high-value customers are at risk of churning?" or "Can we predict and prevent vehicle failures before they strand customers?"

The Guidance for an Automotive Data Platform on AWS addresses these challenges by providing three integrated solutions that break down data silos while maintaining appropriate governance and access controls:

- **Customer 360 Analytics with Agentic AI** - Unifies customer profiles, vehicle health data, service history, and interaction records into a comprehensive analytics platform with AI-powered insights
- **Predictive Maintenance for Vehicle Intelligence** - Analyzes real-time vehicle telemetry using machine learning to predict component failures 7-14 days in advance
- **Multi-Region Data Governance** - Implements EU Data Act and GDPR compliance through centralized governance with regional data residency

## What is a Data Mesh?

A data mesh is an architectural paradigm that treats data as a product, with decentralized domain ownership and federated governance. Unlike traditional centralized data lakes where a single team owns all data, a data mesh recognizes that different domains (customer experience, vehicle operations, service delivery) have unique data needs, expertise, and ownership models.

### Core Principles of Data Mesh

**Domain-Oriented Ownership**: Data is owned by the teams closest to its creation and use. The Customer Experience team owns customer profiles and interaction data, while the Vehicle Operations team owns telemetry and maintenance data. This domain ownership ensures data quality and relevance without creating bottlenecks through centralized data teams.

**Data as a Product**: Each domain treats its data as a product with clear interfaces, documentation, quality guarantees, and SLAs. A customer profile data product provides standardized APIs, maintains data freshness within defined SLAs, and includes comprehensive documentation of schemas and business logic.

**Self-Service Data Platform**: A common platform provides the infrastructure and tools that enable domain teams to create, discover, and consume data products without requiring deep technical expertise. Amazon SageMaker Unified Studio provides this unified interface where teams can explore customer sentiment trends alongside vehicle telemetry patterns.

**Federated Computational Governance**: Centralized policies (security, privacy, compliance) are defined once and enforced automatically across all domains. AWS Lake Formation provides this federated governance, ensuring row-level and column-level security applies consistently whether data is accessed through Amazon Athena, Amazon Q in Quick Suite, or Amazon Bedrock agents.

### Implementing Data Mesh on AWS

AWS provides a comprehensive set of services that enable data mesh architectures:

**AWS Lake Formation** serves as the governance hub, enforcing fine-grained access control policies across all data products. A customer service representative in Germany sees only European customer data, while a global executive sees aggregated metrics across all regions—all enforced automatically at the data catalog level.

**Amazon DataZone** provides data discovery, lineage tracking, and self-service collaboration. Domain teams can publish data products to the DataZone catalog, where other teams discover and request access through automated workflows that respect governance policies.

**Amazon SageMaker Unified Studio** offers a unified interface for data exploration, analytics, and machine learning across domains. Product managers can combine customer sentiment data with vehicle telemetry patterns without understanding the underlying technical complexity.

**AWS Glue Data Catalog** provides the standardized metadata layer that enables interoperability. All data products expose their schemas through the Glue Data Catalog, enabling cross-domain analytics without tight coupling or data duplication.

## Solution Components

### Customer 360 Analytics with Agentic AI

A Customer 360 platform unifies internal systems—CRM, service management, finance, and dealer networks—with external data sources including connected vehicle telemetry, warranty claims, social media sentiment, and third-party market data.

#### Data Ingestion

Internal platforms deliver collaboration, ERP, development, and CRM data to automotive data platforms in real-time, while external sources add vehicle telemetry, supply chain, and sales data for comprehensive analytics. Ingestion services handle data at varying scales and latencies, from millisecond sensor data to scheduled enterprise synchronization.

AWS offers various ingestion pipelines to accommodate diverse data velocities: real-time streaming for vehicle diagnostics and customer interactions, near-real-time APIs for transactional updates, and batch processing for historical sales and demographic enrichment, creating a complete view of customer behavior, vehicle health, and lifetime value.

#### Entity Resolution and Data Quality

Processing pipelines leverage AWS Entity Resolution to deduplicate and link customer records across disparate systems. This unified customer identity is critical for accurate analytics: without it, organizations risk inflating customer counts, underestimating churn, and preventing personalized engagement strategies that require understanding the complete customer relationship across sales, service, and connected vehicle interactions.

#### Lakehouse Architecture

Amazon SageMaker Lakehouse enables a medallion architecture where raw customer and vehicle data lands in the bronze layer, undergoes cleansing and entity resolution in the silver layer to create unified customer profiles, and aggregates into gold layer tables with pre-computed metrics providing optimized tables for real-time dashboard queries.

#### Agentic AI for Autonomous Insights

Agentic AI systems built with Amazon Q in Quick Suite autonomously investigate customer sentiment decline by orchestrating multi-step workflows: detecting negative NPS trends, querying vehicle telemetry for battery degradation patterns, analyzing support case histories for recurring issues, correlating with service appointment delays, and synthesizing findings into root cause reports with recommended interventions—such as proactive battery replacement campaigns for affected VINs—all without human intervention, transforming reactive customer service into predictive, automated retention strategies that execute before customers churn.

Amazon Bedrock Agents with Agent Core Gateway enable natural language access to the automotive data platform, allowing users to query data across Amazon S3, Amazon Athena, and analytics services without writing SQL or navigating dashboards. Business users can ask questions like "What’s causing declining customer sentiment in the Northeast region?" and receive comprehensive answers synthesized from multiple data sources.

### Predictive Maintenance for Vehicle Intelligence

Build a machine learning pipeline to optimize your vehicle data intelligence with tire prediction and component failure models that provide 7-14 days advance warning, enabling proactive service scheduling that reduces roadside breakdowns and improves customer satisfaction.

**How the ML pipeline works:**

- **Hourly Data Processing** - AWS Glue ETL jobs extract tire pressure telemetry from Amazon Redshift, transform sensor readings into standardized formats, and calculate time-series features like pressure drop rates and rolling averages
- **Feature Engineering** - Raw pressure readings are enriched with contextual data (temperature, vehicle load, driving conditions) and compared against historical baselines to create 20+ engineered features per tire reading
- **Weekly Model Training** - Amazon SageMaker trains a Random Cut Forest anomaly detection model on 30 days of historical data, learning normal tire pressure patterns across different vehicle types and operating conditions
- **Daily Batch Predictions** - SageMaker Batch Transform processes new telemetry data, generating anomaly scores (0-1 scale) that indicate likelihood of tire failure within 7-14 days, with scores above 0.7 triggering maintenance alerts
- **Dual-Path Validation** - A parallel statistical filter validates ML predictions using physics-based rules to catch rapid pressure drops, with both pipelines feeding into a consolidated alert system that deduplicates and prioritizes maintenance actions

#### Scalable Vehicle Connectivity

For scalable connectivity, we recommend OEMs use AWS IoT Core as the managed broker to manage connectivity and data ingest from the vehicle to the cloud. AWS IoT Core supports X.509 mTLS authentication to support fan-in MQTT streaming from the connected fleet.

Using AWS IoT Core Basic Ingest and IoT Rules with direct integration with Amazon MSK, vehicles can send encoded and compressed telemetry data directly to a Kafka topic for decoding, decompression and message enrichment.

For the authentication method into Amazon MSK from the IoT Core rule, we recommend using SCRAM/SASL and storing those credentials in AWS Secrets Manager for real-time IoT rule access.

OEMs can also batch telemetry and upload directly to Amazon S3 using an STS token to retrieve a pre-signed URL to upload the batch file direct to S3 for further processing in Kafka to downstream systems.

#### Real-Time Stream Processing

The Amazon Managed Service for Apache Flink (Amazon MSF) applications subscribe to the Kafka message stream and decode and enrich the message prior to republishing to separate Amazon MSK topics. OEMs can use Flink to perform streaming event processing for high throughput vehicle use cases.

Amazon MSF can interact with Amazon DynamoDB using the dedicated connector which enables writing data to DynamoDB tables as a sink. To enable this, the user must configure the Flink application to access the VPC endpoint. In our use case, Amazon MSF writes to Amazon ElastiCache for Redis for last known vehicle state.

#### Machine Learning Pipeline

Amazon SageMaker provides the ML training and inference infrastructure for predictive maintenance models. The Random Cut Forest algorithm detects anomalies in tire pressure, temperature, and wear patterns that indicate impending failures. Step Functions orchestrates the ML workflow from data validation through feature engineering, model training, evaluation, and deployment.

The inference API built with Amazon API Gateway and AWS Lambda provides real-time predictions with sub-second latency, enabling integration with dealer management systems and customer notification workflows.

### Multi-Region Data Governance for EU Data Act Compliance

Build a multi-region data handling workload in accordance with your data governance requirements, ensuring compliance with the EU Data Act and GDPR while enabling global R&D collaboration.

#### Central Governance Region

AWS Lake Formation serves as the global governance hub, enforcing fine-grained access control policies across all regions. AWS Glue Data Catalog maintains centralized metadata, while Amazon DataZone provides data discovery, lineage tracking, and self-service collaboration. AWS Organizations and IAM manage multi-account structure and access permissions. AWS CloudTrail logs all data access for audit trails, and Amazon Macie continuously monitors for PII compliance.

#### Local/Producer Region (EU)

**Data Ingestion**: Connected vehicles transmit telemetry through AWS IoT Core to Amazon Kinesis Data Streams, with Amazon Data Firehose delivering data to Amazon S3 raw storage.

**Data Classification**: AWS Glue Data Quality validates incoming data. AWS Glue ETL Streaming performs real-time classification, separating telemetry into PII and anonymized data stores. The anonymization process includes structured data transformation and video/image anonymization via partner AI solutions.

**Data Stores**: The Local PII Data Store contains precise GPS coordinates, driver information, and detailed vehicle identifiers. The Anonymized Data Store contains hashed identifiers, city-level locations, and aggregated metrics.

**Data Access**: Amazon Cognito authenticates users. The User Portal and Amazon API Gateway provide vehicle owners and authorized third parties access to their PII data as required by the EU Data Act and GDPR. Lake Formation policies validate all access requests.

#### Consumer Region (Global R&D)

R&D teams access anonymized data through Amazon SageMaker for ML model training and Amazon Q in Quick Suite for analytics dashboards. Lake Formation ensures R&D teams can only access anonymized data—never PII.

#### Cross-Region Governance

Lake Formation’s centralized governance enforces consistent policies across regions. Vehicle owners access only their own PII data, while R&D teams access all vehicles' anonymized data. CloudTrail logs all access for compliance reporting. DataZone tracks complete data lineage from ingestion through classification to consumption, providing transparency required for EU Data Act compliance.

## Amazon Q in Quick Suite: Conversational Analytics

Amazon Q in Quick Suite transforms how automotive teams interact with data by providing natural language access to analytics and insights.

### Interactive Dashboards and Reports

Amazon Q in Quick Suite provides interactive dashboards and reports by connecting to Amazon S3, Amazon Athena, and Amazon Redshift, while Amazon Q Business enables natural language queries and conversational analytics, allowing automotive teams to visualize and explore vehicle metrics, supply chain KPIs, and operational data with embedded insights and role-based access.

### Natural Language Queries

Instead of writing SQL or navigating complex dashboard interfaces, users can ask questions in plain English: "Show me customer churn trends by region for the last quarter" or "Which vehicle models have the highest battery degradation rates?" Amazon Q translates these questions into optimized queries against the data lake, respecting Lake Formation permissions to ensure users only see data they’re authorized to access.

### Embedded Insights and Anomaly Detection

Amazon Q continuously monitors dashboard metrics and proactively surfaces insights: "Customer satisfaction in the Northeast region declined 15% this month, primarily driven by battery-related service cases." These embedded insights accelerate decision-making by highlighting trends that might otherwise go unnoticed in large datasets.

### Role-Based Access and Governance

Amazon Q in Quick Suite inherits permissions from Lake Formation policies, ensuring that a customer service representative sees only their assigned region’s data while executives access global aggregations. This governance integration eliminates the need to implement access controls separately in the analytics layer.

## Data Lake Architecture

### Security and Governance

AWS IAM controls access to data lake resources, AWS CloudTrail provides an immutable audit log of all API calls and data access for compliance, and AWS Security Hub aggregates security findings while continuously monitoring against frameworks.

AWS Glue Data Catalog provides centralized management for all data lake assets, Lake Formation enforces fine-grained access controls at the database, table, and column level, and Amazon Athena enables serverless SQL queries with permissions inherited from Lake Formation policies for secure data access.

### Storage and Data Formats

Amazon S3 provides scalable storage for the automotive data lakehouse, supporting Parquet files for columnar analytics, Apache Iceberg tables for ACID transactions and schema evolution, and vector embeddings for semantic search and AI-powered applications.

Parquet’s columnar format reduces query costs by enabling Athena to scan only required columns. Apache Iceberg provides time travel, schema evolution, and partition evolution without rewriting data. Vector embeddings stored in S3 enable semantic search across customer interactions and service records, powering AI applications that understand context beyond keyword matching.

## Key Features

This guidance provides the following capabilities:

- **Unified Customer View** - Integrate customer profiles, vehicle health, service history, and interactions into a single analytics platform
- **Predictive Maintenance** - Detect tire failures and component issues 7-14 days in advance using machine learning
- **AI-Powered Insights** - Query data using natural language through Amazon Bedrock agents and Amazon Q in Quick Suite
- **Data Mesh Architecture** - Enable domain-oriented ownership with federated governance through Lake Formation and DataZone
- **EU Data Act Compliance** - Implement multi-region governance with PII classification and vehicle owner data access
- **Real-Time Processing** - Process vehicle telemetry at scale using Amazon MSK and Apache Flink
- **Serverless Analytics** - Query data lakes using Amazon Athena without managing infrastructure
- **Cost Optimization** - Pay only for actual usage with serverless architecture and intelligent storage tiering
- **Security and Compliance** - Enforce fine-grained access controls, audit all data access, and monitor for PII exposure

## Use Cases

### Customer Retention

Identify at-risk customers based on declining health scores, service issues, and sentiment trends. The AI agent autonomously investigates root causes—correlating battery degradation patterns with service appointment delays—and recommends proactive interventions before customers churn.

### Predictive Maintenance

Prevent tire failures and other component issues through real-time telemetry analysis. The ML model detects anomaly patterns 7-14 days before failures occur, enabling dealers to reach out proactively with service appointments that prevent breakdowns and demonstrate genuine care for customer wellbeing.

### Service Optimization

Analyze service patterns to reduce wait times and improve first-time fix rates. Identify recurring issues across vehicle models and proactively address them through targeted service campaigns or software updates.

### Revenue Protection

Quantify revenue at risk from churning customers and prioritize retention efforts. The platform calculates customer lifetime value and identifies high-value customers showing early warning signs of dissatisfaction.

### Regulatory Compliance

Fulfill EU Data Act and GDPR requirements through automated data classification, vehicle owner data access portals, and complete audit trails. The multi-region architecture ensures PII remains in EU regions while enabling global R&D collaboration with anonymized data.

## Target Audience

### Cost Estimates

The following table provides estimated monthly costs for deploying each solution component. Costs are based on us-east-1 region pricing and assume moderate usage (demo/development workloads). Production workloads with higher data volumes and query rates will scale accordingly.

| Solution Component         | Key Services                                                                 | Monthly Estimate | Notes                                                         |
| -------------------------- | ---------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------- |
| **Foundational Layer**     | S3, Glue Catalog, Athena, Lake Formation, CloudWatch                         | **~$15**         | Shared across all components                                  |
| **Customer 360 Analytics** | Aurora pgvector, Bedrock Agent + KB, QuickSight, Athena, Glue                | **~$160-235**    | QuickSight per-user pricing; Bedrock scales with query volume |
| **Predictive Maintenance** | SageMaker (training + inference), Glue ETL, Lambda, Step Functions, DynamoDB | **~$355-650**    | $355 for 10K vehicles, $650 for 50K vehicles                  |
| **Data Governance**        | S3 (multi-region), Glue ETL, Macie, Lake Formation, CloudTrail               | **~$48-55**      | Scales with data volume scanned by Macie                      |
| **All 3 Components**       | Combined                                                                     | **~$580-955**    | Shared foundational layer reduces per-component overhead      |

###### Note

These estimates are approximate and based on publicly available AWS pricing as of March 2026. Actual costs depend on usage patterns, data volumes, query frequency, and region. Use the [AWS Pricing Calculator](https://calculator.aws/ "https://calculator.aws/") for detailed estimates tailored to your workload. Contact your AWS account team for enterprise pricing and reserved capacity discounts.

For detailed per-service cost breakdowns, see the cost sections within each solution component’s documentation.

## Target Audience

This guidance is designed for:

- **Automotive OEMs** seeking to improve customer retention and vehicle uptime through data-driven insights
- **Automotive Dealers** wanting to optimize service operations and deliver personalized customer experiences
- **Fleet Operators** needing predictive maintenance to reduce vehicle downtime and maintenance costs
- **Connected Vehicle Platforms** looking to monetize telemetry data through advanced analytics and AI
- **Data and Analytics Teams** in automotive organizations building modern data platforms on AWS
- **Solutions Architects** designing scalable, compliant data architectures for automotive use cases
- **Data Engineers** implementing data mesh patterns with domain-oriented ownership
- **ML Engineers** building predictive maintenance and customer analytics models

## How This Guide Is Organized

This implementation guide provides:

- **Architecture Overview** - High-level architecture diagrams and component descriptions for all three solutions
- **Architecture Details** - Detailed technical specifications for Customer 360, Predictive Maintenance, and Multi-Region Governance
- **Plan Your Deployment** - Cost estimates, security considerations, compliance requirements, and prerequisites
- **Deploy the Solution** - Step-by-step deployment instructions with interactive Makefile and CDK stacks
- **Monitor the Solution** - CloudWatch dashboards, X-Ray tracing, and AppRegistry integration
- **Troubleshooting** - Common issues and debugging techniques for Glue, Athena, Bedrock, and SageMaker
- **Developer Guide** - Customization patterns, data mesh best practices, and CI/CD integration
- **Reference** - Links to GitHub repositories, AWS service documentation, and related solutions

The intended audience for using this solution’s features and capabilities in their environment includes solutions architects, business decision makers, DevOps engineers, data scientists, ML engineers, and cloud professionals.
