

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Create a cluster in Timestream for InfluxDB 3
<a name="creating-a-cluster"></a>

 Creating a new InfluxDB 3 cluster in Amazon Timestream involves selecting the appropriate version, deployment model, and configuration settings to meet your workload requirements. 

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the AWS Management Console and open the Timestream for InfluxDB console. 

1.  In the navigation pane, choose **InfluxDB Databases**. 

1.  Choose **Create InfluxDB database**. 

1.  For **Engine Version**, choose **InfluxDB 3** as your engine version 

1.  For **Edition**: 
   +  Choose **Core** for development, testing, or near real-time monitoring of recent data. 
   +  Choose **Enterprise** for production workloads requiring high availability, long-term storage, and compaction. 

1.  Configure Deployment (based on **Edition** selected). 
   + For Core Edition:
     +  Automatically configured as single-node deployment 
     +  No additional node configuration required 
   + For Enterprise Edition:
     +  Choose deployment configuration: 
       +  **Single-node**: One node handling writer, reader, and compactor roles 
       +  **3-node cluster**: 2 writer/reader nodes \+ 1 dedicated compactor node 
       +  **Multi-node cluster (up to 15 nodes)**: Configure via custom parameter group with: 
         +  1-4 writer/reader nodes (ingestQueryInstances) 
         +  0-13 reader-only nodes (queryOnlyInstances) 
         +  1 dedicated compactor (required for clusters with 3\+ nodes) 
**Note**  
To create a multi-node cluster with more than 3 nodes, you must first create a custom parameter group with your desired node configuration, then create the cluster using that parameter group.

1.  Configure cluster settings 
   +  **DB cluster identifier**: Enter a unique name for your cluster. 
   +  **DB instance class**: Select from `db.influx` instance classes (applies to all nodes). 
   +  **Parameter group**: 
     +  Select a service-defined parameter group: 
       +  InfluxDBv3Core (for Core single-node) 
       +  InfluxDBv3Enterprise (for Enterprise 3-node) 
       +  InfluxDBv3Enterprise1Node (for Enterprise single-node) 
     +  Or create/select a custom parameter group for multi-node configurations 

1.  Configure network settings 
   +  **Virtual Private Cloud (VPC)**: Select your VPC. 
   +  **DB subnet group**: Choose subnets across availability zones. 
   +  **VPC security groups**: Select security groups for network access control. 
   +  Public accessibility: 
     +  **Yes**: Cluster accessible from internet (with proper security group rules). 
     +  **No**: Cluster only accessible within VPC. 
**Note**  
Shared VPCs are not currently supported for Timestream for InfluxDB 3.
**Note**  
For multi-node clusters, nodes are automatically distributed across multiple Availability Zones for high availability.

1.  (Optional) Configure additional settings  
   +  **Tags**: Add metadata tags for organization and billing. 

1.  Review and create 
   +  Review all configuration settings. 
   +  Choose **Create InfluxDB database**. 

 The cluster creation process typically takes 10-20 minutes. The console will display the status as "Creating" and change to "Available" when ready. 

## Using the AWS CLI
<a name="using-the-aws-cli"></a>

Create an InfluxDB 3 Core cluster:

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-influxdb3-core-cluster" \
  --db-parameter-group-identifier "InfluxDBv3Core" \
  --db-instance-type db.influx.large \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --publicly-accessible false
```

Create an InfluxDB 3 Enterprise cluster (3-node):

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-influxdb3-enterprise-cluster" \
  --db-parameter-group-identifier "InfluxDBv3Enterprise" \
  --db-instance-type db.influx.xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --publicly-accessible false \
  --log-delivery-configuration '{
    "s3Configuration": {
      "bucketName": "my-influxdb-logs",
      "enabled": true
    }
  }'
```

 Create an InfluxDB 3 Enterprise cluster (single-node):

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-influxdb3-enterprise-single" \
  --db-parameter-group-identifier "InfluxDBv3Enterprise1Node" \
  --db-instance-type db.influx.large \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --publicly-accessible false
