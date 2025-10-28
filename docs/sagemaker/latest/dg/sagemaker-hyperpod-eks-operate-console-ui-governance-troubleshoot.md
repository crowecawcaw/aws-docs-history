# Troubleshoot

The following page contains known solutions for troubleshooting your HyperPod
EKS clusters.

###### Topics

- [Dashboard tab](#hp-eks-troubleshoot-dashboard "#hp-eks-troubleshoot-dashboard")
- [Tasks tab](#hp-eks-troubleshoot-tasks "#hp-eks-troubleshoot-tasks")
- [Policies](#hp-eks-troubleshoot-policies "#hp-eks-troubleshoot-policies")
- [Deleting clusters](#hp-eks-troubleshoot-delete-policies "#hp-eks-troubleshoot-delete-policies")

## Dashboard tab

**The EKS add-on fails to install**

For the EKS add-on installation to succeed, you will need to have a Kubernets
version >= 1.30. To update, see [Update Kubernetes
version](../../../eks/latest/userguide/update-cluster.md "../../../eks/latest/userguide/update-cluster.md").

For the EKS add-on installation to succeed, all of the nodes need to be in
**Ready** status and all of the pods need to be in
**Running** status.

To check the status of your nodes, use the [`list-cluster-nodes`](../../../cli/latest/reference/sagemaker/list-cluster-nodes.md "../../../cli/latest/reference/sagemaker/list-cluster-nodes.md") AWS CLI command or navigate to your
EKS cluster in the [EKS
console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters") and view the status of your nodes. Resolve the issue for each
node or reach out to your administrator. If the node status is
**Unknown**, delete the node. Once all nodes statuses are
**Ready**, retry installing the EKS add-on in HyperPod
from the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").

To check the status of your pods, use the [Kubernetes CLI](https://kubernetes.io/docs/reference/kubectl/ "https://kubernetes.io/docs/reference/kubectl/")
command `kubectl get pods -n cloudwatch-agent` or navigate to your EKS
cluster in the [EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters")
and view the status of your pods with the namespace `cloudwatch-agent`.
Resolve the issue for the pods or reach out to your administrator to resolve the
issues. Once all pod statuses are **Running**, retry installing the
EKS add-on in HyperPod from the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").

For more troubleshooting, see [Troubleshooting the Amazon CloudWatch Observability EKS add-on](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md#Container-Insights-setup-EKS-addon-troubleshoot "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md#Container-Insights-setup-EKS-addon-troubleshoot").

## Tasks tab

If you see the error message about how the **Custom Resource Definition
(CRD) is not configured on the cluster**, grant
`EKSAdminViewPolicy` and `ClusterAccessRole` policies to
your domain execution role.

- For information on how to get your execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").
- To learn how to attach policies to an IAM user or group, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

## Policies

The following lists solutions to errors relating to policies using the
HyperPod APIs or console.

- If the policy is in `CreateFailed` or
  `CreateRollbackFailed` status, you need to delete the failed
  policy and create a new one.
- If the policy is in `UpdateFailed` status, retry the update
  with the same policy ARN.
- If the policy is in `UpdateRollbackFailed` status, you need to
  delete the failed policy and then create a new one.
- If the policy is in `DeleteFailed` or
  `DeleteRollbackFailed` status, retry the delete with the same
  policy ARN.
  - If you ran into an error while trying to delete the
    **Compute prioritization**, or cluster policy,
    using the HyperPod console, try to delete the
    `cluster-scheduler-config` using the API. To check
    the status of the resource, go to the details page of a compute
    allocation.

To see more details into the failure, use the describe API.

## Deleting clusters

The following lists known solutions to errors relating to deleting
clusters.

- When cluster deletion fails due to attached SageMaker HyperPod task governance
  policies, you will need to [Delete policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md").
- When cluster deletion fails due to the missing the following permissions,
  you will need to update your cluster administrator minimum set of
  permissions. See the **Amazon EKS** tab in the [IAM users for
  cluster admin](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin")
  section.
  - `sagemaker:ListComputeQuotas`
  - `sagemaker:ListClusterSchedulerConfig`
  - `sagemaker:DeleteComputeQuota`
  - `sagemaker:DeleteClusterSchedulerConfig`
