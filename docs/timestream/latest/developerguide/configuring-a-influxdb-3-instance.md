For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configuring an InfluxDB 3 cluster in

Timestream

## Creating a DB cluster in Timestream

Using the AWS Management Console:

1.  Open the Amazon Timestream for InfluxDB console.
2.  Choose **InfluxDB Databases** in the navigation pane.
3.  Choose **Create InfluxDB 3 database.**
4.  Select **InfluxDB 3** as your engine version.
5.  Choose **Enterprise** edition for production workloads.
6.  Configure cluster deployment:
    1. Select either **1-node** (single node handling writer,
       reader, and compactor roles) or **3-node** configuration

    ###### Note

    Single node deployments use Single-AZ compute resources. In case of an issue, a new
    compute resource must be initialized, resulting in longer remediation time 2. For 3-node deployments, the system will automatically configure:

        1. Two writer/reader nodes for handling both write and read operations.
        2. One dedicated compactor node for storage optimization.

7.  Configure cluster-level settings:
    1. **Instance class**: Select the appropriate `db.influx`
       instance size (applies to all nodes). Worth noting your bill will show
       `db.influxIOIncluded` on your records.
    2. **Parameter group**: Choose an existing parameter group or
       create a new one for custom engine configuration.
    3. **Network configuration**: Configure VPC, subnets, and security
       groups (applies to all nodes).
    4. **Public accessibility**: Choose whether the cluster endpoints
       should be publicly accessible.

8.  **Important:** If creating a private cluster, make sure you add the
    [required S3 policies to create your Timestream for InfluxDB 3 cluster](s3-vpc-endpoint-private-clusters.md "s3-vpc-endpoint-private-clusters.md")
9.  Review your configuration and choose **Create InfluxDB database**

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
- **Node configuration**: 1-node or 3-node deployment
- **Parameter group**: Engine configuration settings
- **Network type**: IPv4 or dual-stack
- **VPC and subnets**: Network isolation and availability
- **Security groups**: Network access control
- **Public accessibility**: Internet connectivity option

**Important Considerations**

- **Uniform node configuration**: All nodes in a cluster must use
  the same instance class and network configuration.
- **Future scalability**: While initially limited to 1-node and
  3-node configurations, future updates will enable scaling to additional nodes through parameter
  group modifications.
- **High availability**: 3-node configurations provide better
  availability and performance distribution.
- **Compactor optimization**: In 3-node deployments, the dedicated
  compactor node ensures write and read performance isn't impacted by background optimization
  tasks

###### Topics

- [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md "parameter-groups.md")
- [Core and Enterprise versions](core-and-enterprise-versions.md "core-and-enterprise-versions.md")
- [Deployment models](deployment-models.md "deployment-models.md")
- [Endpoints and connectivity](endpoints-and-connectivity.md "endpoints-and-connectivity.md")
