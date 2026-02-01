Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restoring a recovery point

Recovery points in Amazon Redshift Serverless are created approximately every 30 minutes and saved for
24 hours. To restore a recovery point to a serverless namespace, perform the steps in the following
procedure

###### To restore a recovery point to a serverless namespace

1. On the Amazon Redshift Serverless console, choose **Data backup**.
2. Under **Recovery points**, choose the **Creation
   time** of the recovery point that you want to restore.
3. Choose **Restore**. You can only restore to namespaces whose
   statuses are Available.
4. Enter **restore** in the text input field and choose
   **Restore**.
