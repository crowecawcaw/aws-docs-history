

# Step 4: Create a trading capability
<a name="inbound-tutorial-step4-capability"></a>

A trading capability connects your transformer to specific Amazon S3 directories and defines the automated workflow. It monitors your input directory for new EDI files and automatically processes them using your transformer, placing results in the output directory.

**To create a trading capability**

1. In the AWS B2B Data Interchange console, choose **Trading capabilities**.

1. Choose **Create trading capability**.

1. In the **Trading capability settings** section, enter:
   + **Trading capability name**: **Inbound-850-Processing**
   + **EDI direction**: Select **Inbound**
   + **X12 version**: Select **4010**
   + **X12 transaction set**: Select **850 - Purchase Order**
   + **Apply transformer**: Select **X12-850-to-JSON-Transformer**

1. In the **Configure directories** section:

   1. **Input directory**: Choose **Browse S3** and select **my-b2bi-input-bucket-{{your-account-id}}**.

   1. After selecting your input bucket, the console displays a **Copy policy** button. Choose **Copy policy** to copy the automatically generated input bucket policy to your clipboard. Save this policy text in a text editor for the next step.

   1. **Output directory**: Choose **Browse S3** and select **my-b2bi-output-bucket-{{your-account-id}}**.

   1. After selecting your output bucket, choose **Copy policy** to copy the automatically generated output bucket policy to your clipboard. Save this policy text in a text editor for the next step.

   1. Choose **Validate input S3 setup** to verify your input directory configuration. This checks bucket region, EventBridge events, bucket policies, ownership, and KMS permissions.

   1. Choose **Validate output S3 setup** to verify your output directory configuration. This performs the same checks as input validation plus verifies ACL is disabled.
**Note**  
If validation shows warnings for bucket or KMS policies, you can proceed as these are approximations. You'll configure the actual policies in the next section.

1. Choose **Create capability**.

## Configure Amazon S3 bucket policies
<a name="inbound-configure-s3-bucket-policies-tutorial"></a>

**To apply bucket policies**

1. Navigate to your input bucket in the Amazon S3 console.

1. Choose the **Permissions** tab.

1. In the **Bucket policy** section, choose **Edit**.

1. Paste the input bucket policy you copied from the trading capability configuration in the previous step.

1. Choose **Save changes**.

1. Repeat steps 1-5 for your output bucket with the output bucket policy.

## Required fields
<a name="inbound-step4-required-fields"></a>
+ Trading capability name
+ EDI direction
+ X12 version
+ X12 transaction set
+ Transformer selection
+ Input directory Amazon S3 path
+ Output directory Amazon S3 path