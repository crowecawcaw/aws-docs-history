

# Self-managed licenses in License Manager
<a name="license-configurations"></a>

Self-managed licenses (formerly known as *license configurations*) are the core of License Manager. Self-managed licenses contain licensing rules based on the terms of your enterprise agreements. The rules that you create determine how AWS processes commands that consume licenses. While creating self-managed licenses, work closely with your organization's compliance team to review your enterprise agreements.

Self-managed licenses can be used independently within a single AWS account or cross AWS account or integrated with License asset groups for centralized management across multiple AWS accounts and regions across AWS organization. This integration provides enhanced governance, and compliance tracking for enterprise environments.

AWS services such as License Manager have service quotas that define the maximum number of resources or operations per Region that are available to your AWS account for that service. For example, with License Manager, you can have a maximum of `10` self-managed licenses per resource, with no more than `25` self-managed licenses total in any given AWS Region. To find out more about License Manager quotas, see [AWS License Manager Service quotas](https://docs.aws.amazon.com/general/latest/gr/licensemanager.html#limits_license-manager-quotas) in the *AWS General Reference*.

**Note**  
Systems Manager managed instances must be associated with vCPU and instance type self-managed licenses.

**Topics**
+ [Parameters and rules](config-overview.md)
+ [Build rules from vendor licenses](licenses-to-rules.md)
+ [Create a self-managed license](create-license-configuration.md)
+ [Share a self-managed license](share-license-configuration.md)
+ [Edit a self-managed license](modify-license-configuration.md)
+ [View self-managed licenses](view-license-configuration.md)
+ [Deactivate a self-managed license](deactivate-license-configuration.md)
+ [Delete a self-managed license](delete-license-configuration.md)
+ [Self Managed License Rules](license-rules.md)