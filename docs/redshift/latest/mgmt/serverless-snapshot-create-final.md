Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a final snapshot

To create a final snapshot of all data within a namespace before deleting the
namespace, perform the steps in the following procedure.

###### To create a final snapshot

1. On the Amazon Redshift Serverless console, choose **Namespace
   configuration**.
2. Choose the namespace to delete.
3. Choose **Actions**, **Delete**.
4. Choose **Create final snapshot**.
5. Enter a name for the snapshot.
6. Enter delete.
7. Choose **Delete**.
