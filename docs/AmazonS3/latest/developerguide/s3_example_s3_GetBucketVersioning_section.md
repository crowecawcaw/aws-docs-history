# Use `GetBucketVersioning` with a CLI

The following code examples show how to use `GetBucketVersioning`.

CLI

**AWS CLI**

The following command retrieves the versioning configuration for a bucket named `amzn-s3-demo-bucket`:

```
`aws s3api get-bucket-versioning --bucket `amzn-s3-demo-bucket``

```

Output:

```
{
    "Status": "Enabled"
}
```

- For API details, see
  [GetBucketVersioning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-versioning.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-versioning.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command returns the status of versioning with respect to the given bucket.**

```
Get-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket'

```

- For API details, see
  [GetBucketVersioning](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command returns the status of versioning with respect to the given bucket.**

```
Get-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket'

```

- For API details, see
  [GetBucketVersioning](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
