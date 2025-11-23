# Choose the Concurrency Mode for CloudFormation StackSets

**Concurrency Mode** is a parameter for [StackSetOperationPreferences](../APIReference/API_StackSetOperationPreferences.md "../APIReference/API_StackSetOperationPreferences.md") that allows you to choose how the concurrency level behaves
during StackSet operations. You can choose between the following modes:

- **Strict Failure Tolerance**: This option dynamically lowers the concurrency level to ensure
  the number of failed accounts never exceeds the value of **Failure tolerance** +1. The initial
  actual concurrency is set to the lower of either the value of the **Maximum concurrent accounts**,
  or the value of **Failure tolerance** +1. The actual concurrency is then reduced proportionally by
  the number of failures. This is the default behavior.
- **Soft Failure Tolerance**: This option decouples **Failure tolerance** from
  the actual concurrency. This allows StackSet operations to run at the concurrency level set by the
  **Maximum concurrent accounts** value, regardless of the number of failures.
  **Strict Failure Tolerance** lowers the deployment speed as StackSet operation failures occur
  because concurrency decreases for each failure. **Soft Failure Tolerance** prioritizes deployment
  speed while still leveraging CloudFormation safety capabilities. This allows you to review and address StackSet operation
  failures for common issues such as those related to existing resources, service quotas, and permissions.

