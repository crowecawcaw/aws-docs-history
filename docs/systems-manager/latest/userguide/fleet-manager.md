• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# AWS Systems Manager Fleet Manager

Fleet Manager, a tool in AWS Systems Manager, is a unified user interface (UI) experience that helps you
remotely manage your nodes running on AWS or on premises. With Fleet Manager, you can view the
health and performance status of your entire server fleet from one console. You can also
gather data from individual nodes to perform common troubleshooting and management tasks
from the console. This includes connecting to Windows instances using the Remote Desktop
Protocol (RDP), viewing folder and file contents, Windows registry management, operating
system user management, and more.

To get started with Fleet Manager, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/fleet-manager "https://console.aws.amazon.com/systems-manager/fleet-manager"). In the navigation pane,
choose **Fleet Manager**.

## Who should use Fleet Manager?

Any AWS customer who wants a centralized way to manage their node fleet should use
Fleet Manager.

## How can Fleet Manager benefit my organization?

Fleet Manager offers these benefits:

- Perform a variety of common systems administration tasks without having to
  manually connect to your managed nodes.
- Manage nodes running on multiple platforms from a single unified
  console.
- Manage nodes running different operating systems from a single unified
  console.
- Improve the efficiency of your systems administration.

## What are the features of Fleet Manager?

Key features of Fleet Manager include the following:

- **Access the Red Hat Knowledgebase
  Portal**

Access binaries, knowledge-shares, and discussion forums on the Red Hat
Knowledgebase Portal through your Red Hat Enterprise Linux (RHEL) instances.

- **Managed node status**

View which managed instances are `running` and which are
`stopped`. For more information about stopped instances, see
[Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in the
_Amazon EC2 User Guide_. For AWS IoT Greengrass core devices, you can
view which are `online`, `offline`, or show a status of
`Connection lost`.

###### Note

If you stopped your managed instance before July 12, 2021, it won't
display the `stopped` marker. To show the marker, start and stop
the instance.

- **View instance information**

View information about the folder and file data stored on the volumes attached
to your managed instances, performance data about your instances in real-time,
and log data stored on your instances.

- **View edge device information**

View the AWS IoT Greengrass Thing name for the device, SSM Agent ping status and version,
and more.

- **Manage accounts and registry**

Manage operating system (OS) user accounts on your instances and registry on
your Windows instances.

- **Control access to features**

Control access to Fleet Manager features using AWS Identity and Access Management (IAM) policies. With
these policies, you can control which individual users or groups in your
organization can use various Fleet Manager features, and which managed nodes they can
manage.

###### Topics

- [Setting up Fleet Manager](setting-up-fleet-manager.md "setting-up-fleet-manager.md")
- [Working with managed nodes](fleet-manager-managed-nodes.md "fleet-manager-managed-nodes.md")
- [Managing EC2
  instances automatically with Default Host Management Configuration](fleet-manager-default-host-management-configuration.md "fleet-manager-default-host-management-configuration.md")
- [Connecting to a Windows Server
  managed instance using Remote Desktop](fleet-manager-remote-desktop-connections.md "fleet-manager-remote-desktop-connections.md")
- [Managing Amazon EBS volumes on
  managed instances](fleet-manager-manage-amazon-ebs-volumes.md "fleet-manager-manage-amazon-ebs-volumes.md")
- [Accessing the Red Hat
  Knowledge base portal](fleet-manager-red-hat-knowledge-base-access.md "fleet-manager-red-hat-knowledge-base-access.md")
- [Troubleshooting managed
  node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md")
