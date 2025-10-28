# Deleting objects from a directory

bucket

You can delete objects from an Amazon S3 directory bucket by using the Amazon S3 console, AWS Command Line Interface
(AWS CLI), or AWS SDKs. For more information, see [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md") and [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone").

###### Warning

- Deleting an object can't be undone.
- This action deletes all specified objects. When deleting folders, wait for the delete
  action to finish before adding new objects to the folder. Otherwise, new objects might be
  deleted as well.

###### Note

When you programmatically delete multiple objects from a directory bucket, note the
following:

- Object keys in `DeleteObjects` requests must contain at least one non-white
  space character. Strings of all white space characters are not supported.
- Object keys in `DeleteObjects` requests cannot contain Unicode control
  characters, except for newline (`\n`), tab (`\t`), and carriage
  return (`\r`).

###### To delete objects

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. Choose the directory bucket that contains the objects that you want to
   delete.
4. Choose the **Objects** tab. In the **Objects** list,
   select the check box to the left of the object or objects that you want to
   delete.
5. Choose
   **Delete**.
6. On the **Delete objects** page, enter `permanently
delete` in the text box.
7. Choose **Delete objects**.

SDK for Java 2.x
The following example deletes objects in a directory bucket by using the AWS SDK for Java 2.x.

```
static void deleteObject(S3Client s3Client, String bucketName, String objectKey) {



        try {

            DeleteObjectRequest del = DeleteObjectRequest.builder()
                    .bucket(bucketName)
                    .key(objectKey)
                    .build();

            s3Client.deleteObject(del);

            System.out.println("Object " + objectKey + " has been deleted");


        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

    }
```

SDK for Python
The following example deletes objects in a directory bucket by using the AWS SDK for Python (Boto3).

```

import logging
import boto3
from botocore.exceptions import ClientError

def delete_objects(s3_client, bucket_name, objects):
    '''
    Delete a list of objects in a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket that contains objects to be deleted; for example, '`doc-example-bucket`--`usw2-az1`--x-s3'
    :param objects: List of dictionaries that specify the key names to delete
    :return: Response output, else False
    '''

    try:
        response = s3_client.delete_objects(
            Bucket = bucket_name,
            Delete = {
                'Objects': objects
            }
        )
        return response
    except ClientError as e:
        logging.error(e)
        return False


if __name__ == '__main__':
    region = '`us-west-2`'
    bucket_name = '`BUCKET_NAME`'
    objects = [
        {
            'Key': '`0.txt`'
        },
        {
            'Key': '`1.txt`'
        },
        {
            'Key': '`2.txt`'
        },
        {
            'Key': '`3.txt`'
        },
        {
            'Key': '`4.txt`'
        }
    ]

    s3_client = boto3.client('s3', region_name = region)
    results = delete_objects(s3_client, bucket_name, objects)
    if results is not None:
        if 'Deleted' in results:
            print (f'Deleted {len(results["Deleted"])} objects from {bucket_name}')
        if 'Errors' in results:
            print (f'Failed to delete {len(results["Errors"])} objects from {bucket_name}')
```

The following `delete-object` example command shows how you can use the AWS CLI
to delete an object from a directory bucket. To run this command, replace the `user input placeholders`
with your own information.

```
aws s3api delete-object --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME`
```

For more information, see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html") in the _AWS CLI Command Reference_.

The following `delete-objects` example command shows how you can use the AWS CLI
to delete objects from a directory bucket. To run this command, replace the `user input placeholders`
with your own information.

The `delete.json` file is as follows:

```

{
    "Objects": [
        {
            "Key": "0.txt"
        },
        {
            "Key": "1.txt"
        },
        {
            "Key": "2.txt"
        },
        {
            "Key": "3.txt"
        }
    ]
}

```

The `delete-objects` example command is as follows:

```
aws s3api delete-objects --bucket `bucket-base-name`--`zone-id`--x-s3 --delete file://`delete.json`
```

For more information, see [delete-objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html") in the _AWS CLI Command Reference_.
