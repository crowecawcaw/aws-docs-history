

# Deleting and restoring runtimes

As a runtime publisher, you can delete runtimes, runtime versions, and runtime aliases that you no longer need. Deleting a runtime resource can break many Lambda Event Functions, including functions in other AWS accounts that you don't control. Because deletion can have such a wide impact, the deletion design prioritizes preventing accidental deletion and enabling recovery over ease of deletion.

Lambda doesn't delete a runtime resource immediately. Instead, Lambda makes the resource unavailable to functions and schedules it for deletion. The resource stays scheduled for deletion for a waiting period that you choose, from 7 to 30 days. The default is 30 days. Until the waiting period ends, you can restore the resource, and functions that use it recover automatically. After that, Lambda permanently deletes the resource, and you can't recover it.

**Important**  
Lambda doesn't check whether functions use a runtime, runtime version, or runtime alias before you delete it. Before you delete a runtime resource, check its usage metrics and notify your runtime consumers. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md) and [Before you delete](#cmr-delete-before).

## How deletion works
<a name="cmr-delete-design"></a>

Lambda protects functions from accidental deletion with deletion rules and a waiting period.

**Deletion rules** – Lambda rejects delete requests that would leave your runtime resources in an inconsistent state. For example, you can't delete a runtime version that a runtime alias points to, unless that alias is already scheduled for deletion. For more information, see [Deletion rules and order](#cmr-delete-rules).

**Waiting period** – When you call `DeleteRuntime`, `DeleteRuntimeVersion`, or `DeleteRuntimeAlias`, Lambda doesn't delete the resource immediately. Instead, Lambda schedules the resource for deletion after a waiting period of 7–30 days. If you don't specify a waiting period, Lambda uses 30 days. The resource is now scheduled for deletion (the `PENDING_DELETION` state). While a resource is scheduled for deletion, the following applies:
+ Functions can't use the resource. For functions, the resource behaves as if it were permanently deleted.
+ You can't modify the resource.
+ You can restore the resource. When you restore it, functions that use it recover automatically, and you don't need to update them.

When the waiting period ends, Lambda permanently deletes the resource, and you can't recover it. You can't delete a resource immediately. You can't change the waiting period of a resource that's scheduled for deletion. If you delete a resource that's already scheduled for deletion, the request succeeds, but it doesn't change the resource's waiting period. To reschedule the deletion, restore the resource, and then delete it again. For more information, see [Resources scheduled for deletion](#cmr-delete-pending).

These safeguards don't stop you from deleting your resources. You can always delete a runtime that you own, no matter how many functions or accounts use it.

## Deletion rules and order
<a name="cmr-delete-rules"></a>

Lambda applies the following rules when you delete runtime resources:
+ **You can't delete a runtime that has runtime versions or runtime aliases that aren't scheduled for deletion.** Delete the runtime's aliases and versions first. After all of its versions and aliases are scheduled for deletion, you can delete the runtime. You don't need to wait until Lambda permanently deletes them.
+ **You can't delete a runtime version that a runtime alias points to, unless that alias is already scheduled for deletion.** An alias that isn't scheduled for deletion must always point to a valid version. Update the alias to point to a different version, or delete the alias first.

If a delete request breaks one of these rules, Lambda rejects the request. You can't override these rules. There's no force option.

Lambda doesn't apply any rules based on the functions that use a runtime, runtime version, or runtime alias. Functions in other accounts can't prevent you from deleting a runtime that you own.

To delete a runtime and everything in it, delete resources in the following order:

1. Runtime aliases

1. Runtime versions

1. The runtime

