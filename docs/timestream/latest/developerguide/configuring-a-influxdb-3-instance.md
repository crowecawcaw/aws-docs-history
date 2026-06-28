For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configuring an InfluxDB 3 cluster in Timestream

## Creating a DB cluster in Timestream

Using the AWS Management Console:

1. Open the Amazon Timestream for InfluxDB console.
2. Choose **InfluxDB Databases** in the navigation pane.
3. Choose **Create InfluxDB 3 database.**
4. Select **InfluxDB 3** as your engine version.
5. Choose **Enterprise** edition for production workloads.
6. Configure cluster deployment:

   1. Select either **1-node** (single node handling writer,
      reader, and compactor roles), **3-node** configuration, or
      a **multi-node cluster (up to 15 nodes)** using a custom
      parameter group. For details on multi-node configurations, see
      [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md").

   ###### Note

   Single node deployments use Single-AZ compute resources. In case of an issue, a new
   compute resource must be initialized, resulting in longer remediation time 2. For multi-node deployments, the system configures:

        1. 1-4 writer/reader nodes for handling both write and read operations.
        2. 0-13 reader-only nodes dedicated to processing read queries.
        3. One dedicated compactor node for storage optimization (required for clusters with 3+ nodes).

7. Configure cluster-level settings:

   1. **Instance class**: Select the appropriate `db.influx`
      instance size (applies to all nodes). Worth noting your bill will show
      `db.influxIOIncluded` on your records.
   2. **Parameter group**: Choose an existing parameter group or
      create a new one for custom engine configuration.
   3. **Network configuration**: Configure VPC, subnets, and security
      groups (applies to all nodes).

   ###### Note

   Shared VPCs are not currently supported for Timestream for InfluxDB 3. 4. **Public accessibility**: Choose whether the cluster endpoints
   should be publicly accessible.

8. **Important:** If creating a private cluster, make sure you add the
   [required S3 policies to create your Timestream for InfluxDB 3 cluster](s3-vpc-endpoint-private-clusters.md "s3-vpc-endpoint-private-clusters.md")
9. Review your configuration and choose **Create InfluxDB database**

Using the AWS CLI:

```
aws timestream-influxdb create-db-cluster \
     --name myinfluxDbinstance \
     --db-instance-type db.influx.4xlarge \
     --vpc-subnet-ids subnetid1 subnetid2 \
     --vpc-security-group-ids mysecuritygroup \
     --db-parameter-group-identifier dbparametergroupidentifier
```

###### Note

You can label Timestream for InfluxDB resources using tags. Tags let you categorize your
resources in different ways, such as by purpose, owner, environment, or other criteria.

## Settings for DB clusters

Key settings that apply to all nodes in your cluster include:

- **Cluster identifier**: Unique name for your cluster
- **Instance class**: Compute and memory capacity (same for all
  nodes)
- **Node configuration**: 1-node, 3-node, or multi-node deployment
  (up to 15 nodes)
- **Parameter group**: Engine configuration settings
- **Network type**: IPv4 or dual-stack
- **VPC and subnets**: Network isolation and availability
- **Security groups**: Network access control
- **Public accessibility**: Internet connectivity option

**Important Considerations**

- **Uniform node configuration**: All nodes in a cluster must use
  the same instance class and network configuration.
- **Scalability**: Enterprise clusters support up to 15 nodes.
  You can scale your cluster by creating a new parameter group with your desired node
  configuration and applying it to your cluster. See [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md").
- **High availability**: Multi-node configurations provide better
  availability and performance distribution, with nodes spread across multiple Availability
  Zones.
- **Compactor optimization**: In multi-node deployments (3+ nodes),
  the dedicated compactor node ensures write and read performance isn't impacted by background
  optimization tasks

###### Topics

- [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md "parameter-groups.md")
- [Core and Enterprise versions](core-and-enterprise-versions.md "core-and-enterprise-versions.md")
- [Deployment models](deployment-models.md "deployment-models.md")
- [Endpoints and connectivity](endpoints-and-connectivity.md "endpoints-and-connectivity.md")
