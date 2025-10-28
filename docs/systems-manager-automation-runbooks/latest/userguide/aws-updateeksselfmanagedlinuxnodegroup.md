# `AWS-UpdateEKSSelfManagedLinuxNodeGroups`

**Description**

The `AWS-UpdateEKSSelfManagedLinuxNodeGroups` runbook updates
self-managed managed node groups in your Amazon Elastic Kubernetes Service (Amazon EKS) cluster using an
AWS CloudFormation stack.

If your cluster uses auto scaling, we recommend scaling the deployment down to two
replicas before using this runbook.

###### To scale a deployment to two replicas

1. Install the Kubernetes command line utility, `kubectl`. For
   more information, see [Installing kubectl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") in the _Amazon EKS User Guide_.
2. Run the following command.

```
kubectl scale deployments/cluster-autoscaler --replicas=2 -n kube-system
```

3. Run the `AWS-UpdateEKSSelfManagedLinuxNodeGroups` runbook.
4. Scale the deployment back to the desired number of replicas by running the
   following command.

```
kubectl scale deployments/cluster-autoscaler --replicas=`number` -n kube-system
```

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSSelfManagedLinuxNodeGroups "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSSelfManagedLinuxNodeGroups")

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

Description: (Required) The name of the Amazon EKS cluster.

- NodeGroupName

Type: String

Description: (Required) The name of the managed node group.

- ClusterControlPlaneSecurityGroup

Type: String

Description: (Required) The ID of the control plane security group.

- DisableIMDSv1

Type: Boolean

Description: (Optional) Determines whether you want to allow Instance
Metadata Service Version 1 (IMDSv1) and IMDSv2.

- KeyName

Type: String

Description: (Optional) The key name for the instances.

- NodeAutoScalingGroupDesiredCapacity

Type: String

Description: (Optional) The number of nodes that the node group should
maintain.

- NodeAutoScalingGroupMaxSize

Type: String

Description: (Optional) The maximum number of nodes that the node group
can scale out to.

- NodeAutoScalingGroupMinSize

Type: String

Description: (Optional) The minimum number of nodes that the node group
can scale in to.

- NodeInstanceType

Type: String

Default: t3.large

Description: (Optional) The instance type that you want to use for the
node group.

- NodeImageId

Type: String

Description: (Optional) The ID of the Amazon Machine Image (AMI) that you want the
node group to use.

- NodeImageIdSSMParam

Type: String

Default:
/aws/service/eks/optimized-ami/1.21/amazon-linux-2/recommended/image_id

Description: (Optional) The public Systems Manager parameter for the AMI that you
want the node group to use.

- StackName

Type: String

Description: (Required) The name of the AWS CloudFormation stack used to update the
node group.

- Subnets

Type: String

Description: (Required) A comma-separated list of the IDs for the subnets
that you want your cluster to use.

- VpcId

Type: String

Default: Default

Description: (Required) The virtual private cloud (VPC) where your cluster
is deployed.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `eks:CreateCluster`
- `eks:CreateNodegroup`
- `eks:DeleteNodegroup`
- `eks:DeleteCluster`
- `eks:DescribeCluster`
- `eks:DescribeNodegroup`
- `eks:ListClusters`
- `eks:ListNodegroups`
- `eks:UpdateClusterConfig`
- `eks:UpdateNodegroupConfig`

**Document Steps**

- `aws:executeScript` - Updates an Amazon EKS cluster node group
  according to the values that you specify for the runbook input
  parameters.
- `aws:waitForAwsResourceProperty` - Waits for the AWS CloudFormation stack
  update status to be returned.
