

# Prerequisites and Permissions
<a name="ExportPrerequisites"></a>

 Before exporting a domain, you need to prepare your Amazon S3 bucket and configure the necessary permissions. This section describes the prerequisites for exporting domain data. 

## Identify the Amazon S3 Bucket for Export
<a name="IdentifyingS3Bucket"></a>

 You must identify or create an Amazon S3 bucket to store the exported data. The bucket can be in the same AWS Region as your Amazon SimpleDB domain or in a different Region. For optimal performance, we recommend using a bucket in the same Region as your domain. 

 When setting up your Amazon S3 bucket, consider implementing the following security measures: 
+  **Bucket policies** - Configure bucket policies to control access to exported data. 
+  **Default server-side encryption** - Enable default encryption using Amazon S3 managed keys (SSE-S3) or KMS keys (SSE-KMS) to protect data at rest. 
+  **Versioning** - Enable versioning to maintain multiple versions of exported data and protect against accidental deletion. 

 For more information about Amazon S3 buckets, see the following topics in the *Amazon S3 User Guide*: 
+  [ Viewing bucket properties](https://docs.aws.amazon.com/AmazonS3/latest/userguide/view-bucket-properties.html) 
+  [ Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) 
+  [ Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) 

## Provide Access to the Amazon S3 Bucket
<a name="ProvidingS3Access"></a>

 To export domain data, you need appropriate IAM permissions for both Amazon SimpleDB and Amazon S3 operations. The following sections provide example IAM policies for the export operations. 

 For more information about Amazon S3 access control, see [ Identity and access management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-overview.html) in the *Amazon S3 User Guide*. 

### IAM Policy for StartDomainExport
<a name="StartDomainExportPolicy"></a>

 The following IAM policy grants permission to start a domain export and write data to an Amazon S3 bucket: 

```
{
    "Version": "2012-10-17",			 	 	 
    "Statement": [
        {
            "Sid": "AllowSimpleDBStartDomainExportAction",
            "Effect": "Allow",
            "Action": "sdb:StartDomainExport",
            "Resource": "arn:aws:sdb:us-east-1:123456789012:domain/yourDomain"
        },
        {
            "Sid": "AllowWritesToS3Bucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListObjects",
                "s3:PutObject",
                "s3:HeadBucket"
            ],
            "Resource": "arn:aws:s3:::your-bucket/*"
        }
    ]
}
```

 You can use wildcard patterns in the Resource ARN to grant permissions for multiple domains: 
+  All domains: `arn:aws::sdb:us-east-1:111122223333:domain/*` 
+  Pattern match: `arn:aws::sdb:us-east-1:111122223333:domain/test*` 

**Note**  
 The `s3:HeadBucket` permission is optional but recommended. Without it, AWS CloudTrail logs may show "Access Denied" entries when Amazon SimpleDB verifies bucket accessibility, even though the export succeeds. 

### IAM Policy for GetExport
<a name="GetExportPolicy"></a>

 The following IAM policy grants permission to retrieve information about an export: 

```
{
    "Version": "2012-10-17",			 	 	 
    "Statement": [
        {
            "Sid": "AllowSimpleDBGetExportAction",
            "Effect": "Allow",
            "Action": "sdb:GetExport",
            "Resource": "arn:aws:sdb:us-east-1:123456789012:domain/yourDomain/export/fd59ec34-110b-419b-9395-81a1a0914c90"
        }
    ]
}
```

 You can use wildcard patterns to grant permissions for multiple exports: 
+  All exports for a domain: `arn:aws::sdb:us-east-1:111122223333:domain/yourDomain/export/*` 
+  All exports for all domains: `arn:aws::sdb:us-east-1:111122223333:domain/*` 

### IAM Policy for ListExports
<a name="ListExportsPolicy"></a>

 The following IAM policy grants permission to list exports in your account: 

```
{
    "Version": "2012-10-17",			 	 	 
    "Statement": [
        {
            "Sid": "AllowSimpleDBListExportsAction",
            "Effect": "Allow",
            "Action": "sdb:ListExports",
            "Resource": "*"
        }
    ]
}
```

**Important**  
 To list all exports without a domain filter, the Resource must be set to `"*"` with no Deny policy. For filtered listing by domain, you can use domain-specific ARNs, but the least-restricted privilege is recommended for the ListExports operation. 