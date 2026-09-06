

# Use `UpdateSecurityGroupRuleDescriptionsIngress` with a CLI
<a name="example_ec2_UpdateSecurityGroupRuleDescriptionsIngress_section"></a>

The following code examples show how to use `UpdateSecurityGroupRuleDescriptionsIngress`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To update the description of an inbound security group rule with a CIDR source**  
The following `update-security-group-rule-descriptions-ingress` example updates the description for the security group rule for the specified port and IPv4 address range. The description '`SSH access from ABC office`' replaces any existing description for the rule.  

```
aws ec2 update-security-group-rule-descriptions-ingress \
    --group-id {{sg-02f0d35a850ba727f}} \
    --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges='[{CidrIp=203.0.113.0/16,Description="SSH access from corpnet"}]'
```
Output:  

```
{
    "Return": true
}
```
For more information, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#security-group-rules) in the *Amazon EC2 User Guide*.  
**Example 2: To update the description of an inbound security group rule with a prefix list source**  
The following `update-security-group-rule-descriptions-ingress` example updates the description for the security group rule for the specified port and prefix list. The description '`SSH access from ABC office`' replaces any existing description for the rule.  

```
aws ec2 update-security-group-rule-descriptions-ingress \
    --group-id {{sg-02f0d35a850ba727f}} \
    --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,PrefixListIds='[{PrefixListId=pl-12345678,Description="SSH access from corpnet"}]'
```
Output:  

```
{
    "Return": true
}
```
For more information, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#security-group-rules) in the *Amazon EC2 User Guide*.  
+  For API details, see [UpdateSecurityGroupRuleDescriptionsIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/update-security-group-rule-descriptions-ingress.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Updates the description of an existing ingress (inbound) security group rule.**  

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithUpdatedDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
  "Description" = "Updated rule description"
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithUpdatedDescription
```
**Example 2: Removes the description of an existing ingress (inbound) security group rule (by omitting the parameter in the request).**  

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithoutDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithoutDescription
```
+  For API details, see [UpdateSecurityGroupRuleDescriptionsIngress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Updates the description of an existing ingress (inbound) security group rule.**  

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithUpdatedDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
  "Description" = "Updated rule description"
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithUpdatedDescription
```
**Example 2: Removes the description of an existing ingress (inbound) security group rule (by omitting the parameter in the request).**  

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithoutDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithoutDescription
```
+  For API details, see [UpdateSecurityGroupRuleDescriptionsIngress](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.