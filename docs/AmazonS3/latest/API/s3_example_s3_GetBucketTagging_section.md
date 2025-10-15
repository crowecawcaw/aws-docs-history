# Use `GetBucketTagging` with a CLI

The following code examples show how to use `GetBucketTagging`.


CLI


**AWS CLI**

The following command retrieves the tagging configuration for a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api get-bucket-tagging --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "TagSet": [
        {
            "Value": "marketing",
            "Key": "organization"
        }
    ]
}
```


* For API details, see
 [GetBucketTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns all the tags associated with the given bucket.**



```
Get-S3BucketTagging -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketTagging](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns all the tags associated with the given bucket.**



```
Get-S3BucketTagging -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketTagging](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
