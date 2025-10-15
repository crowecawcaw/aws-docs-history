# Use `DeleteBucketLifecycle` with an AWS SDK or CLI

The following code examples show how to use `DeleteBucketLifecycle`.


.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").
 



```

        /// <summary>
        /// This method removes the Lifecycle configuration from the named
        /// S3 bucket.
        /// </summary>
        /// <param name="client">The S3 client object used to call
        /// the RemoveLifecycleConfigAsync method.</param>
        /// <param name="bucketName">A string representing the name of the
        /// S3 bucket from which the configuration will be removed.</param>
        public static async Task RemoveLifecycleConfigAsync(IAmazonS3 client, string bucketName)
        {
            var request = new DeleteLifecycleConfigurationRequest()
            {
                BucketName = bucketName,
            };
            await client.DeleteLifecycleConfigurationAsync(request);
        }



```


* For API details, see
 [DeleteBucketLifecycle](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketLifecycle")
 in *AWS SDK for .NET API Reference*.




CLI


**AWS CLI**

The following command deletes a lifecycle configuration from a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api delete-bucket-lifecycle --bucket `amzn-s3-demo-bucket``

```


* For API details, see
 [DeleteBucketLifecycle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-lifecycle.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-lifecycle.html")
 in *AWS CLI Command Reference*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples").
 



```
class BucketWrapper:
    """Encapsulates S3 bucket actions."""

    def __init__(self, bucket):
        """
        :param bucket: A Boto3 Bucket resource. This is a high-level resource in Boto3
                       that wraps bucket actions in a class-like structure.
        """
        self.bucket = bucket
        self.name = bucket.name


    def delete_lifecycle_configuration(self):
        """
        Remove the lifecycle configuration from the specified bucket.
        """
        try:
            self.bucket.LifecycleConfiguration().delete()
            logger.info(
                "Deleted lifecycle configuration for bucket '%s'.", self.bucket.name
            )
        except ClientError:
            logger.exception(
                "Couldn't delete lifecycle configuration for bucket '%s'.",
                self.bucket.name,
            )
            raise



```


* For API details, see
 [DeleteBucketLifecycle](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketLifecycle")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
