# Use `PutBucketEncryption` with an AWS SDK or CLI

The following code examples show how to use `PutBucketEncryption`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Get started with S3](s3_example_s3_GettingStarted_section.md "s3_example_s3_GettingStarted_section.md")

.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/PutBucketEncryption#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/PutBucketEncryption#code-examples").
 



```
    /// <summary>
    /// Set the bucket server side encryption to use AWSKMS with a customer-managed key id.
    /// </summary>
    /// <param name="bucketName">Name of the bucket.</param>
    /// <param name="kmsKeyId">The Id of the KMS Key.</param>
    /// <returns>True if successful.</returns>
    public static async Task<bool> SetBucketServerSideEncryption(string bucketName, string kmsKeyId)
    {
        var serverSideEncryptionByDefault = new ServerSideEncryptionConfiguration
        {
            ServerSideEncryptionRules = new List<ServerSideEncryptionRule>
            {
                new ServerSideEncryptionRule
                {
                    ServerSideEncryptionByDefault = new ServerSideEncryptionByDefault
                    {
                        ServerSideEncryptionAlgorithm = ServerSideEncryptionMethod.AWSKMS,
                        ServerSideEncryptionKeyManagementServiceKeyId = kmsKeyId
                    }
                }
            }
        };
        try
        {
            var encryptionResponse = await _s3Client.PutBucketEncryptionAsync(new PutBucketEncryptionRequest
            {
                BucketName = bucketName,
                ServerSideEncryptionConfiguration = serverSideEncryptionByDefault,
            });
            
            return encryptionResponse.HttpStatusCode == HttpStatusCode.OK;
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine(ex.ErrorCode == "AccessDenied"
                ? $"This account does not have permission to set encryption on {bucketName}, please try again."
                : $"Unable to set bucket encryption for bucket {bucketName}, {ex.Message}");
        }
        return false;
    }


```


* For API details, see
 [PutBucketEncryption](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketEncryption")
 in *AWS SDK for .NET API Reference*.




CLI


**AWS CLI**

**To configure server-side encryption for a bucket**


The following `put-bucket-encryption` example sets AES256 encryption as the default for the specified bucket.



```
`aws s3api put-bucket-encryption \
 --bucket `amzn-s3-demo-bucket` \
 --server-side-encryption-configuration '`{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}`'`

```

This command produces no output.



* For API details, see
 [PutBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command enables default AES256 server side encryption with Amazon S3 Managed Keys(SSE-S3) on the given bucket.** 



```
$Encryptionconfig = @{ServerSideEncryptionByDefault = @{ServerSideEncryptionAlgorithm = "AES256"}}
Set-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket' -ServerSideEncryptionConfiguration_ServerSideEncryptionRule $Encryptionconfig

```


* For API details, see
 [PutBucketEncryption](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command enables default AES256 server side encryption with Amazon S3 Managed Keys(SSE-S3) on the given bucket.** 



```
$Encryptionconfig = @{ServerSideEncryptionByDefault = @{ServerSideEncryptionAlgorithm = "AES256"}}
Set-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket' -ServerSideEncryptionConfiguration_ServerSideEncryptionRule $Encryptionconfig

```


* For API details, see
 [PutBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
