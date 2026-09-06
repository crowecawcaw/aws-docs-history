

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Converting a recovery point
<a name="serverless-recovery-point-convert"></a>

Recovery points in Amazon Redshift Serverless are created approximately every 30 minutes and saved for 24 hours. To convert a recovery point to a snapshot, perform the steps in the following procedure.

**To convert a recovery point to a snapshot**

1. On the Amazon Redshift Serverless console, choose **Data backup**.

1. Under **Recovery points**, choose the **Creation time** of the recovery point that you want to convert to a snapshot.

1. Choose **Create snapshot from recovery point**.

1. Enter a **Snapshot identifier**.

1. Choose **Create**.