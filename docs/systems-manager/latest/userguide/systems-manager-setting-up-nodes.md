# Setting up managed nodes for AWS Systems Manager

Complete the tasks in this section to set up and configure roles, user accounts,
permissions, and initial resources for using AWS Systems Manager tools. The tasks described in this
section are typically performed by AWS account and systems administrators. After these
steps are complete, users in your organization can use Systems Manager to configure, manage, and
access your _managed nodes_. A managed node is any machine
configured for use with Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment.

###### Note

If you plan to use Amazon EC2 instances _and_ your own
computing resources in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment, follow the steps in [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md"). That topic presents steps in the
best order for completing Systems Manager setup for EC2 instances and non-EC2 machines.

If you already use other AWS services, you have completed some of these steps. However,
other steps are specific to Systems Manager. Therefore, we recommend reviewing this entire section to
make sure that you're ready to use all Systems Manager tools.

###### Topics

- [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md")
- [Managing nodes in hybrid and multicloud environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md")
- [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md "systems-manager-cloud-connector.md")
- [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md")
- [Creating an AWS Organizations delegated administrator for Systems Manager](setting_up_delegated_admin.md "setting_up_delegated_admin.md")
- [General setup for AWS Systems Manager](#setting_up_prerequisites "#setting_up_prerequisites")

## General setup for AWS Systems Manager

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.
