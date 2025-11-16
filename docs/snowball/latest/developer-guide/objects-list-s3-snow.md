AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Listing objects in a bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge

The following example lists objects in an Amazon S3 compatible storage on Snowball Edge bucket using the AWS CLI. The SDK
command is `s3-snow:ListObjectsV2`. To use this command, replace each user
input placeholder with your own information.

```
aws s3api list-objects-v2 --bucket `sample-bucket` --endpoint-url `s3api-endpoint-ip` --profile `your-profile`
```

For more information about this command, see [list-objects-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html") in the _AWS CLI Command Reference_.

The following Amazon S3 compatible storage on Snowball Edge example lists objects in a bucket using the SDK for Java. To
use this command, replace each user input placeholder with your own information.

This example uses [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md"), which is the latest revision of the ListObjects API
operation. We recommend that you use this revised API operation for application
development. For backward compatibility, Amazon S3 continues to support the prior version of
this API operation.

```

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.ListObjectsV2Request;
import com.amazonaws.services.s3.model.ListObjectsV2Result;
import com.amazonaws.services.s3.model.S3ObjectSummary;

public class ListObjectsV2 {

    public static void main(String[] args) {
        String bucketName = "*** Bucket name ***";

        try {
            // This code expects that you have AWS credentials set up per:
            // https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                    .enableUseArnRegion()
                    .build();

            System.out.println("Listing objects");

            // maxKeys is set to 2 to demonstrate the use of
            // ListObjectsV2Result.getNextContinuationToken()
            ListObjectsV2Request req = new ListObjectsV2Request().withBucketName(bucketName).withMaxKeys(2);
            ListObjectsV2Result result;

            do {
                result = s3Client.listObjectsV2(req);

                for (S3ObjectSummary objectSummary : result.getObjectSummaries()) {
                    System.out.printf(" - %s (size: %d)\n", objectSummary.getKey(), objectSummary.getSize());
                }
                // If there are more than maxKeys keys in the bucket, get a continuation token
                // and list the next objects.
                String token = result.getNextContinuationToken();
                System.out.println("Next Continuation Token: " + token);
                req.setContinuationToken(token);
            } while (result.isTruncated());
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }
}

```
