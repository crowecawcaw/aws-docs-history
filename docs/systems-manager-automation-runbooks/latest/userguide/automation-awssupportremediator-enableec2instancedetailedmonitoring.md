

# `AWSSupportRemediator-EnableEc2InstanceDetailedMonitoring`

**Description**

Enables detailed monitoring for an Amazon Elastic Compute Cloud (Amazon EC2) instance.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon EC2 Detailed Monitoring Not Enabled](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ec2-detailed-monitoring-not-enabled).

If the Amazon EC2 instance does not exist, is terminated, or detailed monitoring is already enabled, the automation completes successfully without making changes.

To disable detailed monitoring after enabling, use the Amazon EC2 `UnmonitorInstances` API action.

Enabling detailed monitoring might increase Amazon CloudWatch costs due to additional metrics collected at one-minute intervals. For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ InstanceId

  Type: `AWS::EC2::Instance::Id`

  Description: (Required) The ID of the Amazon EC2 instance.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeInstances`
+ `ec2:MonitorInstances`

**Document Steps**

1. **validateEC2Instance** - Validates that the Amazon EC2 instance exists and checks whether detailed monitoring is already enabled.

1. **branchOnChangeRequired** - Branches on whether detailed monitoring needs to be enabled.

1. **updateEC2Instance** - Enables detailed monitoring for the Amazon EC2 instance.

**Outputs**
+ validateEC2Instance.ChangeRequired: Whether a change is required for the Amazon EC2 instance.
+ validateEC2Instance.ValidationMessage: The reason if no change is required.