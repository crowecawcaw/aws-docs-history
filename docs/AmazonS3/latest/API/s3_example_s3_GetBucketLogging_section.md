# Use `GetBucketLogging` with a CLI

The following code examples show how to use `GetBucketLogging`.


CLI


**AWS CLI**

**To retrieve the logging status for a bucket**


The following `get-bucket-logging` example retrieves the logging status for the specified bucket.



```
`aws s3api get-bucket-logging \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "LoggingEnabled": {
        "TargetPrefix": "",
        "TargetBucket": "amzn-s3-demo-bucket-logs"
          }
}
```


* For API details, see
 [GetBucketLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the logging status for the specified bucket.**



```
Get-S3BucketLogging -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
TargetBucketName   Grants TargetPrefix
----------------   ------ ------------
testbucket1        {}     testprefix
```


* For API details, see
 [GetBucketLogging](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the logging status for the specified bucket.**



```
Get-S3BucketLogging -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
TargetBucketName   Grants TargetPrefix
----------------   ------ ------------
testbucket1        {}     testprefix
```


* For API details, see
 [GetBucketLogging](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
