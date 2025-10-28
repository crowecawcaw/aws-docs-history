# Use `RevokeSecurityGroupEgress` with a CLI

The following code examples show how to use `RevokeSecurityGroupEgress`.

CLI

**AWS CLI**

**Example 1: To remove the rule that allows outbound traffic to a specific address range**

The following `revoke-security-group-egress` example command removes the rule that grants access to the specified address ranges on TCP port 80.

```
`aws ec2 revoke-security-group-egress \
 --group-id `sg-026c12253ce15eff7` \
 --ip-permissions `[{IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=10.0.0.0/16}]``

```

This command produces no output.

For more information, see [Security groups](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md") in the _Amazon EC2 User Guide_.

**Example 2: To remove the rule that allows outbound traffic to a specific security group**

The following `revoke-security-group-egress` example command removes the rule that grants access to the specified security group on TCP port 80.

```
`aws ec2 revoke-security-group-egress \
 --group-id `sg-026c12253ce15eff7` \
 --ip-permissions '`[{"IpProtocol": "tcp", "FromPort": 443, "ToPort": 443,"UserIdGroupPairs": [{"GroupId": "sg-06df23a01ff2df86d"}]}]`'`

```

This command produces no output.

For more information, see [Security groups](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [RevokeSecurityGroupEgress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-egress.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-egress.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the rule for the specified security group for EC2-VPC. This revokes access to the specified IP address range on TCP port 80. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; IpRanges="203.0.113.0/24" }
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip

```

**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 80
$ip.ToPort = 80
$ip.IpRanges.Add("203.0.113.0/24")
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip

```

**Example 3: This example revokes access to the specified source security group on TCP port 80.**

```
$ug = New-Object Amazon.EC2.Model.UserIdGroupPair
$ug.GroupId = "sg-1a2b3c4d"
$ug.UserId = "123456789012"
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission @( @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; UserIdGroupPairs=$ug } )

```

- For API details, see
  [RevokeSecurityGroupEgress](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the rule for the specified security group for EC2-VPC. This revokes access to the specified IP address range on TCP port 80. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; IpRanges="203.0.113.0/24" }
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip

```

**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 80
$ip.ToPort = 80
$ip.IpRanges.Add("203.0.113.0/24")
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip

```

**Example 3: This example revokes access to the specified source security group on TCP port 80.**

```
$ug = New-Object Amazon.EC2.Model.UserIdGroupPair
$ug.GroupId = "sg-1a2b3c4d"
$ug.UserId = "123456789012"
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission @( @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; UserIdGroupPairs=$ug } )

```

- For API details, see
  [RevokeSecurityGroupEgress](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
