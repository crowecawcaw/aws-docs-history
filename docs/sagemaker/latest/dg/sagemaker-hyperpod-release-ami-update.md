# Update your AMI version in your

SageMaker HyperPod cluster

Amazon SageMaker HyperPod Amazon Machine Images (AMIs) are specialized machine images for
distributed machine learning workloads and high-performance computing. Each AMI comes
pre-loaded with drivers, machine learning frameworks, training libraries, and
performance monitoring tools. By updating the AMI version in your cluster, you can use
the latest versions of these components and packages for your training jobs and
workflows.

When updating the AMI version within your cluster, you have the option to process the
update immediately, schedule a one-time only update, or use a cron expression to create
a recurring schedule. You can also choose to update all of the instances in an instance
group or just batches of instances. If you choose to update batches, you set the
percentage or amount of instances that SageMaker AI should upgrade at a time. If you use this
method of updating, you set an interval of how long SageMaker AI should wait in between
batches.

If you choose to update in batches, you can also include a list of alarms and metrics.
During the wait interval, SageMaker AI observes these metrics and if any exceed their threshold,
the corresponding alarm goes into the ALARM state, and SageMaker AI rolls back the AMI update.
To utilize automatic rollbacks, your IAM execution role must have the permission
`cloudwatch:DescribeAlarms`.

###### Note

Updating your cluster in batches is available only for HyperPod clusters
integrated with Amazon EKS. Also, if you’re creating multiple schedules, we recommend
that you have a time buffer in between schedules. If schedules overlap, updates
might fail.

For more information about each AMI release for your HyperPod cluster, see
[Amazon SageMaker HyperPod AMI](sagemaker-hyperpod-release-ami.md "sagemaker-hyperpod-release-ami.md"). For more information about general
HyperPod releases, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

You can use the SageMaker AI API or CLI operations to update your cluster or see scheduled
updates for a specific cluster. If you're using the AWS console, follow these
steps:

###### Note

Updating your AMI with the AWS console is available only for clusters integrated
with Amazon EKS. If you have a Slurm cluster, you must use the SageMaker AI API or CLI
operations.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left, expand **HyperPod Clusters**, and
   choose **Cluster Management**.
3. Choose the cluster that you want to update, then choose
   **Details**, and **Update
   AMI**.
   To create and manage update schedules programmatically, use the following API
   operations:

- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") – create a cluster while specifying an update
  schedule
- [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") – update a cluster to add an update
  schedule
- [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") – to update the platform software of a
  cluster
- [DescribeCluster](../APIReference/API_DescribeCluster.md "../APIReference/API_DescribeCluster.md") – see an update schedule you created for a
  cluster
- [DescribeClusterNode](../APIReference/API_DescribeClusterNode.md "../APIReference/API_DescribeClusterNode.md") and [ListClusterNodes](../APIReference/API_ListClusterNodes.md "../APIReference/API_ListClusterNodes.md") – see when the cluster was last
  updated.

## Required

permissions

Depending to how you configured your [Pod
Disruption Budget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/ "https://kubernetes.io/docs/tasks/run-application/configure-pdb/") in your Amazon EKS cluster, HyperPod evicts pods,
releases nodes, and prevents any update scheduling during the AMI update process. If
any constraints within the budget are violated, HyperPod skips that node
during the AMI update. For SageMaker HyperPod to correctly evict pods, you must add the
necessary permissions to the HyperPod service-linked role. The following
yaml file has the necessary permissions.

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: hyperpod-patching
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list"]
- apiGroups: [""]
  resources: ["pods/eviction"]
  verbs: ["create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: hyperpod-patching
subjects:
- kind: User
  name: hyperpod-service-linked-role
roleRef:
  kind: ClusterRole
  name: hyperpod-patching
  apiGroup: rbac.authorization.k8s.io
```

Use the following commands to apply the permissions.

```
git clone https://github.com/aws/sagemaker-hyperpod-cli.git

cd sagemaker-hyperpod-cli/helm_chart

helm upgrade hyperpod-dependencies HyperPodHelmChart --namespace kube-system --install
```

## Cron

expressions

To configure a one-time update at a certain time or a recurring schedule, use cron
expressions. Cron expressions support six fields and are separated by white space.
All six fields are required.

```
cron(`Minutes` `Hours` `Day-of-month` `Month` `Day-of-week` `Year`)
```

| **Fields**   | **Values**          | **Wildcards** |
| ------------ | ------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minutes      | 00 – 59             | N/A           |
| Hours        | 00 – 23             | N/A           |
| Day-of-month | 01 – 31             | ?             |
| Month        | 01 – 12             | \* /          |
| Day-of-week  | 1 – 7 or MON-SUN    | ? # L         |
| Year         | Current year – 2099 | \*            | ###### Wildcards <br>• The **\*** (asterisk) wildcard includes all values in the field. In the `Hours` field, **\*** would include every hour. <br>• The **/** (forward slash) wildcard specifies increments. In the `Months` field, you could enter `*/3` to specify every 3rd month. <br>• The **?** (question mark) wildcard specifies one or another. In the `Day-of-month` field you could enter **7**, and if you didn't care what day of the week the seventh was, you could enter **?** in the Day-of-week field. <br>• The **L** wildcard in the `day-of-week` or field specifies the last day of the month or week. For example, `5L` means the last Friday of the month. <br>• The **#** wildcard in the ay-of-week field specifies a certain instance of the specified day of the week within a month. For example, 3#2 would be the second Tuesday of the month: the 3 refers to Tuesday because it is the third day of each week, and the 2 refers to the second day of that type within the month. You can use cron expressions for the following scenarios: <br>• One-time schedule that runs at a certain time and day. You can use the `?` wildcard to denote that day-of-month or day-of-week don't matter. `cron(30 14 ? 12 MON 2024)` `cron(30 14 15 12 ? 2024)` <br>• A weekly schedule that runs at a certain time and day. The following example creates a schedule that runs at 12:00pm on every Monday regardless of day-of-month. `cron(00 12 ? * 1 *)` <br>• Monthly schedule that runs every month regardless of the day-of-week. The following schedule runs at 12:30pm on the 15th of every month. `cron(30 12 15 * ? *)` <br>• A monthly schedule that uses day-of-week. `cron(30 12 ? * MON *)` <br>• To create a schedule that runs every Nth month, use the `/` wildcard. The following example creates a monthly schedule that runs every 3 months. The following two examples demonstrate how it works with day-of-week and day-of-month. `cron(30 12 15 */3 ? *)` `cron(30 12 ? */3 MON *)` <br>• A schedule that runs on a certain instance of the specified day of the week. The following example creates a schedule that runs at 12:30pm on the second Monday of every month. `cron(30 12 ? * 1#2 *)` <br>• A schedule that runs on the last instance of the specified day of the week. The following schedule runs at 12:30pm on the last Monday of every month. `cron(30 12 ? * 1L *)` |
