• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Troubleshooting Change Manager

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

Use the following information to help you troubleshoot problems with Change Manager, a tool
in AWS Systems Manager.

###### Topics

- [“Group
  {GUID} not found” error during change request
  approvals when using Active Directory (groups](#change-manager-troubleshooting-sso "#change-manager-troubleshooting-sso")

## “Group

`{GUID}` not found” error during change request
approvals when using Active Directory (groups

**Problem**: When AWS IAM Identity Center (IAM Identity Center) is used for user
identity management, a member of an Active Directory group who is granted approval
permissions in Change Manager receives a “not authorized” or “group not found”
error.

- **Solution**: When you select Active
  Directory groups in IAM Identity Center for access to the AWS Management Console, the system schedules
  a periodic synchronization that copies information from those Active
  Directory groups into IAM Identity Center. This process must complete before users
  authorized through Active Directory group membership can successfully
  approve a request. For more information, see [Connect to your Microsoft AD directory](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md") in the
  _AWS IAM Identity Center User Guide_.
