# Edit policies

You can edit your **Cluster policy** and **Compute
allocation** configurations in the **Policies** tab.
The following provides instructions on how to edit the following
configurations.

- Edit your **Cluster policy** to update how tasks are
  prioritized and idle compute is allocated.
- Edit **Compute allocation** to create a new compute
  allocation policy for a team.

###### Note

When you create a **Compute allocation** you will
need to set up a Kubernetes role-based access control (RBAC) for data
scientist users in the corresponding namespace to run tasks on
HyperPod clusters orchestrated with Amazon EKS. The namespaces have
the format
`hyperpod-ns-`team-name``. To set up
a Kubernetes RBAC, use the instructions in [create team role](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role").
For more information about the HyperPod task governance EKS cluster
policy concepts, see [Policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md").

###### Edit HyperPod task governance policies

This procedure assumes that you have already created an Amazon EKS cluster set up
with HyperPod. If you have not already done so, see [Creating
a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").

1. Navigate to the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, under **HyperPod
   Clusters**, choose **Cluster
   Management**.
3. Choose your Amazon EKS cluster listed under **SageMaker HyperPod
   clusters**.
4. Choose the **Policies** tab.
5. To edit your **Cluster policy**:
   1. Choose the corresponding **Edit** to update how
      tasks are prioritized and idle compute is allocated.
   2. After you have made your changes, choose
      **Submit**.

6. To edit your **Compute allocation**:
7. 1. Choose the configuration you wish to edit under **Compute
      allocation**. This takes you to the configuration
      details page.
   2. If you wish to edit these configurations, choose
      **Edit**.
   3. After you have made your changes, choose
      **Submit**.
