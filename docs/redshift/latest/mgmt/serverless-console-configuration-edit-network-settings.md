Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Editing

security and encryption

Amazon Redshift Serverless is secured by means of KMS encryption. You can update
encryption settings via the console:

1. Choose **Namespace configuration** from the
   main menu on the console, choose the namespace to edit, and choose
   **Edit** on the **Security and
   encryption** tab. A dialog appears.
2. You can select **Customize encryption settings** and
   then **Choose an AWS customer managed key** to change
   the key used to encrypt your resources.
3. For **Audit logging**, choose the logs to export.
   Each log type specifies different metadata.
4. To complete the configuration update, choose **Save
   changes**.
