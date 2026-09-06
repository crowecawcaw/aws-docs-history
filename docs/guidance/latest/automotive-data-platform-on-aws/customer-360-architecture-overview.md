

# Architecture overview
<a name="customer-360-architecture-overview"></a>

The solution combines Quick Suite analytics with Bedrock AI agents in a three-tier architecture.

![Customer 360 Analytics Architecture](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/customer360.png)


## Architecture layers
<a name="architecture-layers"></a>

 **Data Layer**:
+ Amazon S3 Data Lake with bronze/silver/gold architecture
+ AWS Glue Catalog for metadata management
+ AWS Glue Crawlers for schema discovery
+ Amazon Athena for SQL queries

The data layer is grounded in the ADP foundation’s governed data products — `customer_360`, `customer_interactions`, and `service_records` — which provide a curated, access-controlled view of the raw telemetry and CRM data ingested by the platform (see [Data products](data-products.md)).

 **Analytics Layer**:
+ Quick Suite Datasets (8 pre-built datasets)
+ Quick Suite Dashboards with interactive visualizations
+ Quick Automate for AI-powered workflows
+ Quick Flows for approval processes

 **AI Layer**:
+ Amazon Aurora PostgreSQL with pgvector extension
+ Amazon Bedrock Knowledge Base with remediation playbooks
+ Amazon Bedrock Agent with Claude 3.5 Sonnet
+ Lambda functions for action groups

## Data model
<a name="data-model"></a>

The solution uses 11 datasets:

 **Core datasets**: 1. customers (500K records) - Customer master data 2. customer\_health (500K records) - Health scores and NPS 3. interactions (1.4M records) - Customer touchpoints 4. service\_records (900K records) - Service history 5. cases (500K records) - Support cases

 **Aggregated metrics**: 6. monthly\_kpis - NPS and health scores by month 7. operational\_kpis - Service quality metrics 8. issue\_categories - Issue breakdown by type 9. revenue\_streams - Revenue by stream 10. revenue\_trends - Revenue changes 11. at\_risk\_revenue - Revenue at risk by segment

 **Key metrics**: \* NPS: 52 → 42 (declining 1.5% monthly) \* Health Score: 65 → 56 (declining 1.5% monthly) \* Battery Issues: 15% → 40% (increasing 2% monthly)