

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Deleting share requests in AWS Audit Manager
<a name="deleting-shared-framework-requests"></a>



When you no longer need a share request, you can delete it from your Audit Manager environment. This enables you to clean up your workspace and focus on the requests that are relevant to your current tasks and priorities. 

When you delete a share request, only the request itself is deleted. The shared framework itself remains in your framework library.

## Prerequisites
<a name="deleting-shared-framework-requests-prerequisites"></a>

The following procedure assumes that you have previously sent or received a share request. You can't delete share requests that have a status of *active* or *replicating*.

Make sure your IAM identity has appropriate permissions to delete a share request in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="deleting-shared-framework-requests-procedure"></a>

**To delete a share request**

1. From the navigation pane, choose **Share requests**.

1. Choose either the **Sent requests** or the **Received requests** tab.

1. Select the framework that you no longer want and choose **Delete**.

1. In the pop-up window that appears, choose **Delete**.

## Additional resources
<a name="deleting-shared-framework-requests-additional-resources"></a>

To find solutions to issues that you might encounter, see [Troubleshooting framework issues](framework-issues.md).