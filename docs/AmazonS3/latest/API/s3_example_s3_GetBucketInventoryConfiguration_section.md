# Use `GetBucketInventoryConfiguration` with a CLI

The following code examples show how to use `GetBucketInventoryConfiguration`.


CLI


**AWS CLI**

**To retrieve the inventory configuration for a bucket**


The following `get-bucket-inventory-configuration` example retrieves the inventory configuration for the specified bucket with ID `1`.



```
`aws s3api get-bucket-inventory-configuration \
 --bucket `amzn-s3-demo-bucket` \
 --id `1``

```

Output:



```
{
    "InventoryConfiguration": {
        "IsEnabled": true,
        "Destination": {
            "S3BucketDestination": {
                "Format": "ORC",
                "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket",
                "AccountId": "123456789012"
            }
        },
        "IncludedObjectVersions": "Current",
        "Id": "1",
        "Schedule": {
            "Frequency": "Weekly"
        }
    }
}
```


* For API details, see
 [GetBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-inventory-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-inventory-configuration.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the details of the inventory named 'testinventory' for the given S3 bucket.**



```
Get-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testinventory'

```


* For API details, see
 [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the details of the inventory named 'testinventory' for the given S3 bucket.**



```
Get-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testinventory'

```


* For API details, see
 [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
