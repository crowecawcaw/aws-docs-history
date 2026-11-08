

# Setting up
<a name="optimized-log-analytics-prerequisites"></a>

Before you create a domain with the Optimized engine, review the following requirements, limitations, and configuration options.

## Prerequisites
<a name="optimized-log-analytics-prereqs"></a>


| Requirement | Value | 
| --- | --- | 
| OpenSearch version | 3.5 or later | 
| Hot-tier instances | OpenSearch Optimized Instances only (OR1, OR2, or OM2) | 
| Warm-tier instances | OI2 only | 
| Authentication | IAM authentication and IAM Identity Center. IAM Identity Center supports SAML and username/password sign-in. The Optimized engine does not support Amazon Cognito. | 
| Visualization | OpenSearch UI only. OpenSearch Dashboards is not available for Optimized domains. | 
| Query language (UI and plugins) | Piped Processing Language (PPL) and SQL | 
| Query language (programmatic) | PPL and SQL (via API, JDBC/ODBC drivers, and Query Workbench) | 
| Engine mode | Immutable. You cannot change the engine mode after you create the domain. | 

## Supported features
<a name="optimized-log-analytics-supported"></a>

The following Amazon OpenSearch Service features are supported on Optimized domains:
+ Fine-grained access control
+ Multi-AZ with Standby (3-AZ)
+ Warm tier with OI2 instances
+ Custom endpoints
+ Encryption in transit (node-to-node) and at rest
+ VPC access and VPC endpoints
+ Dual-stack (IPv4 and IPv6)
+ Off-peak maintenance window
+ Audit logs
+ Notifications
+ OpenSearch Ingestion and Data Prepper
+ Reserved Instances
+ Dedicated coordinator nodes
+ ISM (Index State Management)
+ Automatic snapshots
+ Amazon CloudWatch monitoring
+ Blue/Green deployments
+ Tags
+ AWS CloudFormation integration
+ GP3 EBS volumes
+ Alerting (with PPL – per-query and per-bucket monitors)
+ Anomaly Detection (with PPL)
+ Nested fields (requires OpenSearch 3.7)
+ Delete operations (requires OpenSearch 3.7)
+ APM (Application Performance Monitoring) (requires OpenSearch 3.7)
+ Agent Traces (requires OpenSearch 3.7)

## Supported field types
<a name="optimized-log-analytics-field-types"></a>

The Optimized engine supports the following field type families in index mappings. Every supported field type is stored as its own Parquet column, so filters, aggregations, and sorts read only the columns a query needs.


| Family | Types | Typical use | 
| --- | --- | --- | 
| Numeric | byte, short, integer, long, unsigned\_long, half\_float, float, double, scaled\_float | Counts, durations, status codes, and measurements | 
| Temporal | date, date\_nanos | Log and span timestamps | 
| Boolean | boolean | Flags | 
| String | keyword, text, match\_only\_text | Exact dimensions and root-level full-text fields | 
| Network | ip | Host and client addresses | 
| Binary | binary | Encoded payloads | 
| Scalar lists | Any scalar type with multi\_value: true | Tags, addresses, and repeated IDs | 
| Correlated object lists | nested (requires OpenSearch 3.7) | Events, links, packages, and resources whose fields belong to one element | 
| Semi-structured | flat\_object | Open-ended attribute bags | 
| Containers | object | A single structured object | 

Numeric, date, IP, and boolean fields use the columnar query path and default to `index: false` on Optimized domains. Leave `index` unset (or set it to `false`) and filter these fields with the `where` command.

**Note**  
Types designed for search-centric workloads, including `token_count`, geospatial types, vectors, completion fields, percolators, joins, and range field types, are available only on the General Purpose engine.

## Unsupported features
<a name="optimized-log-analytics-limitations"></a>

The following features are not supported on Optimized domains. If your workload requires these features, use the General Purpose engine.
+ OpenSearch Dashboards
+ DSL (Domain Specific Language) queries in the visualization layer
+ Amazon Cognito authentication
+ SAML authentication (standalone)
+ JWT authentication
+ Auto-Tune
+ Cold storage
+ Cross-cluster replication
+ Cross-cluster search
+ Custom packages
+ Custom plugins
+ Optional plugins
+ Direct queries and Zero-ETL connections
+ Natural language query processing
+ Security Analytics
+ Vector search and semantic search
+ Machine learning connectors
+ Remote reindex
+ Index rollups
+ Index transforms
+ Data streams
+ Manual snapshots
+ Point in Time (PIT)
+ Learning to Rank
+ Geo queries and GeoPoint fields
+ Highlighting
+ Search result pagination
+ Document-level (percolate) alerting monitors
+ Painless scripting
+ Relevance ranking and scoring
+ Previous-generation instance types
+ Elasticsearch compatibility mode
+ Dashboards Query Language (DQL)

## Configuration
<a name="optimized-log-analytics-configuration"></a>

You configure the Optimized engine during domain creation in the Amazon OpenSearch Service console or programmatically through the AWS CLI.

### Console
<a name="optimized-log-analytics-config-console"></a>

**To create an Optimized domain (console)**

1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home) and choose **Create domain**.

1. For **Domain creation method**, choose **Standard create**.

1. For **Use cases**, select **Observability**.

1. Under **Compare engines or change selection**, verify that the **Optimized** engine mode is selected.

1. For **Version**, choose OpenSearch 3.5 or later.

1. For instance type, choose an OpenSearch Optimized Instance (OR1, OR2, or OM2).

1. Configure network, fine-grained access control, and authentication settings.

1. Choose **Create**.

### AWS CLI
<a name="optimized-log-analytics-config-cli"></a>

Use the `create-domain` command with the `--engine-mode` parameter:

```
aws opensearch create-domain \
  --domain-name my-domain \
  --engine-version "OpenSearch_3.5" \
  --engine-mode OPTIMIZED \
  --use-case OBSERVABILITY \
  --cluster-config "InstanceType=or2.2xlarge.search,InstanceCount=1" \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=100" \
  --encryption-at-rest-options "Enabled=true" \
  --node-to-node-encryption-options "Enabled=true" \
  --region us-east-1
```

**Engine mode is permanent**  
You must specify the `--engine-mode OPTIMIZED` parameter to create an Optimized domain. You cannot change the engine mode after you create the domain.