For instructions, see [Deleting a runtime](#cmr-delete-runtime-howto).

## Resources scheduled for deletion
<a name="cmr-delete-pending"></a>

Runtimes, runtime versions, and runtime aliases each have a `State` field. When you delete one of these resources, Lambda sets its `State` to `PENDING_DELETION`. The `PendingDeletionAt` field shows when Lambda permanently deletes the resource. This field appears only while the resource is scheduled for deletion.

While a resource is scheduled for deletion, the following rules apply:
+ You can only get, list, and restore the resource. You can't modify it.
+ You can't create runtime versions or runtime aliases in a runtime that's scheduled for deletion.
+ You can't create or update a runtime alias to point to a runtime version that's scheduled for deletion.
+ The resource's name stays reserved until Lambda permanently deletes the resource. Until then, you can't create a runtime, runtime version, or runtime alias with the same name. After Lambda permanently deletes the resource, you can create a new one with the same name.
+ List operations include the resource in their results.
+ The resource still counts toward your quotas. For more information, see [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).
+ Runtime metrics still include the resource. Invokes that require a cold start fail, but the `RuntimeInvocations` and `RuntimeInvocationErrors` metrics still track them. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

If you try a blocked operation, Lambda rejects the request with an error.

### Waiting period
<a name="cmr-delete-waiting-period"></a>

When you delete a resource, you can specify a waiting period from 7 to 30 days. If you don't specify one, Lambda uses 30 days. If you specify a value outside this range, the request fails. You can't delete a resource immediately.

You can't change the waiting period of a resource that's scheduled for deletion. If you delete a resource that's already scheduled for deletion, the request succeeds, but it doesn't change the resource's waiting period. To reschedule the deletion, restore the resource, and then delete it again with a new waiting period. For instructions, see [Rescheduling a deletion](#cmr-delete-change-period).

Lambda keeps the waiting periods of related resources consistent:
+ A runtime's waiting period can't end before the waiting period of any of its runtime versions or runtime aliases.
+ A runtime version's waiting period can't end before the waiting period of any runtime alias that references it.

When you delete a runtime or runtime version, Lambda might extend the waiting period that you specify. For a runtime, Lambda extends it to the longest waiting period among its versions and aliases. For a version, Lambda extends it to the longest waiting period among the aliases that reference it. Check the `PendingDeletionAt` field to see the actual date.

### Permanent deletion
<a name="cmr-delete-permanent"></a>

When the waiting period ends, Lambda permanently deletes the resource. An alias, its version, and its runtime might be due for deletion on the same day. In this case, Lambda deletes the alias first, then the version, and then the runtime.

**Warning**  
After the waiting period ends, Lambda permanently deletes the resource. You can't recover a permanently deleted runtime, runtime version, or runtime alias.

After Lambda permanently deletes a runtime, runtime version, or runtime alias, you can create a new one with the same name. A re-created runtime version has the same version ARN as the deleted version.

**Important**  
If you re-create a runtime version with the same name, functions that are pinned to that version's ARN start using the new version at their next cold start. These are functions in **Manual** mode. Before you reuse a version name, review the functions that are pinned to the version.

## How deletion affects functions
<a name="cmr-delete-function-impact"></a>

Functions can't use a runtime resource that's scheduled for deletion. For functions, a resource that's scheduled for deletion behaves exactly like a resource that's permanently deleted.

The effect on a function depends on the function's runtime update mode. For more information about runtime update modes, see [Managing Lambda runtime updates](runtime-management-configure-settings.md). The following table shows how scheduling a runtime alias or runtime version for deletion affects invokes.


**Effect of deletion on function invokes, by runtime update mode**  

| Runtime update mode | If the function's runtime alias is scheduled for deletion | If the runtime version that the function uses is scheduled for deletion | 
| --- | --- | --- | 
| Auto | Invokes that require a cold start fail. Existing execution environments continue to handle invokes. | Not applicable. You can't delete a version that an alias references. If you delete the alias first, invokes fail as described for the alias. | 
| Function update | No effect on invokes. Lambda doesn't resolve the alias when it invokes the function. | Invokes that require a cold start fail. Existing execution environments continue to handle invokes. | 
| Manual | No effect on invokes. Lambda doesn't resolve the alias when it invokes the function. | Invokes that require a cold start fail. Existing execution environments continue to handle invokes. | 

Deletion also affects function create and update operations:
+ In all runtime update modes, function create and update operations fail if the function's runtime alias is scheduled for deletion or deleted. Any update to the function's configuration fails, even an update that doesn't change its runtime settings.
+ You can't use the **Manual** runtime update mode to pin a function to a runtime version that's scheduled for deletion or deleted. If a function in **Manual** mode is already pinned to a runtime version that's scheduled for deletion, updates to the function's code and configuration fail, even an update that doesn't change its runtime settings.

A runtime version that no alias references can still be in use. Functions in **Function update** mode keep the version that the alias pointed to when you last updated them. Functions in **Manual** mode stay pinned to a specific version. If you delete that version, invocations of these functions that require a cold start fail.

Affected functions enter the `Inactive` state, with the state reason code `InvalidRuntime`. Lambda can't create new execution environments for these functions, so only invocations that require a cold start fail. For more information, see [Runtime lifecycle and function states](cmr-using.md#cmr-using-lifecycle). When you restore the runtime version or runtime alias, functions return to the `Active` state automatically. You don't need to update or redeploy them.

## Restoring deleted resources
<a name="cmr-delete-restore-concepts"></a>

During the waiting period, you can restore a runtime, runtime version, or runtime alias with the `RestoreRuntime` operation. To restore a version or an alias, specify its name in addition to the runtime name. Restoring a resource returns its `State` to `ACTIVE` and removes its `PendingDeletionAt`.

Each restore request restores only the resource that you specify. The following rules apply when you restore resources:
+ Restoring a runtime version doesn't restore its runtime.
+ Restoring a runtime alias doesn't restore its version or its runtime.
+ Restoring a runtime doesn't restore its runtime versions or runtime aliases.

Lambda rejects a restore request if the resource's parent is scheduled for deletion:
+ You can't restore a runtime version or runtime alias while its runtime is scheduled for deletion.
+ You can't restore a runtime alias while the runtime version that it points to is scheduled for deletion.

Restore the parent resource first. If a runtime, a version, and an alias that points to that version are all scheduled for deletion, restore them one at a time in the following order:

1. The runtime

1. The runtime version

1. The runtime alias

For example, if you delete a runtime and all of its resources by accident, restore the runtime first. Next, restore the runtime versions that functions use, including the versions that their aliases reference. Then restore the aliases that functions use.

A restore request fails in the following cases:
+ The runtime, version, or alias doesn't exist, or Lambda has already permanently deleted it.
+ The resource isn't scheduled for deletion, or Lambda has already started to permanently delete it.
+ The request specifies both a version and an alias.

For instructions, see [Restoring a runtime, runtime version, or runtime alias](#cmr-delete-restore).

## Container images and charges
<a name="cmr-delete-ecr"></a>

Deleting a runtime version doesn't delete its container image from Amazon ECR. Amazon ECR continues to charge for image storage until you delete the image.

If you delete the image that a runtime version uses, functions that use the runtime version become `Inactive`. This can take up to 24 hours. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. Deleting the repository or removing Lambda's access to the image has the same effect. For more information, see [How deletion affects functions](#cmr-delete-function-impact).

Keep the image while the runtime version is scheduled for deletion. A restored version needs the same image, with an identical digest. After Lambda permanently deletes the version, you can delete the image from Amazon ECR to stop storage charges. For more information, see [Deleting an image in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html) in the *Amazon Elastic Container Registry User Guide*.

## Before you delete
<a name="cmr-delete-before"></a>

Lambda doesn't block deletion of runtime resources that functions are using. Before you delete a runtime resource, we recommend that you complete the following tasks:
+ **Check usage** – Check the `RuntimeInvocations` metric for the runtime, runtime version, or runtime alias. If the metric shows recent invokes, functions still use the resource. The metric includes invokes from all accounts that use the runtime in the Region. Choose a time range long enough to include functions that run infrequently. For instructions, see [Checking usage before you delete](#cmr-delete-check-usage). For more information about runtime metrics, see [Monitoring customer-managed runtimes](cmr-monitoring.md).
+ **Notify consumers** – Lambda doesn't notify runtime consumers when you delete a runtime resource. Tell your consumers in advance, and give them time to move their functions to another runtime or alias. To communicate a planned retirement, set lifecycle dates on the runtime or alias. For more information, see [Runtime lifecycle](cmr-lifecycle.md).
+ **Choose a waiting period** – Choose how long you want to be able to restore the resource, from 7 to 30 days. A longer period gives you more time to find and fix problems. For more information, see [Waiting period](#cmr-delete-waiting-period).
+ **Check permissions** – Make sure that you have the permissions for the delete and restore operations that you plan to use.

To delete and restore runtime resources, you need the following IAM permissions:
+ `lambda:DeleteRuntime`, `lambda:DeleteRuntimeVersion`, and `lambda:DeleteRuntimeAlias`
+ `lambda:RestoreRuntime`, to restore a runtime, runtime version, or runtime alias
+ `lambda:GetRuntime`, `lambda:GetRuntimeVersion`, `lambda:GetRuntimeAlias`, `lambda:ListRuntimeVersions`, and `lambda:ListRuntimeAliases`, to view resources and their state

For more information about permissions, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Checking usage before you delete
<a name="cmr-delete-check-usage"></a>

To find out whether functions still use a runtime alias or runtime version, check its `RuntimeInvocations` metric in Amazon CloudWatch.

In each AWS Region, runtime metrics combine usage from all accounts and organizations that use the runtime. As the runtime publisher, you can use these metrics to check usage by runtime consumers in other accounts. The metrics don't show function names. Runtime metrics help you understand the impact of a potential delete, such as how many invokes might fail. For more information, see [Check usage before you delete or deprecate](cmr-monitoring.md#cmr-monitoring-uses-usage).

To check usage in the CloudWatch console, see [View runtime metrics](cmr-monitoring.md#cmr-monitoring-view).

To get the daily sum of invokes for the `dev` alias over the last 14 days, run the following **get-metric-statistics** command.

```bash
aws cloudwatch get-metric-statistics \
  --region us-east-1 \
  --namespace AWS/Lambda \
  --metric-name RuntimeInvocations \
  --dimensions Name=Runtime,Value={{companyphp8}} Name=RuntimeAlias,Value={{dev}} \
  --start-time {{2026-09-21T00:00:00Z}} \
  --end-time {{2026-10-05T00:00:00Z}} \
  --period 86400 \
  --statistics Sum
```

If the output contains no data points, or every `Sum` value is `0`, no functions invoked through this alias during the time range. To check a runtime version, replace the `RuntimeAlias` dimension with the `RuntimeVersion` dimension. Keep the `Runtime` dimension.

## Deleting a runtime alias
<a name="cmr-delete-alias"></a>

After you delete a runtime alias, it no longer prevents you from deleting the runtime version that it points to. If no other alias that isn't scheduled for deletion points to that version, you can then delete the version.

------
#### [ Console ]

**To delete a runtime alias**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Aliases** tab.

1. Select the runtime alias that you want to delete.

1. Choose **Alias actions**, and then choose **Delete alias**.

1. Review the scheduled deletion waiting period. This is the number of days during which you can recover the alias.

1. Choose **Delete alias**.

The runtime alias enters the `PENDING_DELETION` state for the waiting period.

------
#### [ AWS CLI ]

**To delete a runtime alias**

1. To delete the alias with a 7-day waiting period, run the following **delete-runtime-alias** command.

   ```bash
   aws lambda-core delete-runtime-alias \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{dev}} \
     --recovery-window-in-days {{7}}
   ```

   If the request succeeds, Lambda returns an HTTP `202 Accepted` response with an empty body, and the command produces no output.

1. To confirm that the alias is scheduled for deletion, run the following **get-runtime-alias** command.

   ```bash
   aws lambda-core get-runtime-alias \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{dev}}
   ```

   You should see output similar to the following:

   ```json
   {
       "Name": "dev",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/dev",
       "RuntimeVersion": "v8.3.2",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2",
       "State": "PENDING_DELETION",
       "PendingDeletionAt": "2026-10-14T14:30:00Z",
       "Created": "2026-06-02T09:15:00Z",
       "LastModified": "2026-10-07T14:30:00Z"
   }
   ```

------

## Deleting a runtime version
<a name="cmr-delete-version"></a>

You can delete a runtime version only if no runtime alias that isn't scheduled for deletion points to it. Before you delete the version, check whether functions in **Function update** or **Manual** mode still use it. For more information, see [How deletion affects functions](#cmr-delete-function-impact).

------
#### [ Console ]

**To delete a runtime version**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Versions** tab.

1. Select the check box next to the runtime version that you want to delete.

1. Choose **Version actions**, and then choose **Delete version**.

1. Review the scheduled deletion waiting period. This is the number of days during which you can recover the version.

1. In the confirmation field, enter **Confirm**.

1. Choose **Delete version**.

The runtime version enters the `PENDING_DELETION` state for the waiting period.

------
#### [ AWS CLI ]

**To delete a runtime version**

1. To find the aliases that reference each version, run the following **list-runtime-aliases** command.

   ```bash
   aws lambda-core list-runtime-aliases \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --query 'Items[].[Name,RuntimeVersion,State]' \
     --output table
   ```

   If an active alias references the version, update the alias to point to another version, or delete the alias. For more information, see [Runtime aliases](cmr-aliases.md).

1. To delete the version with a 30-day waiting period, run the following **delete-runtime-version** command.

   ```bash
   aws lambda-core delete-runtime-version \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{v8.3.1}} \
     --recovery-window-in-days {{30}}
   ```

   If the request succeeds, the command produces no output.

1. To confirm that the version is scheduled for deletion, run the following **get-runtime-version** command.

   ```bash
   aws lambda-core get-runtime-version \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{v8.3.1}} \
     --query '{Name:Name,State:State,PendingDeletionAt:PendingDeletionAt}'
   ```

   You should see output similar to the following:

   ```json
   {
       "Name": "v8.3.1",
       "State": "PENDING_DELETION",
       "PendingDeletionAt": "2026-11-06T14:30:00Z"
   }
   ```

If an alias that isn't scheduled for deletion still points to the version, Lambda rejects the request and doesn't delete the version.

------

## Deleting a runtime
<a name="cmr-delete-runtime-howto"></a>

To delete a runtime, you first delete all of its runtime aliases and runtime versions.

------
#### [ Console ]

For instructions on deleting runtime aliases and runtime versions in the console, see [Deleting a runtime alias](#cmr-delete-alias) and [Deleting a runtime version](#cmr-delete-version).

**To delete a runtime**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Select the runtime that you want to delete.

1. Choose **Runtime actions**, and then choose **Delete runtime**.

1. Review the scheduled deletion waiting period. This is the number of days during which you can recover the runtime.

1. Choose **Delete runtime**.

The runtime enters the `PENDING_DELETION` state for the waiting period.

------
#### [ AWS CLI ]

The following example deletes the `companyphp8` runtime, its `dev`, `test`, and `prod` aliases, and its `v8.3.1` and `v8.3.2` versions. Each resource uses a 30-day waiting period.

**To delete a runtime and all of its resources**

1. To list the runtime's aliases, run the following **list-runtime-aliases** command.

   ```bash
   aws lambda-core list-runtime-aliases \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --query 'Items[].Name' \
     --output text
   ```

1. To delete each alias, run the **delete-runtime-alias** command for each alias name.

   ```bash
   for alias in {{dev test prod}}; do
     aws lambda-core delete-runtime-alias \
       --region us-east-1 \
       --runtime-name {{companyphp8}} \
       --name "$alias" \
       --recovery-window-in-days {{30}}
   done
   ```

1. To list the runtime's versions, run the following **list-runtime-versions** command.

   ```bash
   aws lambda-core list-runtime-versions \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --query 'Items[].Name' \
     --output text
   ```

1. To delete each version, run the **delete-runtime-version** command for each version name.

   ```bash
   for version in {{v8.3.1 v8.3.2}}; do
     aws lambda-core delete-runtime-version \
       --region us-east-1 \
       --runtime-name {{companyphp8}} \
       --name "$version" \
       --recovery-window-in-days {{30}}
   done
   ```

1. To delete the runtime, run the following **delete-runtime** command. You can run this command as soon as all of the runtime's aliases and versions are scheduled for deletion.

   ```bash
   aws lambda-core delete-runtime \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --recovery-window-in-days {{30}}
   ```

   If the request succeeds, the command produces no output.

1. To confirm that the runtime is scheduled for deletion, run the following **get-runtime** command.

   ```bash
   aws lambda-core get-runtime \
     --region us-east-1 \
     --runtime-name {{companyphp8}}
   ```

   You should see output similar to the following:

   ```json
   {
       "Name": "companyphp8",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
       "Description": "PHP 8 runtime for Example Corp functions",
       "State": "PENDING_DELETION",
       "PendingDeletionAt": "2026-11-06T14:30:00Z",
       "Created": "2026-05-12T10:00:00Z",
       "LastModified": "2026-10-07T14:30:00Z"
   }
   ```

If the runtime still has aliases or versions that aren't scheduled for deletion, Lambda rejects the request and doesn't delete the runtime.

If any version or alias has a later `PendingDeletionAt` than the waiting period that you specify for the runtime, Lambda extends the runtime's waiting period to match. For more information, see [Waiting period](#cmr-delete-waiting-period).

------

## Rescheduling a deletion
<a name="cmr-delete-change-period"></a>

You can't change the waiting period of a resource that's scheduled for deletion. If you delete a resource that's already scheduled for deletion, the request succeeds, but it doesn't change the resource's waiting period. To reschedule the deletion, restore the resource, and then delete it again with a new waiting period of 7–30 days. The new waiting period starts when you delete the resource again.

If the parent runtime or version is also scheduled for deletion, restore the parent first. For more information, see [Restoring deleted resources](#cmr-delete-restore-concepts).

In the console, you can't change the waiting period of a resource that's scheduled for deletion. To reschedule in the console, recover the resource, and then delete it again. For instructions, see [Restoring a runtime, runtime version, or runtime alias](#cmr-delete-restore).

**To reschedule the deletion of a runtime alias (AWS CLI)**

1. To restore the `dev` alias, run the following **restore-runtime** command.

   ```bash
   aws lambda-core restore-runtime \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --runtime-alias {{dev}}
   ```

1. To delete the alias again with a new 30-day waiting period, run the following **delete-runtime-alias** command.

   ```bash
   aws lambda-core delete-runtime-alias \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{dev}} \
     --recovery-window-in-days {{30}}
   ```

1. To confirm the new date, run the following **get-runtime-alias** command.

   ```bash
   aws lambda-core get-runtime-alias \
     --region us-east-1 \
     --runtime-name {{companyphp8}} \
     --name {{dev}} \
     --query '{State:State,PendingDeletionAt:PendingDeletionAt}'
   ```

   You should see output similar to the following:

   ```json
   {
       "State": "PENDING_DELETION",
       "PendingDeletionAt": "2026-11-06T14:30:00Z"
   }
   ```

A runtime's waiting period can't end before those of its versions and aliases, and a version's can't end before those of the aliases that reference it. For more information, see [Waiting period](#cmr-delete-waiting-period).

## Viewing resources that are scheduled for deletion
<a name="cmr-delete-view"></a>

Get and list operations return resources that are scheduled for deletion. Check the `State` and `PendingDeletionAt` fields to see which resources are scheduled for deletion and when Lambda permanently deletes them.

In the Lambda console, the resource lists show the scheduled deletion for each resource. To see runtimes, use the list on the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes). To see runtime versions and runtime aliases, choose a runtime, and then choose the **Versions** tab or the **Aliases** tab.

To view the state of a runtime with the AWS CLI, run the following **get-runtime** command.

```bash
aws lambda-core get-runtime \
  --region us-east-1 \
  --runtime-name {{companyphp8}} \
  --query '[State,PendingDeletionAt]'
```

To view the state of every version or alias in a runtime, run the following **list-runtime-versions** and **list-runtime-aliases** commands.

```bash
aws lambda-core list-runtime-versions \
  --region us-east-1 \
  --runtime-name {{companyphp8}} \
  --query 'Items[].[Name,State,PendingDeletionAt]' \
  --output table

aws lambda-core list-runtime-aliases \
  --region us-east-1 \
  --runtime-name {{companyphp8}} \
  --query 'Items[].[Name,RuntimeVersion,State,PendingDeletionAt]' \
  --output table
```

To view a single version or alias, use the **get-runtime-version** or **get-runtime-alias** command.

## Restoring a runtime, runtime version, or runtime alias
<a name="cmr-delete-restore"></a>

You can restore a resource only while it's scheduled for deletion. Restoring a resource doesn't restore its parent resources. Lambda rejects a request to restore a runtime version or runtime alias while its runtime is scheduled for deletion. Lambda also rejects a request to restore a runtime alias while its runtime version is scheduled for deletion. If a runtime, a runtime version, and a runtime alias are all scheduled for deletion, restore the runtime first, then the version, and then the alias. For more information, see [Restoring deleted resources](#cmr-delete-restore-concepts).

------
#### [ Console ]

**To restore a runtime, runtime version, or runtime alias**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Go to the runtime, runtime version, or runtime alias in the `PENDING_DELETION` state, and select it.

1. From the actions menu (**Runtime actions**, **Version actions**, or **Alias actions**), choose **Recover from deletion**.

1. In the confirmation dialog box, choose **Recover from deletion**.

------
#### [ AWS CLI ]

To restore a runtime, runtime version, or runtime alias, use the **restore-runtime** command. To restore a version or alias, add the `--runtime-version` or `--runtime-alias` option. Each command restores only the resource that you specify. If the runtime, version, and alias are all scheduled for deletion, run the following commands in order.

To restore the runtime, run the following **restore-runtime** command. This command doesn't restore the runtime's versions or aliases.

```bash
aws lambda-core restore-runtime \
  --region us-east-1 \
  --runtime-name {{companyphp8}}
```

To restore a runtime version, run the following **restore-runtime** command. This command doesn't restore the runtime or any aliases.

```bash
aws lambda-core restore-runtime \
  --region us-east-1 \
  --runtime-name {{companyphp8}} \
  --runtime-version {{v8.3.1}}
```

To restore the `prod` alias, run the following **restore-runtime** command. This command doesn't restore the alias's version or the runtime.

```bash
aws lambda-core restore-runtime \
  --region us-east-1 \
  --runtime-name {{companyphp8}} \
  --runtime-alias {{prod}}
```

You should see output similar to the following:

```json
{
    "RuntimeName": "companyphp8",
    "RuntimeAlias": "prod",
    "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod",
    "State": "ACTIVE",
    "LastModified": "2026-10-08T09:00:00Z"
}
```

You can specify a version or an alias, but not both.

------

## Recovering from an accidental deletion
<a name="cmr-delete-recover"></a>

If you delete a runtime resource by accident, restore it as soon as possible. For functions that depend on the resource, invocations that require a cold start fail. When you restore the resource, functions recover automatically. Each restore request restores only the resource that you specify. You can't restore a resource while its parent is scheduled for deletion, so restore the runtime first, then its runtime versions, and then its runtime aliases.

**To recover from an accidental deletion**

1. Identify the resources that are scheduled for deletion. For instructions, see [Viewing resources that are scheduled for deletion](#cmr-delete-view).

1. If the runtime is scheduled for deletion, restore the runtime.

1. Restore each runtime version that functions use, if it's scheduled for deletion. Include each version that an alias in use references. Also include the versions that functions in **Function update** or **Manual** mode use.

1. Restore each runtime alias that functions use, if it's scheduled for deletion.

1. Restore any other runtime versions and runtime aliases that you want to keep. Restore each version before the aliases that reference it.

1. Confirm that each restored resource has a `State` of `ACTIVE`.

1. Check the `RuntimeInvocations` and `RuntimeInvocationErrors` metrics to confirm that functions recover. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

For the commands to use in each step, see [Restoring a runtime, runtime version, or runtime alias](#cmr-delete-restore). You don't need to update functions after you restore resources. Functions that entered the `Inactive` state return to the `Active` state automatically.

If Lambda has already permanently deleted the resource, you can't restore it. Instead, you can create a new resource with the same name. To get affected functions running again, you can create a new runtime version from the same container image. You can then create a runtime alias with the original alias name that points to the new version. For more information, see [Permanent deletion](#cmr-delete-permanent), [Runtime versions](cmr-versions.md), and [Runtime aliases](cmr-aliases.md).

Functions that reference the original alias name use the new alias. You don't need to update them.