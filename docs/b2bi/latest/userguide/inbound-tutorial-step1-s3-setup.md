# Step 1: Set up your Amazon S3

infrastructure

AWS B2B Data Interchange requires Amazon S3 buckets to store input EDI documents and output transformed
files. You need to configure proper permissions and enable EventBridge notifications for the
service to automatically process your documents.

## Create Amazon S3 buckets

###### To create input and output buckets

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. For **Bucket name**, enter
   `my-b2bi-input-bucket-`your-account-id``.
4. Select your preferred AWS Region (ensure it matches where you'll use
   AWS B2B Data Interchange).
5. Leave other settings as default and choose **Create
   bucket**.
6. Repeat steps 2-5 to create an output bucket named
   `my-b2bi-output-bucket-`your-account-id``.

## Configure EventBridge

notifications

###### To enable EventBridge notifications

1. Navigate to your input bucket.
2. Choose the **Properties** tab.
3. Scroll to **Amazon EventBridge** section.
4. Choose **Edit**.
5. Select **On** and choose **Save
   changes**.
6. Repeat for your output bucket.

## Required fields

- Bucket names (must be globally unique)
- AWS Region (must match your AWS B2B Data Interchange region)
- EventBridge notifications: Enabled
