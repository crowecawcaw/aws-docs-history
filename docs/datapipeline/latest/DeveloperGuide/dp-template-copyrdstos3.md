AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Full copy of Amazon RDS MySQL Table to Amazon S3

The **Full Copy of RDS MySQL Table to S3** template copies an
entire Amazon RDS MySQL table and stores the output in an Amazon S3 location. The output
is stored as a CSV file in a timestamped subfolder under the specified Amazon S3
location.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")
- [SqlDataNode](dp-object-sqldatanode.md "dp-object-sqldatanode.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
