# Schedule a crawler to keep the AWS Glue Data Catalog and Amazon S3 in sync

AWS Glue crawlers can be set up to run on a schedule or on demand. For more information,
see [Time-based schedules for jobs and crawlers](../../../glue/latest/dg/monitor-data-warehouse-schedule.md "../../../glue/latest/dg/monitor-data-warehouse-schedule.md") in the _AWS Glue Developer
Guide_.

If you have data that arrives for a partitioned table at a fixed time, you can set up
an AWS Glue crawler to run on schedule to detect and update table partitions. This can
eliminate the need to run a potentially long and expensive `MSCK REPAIR`
command or manually run an `ALTER TABLE ADD PARTITION` command. For more
information, see [Table
partitions](../../../glue/latest/dg/tables-described.md#tables-partition "../../../glue/latest/dg/tables-described.md#tables-partition") in the _AWS Glue Developer Guide_.
