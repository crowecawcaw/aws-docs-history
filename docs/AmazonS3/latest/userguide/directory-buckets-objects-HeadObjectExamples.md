# Retrieving object metadata

from directory buckets

The following AWS SDK and AWS CLI examples show how to use the `HeadObject` and `GetObjectAttributes`
API operation to retrieve metadata from an object in an Amazon S3 directory bucket without
returning the object itself.

SDK for Java 2.x

###### Example

```

public static void headObject(S3Client s3Client, String bucketName, String objectKey) {
     try {
         HeadObjectRequest headObjectRequest = HeadObjectRequest
                 .builder()
                 .bucket(bucketName)
                 .key(objectKey)
                 .build();
         HeadObjectResponse response = s3Client.headObject(headObjectRequest);
         System.out.format("Amazon S3 object: \"%s\" found in bucket: \"%s\" with ETag: \"%s\"", objectKey, bucketName, response.eTag());
     }
     catch (S3Exception e) {
         System.err.println(e.awsErrorDetails().errorMessage());
```

The following `head-object` example command shows how you can use the AWS CLI to
retrieve metadata from an object. To run this command, replace the `user input placeholders`
with your own information.

```
aws s3api head-object --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME`
```

For more information, see [head-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html") in the
_AWS CLI Command Reference_.

The following `get-object-attributes` example command shows how you can use the AWS CLI to
retrieve metadata from an object. To run this command, replace the `user input placeholders`
with your own information.

```
aws s3api get-object-attributes --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME` --object-attributes "StorageClass" "ETag" "ObjectSize"
```

For more information, see [get-object-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html") in the
_AWS CLI Command Reference_.
