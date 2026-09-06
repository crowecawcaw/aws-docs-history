

# Step 1: Setting up Amazon S3 buckets
<a name="outbound-tutorial-step1-s3-setup"></a>

B2B Data Interchange requires Amazon S3 buckets to store your input JSON files and output EDI documents. You must configure appropriate permissions and enable EventBridge notifications for automated document processing.

## Creating input and output buckets
<a name="outbound-create-s3-buckets"></a>

**To create Amazon S3 buckets**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

1. For the input bucket:
   + For **Bucket name**, enter **my-b2bi-outbound-input-{{account-id}}**.
   + Choose your Region (must match where you'll use B2B Data Interchange).
   + Keep other settings at their defaults.

1. Choose **Create bucket**.

1. Repeat steps 2-4 to create an output bucket named **my-b2bi-outbound-output-{{account-id}}**.

## Enabling EventBridge notifications
<a name="outbound-configure-eventbridge-notifications"></a>

**To enable notifications for your buckets**

1. In the Amazon S3 console, choose your input bucket.

1. Choose the **Properties** tab.

1. In the **EventBridge** section, choose **Edit**.

1. Choose **On**, then choose **Save changes**.

1. Repeat steps 1-4 for your output bucket.

**Important**  
After enabling EventBridge, wait at least 5 minutes before adding files to your buckets. This allows time for the changes to take effect.

## Configuration summary
<a name="outbound-step1-configuration-summary"></a>

Required settings  
+ Input and output bucket names (globally unique)
+ Region (must match your B2B Data Interchange Region)
+ EventBridge notifications enabled on both buckets

Example bucket names  
+ Input: **my-b2bi-outbound-input-{{account-id}}**
+ Output: **my-b2bi-outbound-output-{{account-id}}**