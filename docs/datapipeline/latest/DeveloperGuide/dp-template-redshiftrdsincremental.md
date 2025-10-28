AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Incremental copy of an Amazon RDS MySQL table to

Amazon Redshift

The **Incremental copy of Amazon RDS MySQL table to Amazon Redshift**
template copies data from an Amazon RDS MySQL table to an Amazon Redshift table by staging data
in an Amazon S3 folder.

The Amazon S3 staging folder must be in the same region as the Amazon Redshift cluster.

AWS Data Pipeline uses a translation script to create an Amazon Redshift table with the same schema
as the source Amazon RDS MySQL table if it does not already exist. You must provide
any Amazon RDS MySQL to Amazon Redshift column data type overrides you would like to apply
during Amazon Redshift table creation.

This template copies changes that are made to the Amazon RDS MySQL table between
scheduled intervals, starting from the scheduled start time. Physical deletes to
the Amazon RDS MySQL table are not copied. You must provide the column name that
stores the last modified time value.

When you use the default template to create pipelines for incremental Amazon RDS
copy, an activity with the default name `RDSToS3CopyActivity` is
created. You can rename it.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [RedshiftCopyActivity](dp-object-redshiftcopyactivity.md "dp-object-redshiftcopyactivity.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
- [SqlDataNode](dp-object-sqldatanode.md "dp-object-sqldatanode.md")
- [RedshiftDataNode](dp-object-redshiftdatanode.md "dp-object-redshiftdatanode.md")
- [RedshiftDatabase](dp-object-redshiftdatabase.md "dp-object-redshiftdatabase.md")
