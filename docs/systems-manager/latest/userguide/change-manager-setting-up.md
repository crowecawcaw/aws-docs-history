

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up Change Manager
<a name="change-manager-setting-up"></a>

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 

You can use Change Manager to manage changes for an entire organization, as configured in AWS Organizations, or for a single AWS account.

If you're using Change Manager with an organization, begin with the topic [Setting up Change Manager for an organization (management account)](change-manager-organization-setup.md), and then proceed to [Configuring Change Manager options and best practices](change-manager-account-setup.md).

If you're using Change Manager with a single account, proceed directly to [Configuring Change Manager options and best practices](change-manager-account-setup.md).

**Note**  
If you begin using Change Manager with a single account, but that account is later added to an organizational unit for which Change Manager is allowed, your single account settings are disregarded.

**Topics**
+ [Setting up Change Manager for an organization (management account)](change-manager-organization-setup.md)
+ [Configuring Change Manager options and best practices](change-manager-account-setup.md)
+ [Configuring roles and permissions for Change Manager](change-manager-permissions.md)
+ [Controlling access to auto-approval runbook workflows](change-manager-auto-approval-access.md)