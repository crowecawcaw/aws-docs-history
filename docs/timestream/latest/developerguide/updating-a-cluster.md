

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Update a cluster in Timestream for InfluxDB 3
<a name="updating-a-cluster"></a>

 After your cluster is created, you can modify certain configuration parameters to adapt to changing workload requirements in Amazon Timestream. Note that some modifications may cause temporary downtime during the update process. 

## Update a cluster using the AWS Management Console
<a name="using-the-aws-management-console-1"></a>

1.  Sign in to the AWS Management Console and open the Amazon Timestream for InfluxDB console. 

1.  In the navigation pane, choose **InfluxDB Databases**. 

1.  Select the cluster you want to modify. 

1.  Choose  **Modify**. 

1.  Update available settings: 
   +  **Instance class**: Scale compute resources up or down (applies to all nodes in the cluster and requires cluster restart). 
   +  **Parameter group**: Associate a different parameter group to change engine configuration or cluster shape (requires cluster restart). 
   +  **Log delivery configuration**: Enable or modify CloudWatch Logs export. 
   +  **Edition**: Upgrade from Core to Enterprise (one-way). For details, see [Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md). 

1.  Choose **Continue** and review your changes. 

1.  Select when to apply changes: 
   +  **Apply immediately**: Changes are applied right away (may cause brief downtime). 

1.  Choose **Modify cluster**. 

## Update a cluster using the AWS CLI
<a name="using-the-aws-cli-1"></a>

Update instance type:

```
aws timestream-influxdb update-db-cluster \
  --region us-east-1 \
  --identifier "my-influxdb3-cluster" \
  --db-instance-type db.influxIOIncluded.2xlarge \
  --apply-immediately
```

Update parameter group (including cluster scaling):

To modify your cluster configuration—including scaling the number of nodes—create a new parameter group with your desired configuration and apply it to your cluster:

```
# Step 1: Create a new parameter group with desired node configuration
aws timestream-influxdb create-db-parameter-group \
  --name "scaled-enterprise-pg" \
  --parameters '{
    "InfluxDBv3Enterprise": {
      "ingestQueryInstances": 4,
      "queryOnlyInstances": 10,
      "dedicatedCompactor": true,
      "dataFusionNumThreads": 8,
      "bufferMemLimitMb": 32768
    }
  }'

# Step 2: Apply the new parameter group to your cluster using the parameter group identifier
aws timestream-influxdb update-db-cluster \
  --region us-east-1 \
  --identifier "my-influxdb3-cluster" \
  --db-parameter-group-identifier "<parameter-group-identifier>" \
  --apply-immediately
```

## Scaling your cluster (Enterprise edition)
<a name="scaling-your-cluster"></a>

For Enterprise edition clusters, you can scale your cluster size by applying a new parameter group with your desired node configuration. For detailed guidance, see [Scaling a cluster](multi-node-scaling.md).
+  **Scale up**: Add nodes by increasing ingestQueryInstances (up to 4) or queryOnlyInstances (up to 13) 
+  **Scale down**: Remove nodes by decreasing these values 
+  **Change node modes**: Adjust the ratio of writer/reader nodes to reader-only nodes 

 **Important**: Clusters with 3 or more nodes require a dedicated compactor (dedicatedCompactor: true). When scaling, nodes are automatically distributed across multiple Availability Zones for high availability. 

## Considerations when updating a cluster
<a name="updating-a-cluster-considerations"></a>

 **Modifiable parameters** 

 The following parameters can be modified after cluster creation: 


|  **Parameter**  |  **Description**  |  **Impact**  | 
| --- | --- | --- | 
|  Instance class  |  Scale compute/memory resources up or down  |  Requires rolling restart of nodes  | 
|  Parameter group  |  Change database engine configuration or cluster shape (node count and modes)  |  Requires cluster restart  | 
|  Log delivery  |  Configure CloudWatch Logs export  |  Applied immediately  | 
|  Edition  |  Upgrade from Core to Enterprise (one-way). See [Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md).  |  Requires cluster restart  | 

 **Non-modifiable parameters** 

 The following parameters **cannot** be modified after cluster creation: 
+  **VPC and Subnets**: Network location is fixed. 
+  **Security Groups**: Network access controls cannot be changed. 
+  **Public Accessibility**: Internet accessibility setting is permanent. 
+  **DB Cluster Identifier**: Cluster name cannot be changed. 

 Downtime impact: 
+  Instance class changes: Rolling restart (minimal downtime with multi-node clusters). 
+  Parameter group changes (including cluster scaling): Cluster restart required. For multi-node clusters using cluster endpoints, traffic is automatically redistributed to available nodes during the update process. 
+  Log configuration changes: No downtime. 

 Best practices: 
+  **Plan network configuration carefully** before cluster creation as it cannot be changed. 
+  **Test changes** in non-production environments first. 
+  **Monitor metrics** during and after updates to verify performance. 
+  **Use cluster endpoints** to ensure transparent failover during rolling updates and scaling operations. 
+  **Avoid node-specific endpoints** during update operations, as individual nodes may be restarted or replaced. 
+  **When scaling**, consider your workload patterns to determine the optimal ratio of writer/reader nodes to reader-only nodes. 

 Validation: 
+  The system validates all changes before applying them. 
+  Invalid configurations are rejected with descriptive error messages. 
+  Some parameter combinations may not be compatible (e.g., clusters with 3\+ nodes require a dedicated compactor). 

 Rollback: 
+  Keep previous parameter group configurations for easy rollback. 
+  Document current settings before making changes. 
+  For critical changes, create cluster snapshots before updating. 
+  To rollback a scaling operation, create a parameter group with your previous node configuration and apply it to the cluster. 

 **Monitor update progress** 

 Track the update status through: 

1.  **Console**: The cluster status shows "Modifying" during updates. 

1.  **CLI**: Query cluster status: 

   ```
   aws timestream-influxdb get-db-cluster \
     --identifier "my-influxdb3-cluster"
   ```

   The possible status for a cluster are:
   + `CREATING`
   + `UPDATING`
   + `DELETING`
   + `AVAILABLE`
   + `FAILED`
   + `DELETED`
   + `UPDATING_INSTANCE_TYPE`
   + `PARTIALLY_AVAILABLE` (Applicable only for multi-node clusters when some nodes are still being created or updated)

1.  **CloudWatch Metrics**: Monitor performance metrics during updates. 

 **Limitations** 

 Current limitations for cluster updates: 
+  Cannot modify VPC, subnets, security groups, or public accessibility after creation. 
+  Upgrading from Core to Enterprise is supported (one-way), but you cannot downgrade from Enterprise to Core. See [Upgrade from Core to Enterprise edition](upgrading-core-to-enterprise.md). 
+  Cannot rename the cluster (DB cluster identifier is immutable). 
+  All nodes must use the same instance class (except for the compactor). 
+  Parameter groups are immutable (must create new ones for changes). 
+  Cluster scaling operations (adding/removing nodes) require creating and applying a new parameter group. 

 By understanding these update capabilities and limitations, you can effectively manage and scale your InfluxDB 3 clusters to meet evolving workload requirements while planning appropriately for settings that must be configured at cluster creation time. 