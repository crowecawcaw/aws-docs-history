For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Create a cluster in Timestream for InfluxDB 3

Creating a new InfluxDB 3 cluster in Amazon Timestream involves selecting the appropriate version,
deployment model, and configuration settings to meet your workload requirements.

## Using the AWS Management Console

1. Sign in to the AWS Management Console and open the Timestream for InfluxDB console.
2. In the navigation pane, choose **InfluxDB Databases**.
3. Choose **Create InfluxDB database**.
4. For **Engine Version**, choose **InfluxDB 3** as your
   engine version
5. For **Edition**:
   - Choose **Core** for development, testing, or near real-time
     monitoring of recent data.
   - Choose **Enterprise** for production workloads requiring high
     availability, long-term storage, and compaction.

6. Configure Deployment (based on **Edition** selected).
   - For Core Edition:
     - Automatically configured as single-node deployment
     - No additional node configuration required

   - For Enterprise Edition:
     - Choose deployment configuration:
       - **Single-node**: One node handling writer, reader, and
         compactor roles
       - **3-node cluster**: 2 writer/reader nodes + 1 dedicated
         compactor node

     ###### Note

     Multi-node configurations beyond 3 nodes will be available in future releases via
     parameter group updates

7. Configure cluster settings
   - **DB cluster identifier**: Enter a unique name for your
     cluster.
   - **DB instance class**: Select from
     `db.influxIOIncluded` instance classes (applies to all nodes).
   - **Parameter group**:
     - Select a service-defined parameter group:
       - InfluxDBv3Core (for Core single-node)
       - InfluxDBv3Enterprise (for Enterprise 3-node)
       - InfluxDBv3Enterprise1Node (for Enterprise single-node)

     - Or create/select a custom parameter group

8. Configure network settings
   - **Virtual Private Cloud (VPC)**: Select your VPC.
   - **DB subnet group**: Choose subnets across availability zones.
   - **VPC security groups**: Select security groups for network
     access control.
   - Public accessibility:
     - **Yes**: Cluster accessible from internet (with proper
       security group rules).
     - **No**: Cluster only accessible within VPC.

   ###### Note

   **Important:** When creating a private Timestream for InfluxDB 3 cluster, ensure your S3 VPC endpoint policy allows full access. The cluster creation will fail if the S3 endpoint has restrictive policies.

9. (Optional) Configure additional settings 
   - **Log exports**: Enable export to CloudWatch Logs.
   - **Maintenance window**: Set preferred maintenance schedule.
   - **Backup retention period**: Configure automated backup
     retention.
   - **Tags**: Add metadata tags for organization and billing.

10. Review and create
    - Review all configuration settings.
    - Choose **Create InfluxDB database**.

The cluster creation process typically takes 10-20 minutes. The console will display the
status as "Creating" and change to "Available" when ready.

## Using the AWS CLI

Create an InfluxDB 3 Core cluster:

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-influxdb3-core-cluster" \
  --db-parameter-group-identifier "InfluxDBv3Core" \
  --db-instance-type db.influxIOIncluded.large \
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
  --db-instance-type db.influxIOIncluded.xlarge \
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
  --db-instance-type db.influxIOIncluded.large \
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
      "dataFusionNumThreads": 64
    }
  }'

# Then create the cluster using the custom parameter group
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-custom-enterprise-cluster" \
  --db-parameter-group-identifier "custom-enterprise-pg" \
  --db-instance-type db.influxIOIncluded.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc

```

## Post-creation steps

After your cluster is created and available:

1. **Retrieve endpoints:**

```
aws timestream-influxdb get-db-cluster
  --identifier "my-influxdb3-cluster-id"

```

2. **Obtain your operator token:**
   - Your operator token is stored in a secret in your AWS Secrets Manager account. The secret has the
     same name as your newly created cluster identifier.

3. (Optional) **Access InfluxDB explorer:**

###### Note

InfluxDB 3 Explorer is intended for **basic data exploration and administration with limited query support**. For performance testing or complex query constructions, please use the CLI or API instead

    * Download the InfluxDB Explorer from [https://docs.influxdata.com/influxdb3/explorer/](https://docs.influxdata.com/influxdb3/explorer/ "https://docs.influxdata.com/influxdb3/explorer/").
    * For public clusters: Run the Explorer from any location with internet access.
    * For private clusters: Run the Explorer from within the same VPC (using an EC2
     instance, bastion host, or through VPN connection).

4. **Verify connectivity:**

```
influxdb3 query \
  --host "your-cluster-endpoint:8086" \
  --database "my-bucket" \
  --token "your-token" \
  "SHOW TABLES"

```

**Important considerations:**

- **Edition Selection**: Core is suitable for development and
  short-term data; Enterprise is required for production workloads with long-term storage needs.
- **Node Configuration**: All nodes in a cluster share the same
  instance class and network configuration.
- **Parameter Groups**: Immutable once created; changes require
  creating a new parameter group.
- **Scaling**: Initial release supports 1-node and 3-node
  configurations; future updates will enable additional scaling options. At initial release you
  won’t be able to change your node count after creation.
- **High Availability**: 3-node Enterprise configurations provide
  better fault tolerance and performance distribution.
- **Compaction**: Enterprise edition's compaction capability is
  essential for maintaining performance over time.
