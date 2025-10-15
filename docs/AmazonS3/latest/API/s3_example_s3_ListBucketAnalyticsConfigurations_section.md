# Use `ListBucketAnalyticsConfigurations` with a CLI

The following code examples show how to use `ListBucketAnalyticsConfigurations`.


CLI


**AWS CLI**

**To retrieve a list of analytics configurations for a bucket**


The following `list-bucket-analytics-configurations` retrieves a list of analytics configurations for the specified bucket.



```
`aws s3api list-bucket-analytics-configurations \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "AnalyticsConfigurationList": [
        {
            "StorageClassAnalysis": {},
            "Id": "1"
        }
    ],
    "IsTruncated": false
}
```


* For API details, see
 [ListBucketAnalyticsConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-analytics-configurations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-analytics-configurations.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the first 100 analytics configurations of the given S3 bucket.**



```
Get-S3BucketAnalyticsConfigurationList -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the first 100 analytics configurations of the given S3 bucket.**



```
Get-S3BucketAnalyticsConfigurationList -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
