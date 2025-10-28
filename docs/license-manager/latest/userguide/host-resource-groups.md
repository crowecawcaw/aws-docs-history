# Host resource groups in License Manager

Amazon EC2 Dedicated Hosts are physical servers with EC2 instance capacity fully dedicated to your
use. A host resource group is a collection of Dedicated Hosts that you can manage as a single entity. As you launch
instances, License Manager allocates the hosts and launches instances on them based on the settings that
you configured. You can add existing Dedicated Hosts to a host resource group and take advantage of automated host
management through License Manager. For more information, see [Dedicated Hosts](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md") in the
_Amazon EC2 User Guide_.

You can use host resource groups to separate hosts by purpose, for example, development test
hosts versus production, organizational unit, or license constraint. After you add a Dedicated Host
to a host resource group, you cannot launch instances directly on the Dedicated Host, you
must launch them using the host resource group.

###### Settings

You can configure the following settings for a host resource group:

- **Allocate hosts automatically** – Indicates whether Amazon EC2 can
  allocate new hosts on your behalf if launching an instance in this host resource group would
  exceed its available capacity.
- **Release hosts automatically** – Indicates whether Amazon EC2 can
  release unused hosts on your behalf. An unused host has no running instances.
- **Recover hosts automatically** – Indicates whether Amazon EC2 can move
  instances from a host that has failed unexpectedly to a new host.
- **Associated self-managed licenses** – The self-managed licenses
  that can be used to launch instances in this host resource group.
- **(Optional) Instance families** – The types of instances that you
  can launch. By default, you can launch any instance types that are supported on a Dedicated Host.
  If you launch [Nitro-based](url-ec2-user.md#ec2-nitro-instances "url-ec2-user.md#ec2-nitro-instances") instances, then you can launch instances with different instance
  types in the same host resource group. Otherwise, you must launch only instances with the
  same instance type in the same host resource group.

###### Contents

- [Create a host resource group in License Manager](host-resource-group-create.md "host-resource-group-create.md")
- [Share a host resource group in License Manager](host-resource-group-share.md "host-resource-group-share.md")
- [Add Dedicated Hosts to a host resource group in License Manager](add-hosts.md "add-hosts.md")
- [Launch an instance in a host resource group in License Manager](host-resource-group-launch.md "host-resource-group-launch.md")
- [Modify a host resource group in License Manager](host-resource-group-modify.md "host-resource-group-modify.md")
- [Remove Dedicated Hosts from a host resource group in License Manager](remove-hosts.md "remove-hosts.md")
- [Delete a host resource group in License Manager](host-resource-group-delete.md "host-resource-group-delete.md")
