# Use `DeleteBucketInventoryConfiguration` with a CLI

The following code examples show how to use `DeleteBucketInventoryConfiguration`.


CLI


**AWS CLI**

**To delete the inventory configuration of a bucket**


The following `delete-bucket-inventory-configuration` example deletes the inventory configuration with ID `1` for the specified bucket.



```
`aws s3api delete-bucket-inventory-configuration \
 --bucket `amzn-s3-demo-bucket` \
 --id `1``

```

This command produces no output.



* For API details, see
 [DeleteBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-inventory-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-inventory-configuration.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command removes the invventory named 'testInventoryName' corresponding to the given S3 bucket.**



```
Remove-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testInventoryName'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketInventoryConfiguration (DeleteBucketInventoryConfiguration)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command removes the invventory named 'testInventoryName' corresponding to the given S3 bucket.**



```
Remove-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testInventoryName'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketInventoryConfiguration (DeleteBucketInventoryConfiguration)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
