# Use `GetBucketAccelerateConfiguration` with a CLI

The following code examples show how to use `GetBucketAccelerateConfiguration`.

CLI

**AWS CLI**

**To retrieve the accelerate configuration of a bucket**

The following `get-bucket-accelerate-configuration` example retrieves the accelerate configuration for the specified bucket.

```
`aws s3api get-bucket-accelerate-configuration \
 --bucket `amzn-s3-demo-bucket``

```

Output:

```
{
    "Status": "Enabled"
}
```

- For API details, see
  [GetBucketAccelerateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-accelerate-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-accelerate-configuration.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command returns the value Enabled, if the transfer acceleration settings is enabled for the bucket specified.**

```
Get-S3BucketAccelerateConfiguration -BucketName 'amzn-s3-demo-bucket'

```

**Output:**

```
Value
-----
Enabled
```

- For API details, see
  [GetBucketAccelerateConfiguration](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command returns the value Enabled, if the transfer acceleration settings is enabled for the bucket specified.**

```
Get-S3BucketAccelerateConfiguration -BucketName 'amzn-s3-demo-bucket'

```

**Output:**

```
Value
-----
Enabled
```

- For API details, see
  [GetBucketAccelerateConfiguration](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
