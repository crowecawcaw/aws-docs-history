# Deleting a directory bucket

You can delete only empty Amazon S3 directory buckets. Before you delete your
directory bucket, you must delete all objects in the bucket and abort all in-progress
multipart uploads.

If the directory bucket is attached to an access point, you must delete the access point first. For more information, see [Delete your access point for directory buckets](access-points-directory-buckets-delete.md "access-points-directory-buckets-delete.md").

To empty a directory bucket, see [Emptying a directory bucket](directory-bucket-empty.md "directory-bucket-empty.md"). To abort an in-progress multipart upload, see
[Aborting a multipart upload](abort-mpu.md "abort-mpu.md").

To delete a general purpose bucket, see [Deleting a general purpose bucket](delete-bucket.md "delete-bucket.md").

After you empty your directory bucket and abort all in-progress multipart uploads, you can
delete your bucket.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. In the **Directory buckets** list, choose the option button next to
   the bucket that you want to delete.
4. Choose **Delete**.
5. On the **Delete bucket** page, enter the name of the bucket in the
   text field to confirm the deletion of your bucket.

###### Important

Deleting a directory bucket can't be undone. 6. To delete your directory bucket, choose **Delete bucket**.
The following examples delete a directory bucket by using the AWS SDK for Java 2.x and
AWS SDK for Python (Boto3).

SDK for Java 2.x

```
public static void deleteBucket(S3Client s3Client, String bucketName) {

    try {
        DeleteBucketRequest del = DeleteBucketRequest.builder()
                .bucket(bucketName)
                .build();
        s3Client.deleteBucket(del);
        System.out.println("Bucket " + bucketName + " has been deleted");
    }
    catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
}
```

SDK for Python

```
import logging
import boto3
from botocore.exceptions import ClientError

def delete_bucket(s3_client, bucket_name):
    '''
    Delete a directory bucket in a specified Region

    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket to delete; for example, '`doc-example-bucket`--`usw2-az1`--x-s3'
    :return: True if bucket is deleted, else False
    '''

    try:
        s3_client.delete_bucket(Bucket = bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    bucket_name = '`BUCKET_NAME`'
    region = '`us-west-2`'
    s3_client = boto3.client('s3', region_name = region)
```

This example shows how to delete a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

```
aws s3api delete-bucket --bucket `bucket-base-name`--`zone-id`--x-s3 --region `us-west-2`
```

For more information, see [delete-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html                 ") in the AWS Command Line Interface.
