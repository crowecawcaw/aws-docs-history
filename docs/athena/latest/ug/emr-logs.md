

# Query Amazon EMR logs
<a name="emr-logs"></a>

Amazon EMR and big data applications that run on Amazon EMR produce log files. Log files are written to the [primary node](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html), and you can also configure Amazon EMR to archive log files to Amazon S3 automatically. You can use Amazon Athena to query these logs to identify events and trends for applications and clusters. For more information about the types of log files in Amazon EMR and saving them to Amazon S3, see [View log files](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html) in the *Amazon EMR Management Guide*.

**Topics**
+ [Create and query a basic table based on Amazon EMR log files](emr-create-table.md)
+ [Create and query a partitioned table based on Amazon EMR logs](emr-create-table-partitioned.md)