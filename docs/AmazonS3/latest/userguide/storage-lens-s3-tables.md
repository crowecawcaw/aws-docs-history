

# Working with S3 Storage Lens data in S3 Tables
<a name="storage-lens-s3-tables"></a>

Amazon S3 Storage Lens can export your storage analytics and insights to S3 Tables, enabling you to query your Storage Lens metrics using SQL with AWS analytics services like Amazon Athena, Amazon EMR, Amazon SageMaker Studio (SMStudio), and other AWS analytics tools. When you configure S3 Storage Lens to export to S3 Tables, your metrics are automatically stored in read-only Apache Iceberg tables in the AWS-managed `aws-s3` table bucket.

This integration provides structured data access for querying Storage Lens metrics using standard SQL, analytics integration with AWS analytics services, historical analysis capabilities, and cost optimization with no additional charges for exporting to AWS-managed S3 Tables.

**Topics**
+ [Exporting S3 Storage Lens metrics to S3 Tables](storage-lens-s3-tables-export.md)
+ [Table naming for S3 Storage Lens export to S3 Tables](storage-lens-s3-tables-naming.md)
+ [Understanding S3 Storage Lens table schemas](storage-lens-s3-tables-schemas.md)
+ [Permissions for S3 Storage Lens tables](storage-lens-s3-tables-permissions.md)
+ [Querying S3 Storage Lens data with analytics tools](storage-lens-s3-tables-querying.md)
+ [Using AI assistants with S3 Storage Lens tables](storage-lens-s3-tables-ai-tools.md)