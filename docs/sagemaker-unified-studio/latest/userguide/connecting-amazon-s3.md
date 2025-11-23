# Connecting to Amazon S3

You can create a data connection to Amazon S3 when you need to directly access files stored
in Amazon S3 buckets from your notebooks. This connection is only required if you want to read or
write individual files (such as CSV, JSON, or Parquet files) directly from Amazon S3 storage. If
you are working with Data Catalog tables that are backed by Amazon S3, you do not need to create
a separate Amazon S3 connection, you can access those tables directly through the catalog.

Before connecting to Amazon S3, complete the one of the following prerequisite
options:

- [Prerequisite option 1 (recommended): Gain access using an access role](adding-existing-s3-data.md#adding-existing-s3-access-role "adding-existing-s3-data.md#adding-existing-s3-access-role")
- [Prerequisite option 2: Gain access using the project role](adding-existing-s3-data.md#adding-existing-s3-project-role "adding-existing-s3-data.md#adding-existing-s3-project-role")

###### To connect to Amazon S3

1. In the navigation pane, choose **Connections**.
2. Choose **Create connection**.
3. In the gallery that opens, select Amazon S3.
4. For **Name** enter a descriptive name for your connection.
5. Enter S3 URI - optional. If you do not specify an Amazon S3 URI, SageMaker Unified Studio
   will list all buckets accessible with the provided credential.
6. AWS region - enter the AWS region where the S3 bucket is located.
7. Access role ARN - optional - select an existing IAM role from the dropdown. You
   might need to contact your Administrator for configuring an access role if you are
   connecting to S3 bucket in an AWS account that is different from the AWS account
   where your SageMaker Unified Studio domain is hosted.
8. Choose **Create connection**.
9. If all validations pass, a new Amazon S3 connection will be created.
   After creating the connection, you can use it in your notebooks to read and write files
   directly from the specified S3 location. You can also all the buckets you connected to if
   you select Data on navigation pane and select S3 buckets tab.
