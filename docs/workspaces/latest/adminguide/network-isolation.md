# Network isolation

A virtual private cloud (VPC) is a virtual network in your own logically isolated area
in the AWS Cloud. You can deploy your WorkSpaces in a private subnet in your VPC. For more
information, see [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md "amazon-workspaces-vpc.md").

To allow traffic only from specific address ranges (for example, from your corporate network),
update the security group for your VPC or use an [IP access control group](amazon-workspaces-ip-access-control-groups.md "amazon-workspaces-ip-access-control-groups.md").

You can restrict WorkSpace access to trusted devices with valid certificates. For more
information, see [Restrict access to trusted devices for WorkSpaces Personal](trusted-devices.md "trusted-devices.md").
