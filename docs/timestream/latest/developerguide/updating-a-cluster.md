For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Update a cluster in Timestream for InfluxDB 3

After your cluster is created, you can modify certain configuration parameters to adapt to
changing workload requirements in Amazon Timestream. Note that some modifications may cause temporary
downtime during the update process.

## Update a cluster using the

AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon Timestream for InfluxDB console.
2. In the navigation pane, choose **InfluxDB Databases**.
3. Select the cluster you want to modify.
4. Choose  **Modify**.
5. Update available settings:
   - **Instance class**: Scale compute resources up or down (applies
     to all nodes in the cluster and requires cluster restart).
   - **Parameter group**: Associate a different parameter group
     (requires cluster restart).
   - **Log delivery configuration**: Enable or modify CloudWatch Logs export.

6. Choose **Continue** and review your changes.
7. Select when to apply changes:
   - **Apply immediately**: Changes are applied right away (may
     cause brief downtime).

8. Choose **Modify cluster**.

## Update a cluster using the AWS CLI

To update an existing cluster using the AWS CLI:

```
aws timestream-influxdb update-db-cluster \
  --region us-east-1 \
  --identifier "my-influxdb3-cluster" \
  --db-instance-type db.influxIOIncluded.2xlarge \
  --db-parameter-group-identifier "new-parameter-group" \
  --apply-immediately

```

## Considerations when updating a

cluster

**Modifiable parameters**

The following parameters can be modified after cluster creation:

| **Parameter**       | **Description**                           | **Impact**                        |
| ------------------- | ----------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance class**  | Scale compute/memory resources up or down | Requires rolling restart of nodes |
| **Parameter group** | Change database engine configuration      | Requires cluster restart          |
| **Log delivery**    | Configure CloudWatch Logs export          | Applied immediately               | **Non-modifiable parameters** The following parameters **cannot** be modified after cluster creation: <br>• **VPC and Subnets**: Network location is fixed. <br>• **Security Groups**: Network access controls cannot be changed. <br>• **Public Accessibility**: Internet accessibility setting is permanent. <br>• **DB Cluster Identifier**: Cluster name cannot be changed. <br>• **Edition**: Cannot change between Core and Enterprise. Downtime impact: <br>• Instance class changes: Rolling restart (minimal downtime with multi-node clusters). <br>• Parameter group changes: Full cluster restart required. <br>• Log configuration changes: No downtime. Best practices: <br>• **Plan network configuration carefully** before cluster creation as it cannot be changed. <br>• **Test changes** in non-production environments first. <br>• **Monitor metrics** during and after updates to verify performance. <br>• **Use cluster endpoints** to ensure transparent failover during rolling updates. <br>• **Avoid node-specific endpoints** during update operations. Validation: <br>• The system validates all changes before applying them. <br>• Invalid configurations are rejected with descriptive error messages. <br>• Some parameter combinations may not be compatible. Rollback: <br>• Keep previous parameter group configurations for easy rollback. <br>• Document current settings before making changes. <br>• For critical changes, create cluster snapshots before updating. **Monitor update progress** Track the update status through: 1. **Console**: The cluster status shows "Modifying" during updates. 2. **CLI**: Query cluster status: `aws timestream-influxdb describe-db-cluster \ --identifier "my-influxdb3-cluster"` The possible status for a cluster are: <br>• `CREATING` <br>• `UPDATING` <br>• `DELETING` <br>• `AVAILABLE` <br>• `FAILED` <br>• `DELETED` <br>• `UPDATING_INSTANCE_TYPE` <br>• `PARTIALLY_AVAILABLE` (Applicable only only multi-node cluster when some nodes are still being created) 3. **CloudWatch Metrics**: Monitor performance metrics during updates. **Limitations** Current limitations for cluster updates: <br>• Cannot modify VPC, subnets, security groups, or public accessibility after creation. <br>• Cannot change from Core to Enterprise edition (or vice versa). <br>• Cannot rename the cluster (DB cluster identifier is immutable). <br>• All nodes must use the same instance class. <br>• Parameter groups are immutable (must create new ones for changes). By understanding these update capabilities and limitations, you can effectively manage and scale your InfluxDB 3 clusters to meet evolving workload requirements while planning appropriately for settings that must be configured at cluster creation time. |
