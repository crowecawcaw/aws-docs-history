For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Delete a cluster in Timestream for InfluxDB 3

When you no longer need a cluster in Amazon Timestream, you can delete it to avoid incurring
additional charges. 

###### Important

Deletion permanently removes all data, so ensure you have exported any critical data before
proceeding.

## Delete a cluster using the

AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon Timestream for InfluxDB console.
2. In the navigation pane, choose **InfluxDB Databases**.
3. Select the cluster you want to delete.
4. Choose **Delete** from the Actions menu.
5. In the confirmation dialog box, confirm the deletion and acknowledge that all data will
   be permanently deleted.
6. Choose **Delete**.

The deletion process typically takes five to ten minutes. The cluster status will show
"Deleting" and will be removed from the list once deletion is complete.

## Delete a cluster using the AWS CLI

To delete a cluster using the AWS CLI:

```
aws timestream-influxdb delete-db-cluster \
  --region us-east-1 \
  --identifier "my-influxdb3-cluster"

```

## Considerations when deleting a cluster

Data loss warning:

- **Permanent deletion**: All data is permanently removed with no
  recovery option.
- **Manual backup required**: Export critical data using InfluxDB
  tools before deletion.
- **No built-in snapshot**: The service does not currently provide
  snapshot capabilities.

**No built-in customer-managed snapshot**: The service does
not currently provide customer-managed snapshot capabilities. The service level snapshot is
built with disaster recovery in mind and is kept for 24 hours.

What gets deleted:

- All cluster nodes (writer, reader, and compactor nodes).
- All data stored in InfluxDB Object Storage (Amazon S3).
- Cluster endpoints and DNS entries.

What is retained:

- Database logs exported to Amazon S3 (if configured).
- Parameter groups (not automatically deleted).
- VPC security groups (not automatically deleted).

Dependencies to Check:

- **Active connections**: Ensure no applications are actively using
  the cluster.
- **Scheduled jobs**: Disable any scheduled data ingestion or query
  jobs.
- **Monitoring**: Update or remove CloudWatch alarms associated with the
  cluster.
- **Documentation**: Update any documentation referencing the
  cluster endpoints.

Pre-deletion checklist:

**Critical**: Before deleting your InfluxDB 3 cluster, manually
export all important data:

1. **Export critical data:** Use the following query to export data
   to JSON format. For more information, see [Output format](https://docs.influxdata.com/influxdb3/core/query-data/execute-queries/influxdb3-cli/?section=influxdb3%252Fcore%252Fquery-data#output-format "https://docs.influxdata.com/influxdb3/core/query-data/execute-queries/influxdb3-cli/?section=influxdb3%252Fcore%252Fquery-data#output-format") for the `influxdb3 query` command in the _Influx
   DB 3 documentation_.

```
influxdb3 query \
  --token AUTH_TOKEN \
  --database DATABASE_NAME \
  --format json \
  "SELECT * FROM home WHERE time >= '2025-06-26T08:00:00Z' LIMIT 5

```

2. **Document cluster configuration:**

```
aws timestream-influxdb describe-db-cluster \
  --identifier "my-influxdb3-cluster" > cluster-config-backup.json

```

3. **Save parameter group configuration:**

```
aws timestream-influxdb describe-db-parameter-group \
  --identifier "your-parameter-group-id" > parameter-group-backup.json

```

4. **Check for active connections**
   - Review CloudWatch metrics for active connections.
   - Verify no critical applications are using the cluster.

Billing implications:

- **Immediate cessation**: Compute charges stop once deletion
  begins.
- **Storage charges**: Object storage charges stop after data is
  deleted.
- **Minimum billing**: No minimum billing period applies for
  deletion.

Recovery options after deletion:

- **No automatic recovery**: Deleted clusters and data cannot be
  recovered.
- **Manual restoration only**: You must recreate the cluster and
  reimport data from manual backups.
- **Same name reuse**: The cluster identifier cannot be reused
  after deletion is complete.

The following table covers some common deletion issues and solutions:

| **Issue**             | **Solution**                                         |
| --------------------- | ---------------------------------------------------- |
| Deletion fails        | Check for dependent resources or AWS service issues. |
| Slow deletion         | Large clusters may extend deletion time.             |
| Cannot delete         | Ensure you have proper IAM permissions.              |
| Need to preserve data | Must export data manually before deletion.           |

### Best Practices for deleting a cluster

- **Always export critical data** before deletion.
- **Test data export and reimport process** before deleting
  production clusters.
- **Create comprehensive backups** including schema, data, and
  configuration.
- **Document deletion** for audit and compliance purposes.
- **Coordinate with teams** before deleting shared resources.
- **Verify deletion completion** before removing related
  resources.
