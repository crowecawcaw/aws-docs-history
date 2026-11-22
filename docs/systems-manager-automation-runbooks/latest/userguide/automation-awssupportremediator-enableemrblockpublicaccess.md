

# `AWSSupportRemediator-EnableEmrBlockPublicAccess`

**Description**

Enables Amazon EMR Block Public Access (BPA) at the account level in the current AWS Region.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon EMR block public access setting should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/emr-controls.html#emr-2).

If Amazon EMR Block Public Access is already enabled for the account in the current AWS Region, the automation completes successfully without making changes. The existing Block Public Access configuration remains unchanged.

When Amazon EMR Block Public Access is disabled, this automation enables it by setting `BlockPublicSecurityGroupRules` to `true`.

**Permitted port ranges are reset**  
Amazon EMR resets any existing `PermittedPublicSecurityGroupRuleRanges` to the default (TCP port 22). The automation does not carry over previously configured ranges.

The `validateEmr.InitialBlockPublicAccessConfiguration` output captures the prior Block Public Access configuration. If your workloads need additional public ports on Amazon EMR cluster security groups, review that output before running this automation.

To roll back, call `aws emr put-block-public-access-configuration` with the `BlockPublicSecurityGroupRules` and `PermittedPublicSecurityGroupRuleRanges` values from `validateEmr.InitialBlockPublicAccessConfiguration`.

After enabling Block Public Access, Amazon EMR automatically revokes new Amazon Elastic Compute Cloud (Amazon EC2) security group rules that violate the configuration. This enforcement applies to clusters launched in a public Amazon Virtual Private Cloud (Amazon VPC) subnet.

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

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticmapreduce:GetBlockPublicAccessConfiguration`
+ `elasticmapreduce:PutBlockPublicAccessConfiguration`

**Document Steps**

1. **validateEmr** - Retrieves the current Amazon EMR Block Public Access configuration for the account in the current AWS Region. Determines whether the automation needs to enable Amazon EMR Block Public Access.

1. **branchOnChangeRequired** - Branches on whether the automation needs to enable Amazon EMR Block Public Access. Ends the automation on the no-change path.

1. **putBlockPublicAccessConfiguration** - Enables Amazon EMR Block Public Access for the account in the current AWS Region by setting `BlockPublicSecurityGroupRules` to `true`. Resets any existing `PermittedPublicSecurityGroupRuleRanges` to the Amazon EMR default (TCP port 22) as part of this call.

**Outputs**
+ validateEmr.ChangeRequired: Whether the automation needs to enable Amazon EMR Block Public Access.
+ validateEmr.ValidationMessage: Information about the validation result.
+ validateEmr.InitialBlockPublicAccessConfiguration: The Block Public Access configuration before the automation makes any changes. Use this output to review and re-apply any `PermittedPublicSecurityGroupRuleRanges` the automation resets.