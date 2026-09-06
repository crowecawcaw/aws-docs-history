

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Troubleshooting Change Manager
<a name="change-manager-troubleshooting"></a>

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 

Use the following information to help you troubleshoot problems with Change Manager, a tool in AWS Systems Manager.

**Topics**
+ [“Group {{{GUID}}} not found” error during change request approvals when using Active Directory (groups](#change-manager-troubleshooting-sso)

## “Group {{{GUID}}} not found” error during change request approvals when using Active Directory (groups
<a name="change-manager-troubleshooting-sso"></a>

**Problem**: When AWS IAM Identity Center (IAM Identity Center) is used for user identity management, a member of an Active Directory group who is granted approval permissions in Change Manager receives a “not authorized” or “group not found” error.
+ **Solution**: When you select Active Directory groups in IAM Identity Center for access to the AWS Management Console, the system schedules a periodic synchronization that copies information from those Active Directory groups into IAM Identity Center. This process must complete before users authorized through Active Directory group membership can successfully approve a request. For more information, see [Connect to your Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html) in the *AWS IAM Identity Center User Guide*.