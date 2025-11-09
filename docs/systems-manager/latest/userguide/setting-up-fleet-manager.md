AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Setting up Fleet Manager

Before users in your AWS account can use Fleet Manager, a tool in AWS Systems Manager, to monitor
and manage your managed nodes, they must be granted the necessary permissions. In
addition, any Amazon Elastic Compute Cloud (Amazon EC2) instances; AWS IoT Greengrass core devices; and on-premises
servers, edge devices, and virtual machines (VMs) to be monitored and managed using
Fleet Manager must be Systems Manager _managed nodes_. A managed node is any machine
configured for use with Systems Manager in [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environments.

This means your nodes must meet certain prerequisites and be configured with the
AWS Systems Manager Agent (SSM Agent).

Depending on the machine type, refer to one of the following topics to ensure your
machines meet the requirements for managed nodes.

- Amazon EC2 instances: [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md")

###### Tip

You can also use Quick Setup, a tool in AWS Systems Manager, to help you quickly
configure your Amazon EC2 instances as managed instances in an individual
account. If your business or organization uses AWS Organizations, you can also
configure instances across multiple organizational units (OUs) and
AWS Regions. For more information about using Quick Setup to configure
managed instances, see [Set up Amazon EC2 host management using
Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md").

- On-premises and other server types in the cloud: [Managing nodes in hybrid and multicloud
  environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md")
- AWS IoT Greengrass (edge) devices: [Managing edge devices with
  Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md")

###### Sample policies

- [Controlling access to
  Fleet Manager](configuring-fleet-manager-permissions.md "configuring-fleet-manager-permissions.md")
