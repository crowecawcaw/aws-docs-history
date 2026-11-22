

# `AWSSupportRemediator-DeleteUnusedNacl`

**Description**

Deletes an Amazon Virtual Private Cloud (Amazon VPC) network access control list (network ACL) that is not associated with any subnet and is not the VPC default network ACL.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Unused Network Access Control Lists should be removed](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16).

If the network ACL does not exist, or is associated with one or more subnets, the automation completes successfully without making changes. The automation fails if the specified network ACL is the VPC default network ACL, because default network ACLs cannot be deleted.

**Irreversible action**  
Deleting a network ACL is irreversible. Before deletion, the runbook captures the network ACL configuration, including entries and associations, in the `validateNACL.DetailOfDeletedNACL` output. You can use this output to recreate the configuration manually if needed.

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
+ NetworkAclId

  Type: String

  Description: (Required) The ID of the Amazon VPC network ACL to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DeleteNetworkAcl`
+ `ec2:DescribeNetworkAcls`

**Document Steps**

1. **validateNACL** - Validates that the network ACL exists, is not the VPC default, and is not associated with any subnet. Captures the network ACL configuration before deletion.

1. **branchOnChangeRequired** - Branches on whether the network ACL needs to be deleted.

1. **deleteNACL** - Deletes the network ACL.

**Outputs**
+ validateNACL.ChangeRequired: Whether the network ACL needs to be deleted.
+ validateNACL.ValidationMessage: Information about the validation result.
+ validateNACL.DetailOfDeletedNACL: The network ACL configuration captured prior to deletion, for rollback reference.