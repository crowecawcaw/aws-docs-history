

# `AWSSupportRemediator-DisableTgwAutoVpcAttach`

**Description**

Disables automatic acceptance of shared Amazon Virtual Private Cloud (Amazon VPC) attachment requests for an AWS Transit Gateway by setting the `AutoAcceptSharedAttachments` option to `disable`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon EC2 Transit Gateways should not automatically accept VPC attachment requests](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23).

If the transit gateway does not exist or `AutoAcceptSharedAttachments` is already set to `disable`, the automation completes successfully without making changes.

The automation modifies only the specified transit gateway and does not affect existing Amazon VPC attachments. After this change, you must manually accept future shared Amazon VPC attachment requests.

To revert the change, modify the transit gateway to set `AutoAcceptSharedAttachments` back to `enable`.

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
+ TransitGatewayArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the transit gateway.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeTransitGateways`
+ `ec2:ModifyTransitGateway`

**Document Steps**

1. **validateTGW** - Validates the transit gateway and checks whether automatic Amazon VPC attachment acceptance is already disabled.

1. **branchOnChangeRequired** - Branches on whether disabling automatic Amazon VPC attachment acceptance is required.

1. **disableAutoAcceptSharedAttachments** - Disables automatic acceptance of shared Amazon VPC attachment requests for the transit gateway.

**Outputs**
+ validateTGW.TransitGatewayId: The ID of the transit gateway.
+ validateTGW.ChangeRequired: Whether disabling automatic Amazon VPC attachment acceptance is required.
+ validateTGW.InitialAutoAcceptSharedAttachmentsStatus: The initial status of automatic Amazon VPC attachment acceptance.
+ validateTGW.ValidationMessage: A message describing the validation result.