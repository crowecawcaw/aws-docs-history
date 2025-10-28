# Delete policies

You can delete your **Cluster policy** and **Compute
allocation** configurations using the SageMaker AI console or AWS CLI. The
following page provides instructions on how to delete your SageMaker HyperPod task
governance policies and configurations.

For more information about the HyperPod task governance EKS cluster
policy concepts, see [Policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md").

###### Note

If you are having issues with listing or deleting task governance policies,
you may need to update your cluster administrator minimum set of permissions.
See the **Amazon EKS** tab in the [IAM users for
cluster admin](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin")
section. For additional information, see [Deleting clusters](sagemaker-hyperpod-eks-operate-console-ui-governance-troubleshoot.md#hp-eks-troubleshoot-delete-policies "sagemaker-hyperpod-eks-operate-console-ui-governance-troubleshoot.md#hp-eks-troubleshoot-delete-policies").

The following uses the SageMaker AI console to delete your HyperPod task
governance policies.

###### Note

You cannot delete your **Cluster policy**
(`ClusterSchedulerConfig`) using the SageMaker AI console. To
learn how to do so using the AWS CLI, see [Delete HyperPod task governance policies (AWS CLI)](#sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete-cli "#sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete-cli").

###### To delete task governance policies (console)

1.  Navigate to the [Amazon SageMaker AI
    console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  On the left navigation pane, under **HyperPod
    Clusters**, choose **Cluster
    Management**.
3.  Choose your Amazon EKS cluster listed under **SageMaker HyperPod
    clusters**.
4.  Choose the **Policies** tab.
5.  To delete your **Compute allocation**
    (`ComputeQuota`):

        1. In the **Compute allocation** section,
         select the configuration you want to delete.
        2. In the **Actions** dropdown menu, choose
         **Delete**.
        3. Follow the instructions in the UI to complete the
         task.

    The following uses the AWS CLI to delete your HyperPod task
    governance policies.

###### Note

If you are having issues using the following commands, you may need to
update your AWS CLI. For more information, see [Installing
or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### To delete task governance policies (AWS CLI)

First set your variables for the AWS CLI commands that follow.

```
REGION=`aws-region`
```

1. Get the `cluster-arn` associated with the
   policies you wish to delete. You can use the following AWS CLI command
   to list the clusters in your AWS Region.

```
aws sagemaker list-clusters \
    --region ${REGION}
```

2. To delete your compute allocations
   (`ComputeQuota`):
   1. List all of the compute quotas associated with the
      HyperPod cluster.

   ```
   aws sagemaker list-compute-quotas \
       --cluster-arn `cluster-arn` \
       --region ${REGION}
   ```

   2. For each
      `compute-quota-id`
      you wish to delete, run the following command to delete the
      compute quota.

   ```
   aws sagemaker delete-compute-quota \
       --compute-quota-id `compute-quota-id` \
       --region ${REGION}
   ```

3. To delete your cluster policies
   (`ClusterSchedulerConfig`):
   1. List all of the cluster policies associated with the
      HyperPod cluster.

   ```
   aws sagemaker list-cluster-scheduler-configs \
       --cluster-arn `cluster-arn` \
       --region ${REGION}
   ```

   2. For each
      `cluster-scheduler-config-id`
      you wish to delete, run the following command to delete the
      compute quota.

   ```
   aws sagemaker delete-cluster-scheduler-config
       --cluster-scheduler-config-id `scheduler-config-id` \
       --region ${REGION}
   ```
