AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Full copy of Amazon RDS MySQL table to Amazon Redshift

The **Full copy of Amazon RDS MySQL table to Amazon Redshift** template
copies the entire Amazon RDS MySQL table to an Amazon Redshift table by staging data in an Amazon S3
folder. The Amazon S3 staging folder must be in the same region as the Amazon Redshift cluster.
An Amazon Redshift table is created with the same schema as the source Amazon RDS MySQL table if
it does not already exist. Please provide any Amazon RDS MySQL to Amazon Redshift column data
type overrides you would like to apply during Amazon Redshift table creation.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [RedshiftCopyActivity](dp-object-redshiftcopyactivity.md "dp-object-redshiftcopyactivity.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
- [SqlDataNode](dp-object-sqldatanode.md "dp-object-sqldatanode.md")
- [RedshiftDataNode](dp-object-redshiftdatanode.md "dp-object-redshiftdatanode.md")
- [RedshiftDatabase](dp-object-redshiftdatabase.md "dp-object-redshiftdatabase.md")
