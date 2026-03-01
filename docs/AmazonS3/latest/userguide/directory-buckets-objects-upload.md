# Uploading objects to a directory bucket

After you create an Amazon S3 directory bucket, you can upload objects to it. The following
examples show how to upload an object to a directory bucket by using the S3 console and the
AWS SDKs. For information about bulk object upload operations with S3 Express One Zone, see [Object management](directory-bucket-high-performance.md#s3-express-features-object-management "directory-bucket-high-performance.md#s3-express-features-object-management").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. Choose the name of the bucket that you want to upload your folders or files to.
4. In the **Objects** list, choose **Upload**.
5. On the **Upload** page, do one of the following:
   - Drag and drop files and folders to the dotted upload area.
   - Choose **Add files** or **Add folder**,
     choose the files or folders to upload, and then choose **Open**
     or
     **Upload**.

6. Under **Checksums**, choose the **Checksum
   function** that you want to use.

(Optional) If you're uploading a single object that's less than 16 MB in size, you can
also specify a precalculated checksum value. When you provide a precalculated value,
Amazon S3 compares it with the value that it calculates by using the selected checksum
function. If the values don't match, the upload won't start. 7. The options in the **Permissions** and
**Properties** sections are automatically set to default settings
and can't be modified. Block Public Access is automatically enabled, and S3 Versioning
and S3 Object Lock can't be enabled for directory buckets.

(Optional) If you want to add metadata in key-value pairs to your objects, expand the
**Properties** section, and then in the
**Metadata** section, choose **Add
metadata**. 8. To upload the listed files and folders, choose **Upload**.

Amazon S3 uploads your objects and folders. When the upload is finished, you see a success
message on the **Upload: status** page.

SDK for Java 2.x

###### Example

```
public static void putObject(S3Client s3Client, String bucketName, String objectKey, Path filePath) {
       //Using File Path to avoid loading the whole file into memory
       try {
           PutObjectRequest putObj = PutObjectRequest.builder()
                   .bucket(bucketName)
                   .key(objectKey)
                   //.metadata(metadata)
                   .build();
           s3Client.putObject(putObj, filePath);
           System.out.println("Successfully placed " + objectKey +" into bucket "+bucketName);

       }

       catch (S3Exception e) {
           System.err.println(e.getMessage());
           System.exit(1);
       }
}
```

SDK for Python

###### Example

```
import boto3
import botocore
from botocore.exceptions import ClientError


def put_object(s3_client, bucket_name, key_name, object_bytes):
    """
    Upload data to a directory bucket.
    :param s3_client: The boto3 S3 client
    :param bucket_name: The bucket that will contain the object
    :param key_name: The key of the object to be uploaded
    :param object_bytes: The data to upload
    """
    try:
        response = s3_client.put_object(Bucket=bucket_name, Key=key_name,
                             Body=object_bytes)
        print(f"Upload object '{key_name}' to bucket '{bucket_name}'.")
        return response
    except ClientError:
        print(f"Couldn't upload object '{key_name}' to bucket '{bucket_name}'.")
        raise

def main():
    # Share the client session with functions and objects to benefit from S3 Express One Zone auth key
    s3_client = boto3.client('s3')
    # Directory bucket name must end with --`zone-id`--x-s3
    resp = put_object(s3_client, '`doc-bucket-example`--`use1-az5`--x-s3', '`sample.txt`', b'`Hello, World!`')
    print(resp)

if __name__ == "__main__":
    main()
```

The following `put-object` example command shows how you can use the
AWS CLI to upload an object from Amazon S3. To run this command, replace the
`user input placeholders` with your
own information.

```
aws s3api put-object --bucket `bucket-base-name`--`zone-id`--x-s3 --key `sampleinut/file001.bin` --body `bucket-seed/file001.bin`
```

For more information, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html") in the
_AWS CLI Command Reference_.

###### Topics

- [Using multipart uploads with directory buckets](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md")
