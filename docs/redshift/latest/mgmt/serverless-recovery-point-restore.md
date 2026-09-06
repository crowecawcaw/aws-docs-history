

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Restoring a recovery point
<a name="serverless-recovery-point-restore"></a>

Recovery points in Amazon Redshift Serverless are created approximately every 30 minutes and saved for 24 hours. To restore a recovery point to a serverless namespace, perform the steps in the following procedure

**To restore a recovery point to a serverless namespace**

1. On the Amazon Redshift Serverless console, choose **Data backup**.

1. Under **Recovery points**, choose the **Creation time** of the recovery point that you want to restore.

1. Choose **Restore**. You can only restore to namespaces whose statuses are Available.

1. Enter **restore** in the text input field and choose **Restore**.