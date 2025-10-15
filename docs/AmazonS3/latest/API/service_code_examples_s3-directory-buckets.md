# Code examples for S3 Directory Buckets using AWS SDKs

The following code examples show how to use S3 Directory Buckets with an AWS software development kit (SDK).
 

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.

**Get started**


The following code example shows how to get started using Amazon S3 directory buckets.


Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/directorybucket#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/directorybucket#code-examples").
 



```

package com.example.s3.directorybucket;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.Bucket;
import software.amazon.awssdk.services.s3.model.BucketInfo;
import software.amazon.awssdk.services.s3.model.BucketType;
import software.amazon.awssdk.services.s3.model.CreateBucketConfiguration;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateBucketResponse;
import software.amazon.awssdk.services.s3.model.DataRedundancy;
import software.amazon.awssdk.services.s3.model.DeleteBucketRequest;
import software.amazon.awssdk.services.s3.model.ListDirectoryBucketsRequest;
import software.amazon.awssdk.services.s3.model.ListDirectoryBucketsResponse;
import software.amazon.awssdk.services.s3.model.LocationInfo;
import software.amazon.awssdk.services.s3.model.LocationType;
import software.amazon.awssdk.services.s3.model.S3Exception;

import java.util.List;
import java.util.stream.Collectors;

import static com.example.s3.util.S3DirectoryBucketUtils.createS3Client;

/**
 * Before running this example:
 * <p>
 * The SDK must be able to authenticate AWS requests on your behalf. If you have
 * not configured
 * authentication for SDKs and tools, see
 * https://docs.aws.amazon.com/sdkref/latest/guide/access.html in the AWS SDKs
 * and Tools Reference Guide.
 * <p>
 * You must have a runtime environment configured with the Java SDK.
 * See
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html in
 * the Developer Guide if this is not set up.
 * <p>
 * To use S3 directory buckets, configure a gateway VPC endpoint. This is the
 * recommended method to enable directory bucket traffic without
 * requiring an internet gateway or NAT device. For more information on
 * configuring VPC gateway endpoints, visit
 * https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-networking.html#s3-express-networking-vpc-gateway.
 * <p>
 * Directory buckets are available in specific AWS Regions and Zones. For
 * details on Regions and Zones supporting directory buckets, see
 * https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-networking.html#s3-express-endpoints.
 */

public class HelloS3DirectoryBuckets {
    private static final Logger logger = LoggerFactory.getLogger(HelloS3DirectoryBuckets.class);

    public static void main(String[] args) {
        String bucketName = "test-bucket-" + System.currentTimeMillis() + "--usw2-az1--x-s3";
        Region region = Region.US_WEST_2;
        String zone = "usw2-az1";
        S3Client s3Client = createS3Client(region);

        try {
            // Create the directory bucket
            createDirectoryBucket(s3Client, bucketName, zone);
            logger.info("Created bucket: {}", bucketName);

            // List all directory buckets
            List<String> bucketNames = listDirectoryBuckets(s3Client);
            bucketNames.forEach(name -> logger.info("Bucket Name: {}", name));
        } catch (S3Exception e) {
            logger.error("An error occurred during S3 operations: {} - Error code: {}",
                    e.awsErrorDetails().errorMessage(), e.awsErrorDetails().errorCode(), e);
        } finally {
            try {
                // Delete the created bucket
                deleteDirectoryBucket(s3Client, bucketName);
                logger.info("Deleted bucket: {}", bucketName);
            } catch (S3Exception e) {
                logger.error("Failed to delete the bucket due to S3 error: {} - Error code: {}",
                        e.awsErrorDetails().errorMessage(), e.awsErrorDetails().errorCode(), e);
            } catch (RuntimeException e) {
                logger.error("Failed to delete the bucket due to unexpected error: {}", e.getMessage(), e);
            } finally {
                s3Client.close();
            }
        }
    }

    /**
     * Creates a new S3 directory bucket in a specified Zone (For example, a
     * specified Availability Zone in this code example).
     *
     * @param s3Client   The S3 client used to create the bucket
     * @param bucketName The name of the bucket to be created
     * @param zone       The region where the bucket will be created
     * @throws S3Exception if there's an error creating the bucket
     */
    public static void createDirectoryBucket(S3Client s3Client, String bucketName, String zone) throws S3Exception {
        logger.info("Creating bucket: {}", bucketName);

        CreateBucketConfiguration bucketConfiguration = CreateBucketConfiguration.builder()
                .location(LocationInfo.builder()
                        .type(LocationType.AVAILABILITY_ZONE)
                        .name(zone).build())
                .bucket(BucketInfo.builder()
                        .type(BucketType.DIRECTORY)
                        .dataRedundancy(DataRedundancy.SINGLE_AVAILABILITY_ZONE)
                        .build())
                .build();
        try {
            CreateBucketRequest bucketRequest = CreateBucketRequest.builder()
                    .bucket(bucketName)
                    .createBucketConfiguration(bucketConfiguration).build();
            CreateBucketResponse response = s3Client.createBucket(bucketRequest);
            logger.info("Bucket created successfully with location: {}", response.location());
        } catch (S3Exception e) {
            logger.error("Error creating bucket: {} - Error code: {}", e.awsErrorDetails().errorMessage(),
                    e.awsErrorDetails().errorCode(), e);
            throw e;
        }
    }

    /**
     * Lists all S3 directory buckets.
     *
     * @param s3Client The S3 client used to interact with S3
     * @return A list of bucket names
     */
    public static List<String> listDirectoryBuckets(S3Client s3Client) {
        logger.info("Listing all directory buckets");

        try {
            // Create a ListBucketsRequest
            ListDirectoryBucketsRequest listBucketsRequest = ListDirectoryBucketsRequest.builder().build();

            // Retrieve the list of buckets
            ListDirectoryBucketsResponse response = s3Client.listDirectoryBuckets(listBucketsRequest);

            // Extract bucket names
            List<String> bucketNames = response.buckets().stream()
                    .map(Bucket::name)
                    .collect(Collectors.toList());

            return bucketNames;
        } catch (S3Exception e) {
            logger.error("Failed to list buckets: {} - Error code: {}", e.awsErrorDetails().errorMessage(),
                    e.awsErrorDetails().errorCode(), e);
            throw e;
        }
    }

    /**
     * Deletes the specified S3 directory bucket.
     *
     * @param s3Client   The S3 client used to interact with S3
     * @param bucketName The name of the bucket to delete
     */
    public static void deleteDirectoryBucket(S3Client s3Client, String bucketName) {
        try {
            DeleteBucketRequest deleteBucketRequest = DeleteBucketRequest.builder()
                    .bucket(bucketName)
                    .build();
            s3Client.deleteBucket(deleteBucketRequest);
        } catch (S3Exception e) {
            logger.error("Failed to delete bucket: " + bucketName + " - Error code: " + e.awsErrorDetails().errorCode(),
                    e);
            throw e;
        }
    }

}


```