```

 Create a cluster with a custom parameter group:

```
# First, create a custom parameter group
aws timestream-influxdb create-db-parameter-group \
  --name "custom-enterprise-pg" \
  --engine-type "InfluxDBv3Enterprise" \
  --parameters '{
    "InfluxDBv3Enterprise": {
      "ingestQueryInstances": 2,
      "queryOnlyInstances": 0,
      "dedicatedCompactor": true,
      "bufferMemLimitMb": 32768,
      "dataFusionNumThreads": 8
    }
  }'

# Then create the cluster using the parameter group identifier
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-custom-enterprise-cluster" \
  --db-parameter-group-identifier "<parameter-group-identifier>" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc
```

**Note**  
The `--db-parameter-group-identifier` requires the parameter group identifier (not the name). Set `dataFusionNumThreads` to match the number of vCPUs for your instance type (for example, 8 for `db.influx.2xlarge`). For a complete guide on parameter configuration, see [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md).

Create a multi-node cluster (up to 15 nodes) with a custom parameter group:

```
# First, create a custom parameter group with your desired node configuration
aws timestream-influxdb create-db-parameter-group \
  --name "custom-multinode-pg" \
  --engine-type "InfluxDBv3Enterprise" \
  --parameters '{
    "InfluxDBv3Enterprise": {
      "ingestQueryInstances": 4,
      "queryOnlyInstances": 10,
      "dedicatedCompactor": true,
      "bufferMemLimitMb": 32768,
      "dataFusionNumThreads": 8
    }
  }'

# Then create the cluster using the parameter group identifier
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-multinode-enterprise-cluster" \
  --db-parameter-group-identifier "<parameter-group-identifier>" \
  --db-instance-type db.influxIOIncluded.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc
```

## Post-creation steps
<a name="post-creation-steps"></a>

 After your cluster is created and available: 

1.  **Retrieve endpoints:** 

   ```
   aws timestream-influxdb get-db-cluster \
     --identifier "my-influxdb3-cluster-id"
   ```

   For multi-node clusters, you will receive:
   +  **Cluster read/write endpoint**: Distributes traffic to writer/reader nodes 
   +  **Cluster read-only endpoint**: Distributes traffic to all nodes capable of read operations. This endpoint is only created when at least one reader-only node is present in the cluster. If your cluster has no reader-only nodes, the read-only endpoint will not be available. 
   +  **Node endpoints**: Direct access to specific nodes for workload isolation 

1.  **Obtain your operator token:** 
   + Your operator token is stored in a secret in your AWS Secrets Manager account. The secret has the same name as your newly created cluster identifier. 

1.  (Optional) **Access InfluxDB explorer:** 
   +  Download the InfluxDB Explorer from [https://docs.influxdata.com/influxdb3/explorer/](https://docs.influxdata.com/influxdb3/explorer/). 
   +  For public clusters: Run the Explorer from any location with internet access. 
   +  For private clusters: Run the Explorer from within the same VPC (using an EC2 instance, bastion host, or through VPN connection). 

1.  **Verify connectivity:** 

   ```
   influxdb3 query \
     --host "your-cluster-endpoint:8086" \
     --database "my-database" \
     --token "my-token" \
     "SHOW TABLES"
   ```

 **Please refer to [InfluxDB 3 documentation](https://docs.influxdata.com/influxdb3/enterprise/) to find information on [writing data](https://docs.influxdata.com/influxdb3/enterprise/write-data/), [executing queriers](https://docs.influxdata.com/influxdb3/enterprise/query-data/), or [Administer](https://docs.influxdata.com/influxdb3/enterprise/admin/) your influxDB 3 Database.** 

 **Important considerations:** 
+  **Edition Selection**: Core is suitable for development and short-term data; Enterprise is required for production workloads with long-term storage needs. 
+  **Node Configuration**: All nodes in a cluster share the same instance class and network configuration. 
+  **Parameter Groups**: Immutable once created; changes require creating a new parameter group. 
+  **Scaling**: Initial release supports 1-node and 3-node configurations; future updates will enable additional scaling options. At initial release you won’t be able to change your node count after creation. 
+  **High Availability**: 3-node Enterprise configurations provide better fault tolerance and performance distribution. 
+  **Compaction**: Enterprise edition's compaction capability is essential for maintaining performance over time. 