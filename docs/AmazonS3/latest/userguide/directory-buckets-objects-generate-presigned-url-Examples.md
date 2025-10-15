# Generating presigned URLs to share objects 
 directory bucket

 The following code examples show how to generate 
 presigned URLs to share objects from an Amazon S3 directory bucket.

The following example command shows how you can use the AWS CLI
 to generate a presigned URL for an object from Amazon S3. This command generates a presigned URL for an object
 ``KEY_NAME`` from the directory bucket
 ``bucket-base-name`--`zone-id`--x-s3`. To run this command, replace the ``user input placeholders``
 with your own information.


```
aws s3 presign s3://`bucket-base-name`--`zone-id`--x-s3/`KEY_NAME` --expires-in 7200
```
For more information, see [presign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html") in the
 *AWS CLI Command Reference*.
