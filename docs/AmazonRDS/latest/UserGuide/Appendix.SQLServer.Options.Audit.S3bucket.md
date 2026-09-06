

# Configuring an S3 bucket
<a name="Appendix.SQLServer.Options.Audit.S3bucket"></a>

The audit log files are automatically uploaded from the DB instance to your S3 bucket. The following restrictions apply to the S3 bucket that you use as a target for audit files: 
+ It must be in the same AWS Region and AWS account as the DB instance.
+ It must not be open to the public.
+ The bucket owner must also be the IAM role owner.
+ Your IAM role must have permissions for the customer-managed KMS key associated with the S3 bucket server-side encryption.

The target key that is used to store the data follows this naming schema: `{{amzn-s3-demo-bucket}}/key-prefix/instance-name/audit-name/node_file-name.ext` 

**Note**  
You set both the bucket name and the key prefix values with the (`S3_BUCKET_ARN`) option setting.

The schema is composed of the following elements:
+ **{{amzn-s3-demo-bucket}}** – The name of your S3 bucket.
+ **`key-prefix`** – The custom key prefix you want to use for audit logs.
+ **`instance-name`** – The name of your Amazon RDS instance.
+ **`audit-name`** – The name of the audit.
+ **`node`** – The identifier of the node that is the source of the audit logs (`node1` or `node2`). There is one node for a Single-AZ instance and two replication nodes for a Multi-AZ instance. These are not primary and secondary nodes, because the roles of primary and secondary change over time. Instead, the node identifier is a simple label. 
  + **`node1`** – The first replication node (Single-AZ has one node only).
  + **`node2`** – The second replication node (Multi-AZ has two nodes).
+ **`file-name`** – The target file name. The file name is taken as-is from SQL Server.
+ **`ext`** – The extension of the file (`zip` or `sqlaudit`):
  + **`zip`** – If compression is enabled (default).
  + **`sqlaudit`** – If compression is disabled.