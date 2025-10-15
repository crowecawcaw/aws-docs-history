# Use `GetBucketMetricsConfiguration` with a CLI

The following code examples show how to use `GetBucketMetricsConfiguration`.


CLI


**AWS CLI**

**To retrieve the metrics configuration for a bucket with a specific ID**


The following `get-bucket-metrics-configuration` example displays the metrics configuration for the specified bucket and ID.



```
`aws s3api get-bucket-metrics-configuration \
 --bucket `amzn-s3-demo-bucket` \
 --id `123``

```

Output:



```
{
    "MetricsConfiguration": {
        "Filter": {
            "Prefix": "logs"
        },
        "Id": "123"
    }
}
```


* For API details, see
 [GetBucketMetricsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-metrics-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-metrics-configuration.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the details about the metrics filter named 'testfilter' for the given S3 bucket.**



```
Get-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testfilter'

```


* For API details, see
 [GetBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the details about the metrics filter named 'testfilter' for the given S3 bucket.**



```
Get-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testfilter'

```


* For API details, see
 [GetBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
