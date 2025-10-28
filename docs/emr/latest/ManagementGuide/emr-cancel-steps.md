# Cancel steps when you submit work to an Amazon EMR cluster

You can cancel pending and running steps from the AWS Management Console, the AWS CLI, or the Amazon EMR, when you submit work to your cluster.
API.

Console

###### To cancel steps with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**, and then select the cluster
   that you want to update.
3. On the **Steps** tab on the cluster details page,
   select the check box next to the step you wants to cancel. Choose
   the **Actions** dropdown menu and then select
   **Cancel steps**.
4. In the **Cancel the step** dialog, choose to
   either cancel the step and wait for it to exit, or cancel the step
   and force it to exit. Then choose
   **Confirm**.
5. The status of the steps in the **Steps** table
   changes to `CANCELLED`.

CLI

###### To cancel with using the AWS CLI

- Use the `aws emr cancel-steps` command, specifying the
  cluster and steps to cancel. The following example demonstrates an
  AWS CLI command to cancel two steps.

```
aws emr cancel-steps --cluster-id `j-2QUAXXXXXXXXX` \
--step-ids `s-3M8DXXXXXXXXX s-3M8DXXXXXXXXX` \
--step-cancellation-option SEND_INTERRUPT
```

With Amazon EMR version 5.28.0, you can choose one of the two following
cancellation options for `StepCancellationOption` parameter when
canceling steps.

- `SEND_INTERRUPT`– This is the default option.
  When a step cancellation request is received, EMR sends a
  `SIGTERM` signal to the step. add a
  `SIGTERM` signal handler to your step logic to catch
  this signal and terminate descendant step processes or wait for them
  to complete.
- `TERMINATE_PROCESS` – When this option is
  selected, EMR sends a `SIGKILL` signal to the step and
  all its descendant processes which terminates them
  immediately.

###### Considerations for canceling steps

- Canceling a running or pending step removes that step from the active step
  count.
- Canceling a running step does not allow a pending step to start running,
  assuming no change to `stepConcurrencyLevel`.
- Canceling a running step does not trigger the step
  `ActionOnFailure`.
- For EMR 5.32.0 and later, `SEND_INTERRUPT StepCancellationOption`
  sends a `SIGTERM` signal to the step child process. You should watch
  for this signal and do a cleanup and shutdown gracefully. The
  `TERMINATE_PROCESS StepCancellationOption` sends a
  `SIGKILL` signal to the step child process and all of its
  descendant processes; however, asynchronous processes are not affected.
