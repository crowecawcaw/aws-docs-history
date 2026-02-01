• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Using a delegated administrator

for Quick Setup

After you register a delegated administrator account for Quick Setup, users with the
appropriate permissions in that account can create, update, view, and delete
configuration managers that target organizational units within your AWS Organizations structure.
This delegated administrator account can also manage configuration managers previously
created by your organization's management account.

The management account in Organizations can designate one account within your organization as a
delegated administrator. When you register an account as a delegated administrator for
Quick Setup, this account automatically becomes a delegated administrator for AWS CloudFormation
StackSets and Systems Manager Explorer as well, since these services are required to deploy and
monitor Quick Setup configurations.

###### Note

At this time, the patch policy configuration type isn't supported by the delegated
administrator for Quick Setup. Patch policy configurations for an organization must be
created and maintained in the management account for an organization. For more
information, see [Creating a patch policy](quick-setup-patch-manager.md#create-patch-policy "quick-setup-patch-manager.md#create-patch-policy").

The following topics describe how to register and deregister a delegated administrator
for Quick Setup.

###### Topics

- [Register a delegated
  administrator for Quick Setup](quick-setup-register-delegated-administrator.md "quick-setup-register-delegated-administrator.md")
- [Deregister a
  delegated administrator for Quick Setup](quick-setup-deregister-delegated-administrator.md "quick-setup-deregister-delegated-administrator.md")
