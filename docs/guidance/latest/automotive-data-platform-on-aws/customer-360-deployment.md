# Deployment architecture

A reference implementation of this pattern is structured as a five-stage CDK deployment, each stage building on the previous to progressively compose the full Customer 360 capability.

## Stage structure

**Stage 1: Data Lake Foundation**

The first stage establishes the core data infrastructure: an S3 data lake with bronze/silver/gold prefix structure, a Glue Data Catalog database, an Athena workgroup with result-set location, and Lake Formation permissions scoped to the analytics and AI service principals. This stage has no dependencies on the upper layers and is the prerequisite for all subsequent stages.

**Stage 2: ETL and Catalog**

The second stage wires the catalog layer: Glue crawlers that discover schema from the raw S3 prefix, IAM roles scoped to the crawlers and ETL jobs, and a Quick Suite data source that points at the Athena workgroup created in Stage 1. The Quick Suite data source is provisioned here (not in Stage 4) because the dataset creation in Stage 4 depends on it already existing.

**Stage 3: Data Generation**

The third stage populates the lake with the 11 analytical datasets — approximately 500K customer records, 1.4M interaction records, 900K service records, and the 8 Athena views that aggregate them into the metrics surfaces used by dashboards and agents. In a production deployment this stage is replaced by the live data-ingestion pipeline from the ADP foundation’s governed data products.

**Stage 4: Quick Suite Dashboards**

The fourth stage creates the 8 Quick Suite datasets (one per Athena view), assembles the Customer 360 dashboard from those datasets, and provisions a demo reader user. The datasets use SPICE import mode for performance; refresh schedules are configured to match upstream crawler cadence.

**Stage 5: Bedrock AI Agent**

The fifth stage deploys the AI layer: Aurora PostgreSQL Serverless v2 with the pgvector extension, the Bedrock Knowledge Base backed by that Aurora cluster, the Bedrock Agent with its three action groups, and the Lambda functions that implement the action group handlers. This stage takes the longest to provision (~30 minutes) due to Aurora cluster initialization and Knowledge Base indexing.

## Verification approach

After each stage, the reference implementation includes verification queries to confirm the expected resources exist and are in the correct state. For the data layer, this means confirming the S3 prefix structure is populated and Athena can execute a count query against the core tables. For the Quick Suite layer, this means confirming datasets and dashboards are listed under the account. For the Bedrock layer, this means confirming knowledge bases and agents are registered.

```
# Example: confirm S3 data lake prefix is populated
aws s3 ls s3://automotive-cx-data-lake-<ACCOUNT-ID>/raw/

# Example: confirm Quick Suite datasets exist
aws quicksight list-data-sets --aws-account-id <ACCOUNT-ID>

# Example: confirm Bedrock agent is registered
aws bedrock-agent list-agents
```
