# Use `GetBucketRequestPayment` with a CLI

The following code examples show how to use `GetBucketRequestPayment`.


CLI


**AWS CLI**

**To retrieve the request payment configuration for a bucket**


The following `get-bucket-request-payment` example retrieves the requester pays configuration for the specified bucket.



```
`aws s3api get-bucket-request-payment \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "Payer": "BucketOwner"
}
```


* For API details, see
 [GetBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-request-payment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-request-payment.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: Returns the request payment configuration for the bucket named 'amzn-s3-demo-bucket'. By default, the bucket owner pays for downloads from the bucket.**



```
Get-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [GetBucketRequestPayment](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: Returns the request payment configuration for the bucket named 'amzn-s3-demo-bucket'. By default, the bucket owner pays for downloads from the bucket.**



```
Get-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [GetBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
