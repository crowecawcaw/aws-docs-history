# `AWSSupport-ConfigureTrafficMirroring`

**Description**

The `AWSSupport-ConfigureTrafficMirroring` runbook configures traffic
mirroring to help you troubleshoot connectivity issues between a load balancer and
Amazon Elastic Compute Cloud (Amazon EC2) instances. Traffic mirroring copies inbound and outbound traffic
from the network interfaces that are attached to your instances. To configure
traffic mirroring, this runbook creates the required targets, filters, and sessions.
By default, the runbook configures mirroring for all inbound and outbound traffic
for all protocols except Amazon DNS. If you want to mirror traffic from specific
sources and destinations, you can modify the inbound and outbound rules after the
automation completes.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureTrafficMirroring "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureTrafficMirroring")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- SourceENI

Type: String

Description: (Required) The elastic network interface you want to
configure traffic mirroring for.

- Target

Type: String

Description: (Required) The destination for the mirrored traffic. You must
specify the ID of a network interface, a Network Load Balancer, or a Gateway
Load Balancer endpoint. If you specify a Network Load Balancer, there must
be UDP listeners on port 4789.

- SessionNumber

Type: String

Valid values: 1-32766

Description: (Required) The number of the mirror session you want to
use.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateTrafficMirrorTarget`
- `ec2:CreateTrafficMirrorFilter`
- `ec2:CreateTrafficMirrorFilterRule`
- `ec2:CreateTrafficMirrorSession`
- `ec2:DeleteTrafficMirrorSession`
- `ec2:DeleteTrafficMirrorFilter`
- `ec2:DeleteTrafficMirrorSession`
- `ec2:DeleteTrafficMirrorFilterRule`
- `iam:ListRoles`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`

**Document Steps**

- `aws:executeScript` - Runs a script to create a target.
- `aws:executeAwsApi` - Creates a filter rule.
- `aws:executeAwsApi` - Creates a mirror filter rule for all
  inbound traffic.
- `aws:executeAwsApi` - Creates a mirror filter rule for all
  outbound traffic.
- `aws:executeAwsApi` - Creates a traffic mirror session.
- `aws:executeAwsApi` - Deletes the filter if filter or session
  creation fails.
- `aws:executeAwsApi` - Deletes the target if filter or session
  creation fails.

**Outputs**

CreateFilter.FilterId

CreateSession.SessionId

CreateTarget.TargetIDOutput
