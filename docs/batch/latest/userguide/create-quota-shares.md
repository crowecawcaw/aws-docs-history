

# Creating quota shares
<a name="create-quota-shares"></a>

Quota shares function as virtual queues within the associated job queue that the AWS Batch scheduler iterates between when scheduling. They enable administrators to allocate a compute quota to a team or project via ` capacity limits `, with explicit configuration for resource sharing strategy. 

## Prerequisites
<a name="create-quota-shares-prerequisites"></a>

Before creating quota shares, ensure you have:
+ **Quota management scheduling policy, service environment and job queue** – A quota management scheduling policy, service environment, and job queue with quota management enabled. For more information, see [Create quota management resources](create-quota-management-resources.md).
+ **IAM permissions** – Permissions to create and manage AWS Batch quota shares. For more information, see [AWS Batch IAM policies, roles, and permissions](IAM_policies.md).

------
#### [ Configure quota shares (AWS Batch console) ]

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane, choose **Job queues** and select a quota management enabled job queue from the list. Choose the job queue name link.

1. In the **Quota shares** section, choose **Create quota share**.

1. Provide a **Name** for the quota share.

1. For **Capacity limits**, choose **Add capacity limits**. At least one capacity limit must be specified.

   1. Select an **Instance type** from the dropdown, and set the **Maximum instances** this quota share has allocated to it.

   1. (Optional) Choose **Add capacity limits** and repeat to attach at most five capacity limits.

1. For **Capacity sharing**, choose how this quota share shares its capacity with other quota shares in the same job queue:
   + Select **Reserve** if the quota share should not lend or borrow idle compute.
   + Select **Lend** if the quota share can lend idle compute to other quota shares.
   + Select **Lend and borrow** if the quota share can both lend and borrow idle compute, with lent compute reclaimed via cross-share preemption when work arrives.

1. (Optional) For **In-share preemption**, choose whether to enable or disable in-share preemption. Enabling in-share preemption allows higher-priority jobs to preempt lower priority jobs that are already in `SCHEDULED`, `STARTING`, or `RUNNING` state. Disabling in-share preemption means that the higher priority jobs will wait for capacity to become available.

1. Choose **Create quota share**.

------
#### [ Configure quota shares (AWS CLI) ]

Use the `create-quota-share` command to create a quota share. You must choose a resource sharing strategy and whether to enable in-share preemption.

**Lend and borrow example**

The following example creates a quota share that can lend and borrow idle capacity, with a borrow limit of 100% of its configured capacity limits. It also enables in-share preemption, so higher priority jobs don't wait for lower priority jobs that have been scheduled within SageMaker AI to complete.

```
aws batch create-quota-share \
  --quota-share-name {{lend_and_borrow_qs}} \
  --job-queue {{my-qm-sagemaker-jq}} \
  --capacity-limits maxCapacity=5,capacityUnit=ml.m6i.large \
  --resource-sharing-configuration strategy=LEND_AND_BORROW,borrowLimit=100 \
  --preemption-configuration inSharePreemption=ENABLED
```

**Lend only example**

Quota shares can be configured to only lend idle capacity, but not borrow it themselves. The following example pairs `LEND` with disabling in-share preemption.

```
aws batch create-quota-share \
  --quota-share-name {{lend_qs}} \
  --job-queue {{my-qm-sagemaker-jq}} \
  --capacity-limits maxCapacity=8,capacityUnit=ml.m6i.large \
  --resource-sharing-configuration strategy=LEND \
  --preemption-configuration inSharePreemption=DISABLED
```

**Reserve example**

Quota shares can also be configured to reserve idle capacity. Newly submitted jobs when a quota share has idle capacity may start sooner, but overall queue utilization will be lower if a quota share has no jobs.

```
aws batch create-quota-share \
  --quota-share-name {{reserved_qs}} \
  --job-queue {{my-qm-sagemaker-jq}} \
  --capacity-limits maxCapacity=2,capacityUnit=ml.m6i.large \
  --resource-sharing-configuration strategy=RESERVE \
  --preemption-configuration inSharePreemption=DISABLED
```

------