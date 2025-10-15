# Use `DeleteBucketEncryption` with a CLI

The following code examples show how to use `DeleteBucketEncryption`.


CLI


**AWS CLI**

**To delete the server-side encryption configuration of a bucket**


The following `delete-bucket-encryption` example deletes the server-side encryption configuration of the specified bucket.



```
`aws s3api delete-bucket-encryption \
 --bucket `amzn-s3-demo-bucket``

```

This command produces no output.



* For API details, see
 [DeleteBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-encryption.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This disables the encryption enabled for the S3 bucket provided.**



```
Remove-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketEncryption (DeleteBucketEncryption)" on target "s3casetestbucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketEncryption](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This disables the encryption enabled for the S3 bucket provided.**



```
Remove-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketEncryption (DeleteBucketEncryption)" on target "s3casetestbucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
