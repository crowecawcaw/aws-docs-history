

# `AWSSupportRemediator-RemoveAllRulesFromDefaultSg`

**Description**

Revokes all ingress and egress rules from the default Amazon Elastic Compute Cloud (Amazon EC2) security group of an Amazon Virtual Private Cloud (Amazon VPC).

The runbook first validates that the specified security group is a default security group and is not associated with any network interface. The runbook then revokes any existing ingress rules, followed by any existing egress rules.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [VPC default security groups should not allow inbound or outbound traffic](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-2).

If the specified security group does not exist, or it is a default security group with no ingress and egress rules, the automation completes successfully without making changes.

If the specified security group is not a default security group, or it is associated with one or more network interfaces, the automation fails without making changes.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ VPCDefaultSecurityGroup

  Type: String

  Description: (Required) The ID of the default Amazon EC2 security group from which to revoke all ingress and egress rules.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeSecurityGroups`
+ `ec2:RevokeSecurityGroupEgress`
+ `ec2:RevokeSecurityGroupIngress`

**Document Steps**

1. **validateSG** - Validates that the specified security group exists, is a default security group, and is not associated with any network interface. Returns the existing ingress and egress rules so that later steps can revoke them.

1. **branchOnRevokeIngressRequired** - Branches on whether the default security group has ingress rules to revoke.

1. **revokeIngressRules** - Revokes all ingress rules from the default security group.

1. **branchOnRevokeEgressRequired** - Branches on whether the default security group has egress rules to revoke.

1. **revokeEgressRules** - Revokes all egress rules from the default security group.

**Outputs**
+ validateSG.IngressRules: The inbound rules on the default security group.
+ validateSG.EgressRules: The outbound rules on the default security group.
+ validateSG.ChangeRequired: Whether the default security group has ingress or egress rules that require removal.
+ validateSG.ValidationMessage: A message describing the validation result when no change is required.