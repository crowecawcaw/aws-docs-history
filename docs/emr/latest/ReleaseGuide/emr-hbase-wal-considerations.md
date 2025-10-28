# Considerations and Regions for Amazon EMR

WAL

## Considerations for Amazon EMR WAL

The following list describes important considerations and limitations of Amazon EMR
WAL:

- Amazon EMR WAL is available to use with Amazon EMR releases 6.15.0 and
  higher.
- Amazon EMR WAL is an opt-in, paid service. You pay for what you use: reads,
  writes, and data storage. For more information, see [Understanding Amazon EMR WAL pricing and
  metrics](emr-hbase-wal-metrics.md "emr-hbase-wal-metrics.md")
  and the [Amazon EMR
  pricing](https://aws.amazon.com/emr/pricing/ "https://aws.amazon.com/emr/pricing/") page.
- Amazon EMR WAL uses HBase Write Ahead Log (WAL). To use Amazon EMR WAL, your
  clusters must use HBase WAL.
- To enable Amazon EMR WAL when you create a cluster, you must have the required
  role permissions. For more information, see [Using service-linked roles for write-ahead logging](../ManagementGuide/using-service-linked-roles-wal.md "../ManagementGuide/using-service-linked-roles-wal.md").
- You must enable Amazon EMR WAL when you create the cluster with the AWS Management Console,
  AWS CLI, or API, and you must use the _instance groups_
  configuration. You can't enable Amazon EMR WAL in a running cluster if you didn't
  create the cluster with Amazon EMR WAL. You also can't edit the
  `hbase-site` configurations to enable Amazon EMR WAL in a running
  cluster.
- You can only enable Amazon EMR WAL on clusters that use Amazon S3 for the root
  directory.
- Prior to Amazon EMR version 7.5.0, records in Amazon EMR WAL had to be 4MB or smaller. But with Amazon EMR version 7.5.0 and later, the maximum record size in EMR WAL is configurable,
  using the property `emr.wal.max.payload.size`. The default value is 1GB. The following example sets the maximum record size to 2GB:

```
[
  {
    "Classification":"hbase-site",
    "Properties": {
       "emr.wal.max.payload.size": "2147483648"
    }
  }
]
```

- You can't have multiple active clusters on the same HBase root directory
  in Amazon S3.
- You can't enable Amazon EMR WAL on read replica clusters.
- WAL is replicated across Availability Zones inside the managed service.
- WAL outlives the the cluster, and remains available for the next
  cluster.
- You can't disable Amazon EMR WAL during launch or when your cluster is
  operational (in a running state).
- For information on WAL and workspace limits, see [Amazon EMR endpoints
  and quotas](../../../general/latest/gr/emr.md "../../../general/latest/gr/emr.md").

## Region availability for Amazon EMR WAL

Amazon EMR WAL service is available in the following AWS Regions:

- `ap-northeast-1` – Asia Pacific (Tokyo)
- `ap-northeast-2` – Asia Pacific (Seoul)
- `ap-southeast-1` – Asia Pacific (Singapore)
- `ap-south-1` – Asia Pacific (Mumbai)
- `ap-southeast-2` – Asia Pacific (Sydney)
- `eu-central-1` – Europe (Frankfurt)
- `eu-north-1` – Europe (Stockholm)
- `eu-west-1` – Europe (Ireland)
- `sa-east-1` – South America (São Paulo)
- `us-east-1` – US East (N. Virginia)
- `us-east-2` – US East (Ohio)
- `us-west-2` – US West (Oregon)

Following regions would be only available with Amazon EMR version 7.3.0 or later:

- `ap-east-1` – Asia Pacific (Hong Kong)
- `af-south-1` – Africa (Cape Town)
- `ca-central-1` – Canada (Central)
- `eu-west-2` – Europe (London)
