

# Step 1: Set up your Amazon S3 infrastructure
<a name="inbound-tutorial-step1-s3-setup"></a>

AWS B2B Data Interchange requires Amazon S3 buckets to store input EDI documents and output transformed files. You need to configure proper permissions and enable EventBridge notifications for the service to automatically process your documents.

## Create Amazon S3 buckets
<a name="inbound-create-s3-buckets"></a>

**To create input and output buckets**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

1. For **Bucket name**, enter **my-b2bi-input-bucket-{{your-account-id}}**.

1. Select your preferred AWS Region (ensure it matches where you'll use AWS B2B Data Interchange).

1. Leave other settings as default and choose **Create bucket**.

1. Repeat steps 2-5 to create an output bucket named **my-b2bi-output-bucket-{{your-account-id}}**.

## Configure EventBridge notifications
<a name="inbound-configure-eventbridge-notifications"></a>

**To enable EventBridge notifications**

1. Navigate to your input bucket.

1. Choose the **Properties** tab.

1. Scroll to **Amazon EventBridge** section.

1. Choose **Edit**.

1. Select **On** and choose **Save changes**.

1. Repeat for your output bucket.

## Required fields
<a name="inbound-step1-required-fields"></a>
+ Bucket names (must be globally unique)
+ AWS Region (must match your AWS B2B Data Interchange region)
+ EventBridge notifications: Enabled