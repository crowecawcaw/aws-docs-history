# Use `PutBucketVersioning` with an AWS SDK or CLI

The following code examples show how to use `PutBucketVersioning`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Get started with S3](s3_example_s3_GettingStarted_section.md "s3_example_s3_GettingStarted_section.md")

CLI


**AWS CLI**

The following command enables versioning on a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api put-bucket-versioning --bucket `amzn-s3-demo-bucket` --versioning-configuration `Status=Enabled``

```

The following command enables versioning, and uses an mfa code



```
`aws s3api put-bucket-versioning --bucket `amzn-s3-demo-bucket` --versioning-configuration `Status=Enabled` --mfa `"SERIAL 123456"``

```


* For API details, see
 [PutBucketVersioning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-versioning.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-versioning.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```
    /**
     * Enables bucket versioning for the specified S3 bucket.
     *
     * @param s3Client the S3 client to use for the operation
     * @param bucketName the name of the S3 bucket to enable versioning for
     */
    public static void enableBucketVersioning(S3Client s3Client, String bucketName){
        VersioningConfiguration versioningConfiguration = VersioningConfiguration.builder()
            .status(BucketVersioningStatus.ENABLED)
            .build();

        PutBucketVersioningRequest versioningRequest = PutBucketVersioningRequest.builder()
            .bucket(bucketName)
            .versioningConfiguration(versioningConfiguration)
            .build();

        s3Client.putBucketVersioning(versioningRequest);
        System.out.println("Bucket versioning has been enabled for "+bucketName);
    }


```


* For API details, see
 [PutBucketVersioning](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketVersioning")
 in *AWS SDK for Java 2.x API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: The command enables versioning for the given S3 bucket.**



```
Write-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket' -VersioningConfig_Status Enabled

```


* For API details, see
 [PutBucketVersioning](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: The command enables versioning for the given S3 bucket.**



```
Write-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket' -VersioningConfig_Status Enabled

```


* For API details, see
 [PutBucketVersioning](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
