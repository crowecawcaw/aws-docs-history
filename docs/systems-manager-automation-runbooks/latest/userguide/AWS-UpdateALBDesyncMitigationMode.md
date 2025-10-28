# `AWS-UpdateALBDesyncMitigationMode`

**Description**

The `AWS-UpdateALBDesyncMitigationMode` runbook will update the desync
mitigation mode on an Application Load Balancer (ALB) to the specified mitigation
mode. The desync mitigation mode determines how the load balancer handles requests
that might pose a security risk to your application.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateALBDesyncMitigationMode "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateALBDesyncMitigationMode")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- LoadBalancerArn

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the ALB that you
want to modify the desync mitigation mode of.

- DesyncMitigationMode

Type: String

Valid values: monitor | defensive | strictest

Description: (Required) The mitigation mode that you want the ALB to use.
For information about desync mitigation modes, see [Desync mitigation mode](../../../elasticloadbalancing/latest/application/application-load-balancers.md#desync-mitigation-mode "../../../elasticloadbalancing/latest/application/application-load-balancers.md#desync-mitigation-mode") in the
_User Guide for Application Load Balancers_.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeLoadBalancerAttributes`
- `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

- VerifyLoadBalancerType (aws:assertAwsResourceProperty) - Verifies that the
  value specified for the `LoadBalancerArn` input parameter is for
  an application load balancer before proceeding to the next step.
- ModifyLoadBalancerDesyncMode (aws:executeAwsApi) - Updates the ALB to use
  the specified `DesyncMitigationMode`.
- VerifyLoadBalancerDesyncMitigationMode (aws:executeScript) - Verifies that
  the desync mitigation mode was updated for the target ALB.

**Outputs**

VerifyLoadBalancerDesyncMitigationMode.ModificationResult - Message payload of
the script verifying the modification to your ALB.
