# Table buckets

Amazon S3 table buckets are an S3 bucket type that you can use to create and store tables as
S3 resources. Table buckets are used to store tabular data and metadata as objects for use
in analytics workloads. S3 performs maintenance in your table buckets automatically to
help reduce your table storage costs. For more information, see [S3 Tables maintenance](s3-tables-maintenance-overview.md "s3-tables-maintenance-overview.md").

To interact with the tables stored inside your table buckets, you can integrate your table buckets with analytics applications that support [Apache Iceberg](https://iceberg.apache.org/docs/latest/ "https://iceberg.apache.org/docs/latest/"). Table buckets integrate with AWS analytics services through the AWS Glue Data Catalog. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md"). You can also interact with your tables using open-source query engines using the Amazon S3 Tables Catalog for Apache Iceberg. For more information, see [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").

Each table bucket has a unique Amazon Resource Name (ARN) and resource policy attached to it. Table bucket ARNs follow this format:

```
arn:aws:s3tables:`Region`:`OwnerAccountID`:bucket/`bucket-name`
```

All table buckets and tables are private and can't be made public. These resources can only be accessed by users who are
explicitly granted access. To grant access, you can
use IAM resource-based policies for table buckets and tables, and IAM identity-based
policies for users and roles.

By default, you can create up to 10 table buckets per AWS Region in an AWS account.
To request a quota increase for table buckets or tables, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

## Types of table buckets

Amazon S3 supports the following types of table buckets:

**Customer-managed table buckets**

Customer-managed table buckets are resources for storing Amazon S3 Tables created and managed by customers. You create these buckets explicitly, choose their names, and maintain full control over the tables and namespaces within them. For customer-managed table buckets, you can create, delete, set custom default encryption, or configure maintenance options as needed.

**AWS managed table buckets**

AWS managed table buckets are AWS managed resources that automatically store tables created by AWS services, such as the live inventory and journal tables created by S3 Metadata. These buckets provide a centralized location for all system-generated tables. These buckets follow a standard naming convention, use a standard namespace for all tables, and have preset maintenance and default encryption configurations which S3 modifies on your behalf. You have read-only access to query the data, while AWS handles all table creation, updates, and maintenance operations. For more information, see [Working with AWS managed table buckets](s3-tables-aws-managed-buckets.md "s3-tables-aws-managed-buckets.md").

There are several types of Amazon S3 buckets. Before creating a bucket, make sure that you choose the bucket type that best fits your application and performance requirements. For more information about the various bucket types and the appropriate use cases for each, see [Buckets](Welcome.md#BasicsBucket "Welcome.md#BasicsBucket").

###### Topics

- [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md")
- [Creating a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md")
- [Deleting a table bucket](s3-tables-buckets-delete.md "s3-tables-buckets-delete.md")
- [Viewing details about an Amazon S3 table bucket](s3-tables-buckets-details.md "s3-tables-buckets-details.md")
- [Managing table bucket policies](s3-tables-bucket-policy.md "s3-tables-bucket-policy.md")
- [Working with AWS managed table buckets](s3-tables-aws-managed-buckets.md "s3-tables-aws-managed-buckets.md")
- [Using tags with S3 table buckets](table-bucket-tagging.md "table-bucket-tagging.md")
