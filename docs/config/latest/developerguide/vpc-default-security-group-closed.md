

# vpc-default-security-group-closed
<a name="vpc-default-security-group-closed"></a>

Checks if the default security group of any Amazon Virtual Private Cloud (Amazon VPC) does not allow inbound or outbound traffic. The rule is NON\_COMPLIANT if the default security group has one or more inbound or outbound traffic rules. 

**Note**  
There may be a delay between when AWS Config records the deletion of related resources such as default security groups, which are deleted as part of the Amazon VPC deletion. As a result, even if all default security groups or other related resources have been deleted or remediated, the rule may report NON\_COMPLIANT until the next account baselining process.

**Identifier:** VPC\_DEFAULT\_SECURITY\_GROUP\_CLOSED

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1599c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).