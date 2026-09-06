

# Managing log retention
<a name="deleting-log-files-lifecycle"></a>

An Amazon S3 bucket with server access logging enabled can accumulate many server log objects over time. You can use Amazon S3 Lifecycle configuration to set rules so that Amazon S3 automatically deletes log objects after a specified period. If you specified a prefix in your logging configuration, you can scope the lifecycle rule to that prefix. For example, if your log objects have the prefix `logs/`, you can create a lifecycle rule to delete all objects with that prefix after a specified number of days. For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md).

For logs delivered to CloudWatch Logs, see [Managing log retention](sal-cw-retention.md).