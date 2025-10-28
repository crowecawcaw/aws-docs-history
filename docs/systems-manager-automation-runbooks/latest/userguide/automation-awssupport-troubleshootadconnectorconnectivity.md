# `AWSSupport-TroubleshootADConnectorConnectivity`

**Description**

The `AWSSupport-TroubleshootADConnectorConnectivity` runbook verifies the
following prerequisites for an AD Connector:

- Checks if the required traffic is allowed by the security group and network access
  control list (ACL) rules associated with your AD Connector.
- Checks if the AWS Systems Manager, AWS Security Token Service, and Amazon CloudWatch interface VPC endpoints exist
  in the same virtual private cloud (VPC) as the AD Connector.
  When the prerequisite checks complete successfully, the runbook launches two Amazon Elastic Compute Cloud
  (Amazon EC2) Linux t2.micro instances in the same subnets as your AD Connector. Network
  connectivity tests are then performed using the `netcat` and
  `nslookup` utilities.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootADConnectorConnectivity "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootADConnectorConnectivity")

###### Important

Using this runbook might incur extra charges to your AWS account for the Amazon EC2
instances, Amazon Elastic Block Store volumes and Amazon Machine Image (AMI) created during the automation. For
more information, see [Amazon Elastic Compute Cloud
Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") and [Amazon Elastic Block Store
Pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

If the `aws:deletestack` step fails, go to the AWS CloudFormation console to
manually delete the stack. The stack name created by this runbook begins with
`AWSSupport-TroubleshootADConnectorConnectivity`. For information about
deleting AWS CloudFormation stacks, see [Deleting a
stack](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the _AWS CloudFormation User Guide_.

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

- DirectoryId

Type: String

Description: (Required) The ID of the AD Connector directory you want to
troubleshoot connectivity to.

- Ec2InstanceProfile

Type: String

Maximum characters: 128

Description: (Required) The name of the instance profile you want to assign to the
instances that are launched to perform connectivity tests. The instance profile you
specify must have the `AmazonSSMManagedInstanceCore` policy or equivalent
permissions attached.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `ec2:DescribeImages`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeVpcEndpoints`
- `ec2:CreateTags`
- `ec2:RunInstances`
- `ec2:StopInstances`
- `ec2:TerminateInstances`
- `cloudformation:CreateStack`
- `cloudformation:DescribeStacks`
- `cloudformation:ListStackResources`
- `cloudformation:DeleteStack`
- `ds:DescribeDirectories`
- `ssm:SendCommand`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ssm:GetParameters`
- `ssm:DescribeInstanceInformation`
- `iam:PassRole`

**Document Steps**

- `aws:assertAwsResourceProperty` - Confirms the directory specified in the
  `DirectoryId` parameter is an AD Connector.
- `aws:executeAwsApi` - Gathers information about the AD Connector.
- `aws:executeAwsApi` - Gathers information about the security groups that
  are associated with the AD Connector.
- `aws:executeAwsApi` - Gathers information about the network ACL rules
  that are associated with the subnets for the AD Connector.
- `aws:executeScript` - Evalutes the AD Connector security group rules to
  verify that the required outbound traffic is allowed.
- `aws:executeScript` - Evalutes the AD Connector network ACL rules to
  verify that the required outbound and inbound network traffic is allowed.
- `aws:executeScript` - Checks if the AWS Systems Manager, AWS Security Token Service and Amazon CloudWatch
  interface endpoints exist in the same VPC as the AD Connector.
- `aws:executeScript` - Compiles the outputs of the checks performed in the
  previous steps.
- `aws:branch` - Branches the automation depending on the output of
  previous steps. The automation stops here if the required outbound and inbound rules
  are missing for the security groups and network ACLs.
- `aws:createStack` - Creates an AWS CloudFormation stack to launch Amazon EC2 instances to
  perform connectivity tests.
- `aws:executeAwsApi` - Gathers the IDs of newly launched Amazon EC2 instances.
- `aws:waitForAwsResourceProperty` - Waits for the first newly launched
  Amazon EC2 instance to report as managed by AWS Systems Manager.
- `aws:waitForAwsResourceProperty` - Waits for the second newly launched
  Amazon EC2 instance to report as managed by AWS Systems Manager.
- `aws:runCommand` - Performs network connectivity tests to the on-premises
  DNS server IP addresses from the first Amazon EC2 instance.
- `aws:runCommand` - Performs network connectivity tests to the on-premises
  DNS server IP addresses from the second Amazon EC2 instance.
- `aws:changeInstanceState` - Stops the Amazon EC2 instances used for the
  connectivity tests.
- `aws:deleteStack` - Deletes the AWS CloudFormation stack.
- `aws:executeScript` - Outputs instructions about how to manually delete
  the AWS CloudFormation stack if the automation fails to delete the stack.
