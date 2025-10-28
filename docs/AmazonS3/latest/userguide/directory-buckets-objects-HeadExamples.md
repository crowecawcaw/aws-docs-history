# Determining whether you can access a directory bucket

The following AWS SDK examples show how to use the `HeadBucket` API operation
to determine if an Amazon S3 directory bucket exists and if you have permission to access it.

The following AWS SDK for Java 2.x example shows how to determine if a bucket exists and
if you have permission to access it.

SDK for Java 2.x
AWS SDK for Java 2.x

```

public static void headBucket(S3Client s3Client, String bucketName) {
   try {
        HeadBucketRequest headBucketRequest = HeadBucketRequest
                .builder()
                .bucket(bucketName)
                .build();
        s3Client.headBucket(headBucketRequest);
        System.out.format("Amazon S3 bucket: \"%s\" found.", bucketName);
   }

   catch (S3Exception e) {
       System.err.println(e.awsErrorDetails().errorMessage());
       System.exit(1);
   }
}


```

The following `head-bucket` example command shows how you can use the
AWS CLI to determine if a directory bucket exists and if you have permission to access
it. To run this command, replace the user input placeholders with your own information.

```
aws s3api head-bucket --bucket `bucket-base-name`--`zone-id`--x-s3
```

For more information, see [head-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html") in the
_AWS CLI Command Reference_.
