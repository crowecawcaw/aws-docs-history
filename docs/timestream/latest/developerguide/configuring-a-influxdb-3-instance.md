

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Configuring an InfluxDB 3 cluster in Timestream
<a name="configuring-a-influxdb-3-instance"></a>

## Creating a DB cluster in Timestream
<a name="creating-a-db-cluster"></a>

 Using the AWS Management Console: 

1.  Open the Amazon Timestream for InfluxDB console. 

1.  Choose **InfluxDB Databases** in the navigation pane. 

1.  Choose **Create InfluxDB 3 database.** 

1.  Select **InfluxDB 3** as your engine version. 

1.  Choose **Enterprise** edition for production workloads. 

1.  Configure cluster deployment: 

   1.  Select either **1-node** (single node handling writer, reader, and compactor roles), **3-node** configuration, or a **multi-node cluster (up to 15 nodes)** using a custom parameter group. For details on multi-node configurations, see [Scaling a cluster](multi-node-scaling.md). 
**Note**  
Single node deployments use Single-AZ compute resources. In case of an issue, a new compute resource must be initialized, resulting in longer remediation time

   1.  For multi-node deployments, the system configures: 

      1. 1-4 writer/reader nodes for handling both write and read operations. 

      1. 0-13 reader-only nodes dedicated to processing read queries. 

      1. One dedicated compactor node for storage optimization (required for clusters with 3\+ nodes). 

1.  Configure cluster-level settings: 

   1.  **Instance class**: Select the appropriate `db.influx` instance size (applies to all nodes). Worth noting your bill will show `db.influxIOIncluded` on your records. 

   1.  **Parameter group**: Choose an existing parameter group or create a new one for custom engine configuration. 

   1.  **Network configuration**: Configure VPC, subnets, and security groups (applies to all nodes). 
**Note**  
Shared VPCs are not currently supported for Timestream for InfluxDB 3.

   1.  **Public accessibility**: Choose whether the cluster endpoints should be publicly accessible. 

1. **Important:** If creating a private cluster, make sure you add the [ required S3 policies to create your Timestream for InfluxDB 3 cluster](https://docs.aws.amazon.com/timestream/latest/developerguide/s3-vpc-endpoint-private-clusters.html) 

1.  Review your configuration and choose **Create InfluxDB database** 

 Using the AWS CLI: 

```
aws timestream-influxdb create-db-cluster \
     --name myinfluxDbinstance \
     --db-instance-type db.influx.4xlarge \
     --vpc-subnet-ids subnetid1 subnetid2 \
     --vpc-security-group-ids mysecuritygroup \
     --db-parameter-group-identifier dbparametergroupidentifier
```

**Note**  
 You can label Timestream for InfluxDB resources using tags. Tags let you categorize your resources in different ways, such as by purpose, owner, environment, or other criteria. 

## Settings for DB clusters
<a name="settings-for-db-clusters"></a>

 Key settings that apply to all nodes in your cluster include: 
+  **Cluster identifier**: Unique name for your cluster 
+  **Instance class**: Compute and memory capacity (same for all nodes) 
+  **Node configuration**: 1-node, 3-node, or multi-node deployment (up to 15 nodes) 
+  **Parameter group**: Engine configuration settings 
+  **Network type**: IPv4 or dual-stack 
+  **VPC and subnets**: Network isolation and availability 
+  **Security groups**: Network access control 
+  **Public accessibility**: Internet connectivity option 

 **Important Considerations** 
+  **Uniform node configuration**: All nodes in a cluster must use the same instance class and network configuration. 
+  **Scalability**: Enterprise clusters support up to 15 nodes. You can scale your cluster by creating a new parameter group with your desired node configuration and applying it to your cluster. See [Scaling a cluster](multi-node-scaling.md). 
+  **High availability**: Multi-node configurations provide better availability and performance distribution, with nodes spread across multiple Availability Zones. 
+  **Compactor optimization**: In multi-node deployments (3\+ nodes), the dedicated compactor node ensures write and read performance isn't impacted by background optimization tasks 



**Topics**
+ [Creating a DB cluster in Timestream](#creating-a-db-cluster)
+ [S3 VPC Endpoint for Private Clusters](s3-vpc-endpoint-private-clusters.md)
+ [Settings for DB clusters](#settings-for-db-clusters)
+ [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md)
+ [Core and Enterprise versions](core-and-enterprise-versions.md)
+ [Deployment models](deployment-models.md)
+ [Endpoints and connectivity](endpoints-and-connectivity.md)