For more information on StackSets stack operation failures, see [Common reasons for stack
operation failure](stacksets-troubleshooting.md#common-reasons-for-stack-operation-failure "stacksets-troubleshooting.md#common-reasons-for-stack-operation-failure").

For more information on **Maximum concurrent accounts** and **Failure
tolerance**, see [StackSet operation options](stacksets-concepts.md#stackset-ops-options "stacksets-concepts.md#stackset-ops-options").

## How each Concurrency Mode works

The images below provide a visual representation of how each **Concurrency Mode** works during
a StackSet operation. The string of nodes represents a deployment to single AWS Region and each node is a target
AWS account.

**Strict Failure Tolerance**

When a StackSet operation using **Strict Failure Tolerance** has the **Failure
tolerance** value set to 5 and the **Maximum concurrent accounts** value set to 10, the
actual concurrency is 6. The actual concurrency is 6 because this the **Failure tolerance** value
of 5 +1 is lower than the value of **Maximum concurrent accounts**.

The following image shows the impact that the **Failure tolerance** value has on the
**Maximum concurrent accounts** value, and the impact they both have on the actual concurrency
of the StackSet operation:

![A StackSet operation using strict failure tolerance. Fail tolerance is 5, max concurrent account is 10, and concurrency is 6.](images/concurrency-strict-failure-tolerance-1.png)

When deployment begins and there are failed stack instances, then the actual concurrency reduces to provide a
safe deployment experience. The actual concurrency reduces from 6 to 5 when StackSets fails to deploy 1 stack
instance.

![The StackSet operation using Strict Failure Tolerance has 2 successful deployments and 1 failure.](images/concurrency-strict-failure-tolerance-2.png)

![The StackSet operation using Strict Failure Tolerance has reduced the actual concurrency to 5 now that there is one failure.](images/concurrency-strict-failure-tolerance-3.png)

The **Strict Failure Tolerance** mode reduces the actual concurrency proportionally to the
number of failed stack instances. In the following example, the actual concurrency reduces from 5 to 3 when
StackSets fails to deploy 2 more stack instances, bringing the total of failed stack instances to 3.

![The StackSet operation using Strict Failure Tolerance now has 3 failed deployments. Concurrency has reduced to 3.](images/concurrency-strict-failure-tolerance-4.png)

StackSets fails the StackSet operation when the number of failed stack instances equals the defined value of
**Failure tolerance** +1. In the following example, StackSets fails the operation when there are
6 failed stack instances and the **Failure tolerance** value is 5.

![The StackSet operation using Strict Failure Tolerance now has 6 failed deployments. The StackSet operation fails.](images/concurrency-strict-failure-tolerance-5.png)

In this example, CloudFormation deployed 9 stack instances (3 successful and 6 failed) before stopping the
StackSet operation.

**Soft Failure Tolerance**

When a StackSet operation using **Soft Failure Tolerance** has the **Failure
tolerance** value set to 5 and the **Maximum concurrent accounts** value set to 10, the
actual concurrency is 10.

![A StackSet operation with Soft Failure Tolerance. Fail tolerance is 5 max concurrent accounts and actual concurrency are 10.](images/concurrency-soft-failure-tolerance-1.png)

When deployment begins and there are failed stack instances, the actual concurrency doesn't change. In the
following example, 1 stack operation failed, but the actual concurrency remains at 10.

![The StackSet operation with Soft Failure Tolerance encounters the first failure. Actual concurrency remains at 10.](images/concurrency-soft-failure-tolerance-2.png)

The actual concurrency remains at 10 even after 2 more stack instance failures.

![The StackSet operation with Soft Failure Tolerance now has 2 successes and 3 failures, but actual concurrency is still 10.](images/concurrency-soft-failure-tolerance-3.png)

StackSets fails the StackSet operation when failed stack instances exceeds the **Failure
tolerance** value. In the following example, StackSets fails the operation when there are 6 failed stack
instances and the **Failure tolerance** count is 5. However, the operation won't end until the
remaining operations in the concurrency queue finish.

![The StackSet operation with Soft Failure Tolerance reaches 6 fails, but it must finish what's left in the concurrency queue.](images/concurrency-soft-failure-tolerance-4.png)

StackSets continues to deploy stack instances that are already in the concurrency queue. This means that the
number of failed stack instances can be higher than **Failure tolerance**. In the following
example, there are 8 failed stack instances because the concurrency queue still had 7 operations left to perform,
even though the StackSet operation had reached the **Failure tolerance** of 5.

![The StackSet operation has 8 total fails because it had 7 deployments left in the queue after it reached the fail threshold.](images/concurrency-soft-failure-tolerance-5.png)

In this example, StackSets deployed 15 stack instances (7 successful and 8 failed) before stopping the
stack operation.

## Choosing between Strict failure tolerance and Soft failure tolerance

based on deployment speed

Choosing between **Strict failure tolerance** and **Soft failure tolerance**
modes depends on the preferred speed of your StackSet deployment and the permissible number of deployment
failures.

The following tables show how each concurrency mode handles a StackSet operation that fails while trying to
deploy 1000 total stack instances. In each scenario, the **Failure tolerance** value is set to 100
stack instances and the **Maximum concurrent accounts** value is set to 250 stack instances.

While StackSets actually queues accounts as a sliding window (see [How each Concurrency Mode works](#concurrency-mode-example "#concurrency-mode-example")), this example shows the operation in
batches to demonstrate the speed of each mode.

### Strict failure tolerance

This example using **Strict failure tolerance** mode lowers the actual concurrency relative to
the number of failures that occur in each preceding batch. Each batch has 20 failed instances, which then lowers the
actual concurrency of the following batch by 20 until the StackSet operation reaches the **Failure
tolerance** value of 100.

In following table, the initial actual concurrency of the first batch is 101 stack instances. The actual
concurrency is 101 because it's the lower value of either the **Maximum concurrent accounts** (250)
and the **Failure tolerance** (100) +1. Each batch contains 20 failed stack instance deployments,
which then lowers the actual concurrency of each following batch by 20 stack instances.

| **Strict failure tolerance**        | **Batch 1** | **Batch 2** | **Batch 3** | **Batch 4** | **Batch 5** | **Batch 6** |
| ----------------------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Actual concurrency count**        | 101         | 81          | 61          | 41          | 21          | -           |
| **Failed instance count**           | 20          | 20          | 20          | 20          | 20          | -           |
| **Successful stack instance count** | 81          | 61          | 41          | 21          | 1           | -           |

The operation using **Strict failure tolerance** completed 305 stack instance deployments in 5
batches by the time the StackSet operation reached the **Failure tolerance** of 100 stack
instances. The StackSet operation successfully deploys 205 stack instances before it fails.

### Soft failure tolerance

This example using **Soft failure tolerance** mode maintains the same actual concurrency count
defined by the **Maximum concurrent accounts** value of 250 stack instances, regardless of the
number of failed instances. The StackSet operations keeps the same actual concurrency until it reaches the
**Failure tolerance** value of 100 instances.

In following table, the initial actual concurrency of the first batch is 250 stack instances. The actual
concurrency is 250 because the **Maximum concurrent accounts** value is set to 250 and
**Soft failure tolerance** mode allows StackSets to use this value as the actual concurrency,
regardless of the number of failures. Even though there are 50 failures in each of the batches for this example, the
actual concurrency remains unaffected.

| **Soft failure tolerance**          | **Batch 1** | **Batch 2** | **Batch 3** | **Batch 4** | **Batch 5** | **Batch 6** |
| ----------------------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Actual concurrency count**        | 250         | 250         | -           | -           | -           | -           |
| **Failed instance count**           | 50          | 50          | -           | -           | -           | -           |
| **Successful stack instance count** | 200         | 200         | -           | -           | -           | -           |

Using the same **Maximum concurrent accounts** value and **Failure
tolerance** value, the operation using **Soft failure tolerance** mode completed 500
stack instance deployments in 2 batches. The StackSet operation successfully deploys 400 stack instances before it
fails.

## Choosing your Concurrency Mode (console)

When creating or updating a StackSet, on the **Set deployment options** page,
for **Concurrency mode**, choose **Strict failure tolerance** or **Soft failure
tolerance**.

## Choosing your Concurrency Mode (AWS CLI)

You can use the `ConcurrencyMode` parameter with the following StackSets commands:

- [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md")
- [delete-stack-instances](../../../cli/latest/reference/cloudformation/delete-stack-instances.md "../../../cli/latest/reference/cloudformation/delete-stack-instances.md")
- [detect-stack-set-drift](../../../cli/latest/reference/cloudformation/detect-stack-set-drift.md "../../../cli/latest/reference/cloudformation/detect-stack-set-drift.md")
- [import-stacks-to-stack-set](../../../cli/latest/reference/cloudformation/import-stacks-to-stack-set.md "../../../cli/latest/reference/cloudformation/import-stacks-to-stack-set.md")
- [update-stack-instances](../../../cli/latest/reference/cloudformation/update-stack-instances.md "../../../cli/latest/reference/cloudformation/update-stack-instances.md")
- [update-stack-set](../../../cli/latest/reference/cloudformation/update-stack-set.md "../../../cli/latest/reference/cloudformation/update-stack-set.md")

These commands have an existing parameter called `--operation-preferences` that can use the
`ConcurrencyMode` setting. `ConcurrencyMode` can be set to one of the following values:

- `STRICT_FAILURE_TOLERANCE`
- `SOFT_FAILURE_TOLERANCE`

The following example creates a stack instance using the `STRICT_FAILURE_TOLERANCE`
`ConcurrencyMode`, with a `FailureToleranceCount` set to 10 and a
`MaxConcurrentCount` set to 5.

```
aws cloudformation create-stack-instances \
  --stack-set-name `example-stackset` \
  --accounts `123456789012` \
  --regions `eu-west-1`  \
  --operation-preferences ConcurrencyMode=STRICT_FAILURE_TOLERANCE,FailureToleranceCount=10,MaxConcurrentCount=5
```

###### Note

For detailed procedures for creating and updating a StackSet, see the following topics:

- [Create
  StackSets (self-managed permissions)](stacksets-getting-started-create-self-managed.md "stacksets-getting-started-create-self-managed.md")
- [Create
  StackSets (service-managed permissions)](stacksets-orgs-associate-stackset-with-org.md "stacksets-orgs-associate-stackset-with-org.md")
- [Update StackSets](stacksets-update.md "stacksets-update.md")
