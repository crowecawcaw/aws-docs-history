

# `AWSSupportRemediator-ReleaseElasticIP`

**Description**

Releases an unassociated Amazon Elastic Compute Cloud (Amazon EC2) Elastic IP address.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Unassociated Elastic IP Addresses](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#unassociated-elastic-ip-addresses).

If the Elastic IP address does not exist in the account or is currently associated with a resource, the automation completes successfully without making changes.

**Irreversible action**  
Releasing an Elastic IP address is irreversible. A new Elastic IP address has a different public IP address.

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
+ PublicIp

  Type: String

  Description: (Required) The public IP address of the Elastic IP address.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeAddresses`
+ `ec2:ReleaseAddress`

**Document Steps**

1. **getAllocationId** - Validates whether the Elastic IP address exists and is not associated with any resource.

1. **branchOnChangeRequired** - Branches on whether the Elastic IP address needs to be released.

1. **releaseElasticIp** - Releases the Elastic IP address.

**Outputs**
+ getAllocationId.ChangeRequired: Whether the Elastic IP address needs to be released.
+ getAllocationId.ValidationMessage: A message describing the validation result.