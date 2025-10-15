# Use `GetBucketEncryption` with an AWS SDK or CLI

The following code examples show how to use `GetBucketEncryption`.


.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/PutBucketEncryption#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/PutBucketEncryption#code-examples").
 



```
    /// <summary>
    /// Get and print the encryption settings of a bucket.
    /// </summary>
    /// <param name="bucketName">Name of the bucket.</param>
    /// <returns>Async task.</returns>
    public static async Task GetEncryptionSettings(string bucketName)
    {
        // Check and print the bucket encryption settings.
        Console.WriteLine($"Getting encryption settings for bucket {bucketName}.");

        try
        {
            var settings =
                await _s3Client.GetBucketEncryptionAsync(
                    new GetBucketEncryptionRequest() { BucketName = bucketName });

            foreach (var encryptionSettings in settings?.ServerSideEncryptionConfiguration?.ServerSideEncryptionRules!)
            {
                Console.WriteLine(
                    $"\tAlgorithm: {encryptionSettings.ServerSideEncryptionByDefault.ServerSideEncryptionAlgorithm}");
                Console.WriteLine(
                    $"\tKey: {encryptionSettings.ServerSideEncryptionByDefault.ServerSideEncryptionKeyManagementServiceKeyId}");
            }
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine(ex.ErrorCode == "InvalidBucketName"
                ? $"Bucket {bucketName} was not found."
                : $"Unable to get bucket encryption for bucket {bucketName}, {ex.Message}");
        }
    }


```


* For API details, see
 [GetBucketEncryption](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketEncryption")
 in *AWS SDK for .NET API Reference*.




CLI


**AWS CLI**

**To retrieve the server-side encryption configuration for a bucket**


The following `get-bucket-encryption` example retrieves the server-side encryption configuration for the bucket `amzn-s3-demo-bucket`.



```
`aws s3api get-bucket-encryption \
 --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "ServerSideEncryptionConfiguration": {
        "Rules": [
            {
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256"
                }
            }
        ]
    }
}
```


* For API details, see
 [GetBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns all the server side encryption rules associated with the given bucket.**



```
Get-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketEncryption](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns all the server side encryption rules associated with the given bucket.**



```
Get-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
