AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Incremental copy of Amazon RDS MySQL table to

Amazon S3

The **Incremental Copy of RDS MySQL Table to S3** template
does an incremental copy of the data from an Amazon RDS MySQL table and stores the
output in an Amazon S3 location. The Amazon RDS MySQL table must have a Last Modified
column.

This template copies changes that are made to the table between scheduled
intervals starting from the scheduled start time. The schedule type is time series so if a copy was
scheduled for a certain hour, AWS Data Pipeline copies the table rows that have a Last
Modified time stamp that falls within the hour. Physical deletes to the table
are not copied. The output is written in a timestamped subfolder under the Amazon S3
location on every scheduled run.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")
- [SqlDataNode](dp-object-sqldatanode.md "dp-object-sqldatanode.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
