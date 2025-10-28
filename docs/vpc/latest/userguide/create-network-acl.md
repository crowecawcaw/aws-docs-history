# Create a network ACL for your VPC

The following tasks show you how to create a network ACL, add rules to the network ACL,
and then associate the network ACL with a subnet.

###### Tasks

- [Step 1: Create a network ACL](#CreateACL "#CreateACL")
- [Step 2: Add rules](#Rules "#Rules")
- [Step 3: Associate a subnet with a network ACL](#NetworkACL "#NetworkACL")
- [(Optional) Manage network ACLs using Firewall Manager](#nacls-using-firewall-manager "#nacls-using-firewall-manager")

## Step 1: Create a network ACL

You can create a custom network ACL for your VPC. The initial rules for a custom network
ACL block all inbound and outbound traffic. Your new custom network ACL is not associated
with a subnet by default and must be explicitly associated with subnets.

###### To create a network ACL using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Network ACLs**.
3. Choose **Create network ACL**.
4. (Optional) For **Name**, enter a name for your
   network ACL.
5. For **VPC**, select the VPC.
6. (Optional) For **Tags**, choose **Add tag** and
   then enter a tag key and a tag value.
7. Choose **Create network ACL**.

###### To create a network ACL using the command line

- [create-network-acl](../../../cli/latest/reference/ec2/create-network-acl.md "../../../cli/latest/reference/ec2/create-network-acl.md") (AWS CLI)
- [New-EC2NetworkAcl](../../../powershell/latest/reference/items/New-EC2NetworkAcl.md "../../../powershell/latest/reference/items/New-EC2NetworkAcl.md") (AWS Tools for Windows PowerShell)

## Step 2: Add rules

You can add rules that allow or deny inbound or outbound traffic.

We process the rules in order, starting with the rule with the lowest number.
We recommend that you leave gaps between the rule numbers (such as 100, 200, 300),
rather than using sequential numbers (101, 102, 103). This makes it easier add a new
rule without having to renumber the existing rules.

If you're using the Amazon EC2 API or a command line tool, you can't modify rules. You can
only add and delete rules. If you're using the Amazon VPC console, you can modify the entries for
existing rules. The console removes the existing rule and adds a new rule for you. If you
need to change the order of a rule in the ACL, you must add a new rule with the new rule
number, and then delete the original rule.

###### To add rules to a network ACL using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Network ACLs**.
3. Select the network ACL.
4. To add an inbound rule, do the following:
   1. Choose the **Inbound rules** tab.
   2. Choose **Edit inbound rules**, **Add new rule**.
   3. Enter a rule number that is not already in use, a type, protocol, port range, source,
      and whether to allow or deny the traffic. For some types, we fill in the protocol and port
      for you. If you are prompted for a port range, enter a port number or a port range
      (for example, 49152-65535).

   To use a protocol that's not listed, choose **Custom Protocol** for the
   type and then select the protocol. For more information, see
   [IANA
   Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml "http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"). 4. Choose **Save changes**.

5. To add an outbound rule, do the following:
   1. Choose the **Outbound rules** tab.
   2. Choose **Edit outbound rules**, **Add new rule**.
   3. Enter a rule number that is not already in use, a type, protocol, port range, source,
      and whether to allow or deny the traffic. For some types, we fill in the protocol and port
      for you. If you are prompted for a port range, enter a port number or a port range
      (for example, 49152-65535).

   To use a protocol that's not listed, choose **Custom Protocol** for the
   type and then select the protocol. For more information, see
   [IANA
   Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml "http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"). 4. Choose **Save changes**.

###### To add a rule to a network ACL using the command line

- [create-network-acl-entry](../../../cli/latest/reference/ec2/create-network-acl-entry.md "../../../cli/latest/reference/ec2/create-network-acl-entry.md") (AWS CLI)
- [New-EC2NetworkAclEntry](../../../powershell/latest/reference/items/New-EC2NetworkAclEntry.md "../../../powershell/latest/reference/items/New-EC2NetworkAclEntry.md") (AWS Tools for Windows PowerShell)

###### To replace a rule in a network ACL using the command line

- [replace-network-acl-entry](../../../cli/latest/reference/ec2/replace-network-acl-entry.md "../../../cli/latest/reference/ec2/replace-network-acl-entry.md") (AWS CLI)
- [Set-EC2NetworkAclEntry](../../../powershell/latest/reference/items/Set-EC2NetworkAclEntry.md "../../../powershell/latest/reference/items/Set-EC2NetworkAclEntry.md") (AWS Tools for Windows PowerShell)

###### To delete a rule from a network ACL using the command line

- [delete-network-acl-entry](../../../cli/latest/reference/ec2/delete-network-acl-entry.md "../../../cli/latest/reference/ec2/delete-network-acl-entry.md") (AWS CLI)
- [Remove-EC2NetworkAclEntry](../../../powershell/latest/reference/items/Remove-EC2NetworkAclEntry.md "../../../powershell/latest/reference/items/Remove-EC2NetworkAclEntry.md") (AWS Tools for Windows PowerShell)

## Step 3: Associate a subnet with a network ACL

To apply the rules of a network ACL to a particular subnet, you must associate the
subnet with the network ACL. You can associate a network ACL with multiple subnets. However,
a subnet can be associated with only one network ACL. Any subnet that is not associated with
a particular ACL is associated with the default network ACL by default.

###### To associate a subnet with a network ACL

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Network ACLs**, and then select
   the network ACL.
3. In the details pane, on the **Subnet Associations** tab, choose
   **Edit**. Select the **Associate** check box for the
   subnet to associate with the network ACL, and then choose
   **Save**.

## (Optional) Manage network ACLs using Firewall Manager

AWS Firewall Manager simplifies your network ACL administration and maintenance tasks across multiple accounts and subnets.
You can use Firewall Manager to monitor accounts and subnets in your organization and to automatically apply the network ACL configurations that you've defined.
Firewall Manager is particularly useful when you want to protect your entire organization, or if you frequently add new subnets
that you want to automatically protect from a central administrator account.

With a Firewall Manager network ACL policy, using a single administrator account, you can
configure, monitor, and manage the minimum rule sets that you want to have defined in the network ACLs that you use across your organization.
You specify which accounts and subnets in your organization are within scope of the Firewall Manager policy. Firewall Manager reports
the compliance status of the network ACLs for in-scope subnets, and you can configure
Firewall Manager to automate the remediation of noncompliant network ACLs.

For more information, see the following resources in the _AWS Firewall Manager Developer Guide_:

- [AWS Firewall Manager prerequisites](../../../waf/latest/developerguide/fms-prereq.md "../../../waf/latest/developerguide/fms-prereq.md")
- [Setting up AWS Firewall Manager network ACL policies](../../../waf/latest/developerguide/getting-started-fms-network-acl.md "../../../waf/latest/developerguide/getting-started-fms-network-acl.md")
- [Using network ACL policies with Firewall Manager](../../../waf/latest/developerguide/network-acl-policies.md "../../../waf/latest/developerguide/network-acl-policies.md")
