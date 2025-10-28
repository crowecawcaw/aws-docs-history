# Self-managed licenses in License Manager

Self-managed licenses (formerly known as _license configurations_) are
the core of License Manager. Self-managed licenses contain licensing rules based on the terms
of your enterprise agreements. The rules that you create determine how AWS processes
commands that consume licenses. While creating self-managed licenses, work closely with your
organization's compliance team to review your enterprise agreements.

AWS services such as License Manager have service quotas that define the maximum number of
resources or operations per Region that are available to your AWS account for that service.
For example, with License Manager, you can have a maximum of `10` self-managed licenses per
resource, with no more than `25` self-managed licenses total in any given AWS Region.
To find out more about License Manager quotas, see [AWS License Manager Service
quotas](../../../general/latest/gr/licensemanager.md#limits_license-manager-quotas "../../../general/latest/gr/licensemanager.md#limits_license-manager-quotas") in the _AWS General Reference_.

###### Note

Systems Manager managed instances must be associated with vCPU and instance type self-managed
licenses.

###### Contents

- [Parameters and rules](config-overview.md "config-overview.md")
- [Build rules from vendor licenses](licenses-to-rules.md "licenses-to-rules.md")
- [Create a self-managed license](create-license-configuration.md "create-license-configuration.md")
- [Share a self-managed license](share-license-configuration.md "share-license-configuration.md")
- [Edit a self-managed license](modify-license-configuration.md "modify-license-configuration.md")
- [Deactivate a self-managed license](deactivate-license-configuration.md "deactivate-license-configuration.md")
- [Delete a self-managed license](delete-license-configuration.md "delete-license-configuration.md")
