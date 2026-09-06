

# Create and populate an Amazon S3 source bucket for your unsigned object files
<a name="s3-source-iot"></a>

This topic discusses how to prepare an Amazon S3 bucket and add your unsigned object files to it. 

To create a bucket, sign into the AWS Management Console at [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home) and follow the procedure in [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html). 

While you are configuring the bucket, note the following requirements:
+ Accept the default security option **Block *all* public access**.
+ Set **Bucket Versioning** to **Enable**.

After you create the bucket, you can add objects to it as described in the [Upload an object to your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-an-object-bucket.html) topic.

