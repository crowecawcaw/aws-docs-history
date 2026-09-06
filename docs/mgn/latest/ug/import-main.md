

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Importing your data inventory
<a name="import-main"></a>

The **Import** feature allows you to easily import your inventory of servers, applications, and waves from a CSV file that is saved in your local disk or an S3 bucket.

**Note**  
The import feature is not supported for IPv6.

**Topics**
+ [Define required permissions for importing](#import-required-permissions)
+ [Inventory Import parameters](import-parameters.md)
+ [Importing your data inventory from a local disk](import-local-disk.md)
+ [Importing your data inventory from an S3 bucket](import-s3.md)
+ [View import history](import-history.md)

## Define required permissions for importing
<a name="import-required-permissions"></a>

In order to use the import feature, you will need to create a role with the following policies (or any extension of them):

**Managed policies:**
+ [AWSApplicationMigrationFullAccess](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md)
+ [AWSApplicationMigrationEC2Access](security-iam-awsmanpol-AWSApplicationMigrationEC2Access.md)

**Note**  
These managed policies grant broad access to MGN features beyond the import function. For least privilege, use IAM Access Analyzer to generate a policy scoped to only the actions required for your import workflow. For more information, see [Generate policies based on access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html).

**Additional policies:**

```
{
  "Sid":  "AllowS3Access",
   "Effect":  "Allow",
   "Action": [
     "s3:GetObject"
  ],
   "Resource":  "arn:aws:s3:::amzn-s3-demo-bucket/*"
}
```

When starting an import on an Amazon S3 bucket source that is owned by another account, ensure that the role or user has access to the Amazon S3 objects. When using the API, the Amazon S3 bucket owner parameter defaults to the current user’s account ID.

The following is an example of an S3 bucket policy in the target account:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
   "Statement": [
    {
       "Sid":  "ExampleStatement",
       "Effect":  "Allow",
       "Principal": {
         "AWS":  "arn:aws:iam::123456789012:user/Dave"
      },
       "Action": [
         "s3:GetObject"
      ],
       "Resource":  "arn:aws:s3:::amzn-s3-demo-bucket/*"
    }
  ]
}
```

------

**Note**  
If the Amazon S3 objects are encrypted with SSE-KMS, ensure that the role or user initiating the import has access to decrypt using the AWS KMS key. This feature does not support SSE-C encrypted Amazon S3 objects.