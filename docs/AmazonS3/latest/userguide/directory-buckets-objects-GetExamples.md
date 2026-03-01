# Downloading an object from a directory bucket

The following code examples show how to read data from (download) an object in an Amazon S3
directory bucket by using the `GetObject` API operation.

SDK for Java 2.x

###### Example

The following code example shows how to read data from an object in a directory bucket
by using the AWS SDK for Java 2.x.

```
public static void getObject(S3Client s3Client, String bucketName, String objectKey) {
     try {
         GetObjectRequest objectRequest = GetObjectRequest
            .builder()
            .key(objectKey)
            .bucket(bucketName)
            .build();

         ResponseBytes GetObjectResponse objectBytes = s3Client.getObjectAsBytes(objectRequest);
         byte[] data = objectBytes.asByteArray();

         //Print object contents to console
         String s = new String(data, StandardCharsets.UTF_8);
         System.out.println(s);
    }

    catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
}
```

SDK for Python

###### Example

The following code example shows how to read data from an object in a directory bucket
by using the AWS SDK for Python (Boto3).

```
import boto3
from botocore.exceptions import ClientError
from botocore.response import StreamingBody

def get_object(s3_client: boto3.client, bucket_name: str, key_name: str) -> StreamingBody:
    """
    Gets the object.
    :param s3_client:
    :param bucket_name: The bucket that contains the object.
    :param key_name: The key of the object to be downloaded.
    :return: The object data in bytes.
    """
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key_name)
        body = response['Body'].read()
        print(f"Got object '{key_name}' from bucket '{bucket_name}'.")
    except ClientError:
        print(f"Couldn't get object '{key_name}' from bucket '{bucket_name}'.")
        raise
    else:
        return body

def main():
    s3_client = boto3.client('s3')
    resp = get_object(s3_client, '`doc-example-bucket`--`use1-az4`--x-s3', '`sample.txt`')
    print(resp)

if __name__ == "__main__":
     main()
```

The following `get-object` example command shows how you can use the AWS CLI
to download an object from Amazon S3. This command gets the object
`KEY_NAME` from the directory bucket
``bucket-base-name`--`zone-id`--x-s3`. The object will be downloaded to a file
 named ``LOCAL_FILE_NAME`. To run this command, replace the `user input placeholders``
with your own information.

```
aws s3api get-object --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME` `LOCAL_FILE_NAME`
```

For more information, see [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html") in the
_AWS CLI Command Reference_.
