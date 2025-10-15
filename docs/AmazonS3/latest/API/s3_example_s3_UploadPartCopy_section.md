# Use `UploadPartCopy` with an AWS SDK or CLI

The following code examples show how to use `UploadPartCopy`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Perform a multipart copy](s3_example_s3_MultipartCopy_section.md "s3_example_s3_MultipartCopy_section.md")

CLI


**AWS CLI**

**To upload part of an object by copying data from an existing object as the data source**


The following `upload-part-copy` example uploads a part by copying data from an existing object as a data source.



```
`aws s3api upload-part-copy \
 --bucket `amzn-s3-demo-bucket` \
 --key `"Map_Data_June.mp4"` \
 --copy-source `"amzn-s3-demo-bucket/copy_of_Map_Data_June.mp4"` \
 --part-number `1` \
 --upload-id `"bq0tdE1CDpWQYRPLHuNG50xAT6pA5D.m_RiBy0ggOH6b13pVRY7QjvLlf75iFdJqp_2wztk5hvpUM2SesXgrzbehG5hViyktrfANpAD0NO.Nk3XREBqvGeZF6U3ipiSm"``

```

Output:



```
{
    "CopyPartResult": {
        "LastModified": "2019-12-13T23:16:03.000Z",
        "ETag": "\"711470fc377698c393d94aed6305e245\""
    }
}
```


* For API details, see
 [UploadPartCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part-copy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part-copy.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```
    public CompletableFuture<String> performMultiCopy(String toBucket, String bucketName, String key) {
        CreateMultipartUploadRequest createMultipartUploadRequest = CreateMultipartUploadRequest.builder()
            .bucket(toBucket)
            .key(key)
            .build();

        getAsyncClient().createMultipartUpload(createMultipartUploadRequest)
            .thenApply(createMultipartUploadResponse -> {
                String uploadId = createMultipartUploadResponse.uploadId();
                System.out.println("Upload ID: " + uploadId);

                UploadPartCopyRequest uploadPartCopyRequest = UploadPartCopyRequest.builder()
                    .sourceBucket(bucketName)
                    .destinationBucket(toBucket)
                    .sourceKey(key)
                    .destinationKey(key)
                    .uploadId(uploadId)  // Use the valid uploadId.
                    .partNumber(1)  // Ensure the part number is correct.
                    .copySourceRange("bytes=0-1023")  // Adjust range as needed
                    .build();

                return getAsyncClient().uploadPartCopy(uploadPartCopyRequest);
            })
            .thenCompose(uploadPartCopyFuture -> uploadPartCopyFuture)
            .whenComplete((uploadPartCopyResponse, exception) -> {
                if (exception != null) {
                    // Handle any exceptions.
                    logger.error("Error during upload part copy: " + exception.getMessage());
                } else {
                    // Successfully completed the upload part copy.
                    System.out.println("Upload Part Copy completed successfully. ETag: " + uploadPartCopyResponse.copyPartResult().eTag());
                }
            });
        return null;
    }


```


* For API details, see
 [UploadPartCopy](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UploadPartCopy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UploadPartCopy")
 in *AWS SDK for Java 2.x API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
