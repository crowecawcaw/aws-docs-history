# Setting up permissions for configuring metadata
 tables

To create a metadata table configuration, you must have the necessary AWS Identity and Access Management (IAM) permissions
 to both create and manage your metadata table configuration and to create and manage your metadata
 tables and the table bucket where your metadata tables are stored. 

To create and manage your metadata table configuration, you must have these permissions: 


* `s3:CreateBucketMetadataTableConfiguration` – This permission allows you to
 create a metadata table configuration for your general purpose bucket. To create a metadata table
 configuration, additional permissions, including S3 Tables permissions, are required, as explained
 in the following sections. For a summary of the required permissions, see [Bucket operations and permissions](using-with-s3-policy-actions.md#using-with-s3-policy-actions-related-to-buckets "using-with-s3-policy-actions.md#using-with-s3-policy-actions-related-to-buckets").
* `s3:GetBucketMetadataTableConfiguration` – This permission allows you to
 retrieve information about your metadata table configuration.
* `s3:DeleteBucketMetadataTableConfiguration` – This permission allows you to
 delete your metadata table configuration.
* `s3:UpdateBucketMetadataJournalTableConfiguration` – This permission allows
 you to update your journal table configuration to expire journal table records.
* `s3:UpdateBucketMetadataInventoryTableConfiguration` – This permission allows
 you to update your inventory table configuration to enable or disable the inventory table. To update
 an inventory table configuration, additional permissions, including S3 Tables permissions, are
 required. For a list of the required permissions, see [Bucket operations and permissions](using-with-s3-policy-actions.md#using-with-s3-policy-actions-related-to-buckets "using-with-s3-policy-actions.md#using-with-s3-policy-actions-related-to-buckets").


###### Note

The `s3:CreateBucketMetadataTableConfiguration`,
 `s3:GetBucketMetadataTableConfiguration`, and
 `s3:DeleteBucketMetadataTableConfiguration` permissions are used for both V1 and V2
 S3 Metadata configurations. For V2, the names of the corresponding API operations are
 `CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`, and
 `DeleteBucketMetadataConfiguration`.
To create and work with tables and table buckets, you must have certain
 `s3tables` permissions. At a minimum, to create a metadata table configuration,
 you must have the following `s3tables` permissions: 


* `s3tables:CreateTableBucket` – This permission allows you to create an AWS
 managed table bucket. All metadata table configurations in your account and in the same Region are
 stored in a single AWS managed table bucket named `aws-s3`. For more information, see
 [How metadata tables work](metadata-tables-overview.md#metadata-tables-how-they-work "metadata-tables-overview.md#metadata-tables-how-they-work") and [Working with AWS managed
 table buckets](s3-tables-aws-managed-buckets.md "s3-tables-aws-managed-buckets.md").
* `s3tables:CreateNamespace` – This permission allows you to create a namespace
 in a table bucket. Metadata tables typically use the
 `b_`general_purpose_bucket_name`` namespace. For more
 information about metadata table namespaces, see [How metadata tables work](metadata-tables-overview.md#metadata-tables-how-they-work "metadata-tables-overview.md#metadata-tables-how-they-work").
* `s3tables:CreateTable` – This permission allows you to create your metadata
 tables.
* `s3tables:GetTable` – This permission allows you to retrieve information about
 your metadata tables.
* `s3tables:PutTablePolicy` – This permission allows you to add or update your
 metadata table policies.
* `s3tables:PutTableEncryption` – This permission allows you to set server-side
 encryption for your metadata tables. Additional permissions are required if you want to encrypt your
 metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS). For more
 information, see [Permissions for SSE-KMS](#metadata-kms-permissions "#metadata-kms-permissions").
* `kms:DescribeKey` – This permission allows you to retrieve information about a
 KMS key.
For detailed information about all table and table bucket permissions, see [Access
 management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").

###### Important

If you also want to integrate your table bucket with AWS analytics services so that you can query your metadata table, you need additional permissions. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").


###### Permissions for SSE-KMS


To encrypt your metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS),
 you must have additional permissions. 



1. The user or AWS Identity and Access Management (IAM) role needs the following permissions. You can grant these
 permissions by using the IAM console: [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").




	1. `s3tables:PutTableEncryption` to configure table encryption
	2. `kms:DescribeKey` on the AWS KMS key used
2. On the resource policy for the KMS key, you need the following permissions. You can grant
 these permissions by using the AWS KMS console: [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").




	1. Grant `kms:GenerateDataKey` permission to
	 `metadata.s3.amazonaws.com` and
	 `maintenance.s3tables.amazonaws.com`.
	2. Grant `kms:Decrypt` permission to `metadata.s3.amazonaws.com` and
	 `maintenance.s3tables.amazonaws.com`.
	3. Grant `kms:DescribeKey` permission to the invoking AWS principal.
In addition to these permissions, make sure that the customer managed KMS key used to encrypt the
 tables still exists, is active, is in the same Region as your general purpose bucket.


###### Example policy


To create and work with metadata tables and table buckets, you can use the following example policy.
 In this policy, the general purpose bucket that you're applying the metadata table configuration to is
 referred to as ``amzn-s3-demo-bucket``. To use this policy, replace the
 ``user input placeholders`` with your own information. 


When you create your metadata table configuration, your metadata tables are stored in an AWS
 managed table bucket. All metadata table configurations in your account and in the same Region are
 stored in a single AWS managed table bucket named `aws-s3`. 


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "PermissionsToWorkWithMetadataTables",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucketMetadataTableConfiguration",
 "s3:GetBucketMetadataTableConfiguration",
 "s3:DeleteBucketMetadataTableConfiguration",
 "s3:UpdateBucketMetadataJournalTableConfiguration",
 "s3:UpdateBucketMetadataInventoryTableConfiguration",
 "s3tables:*",
 "kms:DescribeKey"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/aws-s3",
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/aws-s3/table/*"
 ]
 }
 ]
}`

```




To query metadata tables, you can use the following example policy. If your metadata tables have
 been encrypted with SSE-KMS, you will need the `kms:Decrypt` permission as shown. To use this
 policy, replace the ``user input placeholders`` with your own
 information.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "PermissionsToQueryMetadataTables",
 "Effect": "Allow",
 "Action": [
 "s3tables:GetTable",
 "s3tables:GetTableData",
 "s3tables:GetTableMetadataLocation",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/aws-s3",
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/aws-s3/table/*"
 ]
 }
 ]
}`

```
