Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Deleting a namespace

If you want to delete a namespace with an associated workgroup, you have to
first delete the workgroup.

On the Amazon Redshift Serverless console, complete the following steps:

1. Choose **Namespace configuration** from the
   left menu and then choose the namespace you want to delete from the
   list.
2. Choose **Actions** and select **Delete
   namespace**.
3. A dialogue box opens. You can keep your data by creating a manual
   snapshot prior to completing the delete operation.

Type _delete_ and select
**Delete** to confirm.
