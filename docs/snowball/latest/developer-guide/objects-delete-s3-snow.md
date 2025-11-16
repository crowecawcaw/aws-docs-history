AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Deleting objects in buckets in Amazon S3 compatible storage on Snowball Edge

You can delete one or more objects from an Amazon S3 compatible storage on Snowball Edge bucket. The following example
deletes an object named `sample-object.xml` using the AWS CLI. To
use this command, replace each user input placeholder with your own information.

```
aws s3api delete-object --bucket `sample-bucket` --key `key` --endpoint-url `s3api-endpoint-ip` --profile `your-profile`
```

For more information about this command, see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-object.html") in the _AWS CLI Command Reference_.

The following Amazon S3 compatible storage on Snowball Edge example deletes an object in a bucket using the SDK for
Java. To use this example, specify the key name for the object that you want to delete.
For more information, see [DeleteObject](../../../AmazonS3/latest/API/API_DeleteObject.md "../../../AmazonS3/latest/API/API_DeleteObject.md") in the Amazon Simple Storage Service API Reference.

```

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.DeleteObjectRequest;

public class DeleteObject {
    public static void main(String[] args) {
        String bucketName = "*** Bucket name ***";
        String keyName = "*** key name ****";

        try {
            // This code expects that you have AWS credentials set up per:
            // https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                    .enableUseArnRegion()
                    .build();

            DeleteObjectRequest deleteObjectRequest = DeleteObjectRequest.builder()
                    .bucket(bucketName)
                    .key(keyName)
                    .build()));
            s3Client.deleteObject(deleteObjectRequest);
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
