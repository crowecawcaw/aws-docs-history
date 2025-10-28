# Create a security group for your Amazon EC2 instance

Security groups act as a firewall for associated instances, controlling both inbound
and outbound traffic at the instance level. You can add rules to a security group that
enable you to connect to your instance using SSH (Linux instances) or RDP (Windows instances).
You can also add rules that allow client traffic, for example, HTTP and HTTPS traffic
destined to a web server.

You can associate a security group with an instance when you launch the instance. When
you add or remove rules from associated security groups, those changes are automatically
applied to all instances to which you've associated the security group.

After you launch an instance, you can associate additional security groups.
For more information, see [Change the security groups for your Amazon EC2 instance](changing-security-group.md "changing-security-group.md").

You can add inbound and outbound security group rules when you create a security group or
you can add them later on. For more information, see [Configure security group rules](changing-security-group.md#add-remove-security-group-rules "changing-security-group.md#add-remove-security-group-rules"). For examples of rules that you can add to a security group, see
[Security group rules for different use cases](security-group-rules-reference.md "security-group-rules-reference.md").

###### Considerations

- New security groups start with only an outbound rule that allows all traffic to leave the
  resource. You must add rules to enable any inbound traffic or to restrict the
  outbound traffic.
- When configuring a source for a rule that allows SSH or RDP access to your
  instances, do not allow access from anywhere, because it would allow this access
  to your instance from all IP addresses on the internet. This is acceptable for
  a short time in a test environment, but it is unsafe for production environments.
- If there is more than one rule for a specific port, Amazon EC2 applies the most permissive rule.
  For example, if you have a rule that allows access to TCP port 22 (SSH) from IP address
  203.0.113.1, and another rule that allows access to TCP port 22 from anywhere, then
  everyone has access to TCP port 22.
- You can associate multiple security groups with an instance. Therefore, an instance
  can have hundreds of rules that apply. This might cause problems when you access
  the instance. We recommend that you condense your rules as much as possible.
- When you specify a security group as the source or destination for a rule, the rule affects
  all instances that are associated with the security group. Incoming traffic is allowed
  based on the private IP addresses of the instances that are associated with the source
  security group (and not the public IP or Elastic IP addresses). For more information
  about IP addresses, see [Amazon EC2 instance IP addressing](using-instance-addressing.md "using-instance-addressing.md").
- Amazon EC2 blocks traffic on port 25 by default. For more information, see
  [Restriction on email sent using port 25](ec2-resource-limits.md#port-25-throttle "ec2-resource-limits.md#port-25-throttle").

Console

###### To create a security group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups**.
3. Choose **Create security group**.
4. Enter a descriptive name and brief description for the security group.
   You can't change the name and description of a security group after it
   is created.
5. For **VPC**, choose the VPC in which you'll run
   your Amazon EC2 instances.
6. (Optional) To add inbound rules, choose **Inbound rules**.
   For each rule, choose **Add rule** and specify the protocol,
   port, and source. For example, to allow SSH traffic, choose **SSH**
   for **Type** and specify the public IPv4 address of your computer
   or network for **Source**.
7. (Optional) To add outbound rules, choose **Outbound rules**.
   For each rule, choose **Add rule** and specify the protocol,
   port, and destination. Otherwise, you can keep the default rule, which allows
   all outbound traffic.
8. (Optional) To add a tag, choose **Add new tag** and
   enter the tag key and value.
9. Choose **Create security group**.

AWS CLI

###### To create a security group

Use the following [create-security-group](../../../cli/latest/reference/ec2/create-security-group.md "../../../cli/latest/reference/ec2/create-security-group.md")
command.

```
aws ec2 create-security-group \
    --group-name `my-security-group` \
    --description "`my security group`" \
    --vpc-id `vpc-1234567890abcdef0`
```

For examples that add rules, see [Configure security group rules](changing-security-group.md#add-remove-security-group-rules "changing-security-group.md#add-remove-security-group-rules").

PowerShell

###### To create a security group

Use the [New-EC2SecurityGroup](../../../powershell/latest/reference/items/New-EC2SecurityGroup.md "../../../powershell/latest/reference/items/New-EC2SecurityGroup.md")
cmdlet.

```
New-EC2SecurityGroup `
    -GroupName `my-security-group` `
    -Description "`my security group`" `
    -VpcId `vpc-1234567890abcdef0`
```

For examples that add rules, see [Configure security group rules](changing-security-group.md#add-remove-security-group-rules "changing-security-group.md#add-remove-security-group-rules").
