# Use `GetPublicAccessBlock` with a CLI

The following code examples show how to use `GetPublicAccessBlock`.


CLI


**AWS CLI**

**To set or modify the block public access configuration for a bucket**


The following `get-public-access-block` example displays the block public access configuration for the specified bucket.



```
`aws s3api get-public-access-block \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "PublicAccessBlockConfiguration": {
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "BlockPublicAcls": true,
        "RestrictPublicBuckets": true
    }
}
```


* For API details, see
 [GetPublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-public-access-block.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-public-access-block.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: The command returns the public access block configuration of the given S3 bucket.**



```
Get-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetPublicAccessBlock](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: The command returns the public access block configuration of the given S3 bucket.**



```
Get-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetPublicAccessBlock](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
