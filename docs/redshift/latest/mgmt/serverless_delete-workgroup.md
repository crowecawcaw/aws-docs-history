Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a workgroup

You can delete a workgroup using the console. Before you do this, make sure
that you have your data backed up and snapshots in place. Resources deleted as
part of the workgroup in many cases can't be retrieved.

Complete the following steps:

1. Choose **Amazon Redshift Serverless**, choose
   **Workgroup configuration** and choose
   **Delete Amazon Redshift Serverless instance**.
2. A dialogue opens. When you choose to delete the workgroup, all usage
   limits are removed, all VPC endpoints are removed, and access to VPC
   endpoints is removed.

Type _delete_ and select
**Delete** to confirm.
After you complete the steps, the status of the workgroup is
_Deleting_ and a banner indicates that the workgroup is
being deleted. While the delete process is in progress, some features under the
**Serverless dashboard** are disabled. But you can
configure provisioned clusters on the **Provisioned clusters
dashboard**.

After you delete the workgroup, it doesn't appear with the namespace. You can
choose the **Create workgroup** button to create a new
one.

You can delete an existing workgroup and associate a new workgroup with a
different configuration to the same namespace. When creating the new workgroup,
choose the base capacity that works with the size of the data associated with
the namespace.

You can associate a workgroup with a namespace that was created with a
customer-managed key (CMK). For more information about AWS KMS, see [AWS KMS concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").
