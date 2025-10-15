# Use `ListBucketInventoryConfigurations` with a CLI

The following code examples show how to use `ListBucketInventoryConfigurations`.


CLI


**AWS CLI**

**To retrieve a list of inventory configurations for a bucket**


The following `list-bucket-inventory-configurations` example lists the inventory configurations for the specified bucket.



```
`aws s3api list-bucket-inventory-configurations \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "InventoryConfigurationList": [
        {
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
        },
        {
            "IsEnabled": true,
            "Destination": {
                "S3BucketDestination": {
                    "Format": "CSV",
                    "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket",
                    "AccountId": "123456789012"
                }
            },
            "IncludedObjectVersions": "Current",
            "Id": "2",
            "Schedule": {
                "Frequency": "Daily"
            }
        }
    ],
    "IsTruncated": false
}
```


* For API details, see
 [ListBucketInventoryConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-inventory-configurations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-inventory-configurations.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the first 100 inventory configurations of the given S3 bucket.**



```
Get-S3BucketInventoryConfigurationList -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the first 100 inventory configurations of the given S3 bucket.**



```
Get-S3BucketInventoryConfigurationList -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
