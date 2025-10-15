# Use `DeletePublicAccessBlock` with a CLI

The following code examples show how to use `DeletePublicAccessBlock`.


CLI


**AWS CLI**

**To delete the block public access configuration for a bucket**


The following `delete-public-access-block` example removes the block public access configuration on the specified bucket.



```
`aws s3api delete-public-access-block \
 --bucket `amzn-s3-demo-bucket``

```

This command produces no output.



* For API details, see
 [DeletePublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-public-access-block.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-public-access-block.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command turns off the block public access setting for the given bucket.**



```
Remove-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket' -Force -Select '^BucketName'

```

**Output:**



```
amzn-s3-demo-bucket
```


* For API details, see
 [DeletePublicAccessBlock](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command turns off the block public access setting for the given bucket.**



```
Remove-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket' -Force -Select '^BucketName'

```

**Output:**



```
amzn-s3-demo-bucket
```


* For API details, see
 [DeletePublicAccessBlock](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
