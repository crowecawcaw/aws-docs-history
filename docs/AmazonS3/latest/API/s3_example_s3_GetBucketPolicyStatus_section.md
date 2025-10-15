# Use `GetBucketPolicyStatus` with a CLI

The following code examples show how to use `GetBucketPolicyStatus`.


CLI


**AWS CLI**

**To retrieve the policy status for a bucket indicating whether the bucket is public**


The following `get-bucket-policy-status` example retrieves the policy status for the bucket `amzn-s3-demo-bucket`.



```
`aws s3api get-bucket-policy-status \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "PolicyStatus": {
        "IsPublic": false
    }
}
```


* For API details, see
 [GetBucketPolicyStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy-status.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns policy status for the given S3 bucket, indicating whether the bucket is public.**



```
Get-S3BucketPolicyStatus -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketPolicyStatus](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns policy status for the given S3 bucket, indicating whether the bucket is public.**



```
Get-S3BucketPolicyStatus -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketPolicyStatus](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
