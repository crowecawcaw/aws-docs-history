# Setting up

Before you create a domain with the Optimized engine, review the following
requirements, limitations, and configuration options.

## Prerequisites

| Requirement                     | Value                                                                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenSearch version              | 3.5 or above                                                                                                                                        |
| Hot-tier instances              | OpenSearch Optimized Instances only (OR1, OR2, or OM2)                                                                                              |
| Warm-tier instances             | OI2 only                                                                                                                                            |
| Authentication                  | IAM authentication and IAM Identity Center. IAM Identity Center supports<br>SAML and username/password sign-in. Amazon Cognito is not<br>supported. |
| Visualization                   | OpenSearch UI only. OpenSearch Dashboards is not available for<br>Optimized domains.                                                                |
| Query language (UI and plugins) | Piped Processing Language (PPL) and SQL                                                                                                             |
| Query language (programmatic)   | PPL and SQL (via API, JDBC/ODBC drivers, and Query<br>Workbench)                                                                                    |
| Engine mode                     | Immutable. You cannot change the engine mode after you create<br>the domain.                                                                        |

## Supported features

The following Amazon OpenSearch Service features are supported on Optimized domains:

- Fine-grained access control
- Multi-AZ with Standby (3-AZ)
- Warm tier with OI2 instances
- Custom endpoints
- Encryption in transit (node-to-node) and at rest
- VPC access and VPC endpoints
- Dual-stack (IPv4 and IPv6)
- Off-peak maintenance window
- Audit logs
- Notifications
- OpenSearch Ingestion and Data Prepper
- Reserved Instances
- Dedicated coordinator nodes
- ISM (Index State Management)
- Automatic snapshots
- Amazon CloudWatch monitoring
- Blue/Green deployments
- Tags
- AWS CloudFormation integration
- GP3 EBS volumes
- Alerting (with PPL – per-query and per-bucket monitors)
- Anomaly Detection (with PPL)

## Supported field types

The Optimized engine supports the following field types in index mappings:

- `half_float`
- `float`
- `double`
- `byte`
- `short`
- `integer`
- `long`
- `unsigned_long`
- `scaled_float`
- `date`
- `date_nanos`
- `boolean`
- `text`
- `keyword`
- `ip`
- `match_only_text`
- `binary`

## Unsupported features

The following features are not supported on Optimized domains. If your workload
requires these features, use the General Purpose engine.

- OpenSearch Dashboards
- DSL (Domain Specific Language) queries in the visualization layer
- Amazon Cognito authentication
- SAML authentication (standalone)
- JWT authentication
- Auto-Tune
- Cold storage
- Cross-cluster replication
- Cross-cluster search
- Custom packages
- Custom plugins
- Optional plugins
- Direct queries and Zero-ETL connections
- Natural language query processing
- Security Analytics
- Vector search and semantic search
- Machine learning connectors
- Remote reindex
- Index rollups
- Index transforms
- Data streams
- Manual snapshots
- Point in Time (PIT)
- Learning to Rank
- Geo queries and GeoPoint fields
- Nested fields
- Highlighting
- Delete operations
- APM (Application Performance Monitoring)
- Agent Traces
- Search result pagination
- Document-level (percolate) alerting monitors
- Painless scripting
- Relevance ranking and scoring
- Previous-generation instance types
- Elasticsearch compatibility mode
- Dashboards Query Language (DQL)

## Configuration

You configure the Optimized engine during domain creation in the Amazon OpenSearch Service console
or programmatically through the AWS CLI.

### Console

###### To create an Optimized domain (console)

1. Open the Amazon OpenSearch Service console and choose **Create domain**.
2. For **Domain creation method**, choose **Standard create**.
3. For **Use cases**, select **Observability**.
4. Under **Compare engines or change selection**, verify that the **Optimized** engine mode is selected.
5. For **Version**, choose OpenSearch 3.5 or above.
6. For instance type, choose an OpenSearch Optimized Instance (OR1, OR2, or OM2).
7. Configure network, fine-grained access control, and authentication settings.
8. Choose **Create**.

### AWS CLI

Use the `create-domain` command with the
`--engine-mode` parameter:

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

###### Engine mode is permanent

You must specify the `--engine-mode OPTIMIZED` parameter to create
an Optimized domain. You cannot change the engine mode after you create
the domain.
