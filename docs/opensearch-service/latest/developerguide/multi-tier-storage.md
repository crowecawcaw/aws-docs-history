# Multi-tier storage for Amazon OpenSearch Service

Multi-tier storage for Amazon OpenSearch Service is an intelligent data management solution that optimizes both performance and costs by managing data across different storage tiers. This architecture allows organizations to efficiently balance the trade-off between performance and cost by keeping frequently accessed data in high-performance hot storage while moving less frequently accessed data to more cost-effective warm storage.

Amazon OpenSearch Service offers two architecture options for hot/warm storage tier:

- **OpenSearch Multi-tier Storage Architecture**
  - Combines Amazon S3 with local instance storage
  - Powered by OpenSearch Optimized Instances
  - Supports write operations in warm tier
  - Supports seamless data migration between hot and warm tier
  - Available on OpenSearch 3.3 and above
  - Does not support Cold Tier

- **UltraWarm-based Architecture**
  - Combines Amazon S3 with local instance storage
  - Powered by UltraWarm nodes
  - Optimized for read-only warm tier workloads
  - Available on Elasticsearch version 6.8 and above and all OpenSearch versions
  - Supports Cold Tier

###### Note

This documentation only focuses on the multi-tier architecture.
For Ultrawarm storage architecture, see [Ultrawarm](ultrawarm.md "ultrawarm.md") and [Cold Storage](cold-storage.md "cold-storage.md")

## Multi-tier storage architecture

###### Topics

