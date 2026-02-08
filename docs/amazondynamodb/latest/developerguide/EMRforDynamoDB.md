# Performance tuning

When you create a Hive external table that maps to a DynamoDB table, you do not consume
any read or write capacity from DynamoDB. However, read and write activity on the Hive
table (such as `INSERT` or `SELECT`) translates directly into read
and write operations on the underlying DynamoDB table.

Apache Hive on Amazon EMR implements its own logic for balancing the I/O load on the DynamoDB
table and seeks to minimize the possibility of exceeding the table's provisioned
throughput. At the end of each Hive query, Amazon EMR returns runtime metrics, including the
number of times your provisioned throughput was exceeded. You can use this information,
together with CloudWatch metrics on your DynamoDB table, to improve performance in subsequent
requests.

The Amazon EMR console provides basic monitoring tools for your cluster. For more
information, see [View and Monitor a Cluster](../../../ElasticMapReduce/latest/ManagementGuide/emr-manage-view.md "../../../ElasticMapReduce/latest/ManagementGuide/emr-manage-view.md") in the _Amazon EMR Management
Guide_.

You can also monitor your cluster and Hadoop jobs using web-based tools, such as Hue,
Ganglia, and the Hadoop web interface. For more information, see [View Web Interfaces Hosted on Amazon EMR Clusters](../../../ElasticMapReduce/latest/ManagementGuide/emr-web-interfaces.md "../../../ElasticMapReduce/latest/ManagementGuide/emr-web-interfaces.md") in the _Amazon EMR
Management Guide_.

This section describes steps you can take to performance-tune Hive operations on
external DynamoDB tables.

###### Topics

- [DynamoDB provisioned
  throughput](EMRforDynamoDB.PerformanceTuning.md "EMRforDynamoDB.PerformanceTuning.md")
- [Adjusting the
  mappers](EMRforDynamoDB.PerformanceTuning.md "EMRforDynamoDB.PerformanceTuning.md")
- [Additional topics](EMRforDynamoDB.PerformanceTuning.md "EMRforDynamoDB.PerformanceTuning.md")
