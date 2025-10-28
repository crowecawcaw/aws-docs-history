# Security groups for WorkSpaces Personal

When you register a directory with WorkSpaces, it creates two security groups,
one for directory controllers and another for WorkSpaces in the directory.
The security group for directory controllers has a name that consists of the
directory identifier followed by **\_controllers** (for example,
d-12345678e1_controllers). The security group for
WorkSpaces has a name that consists of the directory identifier followed by
**\_workspacesMembers** (for example, d-123456fc11_workspacesMembers).

###### Warning

Avoid modifying, deleting, or detaching the **\_controllers** and the
**\_workspacesMembers** security groups. Be cautious when modifying or
deleting these security groups, because you will not be able to recreate these groups and
add them back after they have been modified or deleted. For more information, see [Amazon EC2
security groups for Linux instance](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md") or [Amazon EC2 security groups
for Windows instances](../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md "../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md").

You can add a default WorkSpaces security group to a directory. After you associate a new security group
with a WorkSpaces directory, new WorkSpaces that you launch or existing WorkSpaces that you rebuild will have
the new security group. You can also [add this new default
security group to existing WorkSpaces without rebuilding them](#security_group_existing_workspace "#security_group_existing_workspace"), as explained later in this topic.

When you associate multiple security groups with a WorkSpaces directory, the rules from each security group are
effectively aggregated to create one set of rules. We recommend condensing your security group rules as much
as possible.

For more information about security groups, see [Security Groups for Your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon VPC User Guide_.

###### To add a security group to a WorkSpaces directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select the directory and choose **Actions**, **Update Details**.
4. Expand **Security Group** and select a security group.
5. Choose **Update and Exit**.
   To add a security group to an existing WorkSpace without rebuilding it, you assign the new security group to
   the elastic network interface (ENI) of the WorkSpace.

###### To add a security group to an existing WorkSpace

1. Find the IP address for each WorkSpace that needs to be updated.
   1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
   2. Expand each WorkSpace and record its WorkSpace IP address.

2. Find the ENI for each WorkSpace and update its security group assignment.
   1. Open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. Under **Network & Security**, choose **Network Interfaces**.
   3. Search for the first IP address that you recorded in Step 1.
   4. Select the ENI associated with the IP address, choose **Actions**, and then
      choose **Change Security Groups**.
   5. Select the new security group, and choose **Save**.
   6. Repeat this process as needed for any other WorkSpaces.
