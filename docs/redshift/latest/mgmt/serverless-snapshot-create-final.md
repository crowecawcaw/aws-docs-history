

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating a final snapshot
<a name="serverless-snapshot-create-final"></a>

To create a final snapshot of all data within a namespace before deleting the namespace, perform the steps in the following procedure.

**To create a final snapshot**

1. On the Amazon Redshift Serverless console, choose **Namespace configuration**.

1. Choose the namespace to delete.

1. Choose **Actions**, **Delete**.

1. Choose **Create final snapshot**.

1. Enter a name for the snapshot.

1. Enter delete.

1. Choose **Delete**.