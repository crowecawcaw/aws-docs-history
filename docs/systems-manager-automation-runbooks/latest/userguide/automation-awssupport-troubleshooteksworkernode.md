# `AWSSupport-TroubleshootEKSWorkerNode`

**Description**

The `AWSSupport-TroubleshootEKSWorkerNode` runbook analyzes an
Amazon Elastic Compute Cloud (Amazon EC2) worker node and Amazon Elastic Kubernetes Service (Amazon EKS) cluster to help you identify and
troubleshoot common causes that prevent worker nodes from joining a cluster. The
runbook outputs guidance to help you resolve any issues that are identified.

###### Important

To successfully run this automation, the state of your Amazon EC2 worker node must
be `running` , and the Amazon EKS cluster state must be
`ACTIVE` .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSWorkerNode "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSWorkerNode")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ClusterName

Type: String

Description: (Required) The name of the Amazon EKS cluster.

- WorkerID

Type: String

Description: (Required) The ID of the Amazon EC2 worker node that failed to
join the cluster.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeDhcpOptions`
- `ec2:DescribeImages`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeNatGateways`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeVpcEndpoints`
- `ec2:DescribeVpcs`
- `eks:DescribeCluster`
- `iam:GetInstanceProfile`
- `iam:GetRole`
- `iam:ListAttachedRolePolicies`
- `ssm:DescribeInstanceInformation`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:SendCommand`

**Document Steps**

- `aws:assertAwsResourceProperty` - Confirms that the Amazon EKS cluster
  you specify in the `ClusterName` parameter exists and is in an
  `ACTIVE` state.
- `aws:assertAwsResourceProperty` - Confirms that the Amazon EC2 worker
  node you specify in the `WorkerID` parameter exists and is in a
  `running` state.
- `aws:executeScript` - Runs a Python script that helps identify
  possible causes for the worker node failing to join the cluster.
