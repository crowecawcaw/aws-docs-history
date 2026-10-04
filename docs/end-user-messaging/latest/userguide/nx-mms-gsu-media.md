

# Step 2: Store your media in Amazon S3
<a name="nx-mms-gsu-media"></a>

AWS End User Messaging sends MMS media from an Amazon S3 bucket. You store your image, audio, video, or other media files in Amazon S3, and reference each file by its Amazon S3 URI when you send. The Amazon S3 bucket must be in the same AWS account and AWS Region as your MMS-capable origination identity, and the identity that calls `send-media-message` must have read access to the bucket.

**To store MMS media in Amazon S3**

1. Create an Amazon S3 bucket in the same AWS Region as your origination identity, using the [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html) command:

   ```
   aws s3api create-bucket --region {{us-east-1}} --bucket {{BucketName}}
   ```

1. Upload each media file to the bucket, using the [cp](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-copy) command:

   ```
   aws s3 cp {{SourceFilePathAndName}} s3://{{BucketName}}/{{FileName}}
   ```

1. Note the Amazon S3 URI of each file. This is the value you pass to the `media-urls` parameter when you send. Each message carries a single media file, so you pass one Amazon S3 URI:

   ```
   s3://{{BucketName}}/{{FileName}}
   ```

Grant the identity that sends MMS read access to the bucket. For example policies, see [Identity-based policy examples for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html) in the *Amazon S3 User Guide*. For the supported media types and size limits, see the [SendMediaMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.html) API reference.