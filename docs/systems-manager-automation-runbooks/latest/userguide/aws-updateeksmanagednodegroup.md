# `AWS-UpdateEKSManagedNodeGroup`

**Description**

The `AWS-UpdateEKSManagedNodeGroup` runbook helps you update an
Amazon Elastic Kubernetes Service (Amazon EKS) managed node group. You can either choose a `Version`
or `Configuration` update.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSManagedNodeGroup "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSManagedNodeGroup")

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

Description: (Required) The name of the cluster whose node group you want
to update.

- NodeGroupName

Type: String

Description: (Required) The name of the node group to update.

- UpdateType

Type: String

Valid values: Update Node Group Version | Update Node Group
Configurations

Default: Update Node Group Version

Description: (Required) The type of update that you want to perform on the
node group.
The following parameters apply only to the `Version` update
type:

- AMIReleaseVersion

Type: String

Description: (Optional) The version of the Amazon EKS optimized AMI that you
want to use. By default, the latest version is used.

- ForceUpgrade

Type: Boolean

Description: (Optional) If true, the update won't fail in response to a
pod disruption budget violation.

- KubernetesVersion

Type: String

Description: (Optional) The Kubernetes version to update the node group
to.

- LaunchTemplateId

Type: String

Description: (Optional) The ID of the launch template.

- LaunchTemplateName

Type: String

Description: (Optional) The name of the launch template.

- LaunchTemplateVersion

Type: String

Description: (Optional) The Amazon Elastic Compute Cloud (Amazon EC2) launch template version.
This parameter is only valid if a node group was created from a launch
template.
The following parameters apply only to the `Configuration` update
type:

- AddOrUpdateNodeGroupLabels

Type: StringMap

Description: (Optional) Kubernetes labels that you want to add or
update.

- AddOrUpdateKubernetesTaintsEffect

Type: StringList

Description: (Optional) The Kubernetes taints that you want to add or
update.

- MaxUnavailableNodeGroups

Type: Integer

Default: 0

Description: (Optional) The maximum number of nodes that are unavailable
at once during a version update.

- MaxUnavailablePercentageNodeGroup

Type: Integer

Default: 0

Description: (Optional) The percentage of nodes that are unavailable
during a version update.

- NodeGroupDesiredSize

Type: Integer

Default: 0

Description: (Optional) The number of nodes that the managed node group
should maintain.

- NodeGroupMaxSize

Type: Integer

Default: 0

Description: (Optional) The maximum number of nodes that the managed node
group can scale out to.

- NodeGroupMinSize

Type: Integer

Default: 0

Description: (Optional) The minimum number of nodes that the managed node
group can scale in to.

- RemoveKubernetesTaintsEffect

Type: StringList

Description: (Optional) The Kubernetes taints that you want to
remove.

- RemoveNodeGroupLabels

Type: StringList

Description: (Optional) A comma-separated list of labels that you want to
remove.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `eks:UpdateNodegroupConfig`
- `eks:UpdateNodegroupVersion`

**Document Steps**

- `aws:executeScript` - Updates an Amazon EKS cluster node group
  according to the values that you specify for the runbook input parameters.
- `aws:waitForAwsResourceProperty` - Waits for the cluster update
  status to be `Successful`.
