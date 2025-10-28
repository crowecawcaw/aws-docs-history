# DataBrew dependency on other AWS services

To work with the DataBrew console, you need a minimum set of permissions to work with the
DataBrew resources for your AWS account. In addition to these DataBrew permissions, the
console requires permissions from the following services:

- CloudWatch Logs permissions to display logs.
- IAM permissions to list and pass roles.
- Amazon EC2 permissions to list VPCs, subnets, security groups, instances, and other
  objects. DataBrew uses these permissions to set up Amazon EC2 items such as VPCs when
  running DataBrew jobs.
- Amazon S3 permissions to list buckets and objects.
- AWS Glue permissions to read AWS Glue schema objects, such as databases, partitions, tables, and connections.
- AWS Lake Formation permissions to work with Lake Formation data lakes.
