# Use `GetObjectAttributes` with an AWS SDK

The following code example shows how to use `GetObjectAttributes`.


Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/directorybucket#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/directorybucket#code-examples").
 


Get an object attributes from a directory bucket.



```

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectAttributesRequest;
import software.amazon.awssdk.services.s3.model.GetObjectAttributesResponse;
import software.amazon.awssdk.services.s3.model.ObjectAttributes;
import software.amazon.awssdk.services.s3.model.S3Exception;

import java.nio.file.Path;

import static com.example.s3.util.S3DirectoryBucketUtils.createDirectoryBucket;
import static com.example.s3.util.S3DirectoryBucketUtils.createS3Client;
import static com.example.s3.util.S3DirectoryBucketUtils.deleteAllObjectsInDirectoryBucket;
import static com.example.s3.util.S3DirectoryBucketUtils.deleteDirectoryBucket;
import static com.example.s3.util.S3DirectoryBucketUtils.getFilePath;
import static com.example.s3.util.S3DirectoryBucketUtils.putDirectoryBucketObject;

    /**
     * Retrieves attributes for an object in the specified S3 directory bucket.
     *
     * @param s3Client   The S3 client used to interact with S3
     * @param bucketName The name of the directory bucket
     * @param objectKey  The key (name) of the object to retrieve attributes for
     * @return True if the object attributes are successfully retrieved, false
     *         otherwise
     */
    public static boolean getDirectoryBucketObjectAttributes(S3Client s3Client, String bucketName, String objectKey) {
        logger.info("Retrieving attributes for object: {} from bucket: {}", objectKey, bucketName);

        try {
            // Create a GetObjectAttributesRequest
            GetObjectAttributesRequest getObjectAttributesRequest = GetObjectAttributesRequest.builder()
                    .bucket(bucketName)
                    .key(objectKey)
                    .objectAttributes(ObjectAttributes.E_TAG, ObjectAttributes.STORAGE_CLASS,
                            ObjectAttributes.OBJECT_SIZE)
                    .build();

            // Retrieve the object attributes
            GetObjectAttributesResponse response = s3Client.getObjectAttributes(getObjectAttributesRequest);
            logger.info("Attributes for object {}:", objectKey);
            logger.info("ETag: {}", response.eTag());
            logger.info("Storage Class: {}", response.storageClass());
            logger.info("Object Size: {}", response.objectSize());
            return true;

        } catch (S3Exception e) {
            logger.error("Failed to retrieve object attributes: {} - Error code: {}",
                    e.awsErrorDetails().errorMessage(), e.awsErrorDetails().errorCode(), e);
            return false;
        }
    }


```


* For API details, see
 [GetObjectAttributes](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributes")
 in *AWS SDK for Java 2.x API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
