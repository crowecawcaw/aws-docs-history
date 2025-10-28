# Change the security groups for your Amazon EC2 instance

You can specify security groups for your Amazon EC2 instances when you launch them.
After you launch an instance, you can add or remove security groups. You can also
add, remove, or edit security group rules for associated security groups at any
time.

Security groups are associated with network interfaces. Adding or removing security
groups changes the security groups associated with the primary network interface. You
can also change the security groups associated with any secondary network interfaces.
For more information, see [Modify network interface attributes](modify-network-interface-attributes.md "modify-network-interface-attributes.md").

###### Tasks

- [Add or remove security groups](#add-remove-instance-security-groups "#add-remove-instance-security-groups")
- [Configure security group rules](#add-remove-security-group-rules "#add-remove-security-group-rules")

## Add or remove security groups

After you launch an instance, you can add or remove security groups from the
list of associated security groups. When you associate multiple security groups
with an instance, the rules from each security group are effectively aggregated
to create one set of rules. Amazon EC2 uses this set of rules to determine whether
to allow traffic.

###### Requirements

- The instance must be in the `running` or `stopped` state.

Console

###### To change the security groups for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select your instance, and then choose **Actions**, **Security**,
   **Change security groups**.
4. For **Associated security groups**, select a security group from the
   list and choose **Add security group**.

To remove an already associated security group, choose **Remove** for
that security group. 5. Choose **Save**.

AWS CLI

###### To change the security groups for an instance

Use the following [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --groups `sg-1234567890abcdef0`
```

PowerShell

###### To change the security groups for an instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -Group `sg-1234567890abcdef0`
```

## Configure security group rules

After you create a security group, you can add, update, and delete its security
group rules. When you add, update, or delete a rule, the change is automatically
applied to the resources that are associated with the security group.

For examples of rules that you can add to a security group, see
[Security group rules for different use cases](security-group-rules-reference.md "security-group-rules-reference.md").

###### Required permissions

Before you begin, ensure that you have the required permissions. For more information, see
[Example: Work with security groups](iam-policies-ec2-console.md#ex-security-groups "iam-policies-ec2-console.md#ex-security-groups").

###### Protocols and ports

- With the console, when you select a predefined type, **Protocol**
  and **Port range** are specified for you. To enter a port range,
  you must select one of the following custom types: **Custom TCP**
  or **Custom UDP**.
- With the AWS CLI, you can add a single rule with a single port using the
  `--protocol` and `--port` options. To add multiple
  rules, or a rule with a port range, use the `--ip-permissions`
  option instead.

###### Sources and destinations

- With the console, you can specify the following as sources for inbound rules or
  destinations for outbound rules:
  - **Custom** – An IPv4 CIDR block, an IPv6 CIDR block,
    a security group, or a prefix list.
  - **Anywhere-IPv4** – The 0.0.0.0/0 IPv4 CIDR block.
  - **Anywhere-IPv6** – The ::/0 IPv6 CIDR block.
  - **My IP** – The public IPv4 address of your local
    computer.

- With the AWS CLI, you can specify an IPv4 CIDR block using the `--cidr` option
  or a security group using the `--source-group` option. To specify a prefix list
  or an IPv6 CIDR block, use the `--ip-permissions` option.

###### Warning

If you add inbound rules for ports 22 (SSH) or 3389 (RDP), we strongly
recommend that you authorize only the specific IP address or range of addresses
that need access to your instances. If you choose **Anywhere-IPv4**,
you allow traffic from all IPv4 addresses to access your instances using the
specified protocol. If you choose **Anywhere-IPv6**,
you allow traffic from all IPv6 addresses to access your instances using the
specified protocol.

Console

###### To configure security group rules

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups**.
3. Select the security group.
4. To edit the inbound rules, choose **Edit inbound rules** from
   **Actions** or the **Inbound rules** tab.
   1. To add a rule, choose **Add rule** and enter the
      type, protocol, port, and source for the rule.

   If the type is TCP or UDP, you must enter the port range to allow.
   For custom ICMP, you must choose the ICMP type name from
   **Protocol**, and, if applicable, the code name
   from **Port range**. For any other type, the
   protocol and port range are configured for you. 2. To update a rule, change its protocol, description, and source as
   needed. However, you can't change the source type. For example, if the
   source is an IPv4 CIDR block, you can't specify an IPv6 CIDR block,
   a prefix list, or a security group. 3. To delete a rule, choose its **Delete** button.

5. To edit the outbound rules, choose **Edit outbound rules** from
   **Actions** or the **Outbound rules** tab.
   1. To add a rule, choose **Add rule** and enter the
      type, protocol, port, and destination for the rule. You can also enter
      an optional description.

   If the type is TCP or UDP, you must enter the port range to allow.
   For custom ICMP, you must choose the ICMP type name from
   **Protocol**, and, if applicable, the code name
   from **Port range**. For any other type, the
   protocol and port range are configured for you. 2. To update a rule, change its protocol, description, and source as
   needed. However, you can't change the source type. For example, if the
   source is an IPv4 CIDR block, you can't specify an IPv6 CIDR block,
   a prefix list, or a security group. 3. To delete a rule, choose its **Delete** button.

6. Choose **Save rules**.

AWS CLI

###### To add security group rules

Use the [authorize-security-group-ingress](../../../cli/latest/reference/ec2/authorize-security-group-ingress.md "../../../cli/latest/reference/ec2/authorize-security-group-ingress.md")
command to add inbound rules. The following example allows inbound SSH traffic
from the CIDR blocks in the specified prefix list.

```
aws ec2 authorize-security-group-ingress \
    --group-id `sg-1234567890abcdef0` \
    --ip-permissions 'IpProtocol=tcp,FromPort=22,ToPort=22,PrefixListIds=[{PrefixListId=`pl-f8a6439156EXAMPLE`}]'
```

Use the [authorize-security-group-egress](../../../cli/latest/reference/ec2/authorize-security-group-egress.md "../../../cli/latest/reference/ec2/authorize-security-group-egress.md")
command to add outbound rules. The following example allows outbound TCP traffic
on port 80 to instances with the specified security group.

```
aws ec2 authorize-security-group-egress \
    --group-id `sg-1234567890abcdef0` \
    --ip-permissions 'IpProtocol=tcp,FromPort=80,ToPort=80,UserIdGroupPairs=[{GroupId=`sg-0aad1c26bb6EXAMPLE`}]'
```

###### To remove security group rules

Use the following [revoke-security-group-ingress](../../../cli/latest/reference/ec2/revoke-security-group-ingress.md "../../../cli/latest/reference/ec2/revoke-security-group-ingress.md")
command to remove an inbound rule.

```
aws ec2 revoke-security-group-egress \
    --group id `sg-1234567890abcdef0` \
    --security-group-rule-ids `sgr-09ed298024EXAMPLE`
```

Use the following [revoke-security-group-egress](../../../cli/latest/reference/ec2/revoke-security-group-egress.md "../../../cli/latest/reference/ec2/revoke-security-group-egress.md")
command to remove an outbound rule.

```
aws ec2 revoke-security-group-ingress \
    --group id `sg-1234567890abcdef0` \
    --security-group-rule-ids `sgr-0352250c1aEXAMPLE`
```

###### To modify security group rules

Use the [modify-security-group-rules](../../../cli/latest/reference/ec2/modify-security-group-rules.md "../../../cli/latest/reference/ec2/modify-security-group-rules.md")
command. The following example changes the IPv4 CIDR block of the
specified security group rule.

```
aws ec2 modify-security-group-rules \
    --group id `sg-1234567890abcdef0` \
    --security-group-rules 'SecurityGroupRuleId=`sgr-09ed298024EXAMPLE`,SecurityGroupRule={IpProtocol=tcp,FromPort=80,ToPort=80,CidrIpv4=`0.0.0.0/0`}'
```

PowerShell

###### To add security group rules

Use the [Grant-EC2SecurityGroupIngress](../../../powershell/latest/reference/items/Grant-EC2SecurityGroupIngress.md "../../../powershell/latest/reference/items/Grant-EC2SecurityGroupIngress.md")
cmdlet to add inbound rules. The following example allows inbound SSH traffic
from the CIDR blocks in the specified prefix list.

```
$plid = New-Object -TypeName Amazon.EC2.Model.PrefixListId
$plid.Id = "`pl-f8a6439156EXAMPLE`"
Grant-EC2SecurityGroupIngress `
    -GroupId `sg-1234567890abcdef0` `
    -IpPermission @{IpProtocol="tcp"; FromPort=22; ToPort=22; PrefixListIds=$plid}
```

Use the [Grant-EC2SecurityGroupEgress](../../../powershell/latest/reference/items/Grant-EC2SecurityGroupEgress.md "../../../powershell/latest/reference/items/Grant-EC2SecurityGroupEgress.md")
cmdlet to add outbound rules. The following example allows outbound
TCP traffic on port 80 to instances with the specified security group.

```
$uigp = New-Object -TypeName Amazon.EC2.Model.UserIdGroupPair
$uigp.GroupId = "`sg-0aad1c26bb6EXAMPLE`"
Grant-EC2SecurityGroupEgress `
    -GroupId `sg-1234567890abcdef0` `
    -IpPermission @{IpProtocol="tcp"; FromPort=80; ToPort=80; UserIdGroupPairs=$uigp}
```

###### To remove security group rules

Use the [Revoke-EC2SecurityGroupIngress](../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupIngress.md "../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupIngress.md")
cmdlet to remove inbound rules.

```
Revoke-EC2SecurityGroupIngress `
    -GroupId `sg-1234567890abcdef0` `
    -SecurityGroupRuleId `sgr-09ed298024EXAMPLE`
```

Use the [Revoke-EC2SecurityGroupEgress](../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupEgress.md "../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupEgress.md")
cmdlet to remove outbound rules.

```
Revoke-EC2SecurityGroupEgress `
    -GroupId `sg-1234567890abcdef0` `
    -SecurityGroupRuleId `sgr-0352250c1aEXAMPLE`
```

###### To modify security group rules

Use the [Edit-EC2SecurityGroupRule](../../../powershell/latest/reference/items/Edit-EC2SecurityGroupRule.md "../../../powershell/latest/reference/items/Edit-EC2SecurityGroupRule.md")
cmdlet. The following example changes the IPv4 CIDR block
of the specified security group rule.

```
$sgrr = New-Object -TypeName Amazon.EC2.Model.SecurityGroupRuleRequest
$sgrr.IpProtocol = "tcp"
$sgrr.FromPort = 80
$sgrr.ToPort = 80
$sgrr.CidrIpv4 = "0.0.0.0/0"
$sgr = New-Object -TypeName Amazon.EC2.Model.SecurityGroupRuleUpdate
$sgr.SecurityGroupRuleId = "`sgr-09ed298024EXAMPLE`"
$sgr.SecurityGroupRule = $sgrr
Edit-EC2SecurityGroupRule  `
    -GroupId `sg-1234567890abcdef0` `
    -SecurityGroupRule $sgr
```
