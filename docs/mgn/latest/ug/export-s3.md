NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Exporting your data inventory to an S3 bucket

To export your inventory to an S3 bucket, take the following steps:

1. Select **Export** from the left-hand navigation
   menu (under **Import and export**) and you’ll be
   navigated to the **Export inventory** tab.
2. Select **Export to S3 bucket**.
3. Click **Browse S3** to choose the Amazon S3 storage
   target to which you want to export the data.
4. Specify the Amazon S3 bucket owner (the current AWS account or a different one)
   according to your preferences. If you select a different AWS account, you must enter
   the bucket owner’s account ID.

###### Note

    * You must have write privileges to export an inventory to a specific
     bucket.
    * It is highly recommended that you [apply S3 bucket security practices](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") where your CSV files are stored.
     [Learn more about S3 permissions and policies.](../../../AmazonS3/latest/userguide/access-policy-language-overview.md "../../../AmazonS3/latest/userguide/access-policy-language-overview.md")

5. Click **Export**.
