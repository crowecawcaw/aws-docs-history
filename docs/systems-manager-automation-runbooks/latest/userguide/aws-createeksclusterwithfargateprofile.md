# `AWS-CreateEKSClusterWithFargateProfile`

**Description**

The `AWS-CreateEKSClusterWithFargateProfile` runbook creates an
Amazon Elastic Kubernetes Service (Amazon EKS) cluster using an AWS Fargate.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateEKSClusterWithFargateProfile "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateEKSClusterWithFargateProfile")

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

- ClusterName

Type: String

Description: (Required) A unique name for the cluster.

- ClusterRoleArn

Type: String

Description: (Required) The ARN of the IAM role that provides
permissions for the Kubernetes control plane to make calls to AWS API
operations on your behalf.

- FargateProfileName

Type: String

Description: (Required) The name of the Fargate profile.

- FargateProfileRoleArn

Type: String

Description: (Required) The ARN of the Amazon EKS Pod execution IAM
role.

- FargateProfileSelectors

Type: String

Description: (Required) The selectors to match pods to the Fargate
profile.

- SubnetIds

Type: StringList

Description: (Required) The IDs of the subnets you want to use for your
Amazon EKS cluster. Amazon EKS creates elastic network interfaces in these subnets for
communication between your nodes and the Kubernetes control plane. You must
specify at least two subnet IDs.

- EKSEndpointPrivateAccess

Type: Boolean

Default: True

Description: (Optional) Set this value to `True` to allow
private access for your cluster's Kubernetes API server endpoint. If you
enable private access, Kubernetes API requests from within your cluster's
VPC use the private VPC endpoint. If you disable private access and you have
nodes or AWS Fargate pods in the cluster, then ensure that
`publicAccessCidrs` include the necessary CIDR blocks for
communication with the nodes or Fargate pods.

- EKSEndpointPublicAccess

Type: Boolean

Default: False

Description: (Optional) Set this value to `False` to disable
public access to your cluster's Kubernetes API server endpoint. If you
disable public access, your cluster's Kubernetes API server can only receive
requests from within the VPC where it was launched.

- PublicAccessCIDRs

Type: StringList

Description: (Optional) The CIDR blocks that are allowed access to your
cluster's public Kubernetes API server endpoint. Communication to the
endpoint from addresses outside of the CIDR blocks that you specify is
denied. If you've disabled private endpoint access and you have nodes or
Fargate pods in the cluster, then ensure that you specify the necessary
CIDR blocks.

- SecurityGroupIds

Type: StringList

Description: (Optional) Specify one or more security groups to associate
with the elastic network interfaces created in your account by Amazon EKS.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcs`
- `eks:CreateCluster`
- `eks:CreateFargateProfile`
- `eks:DescribeCluster`
- `eks:DescribeFargateProfile`
- `iam:CreateServiceLinkedRole`
- `iam:GetRole`
- `iam:ListAttachedRolePolicies`
- `iam:PassRole`

**Document Steps**

- CreateEKSCluster (aws:executeAwsApi) - Creates an Amazon EKS cluster.
- VerifyEKSClusterIsActive (aws:waitForAwsResourceProperty) - Verifies the
  cluster state is `ACTIVE`.
- CreateFargateProfile (aws:executeAwsApi) - Creates a Fargate for the
  cluster.
- VerifyFargateProfileIsActive (aws:waitForAwsResourceProperty) - Verifies
  the Fargate profile state is `ACTIVE`.

**Outputs**

`CreateEKSCluster.CreateClusterResponse`

Description: Response received from the `CreateCluster` API
call.

`CreateFargateProfile.CreateFargateProfileResponse`

Description: Response received from the
`CreateFargateProfile` API call.
