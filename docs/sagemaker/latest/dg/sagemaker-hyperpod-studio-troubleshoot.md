# Troubleshooting

The following section lists troubleshooting solutions for HyperPod in
Studio.

###### Topics

- [Tasks tab](#sagemaker-hyperpod-studio-troubleshoot-tasks "#sagemaker-hyperpod-studio-troubleshoot-tasks")
- [Metrics tab](#sagemaker-hyperpod-studio-troubleshoot-metrics "#sagemaker-hyperpod-studio-troubleshoot-metrics")

## Tasks tab

If you get **`Custom Resource Definition (CRD) is not configured on the
 cluster`** while in the **Tasks** tab.

- Grant `EKSAdminViewPolicy` and `ClusterAccessRole` policies to your
  domain execution role.

For information on how to add tags to your execution role, see [Tag IAM
roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md").

To learn how to attach policies to an IAM user or group, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

If the tasks grid for Slurm metrics doesn’t stop loading in the **Tasks**
tab.

- Ensure that `RunAs` enabled in your [AWS Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") preferences
  and the role you are using has the `SSMSessionRunAs` tag attached.
  - To enable `RunAs`, navigate to the **Preference** tab in
    the [Systems Manager console](https://console.aws.amazon.com/systems-manager/session-manager "https://console.aws.amazon.com/systems-manager/session-manager").
  - [Turn on Run As
    support for Linux and macOS managed nodes](../../../systems-manager/latest/userguide/session-preferences-run-as.md "../../../systems-manager/latest/userguide/session-preferences-run-as.md")

For restricted task view in Studio for EKS clusters:

- If your execution role doesn’t have permissions to list namespaces for EKS
  clusters.
  - See [Restrict task view in
    Studio for EKS clusters](sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view "sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view").

- If users are experiencing issues with access for EKS clusters.
  1.  Verify RBAC is enabled by running the following AWS CLI command.

  ```
  kubectl api-versions | grep rbac
  ```

  This should return rbac.authorization.k8s.io/v1. 2. Check if the `ClusterRole` and `ClusterRoleBinding` exist by
  running the following commands.

  ```
  kubectl get clusterrole pods-events-crd-cluster-role
  kubectl get clusterrolebinding pods-events-crd-cluster-role-binding
  ```

  3.  Verify user group membership. Ensure the user is correctly assigned to the
      `pods-events-crd-cluster-level` group in your identity provider or IAM.

- If user can't see any resources.
  - Verify group membership and ensure the `ClusterRoleBinding` is correctly
    applied.

- If users can see resources in all namespaces.
  - If namespace restriction is required, consider using `Role` and
    `RoleBinding` instead of `ClusterRole` and
    `ClusterRoleBinding`.

- If configuration appears correct, but permissions aren't applied.
  - Check if there are any `NetworkPolicies` or `PodSecurityPolicies`
    interfering with access.

## Metrics tab

If there are no Amazon CloudWatch metrics are displayed in the **Metrics**
tab.

- The `Metrics` section of HyperPod cluster details uses CloudWatch to fetch
  the data. In order to see the metrics in this section, you need to have enabled [Cluster and task
  observability](sagemaker-hyperpod-eks-cluster-observability-cluster.md "sagemaker-hyperpod-eks-cluster-observability-cluster.md"). Contact your
  administrator to configure metrics.
