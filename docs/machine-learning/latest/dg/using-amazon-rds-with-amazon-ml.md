We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Using Data from an Amazon RDS Database to Create an

Amazon ML Datasource

Amazon ML allows you to create a datasource object from data stored in a MySQL database in
Amazon Relational Database Service (Amazon RDS). When you perform this action, Amazon ML creates an AWS Data Pipeline object that
executes the SQL query that you specify, and places the output into an S3 bucket of your choice.
Amazon ML uses that data to create the datasource.

###### Note

Amazon ML supports only MySQL databases in VPCs.

Before Amazon ML can read your input data, you must export that data to Amazon Simple Storage Service (Amazon S3). You can
set up Amazon ML to perform the export for you by using the API. (RDS is limited to the API, and is
not available from the console.)

In order for Amazon ML to connect to your MySQL database in Amazon RDS and read data on your behalf,
you need to provide the following:

- The RDS DB instance identifier
- The MySQL database name
- The AWS Identity and Access Management (IAM) role that is used to create, activate, and execute the data
  pipeline
- The database user credentials:
  - User name
  - Password

- The AWS Data Pipeline security information:
  - The IAM resource role
  - The IAM service role

- The Amazon RDS security information:
  - The subnet ID
  - The security group IDs

- The SQL query that specifies the data that you want to use to create the datasource
- The S3 output location (bucket) used to store the results of the query
- (Optional) The location of the data schema file
  Additionally, you need to ensure that the IAM users or roles that create Amazon RDS datasources
  by using the [CreateDataSourceFromRDS](../APIReference/API_CreateDataSourceFromRDS.md "../APIReference/API_CreateDataSourceFromRDS.md") operation have the `iam:PassRole` permission. For
  more information, see [Controlling Access to
  Amazon ML Resources -with IAM](controlling-access-to-amazon-ml-resources-by-using-iam.md "controlling-access-to-amazon-ml-resources-by-using-iam.md").

###### Topics

- [RDS Database Instance Identifier](#rds-database-instance-identifier "#rds-database-instance-identifier")
- [MySQL Database Name](#mysql-database-name "#mysql-database-name")
- [Database User Credentials](#database-user-credentials "#database-user-credentials")
- [AWS Data Pipeline Security Information](#aws-data-pipeline-security-information "#aws-data-pipeline-security-information")
- [Amazon RDS Security Information](#amazon-rds-security-information "#amazon-rds-security-information")
- [MySQL SQL Query](#mysql-sql-query "#mysql-sql-query")
- [S3 Output Location](#s3-output-location-1 "#s3-output-location-1")

## RDS Database Instance Identifier

The RDS DB instance identifier is a unique name that you supply that identifies the
database instance that Amazon ML should use when interacting with Amazon RDS. You can find the RDS DB
instance identifier in the Amazon RDS console.

## MySQL Database Name

MySQL Database Name specifies the name of the MySQL database in the RDS DB instance.

## Database User Credentials

To connect to the RDS DB instance, you must supply the user name and password of the
database user who has sufficient permissions to execute the SQL query that you provide.

## AWS Data Pipeline Security Information

To enable secure AWS Data Pipeline access, you must provide the names of the IAM
resource role and the IAM service role.

An EC2 instance assumes the resource role to copy data from Amazon RDS to Amazon S3. The easiest way
to create this resource role is by using the `DataPipelineDefaultResourceRole`
template, and listing `machinelearning.aws.com` as a trusted service. For
more information about the template, see [Setting Up IAM roles](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md") in the _AWS Data Pipeline Developer Guide_.

If you create your own role, it must have the following contents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "machinelearning.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": { "aws:SourceAccount": "`123456789012`" },
 "ArnLike": { "aws:SourceArn": "arn:aws:machinelearning:us-east-1:`123456789012`:datasource/*" }
 }
 }]
}`

```

AWS Data Pipeline assumes the service role to monitor the progress of copying data from
Amazon RDS to Amazon S3. The easiest way to create this resource role is by using the
`DataPipelineDefaultRole` template, and listing
`machinelearning.aws.com` as a trusted service. For more information about the
template, see [Setting Up IAM roles](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md") in the _AWS Data Pipeline Developer Guide_.

## Amazon RDS Security Information

To enable secure Amazon RDS access, you need to provide the `VPC Subnet ID` and
`RDS Security Group IDs`. You also need to set up appropriate ingress rules for
the VPC subnet that is pointed at by the `Subnet ID` parameter, and provide the ID
of the security group that has this permission.

## MySQL SQL Query

The `MySQL SQL Query` parameter specifies the SQL SELECT query that you want
to execute on your MySQL database. The results of the query is copied to the S3 output
location (bucket) that you specify.

###### Note

Machine learning technology works best when input records are presented in random order
(shuffled). You can easily shuffle the results of your MySQL SQL query by using the
`rand()` function. For example, let's say that this is the original query:

"SELECT col1, col2, … FROM training_table"

You can add random shuffling by updating the query like this:

"SELECT col1, col2, … FROM training_table ORDER BY rand()"

## S3 Output Location

The `S3 Output Location` parameter specifies the name of the
"staging" Amazon S3 location where the results of the MySQL SQL query is output.

###### Note

You need to ensure that Amazon ML has permissions to read data from this location once the
data is exported from Amazon RDS. For information about setting these permissions, see Granting
Amazon ML Permissions to Read Your Data from Amazon S3 .
