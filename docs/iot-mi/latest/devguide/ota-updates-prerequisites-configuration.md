

# Prerequisites for OTA updates
<a name="ota-updates-prerequisites-configuration"></a>

Before creating Over-the-Air (OTA) tasks, you need to complete the following configuration tasks in your environment.

## Configure Amazon S3 access
<a name="configure-amazon-s3-access"></a>

To enable OTA updates, you must upload your job documents to an Amazon Simple Storage Service (Amazon S3) bucket and configure the appropriate access permissions for the bucket.

**To configure Amazon S3 access**

1. Determine which S3 bucket you want to use for OTA updates.

1. Upload your OTA job document to the bucket.

1. Configure the bucket policy to allow AWS IoT Managed Integrations to access your job documents in the bucket:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PolicyForS3JobDocument",
         "Effect": "Allow",
         "Principal": {
           "Service": "iotmanagedintegrations.amazonaws.com"
         },
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{111122223333}}"
           }
         }
       }
     ]
   }
   ```

   Update the preceding policy with the correct values for your environment. In the `Resource` element, replace `{{amzn-s3-demo-bucket}}` with the name of your bucket. To restrict access to a specific location in the bucket, also add the prefix for the path to the location—for example, `arn:aws:s3:::amzn-s3-demo-bucket/my-OTA-job-documents/*`. In the `Condition` block, replace `{{111122223333}}` with the account ID for your AWS account. 