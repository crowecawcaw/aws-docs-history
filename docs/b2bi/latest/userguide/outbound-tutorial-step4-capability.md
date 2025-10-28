# Step 4: Create a trading

capability

A trading capability connects your outbound transformer to specific Amazon S3 directories
and defines the automated workflow. It monitors your input directory for new JSON files
and automatically processes them using your transformer, placing EDI results in the
output directory.

###### To create an outbound trading capability

1. In the AWS B2B Data Interchange console, choose **Trading
   capabilities**.
2. Choose **Create trading capability**.
3. In the **Trading capability settings** section, enter:
   - **Trading capability name**:
     `Outbound-850-Generation`
   - **EDI direction**: Select
     **Outbound**
   - **X12 version**: Select
     **4010**
   - **X12 transaction set**: Select
     **850** (Purchase Order)
   - **Apply transformer**: Select
     **JSON-to-X12-850-Transformer**

4. In the **Configure directories** section:
   1. **Input directory**: Choose **Browse
      S3** and select
      `my-b2bi-outbound-input-bucket-`your-account-id``.
   2. After selecting your input bucket, the console displays a
      **Copy policy** button. Choose **Copy
      policy** to copy the automatically generated input bucket
      policy to your clipboard. Save this policy text in a text editor for the
      next step.
   3. **Output directory**: Choose **Browse
      S3** and select
      `my-b2bi-outbound-output-bucket-`your-account-id``.
   4. After selecting your output bucket, choose **Copy
      policy** to copy the automatically generated output bucket
      policy to your clipboard. Save this policy text in a text editor for the
      next step.

   ###### Note

   You'll validate your S3 setup after configuring the bucket
   policies in the next section.

5. Choose **Create capability**.

## Configure Amazon S3

bucket policies

###### To apply bucket policies

1. Navigate to your input bucket in the Amazon S3 console.
2. Choose the **Permissions** tab.
3. In the **Bucket policy** section, choose
   **Edit**.
4. Paste the input bucket policy you copied from the trading capability
   configuration in the previous step.
5. Choose **Save changes**.
6. Repeat steps 1-5 for your output bucket with the output bucket
   policy.
7. Return to the trading capability configuration page and choose
   **Validate input S3 setup** to verify your input
   directory configuration. This checks bucket region, EventBridge events, bucket
   policies, ownership, and KMS permissions.
8. Choose **Validate output S3 setup** to verify your output
   directory configuration. This performs the same checks as input validation
   plus verifies ACL is disabled.

###### Note

Now that you've configured the bucket policies, the validation should
pass without warnings. Any remaining warnings can typically be ignored
as they are approximations.

## Required fields

- Trading capability name
- EDI direction (must be Outbound)
- X12 version
- X12 transaction set
- Transformer selection
- Input directory Amazon S3 path
- Output directory Amazon S3 path
