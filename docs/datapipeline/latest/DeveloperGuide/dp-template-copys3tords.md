AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Load S3 data into Amazon RDS MySQL table

The **Load S3 Data into RDS MySQL Table** template schedules
an Amazon EC2 instance to copy the CSV file from the Amazon S3 file path specified below
to an Amazon RDS MySQL table. The CSV file should not have a header row. The template
updates existing entries in the Amazon RDS MySQL table with those in the Amazon S3 data
and adds new entries from the Amazon S3 data to the Amazon RDS MySQL table. You can load
the data into an existing table or provide an SQL query to create a new
table.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")
- [SqlDataNode](dp-object-sqldatanode.md "dp-object-sqldatanode.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
