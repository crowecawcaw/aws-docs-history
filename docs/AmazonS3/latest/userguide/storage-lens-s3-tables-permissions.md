

# Permissions for S3 Storage Lens tables
<a name="storage-lens-s3-tables-permissions"></a>

To work with S3 Storage Lens data exported to S3 Tables, you need appropriate AWS Identity and Access Management (IAM) permissions. This topic covers the permissions required for exporting metrics and managing encryption.

## Permissions for metrics export to S3 Tables
<a name="storage-lens-s3-tables-permissions-export"></a>

To create and work with S3 Storage Lens tables and table buckets, you must have certain `s3tables` permissions. At a minimum, to configure S3 Storage Lens to S3 Tables, you must have the following `s3tables` permissions:
+  `s3tables:CreateTableBucket` – This permission allows you to create an AWS-managed table bucket. All S3 Storage Lens metrics in your account are stored in a single AWS-managed table bucket named `aws-s3`. 
+  `s3tables:PutTableBucketPolicy` – S3 Storage Lens uses this permission to set a table bucket policy that allows `systemtables.s3.amazonaws.com` access to the bucket so that logs can be delivered.

**Important**  
If you remove permissions for the service principal `systemtables.s3.amazonaws.com`, S3 Storage Lens will not be able to update the S3 tables with data based on your configuration. We recommend adding other access control policies in addition to the policy already provided, instead of editing the canned policy that is added when your table bucket is set up.

**Note**  
A separate S3 table for each type of metric export is created for each Storage Lens configuration. If you have multiple Storage Lens configurations in the Region, separate tables are created for additional configurations. For example, there are three types of tables available for your S3 table bucket.

## Permissions for AWS KMS encrypted tables
<a name="storage-lens-s3-tables-permissions-kms"></a>

All data in S3 tables including S3 Storage Lens metrics are encrypted with SSE-S3 encryption by default. You can choose to encrypt your Storage Lens metrics report with AWS KMS keys (SSE-KMS). If you choose to encrypt your S3 Storage Lens metric reports with KMS keys, you must have additional permissions.

1. The user or IAM role needs the following permissions. You can grant these permissions by using the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
   +  `kms:DescribeKey` on the AWS KMS key used

1. On the key policy for the AWS KMS key, you need the following permissions. You can grant these permissions by using the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms). To use this policy, replace the ` {{user input placeholders}} ` with your own information.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "EnableSystemTablesKeyUsage",
               "Effect": "Allow",
               "Principal": {
                   "Service": "systemtables.s3.amazonaws.com"
               },
               "Action": [
                   "kms:DescribeKey",
                   "kms:GenerateDataKey",
                   "kms:Decrypt"
               ],
               "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Sid": "EnableKeyUsage",
               "Effect": "Allow",
               "Principal": {
                   "Service": "maintenance.s3tables.amazonaws.com"
               },
               "Action": [
                   "kms:GenerateDataKey",
                   "kms:Decrypt"
               ],
               "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}",
               "Condition": {
                   "StringLike": {
                       "kms:EncryptionContext:aws:s3:arn": "{{<table-bucket-arn>}}/*"
                   }
               }
           }
       ]
   }
   ```

## Service-linked role for S3 Storage Lens
<a name="storage-lens-s3-tables-permissions-slr"></a>

S3 Storage Lens uses a service-linked role to write metrics to S3 Tables. This role is automatically created when you enable S3 Tables export for the first time in your account. The service-linked role has the following permissions:
+  `s3tables:CreateTable` - To create tables in the `aws-s3` table bucket
+  `s3tables:PutTableData` - To write metrics data to tables
+  `s3tables:GetTable` - To retrieve table metadata

You don't need to manually create or manage this service-linked role. For more information about service-linked roles, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*. 

## Best practices for permissions
<a name="storage-lens-s3-tables-permissions-best-practices"></a>

Follow these best practices when configuring permissions for S3 Storage Lens tables:
+  **Use least privilege** - Grant only the permissions required for specific tasks. For example, if users only need to query data, don't grant permissions to modify Storage Lens configurations.
+  **Use IAM roles** - Use IAM roles instead of long-term access keys for applications and services that access S3 Storage Lens tables.
+  **Enable AWS CloudTrail** - Enable CloudTrail logging to monitor access to S3 Storage Lens tables and track permission changes.
+  **Use resource-based policies** - When possible, use resource-based policies to control access to specific tables or namespaces.
+  **Regularly review permissions** - Periodically review and audit IAM policies and Lake Formation permissions to ensure they follow the principle of least privilege.

## Troubleshooting permissions
<a name="storage-lens-s3-tables-permissions-troubleshooting"></a>

### Access denied when enabling S3 Tables export
<a name="storage-lens-s3-tables-permissions-troubleshooting-export"></a>

 **Problem:** You receive an "access denied" error when trying to enable S3 Tables export.

 **Solution:** Verify that your IAM user or role has the `s3:PutStorageLensConfiguration` permission and the necessary S3 Tables permissions.

### Access denied when querying tables
<a name="storage-lens-s3-tables-permissions-troubleshooting-query"></a>

 **Problem:** You receive an "access denied" error when querying S3 Storage Lens tables in Amazon Athena.

 **Solution:** Verify that:
+ Analytics integration is enabled on the `aws-s3` table bucket
+ Lake Formation permissions are correctly configured
+ Your IAM user or role has the necessary Amazon Athena permissions

### KMS encryption errors
<a name="storage-lens-s3-tables-permissions-troubleshooting-kms"></a>

 **Problem:** You receive KMS-related errors when accessing encrypted tables.

 **Solution:** Verify that:
+ Your IAM policy includes the required KMS permissions
+ The KMS key policy grants permissions to the S3 Storage Lens service principal
+ The KMS key is in the same Region as your Storage Lens configuration

## Next steps
<a name="storage-lens-s3-tables-permissions-next-steps"></a>
+ Learn about [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md) 
+ Learn about [Querying S3 Storage Lens data with analytics tools](storage-lens-s3-tables-querying.md) 
+ Learn about [Using AI assistants with S3 Storage Lens tables](storage-lens-s3-tables-ai-tools.md) 