- [Key benefits](#multi-tier-benefits "#multi-tier-benefits")
- [Prerequisites](#multi-tier-prerequisites "#multi-tier-prerequisites")
- [Limitations](#multi-tier-limitations "#multi-tier-limitations")
- [Things to note](#things-to-note "#things-to-note")
- [Creating a multi-tier domain](#multi-tier-creating "#multi-tier-creating")
- [Managing tier migrations](#multi-tier-managing "#multi-tier-managing")
- [Security configuration](#multi-tier-security "#multi-tier-security")
- [Best practices](#multi-tier-best-practices "#multi-tier-best-practices")
- [Monitoring metrics](#multi-tier-metrics "#multi-tier-metrics")

### Key benefits

- **Writable Warm:** Supports write operations on warm indices
- **Seamless Migration:** Seamless movement of data across storage tiers
- **Cost Optimization:** Reduce storage costs by moving less-active data to cost-effective warm storage
- **Performance Enhancement:** Maintain high performance for frequently accessed data in the hot tier
- **Flexible Data Management:** Choose the architecture that best fits your workload requirements
- **Automated Management:** Simplified data lifecycle management across storage tiers

### Prerequisites

- **Engine version:** OpenSearch **3.3 or later**
- **Instance families:**
  - Hot nodes: OR1, OR2, OM2, or OI2
  - Warm Nodes: OI2

- **Security:** Node-to-node encryption, encryption at rest, HTTPS enforced

### Limitations

- Works on all domains with OpenSearch optimized instances that do not have Ultrawarm enabled already
- No support for cold tier

### Things to note

- Hot to warm migrations do not trigger a force merge in mult-tier architecture. If needed, user can still orchestrate force merges using Index Management policy.
- Apart from indexing, warm nodes now also perform background merge operations (similar to hot).
- All search requests on warm indices are routed to primary shard and replica serves reads only when primary shard is down.
- Automated snapshots for warm indices are also supported with this architecture
- Cross cluster replication is only supported for hot indices
- Index APIs such as Shrink, Split and Clone doesn't work with warm indices.

### Creating a multi-tier domain

#### Step 1: Create the domain

```
aws opensearch create-domain \
      --domain-name my-domain \
      --engine-version OpenSearch_3.3 \
      --cluster-config InstanceCount=3,InstanceType=or2.large.search,DedicatedMasterEnabled=true,DedicatedMasterType=m6g.large.search,DedicatedMasterCount=3,WarmEnabled=true,WarmCount=3,WarmType=oi2.2xlarge.search \
      --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=11 \
      --node-to-node-encryption-options Enabled=true \
      --encryption-at-rest-options Enabled=true \
      --domain-endpoint-options EnforceHTTPS=true,TLSSecurityPolicy=Policy-Min-TLS-1-2-2019-07 \
      --advanced-security-options '{"Enabled":true,"InternalUserDatabaseEnabled":true,"MasterUserOptions":{"MasterUserName":"user_name","MasterUserPassword":"your_pass"}}' \
      --access-policies '{"Version": "2012-10-17",		 	 	  "Statement":[{"Effect":"Allow","Principal":"*","Action":"es:*","Resource":"*"}]}' \
      --region us-east-1
```

#### Step 2: Verify warm nodes

```
aws opensearch describe-domain-nodes --domain-name my-domain --region us-east-1
```

Sample response (excerpt):

```
{
      "NodeType": "Warm",
      "InstanceType": "oi2.large.search",
      "NodeStatus": "Active"
    }
```

### Managing tier migrations

Multi-tier domains support:

- New Tiering APIs for a simplified experience
- Legacy UltraWarm APIs for compatibility

#### New tiering APIs

**Migrate an index to warm:**

```
curl -XPOST 'https://localhost:9200/index-name/_tier/warm'
```

Response:

```
{"acknowledged": true}
```

**Migrate an index to hot:**

```
curl -XPOST 'https://localhost:9200/index-name/_tier/hot'
```

Response:

```
{"acknowledged": true}
```

**Check tiering status:**

```
curl -XGET 'https://localhost:9200/index-name/_tier'
```

Example response:

```
{
      "tiering_status": {
         "index": "index-name",
         "state": "RUNNING_SHARD_RELOCATION",
         "source": "HOT",
         "target": "WARM",
         "start_time": 1745836500563,
         "shard_level_status": {
           "running": 0,
           "total": 100,
           "pending": 100,
           "succeeded": 0
         }
      }
    }
```

**Detailed shard view:**

```
curl 'https://localhost:9200/index1/_tier?detailed=true'
```

**List all ongoing migrations (text):**

```
curl 'https://localhost:9200/_tier/all'
```

**List all ongoing migrations (JSON):**

```
curl 'https://localhost:9200/_tier/all?format=json'
```

**Filter by target tier:**

```
curl 'https://localhost:9200/_tier/all?target=_warm'
```

#### Legacy UltraWarm APIs for compatibility

**Migrate to warm:**

```
curl -XPOST localhost:9200/_ultrawarm/migration/index2/_warm
```

**Migrate to hot:**

```
curl -XPOST localhost:9200/_ultrawarm/migration/index2/_hot
```

**Check status:**

```
curl -XGET localhost:9200/_ultrawarm/migration/index2/_status
```

### Security configuration

If you enable multi-tier storage on a preexisting Amazon OpenSearch Service domain, the `storage_tiering_manager` role might not be defined on the domain. Non-admin users must be mapped to this role in order to manage warm indexes on domains using fine-grained access control. To manually create the `storage_tiering_manager` role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Permissions**.
2. Choose **Create action group** and configure the following groups:

| Group Name                  | Permissions                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| storage_tiering_cluster     | indices:admin/\_tier/all                                           |
| storage_tiering_index_read  | indices:admin/\_tier/get, indices:admin/get                        |
| storage_tiering_index_write | indices:admin/\_tier/hot_to_warm, indices:admin/\_tier/warm_to_hot |

3. Choose **Roles** and **Create role**.
4. Name the role `storage_tiering_manager`.
5. For **Cluster permissions**, select `storage_tiering_cluster` and `cluster_monitor`.
6. For **Index**, type `*`.
7. For **Index permissions**, select `storage_tiering_index_read`, `storage_tiering_index_write` and `indices_monitor`.
8. Choose **Create**.
9. After you create the role, map it to any user or backend role that will manage multi-tier indexes.

### Best practices

As you implement multi-tier storage in your Amazon OpenSearch Service domains, consider the following best practices:

- Regularly review your data access patterns to optimize tier allocation
- Monitor performance metrics to ensure efficient resource utilization
- Use the new tiering APIs for granular control over data migration

### Monitoring metrics

Multi-tier storage domains provide additional metrics for monitoring warm tier performance. These metrics include both existing UltraWarm metrics and new metrics specific to the OpenSearch Optimized Instances architecture:

#### New metrics

| Metric Name                    | Node Level Stats | Cluster Level Stats   | Granularity |
| ------------------------------ | ---------------- | --------------------- | ----------- |
| WarmIndexingLatency            | Average          | Average               | 1 min       |
| WarmIndexingRate               | Average          | Average, Maximum, Sum | 1 min       |
| WarmThreadpoolIndexingQueue    | Maximum          | Sum, Maximum, Average | 1 min       |
| WarmThreadpoolIndexingRejected | Maximum          | Sum                   | 1 min       |
| WarmThreadpoolIndexingThreads  | Maximum          | Sum, Average          | 1 min       |
