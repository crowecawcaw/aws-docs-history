Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a

namespace

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