* For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.




	+ [CreateBucket](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucket "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucket")
	+ [ListDirectoryBuckets](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListDirectoryBuckets")





###### Code examples

* [Basics](service_code_examples_s3-directory-buckets_basics.md "service_code_examples_s3-directory-buckets_basics.md")


	+ [Hello Amazon S3 directory buckets](s3-directory-buckets_example_s3-directory-buckets_Hello_section.md "s3-directory-buckets_example_s3-directory-buckets_Hello_section.md")
	+ [Learn the basics](s3-directory-buckets_example_s3-directory-buckets_Scenario_ExpressBasics_section.md "s3-directory-buckets_example_s3-directory-buckets_Scenario_ExpressBasics_section.md")
	+ [Actions](service_code_examples_s3-directory-buckets_actions.md "service_code_examples_s3-directory-buckets_actions.md")
	
	
		- [AbortMultipartUpload](s3-directory-buckets_example_s3-directory-buckets_AbortMultipartUpload_section.md "s3-directory-buckets_example_s3-directory-buckets_AbortMultipartUpload_section.md")
		- [CompleteMultipartUpload](s3-directory-buckets_example_s3-directory-buckets_CompleteMultipartUpload_section.md "s3-directory-buckets_example_s3-directory-buckets_CompleteMultipartUpload_section.md")
		- [CopyObject](s3-directory-buckets_example_s3-directory-buckets_CopyObject_section.md "s3-directory-buckets_example_s3-directory-buckets_CopyObject_section.md")
		- [CreateBucket](s3-directory-buckets_example_s3-directory-buckets_CreateBucket_section.md "s3-directory-buckets_example_s3-directory-buckets_CreateBucket_section.md")
		- [CreateMultipartUpload](s3-directory-buckets_example_s3-directory-buckets_CreateMultipartUpload_section.md "s3-directory-buckets_example_s3-directory-buckets_CreateMultipartUpload_section.md")
		- [CreateSession](s3-directory-buckets_example_s3-directory-buckets_CreateSession_section.md "s3-directory-buckets_example_s3-directory-buckets_CreateSession_section.md")
		- [DeleteBucket](s3-directory-buckets_example_s3-directory-buckets_DeleteBucket_section.md "s3-directory-buckets_example_s3-directory-buckets_DeleteBucket_section.md")
		- [DeleteBucketEncryption](s3-directory-buckets_example_s3-directory-buckets_DeleteBucketEncryption_section.md "s3-directory-buckets_example_s3-directory-buckets_DeleteBucketEncryption_section.md")
		- [DeleteBucketPolicy](s3-directory-buckets_example_s3-directory-buckets_DeleteBucketPolicy_section.md "s3-directory-buckets_example_s3-directory-buckets_DeleteBucketPolicy_section.md")
		- [DeleteObject](s3-directory-buckets_example_s3-directory-buckets_DeleteObject_section.md "s3-directory-buckets_example_s3-directory-buckets_DeleteObject_section.md")
		- [DeleteObjects](s3-directory-buckets_example_s3-directory-buckets_DeleteObjects_section.md "s3-directory-buckets_example_s3-directory-buckets_DeleteObjects_section.md")
		- [GetBucketEncryption](s3-directory-buckets_example_s3-directory-buckets_GetBucketEncryption_section.md "s3-directory-buckets_example_s3-directory-buckets_GetBucketEncryption_section.md")
		- [GetBucketPolicy](s3-directory-buckets_example_s3-directory-buckets_GetBucketPolicy_section.md "s3-directory-buckets_example_s3-directory-buckets_GetBucketPolicy_section.md")
		- [GetObject](s3-directory-buckets_example_s3-directory-buckets_GetObject_section.md "s3-directory-buckets_example_s3-directory-buckets_GetObject_section.md")
		- [GetObjectAttributes](s3-directory-buckets_example_s3-directory-buckets_GetObjectAttributes_section.md "s3-directory-buckets_example_s3-directory-buckets_GetObjectAttributes_section.md")
		- [HeadBucket](s3-directory-buckets_example_s3-directory-buckets_HeadBucket_section.md "s3-directory-buckets_example_s3-directory-buckets_HeadBucket_section.md")
		- [HeadObject](s3-directory-buckets_example_s3-directory-buckets_HeadObject_section.md "s3-directory-buckets_example_s3-directory-buckets_HeadObject_section.md")
		- [ListDirectoryBuckets](s3-directory-buckets_example_s3-directory-buckets_ListDirectoryBuckets_section.md "s3-directory-buckets_example_s3-directory-buckets_ListDirectoryBuckets_section.md")
		- [ListMultipartUploads](s3-directory-buckets_example_s3-directory-buckets_ListMultipartUploads_section.md "s3-directory-buckets_example_s3-directory-buckets_ListMultipartUploads_section.md")
		- [ListObjectsV2](s3-directory-buckets_example_s3-directory-buckets_ListObjectsV2_section.md "s3-directory-buckets_example_s3-directory-buckets_ListObjectsV2_section.md")
		- [ListParts](s3-directory-buckets_example_s3-directory-buckets_ListParts_section.md "s3-directory-buckets_example_s3-directory-buckets_ListParts_section.md")
		- [PutBucketEncryption](s3-directory-buckets_example_s3-directory-buckets_PutBucketEncryption_section.md "s3-directory-buckets_example_s3-directory-buckets_PutBucketEncryption_section.md")
		- [PutBucketPolicy](s3-directory-buckets_example_s3-directory-buckets_PutBucketPolicy_section.md "s3-directory-buckets_example_s3-directory-buckets_PutBucketPolicy_section.md")
		- [PutObject](s3-directory-buckets_example_s3-directory-buckets_PutObject_section.md "s3-directory-buckets_example_s3-directory-buckets_PutObject_section.md")
		- [UploadPart](s3-directory-buckets_example_s3-directory-buckets_UploadPart_section.md "s3-directory-buckets_example_s3-directory-buckets_UploadPart_section.md")
		- [UploadPartCopy](s3-directory-buckets_example_s3-directory-buckets_UploadPartCopy_section.md "s3-directory-buckets_example_s3-directory-buckets_UploadPartCopy_section.md")
* [Scenarios](service_code_examples_s3-directory-buckets_scenarios.md "service_code_examples_s3-directory-buckets_scenarios.md")


	+ [Create a presigned URL to get an object](s3-directory-buckets_example_s3-directory-buckets_GeneratePresignedGetURLForDirectoryBucket_section.md "s3-directory-buckets_example_s3-directory-buckets_GeneratePresignedGetURLForDirectoryBucket_section.md")
