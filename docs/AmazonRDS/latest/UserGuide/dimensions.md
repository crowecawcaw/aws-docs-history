

# Amazon CloudWatch dimensions for Amazon RDS
<a name="dimensions"></a>

You can filter Amazon RDS metrics data by using any dimension in the following table.


|  Dimension  |  Filters the requested data for . . .  | 
| --- | --- | 
|  DBInstanceIdentifier  | A specific DB instance. | 
|  DatabaseClass  | All instances in a database class. For example, you can aggregate metrics for all instances that belong to the database class `db.r5.large`. | 
|  EngineName  | The identified engine name only. For example, you can aggregate metrics for all instances that have the engine name `postgres`. | 
|  SourceRegion  | The specified Region only. For example, you can aggregate metrics for all DB instances in the `us-east-1` Region. | 
|  DbInstanceIdentifier, VolumeName  | The metrics per-volume for a single instance.<br />RDS captures metrics for multiple storage volumes. | 

**Note**  
If you are using additional storage volumes, you can see aggregate storage metrics under the `DBInstanceIdentifier` dimension. To see per-volume storage metrics, use the `DbInstanceIdentifier, VolumeName` dimensions.

For Multi-AZ DB clusters, Amazon RDS publishes metrics for each DB instance in the cluster under the `DBInstanceIdentifier` dimension. Metrics aren't available under a DB cluster dimension such as `DBClusterIdentifier`.

To monitor a Multi-AZ DB cluster, view the metrics for each DB instance in the cluster. To create an alarm that evaluates all of the DB instances in the cluster, use a metric math expression. For an example, see [Tutorial: Creating an Amazon CloudWatch alarm for Multi-AZ DB cluster replica lag for Amazon RDS](multi-az-db-cluster-cloudwatch-alarm.md).