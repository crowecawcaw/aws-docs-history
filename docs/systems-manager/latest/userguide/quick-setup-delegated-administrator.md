# Using a delegated administrator for Quick Setup

After you register a delegated administrator account for Quick Setup, users with the
appropriate permissions in that account can create, update, view, and delete
configuration managers that target organizational units within your AWS Organizations structure.
This delegated administrator account can also manage configuration managers previously
created by your organization's management account.

The management account in Organizations can designate one account within your organization as a
delegated administrator. When you register an account as a delegated administrator for
Quick Setup, this account also becomes a delegated administrator for AWS CloudFormation
StackSets and Systems Manager Explorer. These services are needed to deploy and
monitor Quick Setup configurations.

###### Note

Currently, the patch policy configuration type isn't supported by the delegated
administrator for Quick Setup. Patch policy configurations for an organization must be
created and maintained in the management account for an organization. For more
information, see [Creating a patch policy](quick-setup-patch-manager.md#create-patch-policy "quick-setup-patch-manager.md#create-patch-policy").

The following topics describe how to register and deregister a delegated administrator
for Quick Setup.
