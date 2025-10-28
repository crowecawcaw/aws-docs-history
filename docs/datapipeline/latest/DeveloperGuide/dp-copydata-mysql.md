AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Export MySQL Data to Amazon S3 Using AWS Data Pipeline

This tutorial walks you through the process of creating a data pipeline to copy data
(rows) from a table in MySQL database to a CSV (comma-separated values) file in an Amazon S3
bucket and then sending an Amazon SNS notification after the copy activity completes successfully.
You will use an EC2 instance provided by AWS Data Pipeline for this copy activity.

###### Pipeline Objects

The pipeline uses the following objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")
- [MySqlDataNode](dp-object-mysqldatanode.md "dp-object-mysqldatanode.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
- [SnsAlarm](dp-object-snsalarm.md "dp-object-snsalarm.md")

###### Contents

- [Before You Begin](dp-copydata-mysql-prereq.md "dp-copydata-mysql-prereq.md")
- [Copy MySQL Data Using the Command Line](dp-copymysql-cli.md "dp-copymysql-cli.md")
