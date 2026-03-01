# Deleting share requests in AWS Audit Manager

When you no longer need a share request, you can delete it from your Audit Manager environment.
This enables you to clean up your workspace and focus on the requests that are relevant to
your current tasks and priorities.

When you delete a share request, only the request itself is deleted. The shared
framework itself remains in your framework library.

## Prerequisites

The following procedure assumes that you have previously sent or received a share
request. You can't delete share requests that have a status of _active_ or _replicating_.

Make sure your IAM identity has appropriate permissions to delete a share request in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To delete a share request

1. From the navigation pane, choose **Share requests**.
2. Choose either the **Sent requests** or the **Received
   requests** tab.
3. Select the framework that you no longer want and choose
   **Delete**.
4. In the pop-up window that appears, choose **Delete**.

## Additional resources

To find solutions to issues that you might encounter, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md").
