# Safety Levers for AWS FIS

Safety levers are used to stop all running experiments and prevent new experiments from starting. You may want to use the safety lever to prevent FIS experiments during certain time periods or in response to application health alarms. Every AWS account has a safety lever per AWS Region.

For in-progress experiments that are stopped by the safety lever, you only pay for the action duration that ran before the experiment was stopped. Experiments that are prevented from starting will not incur any costs. The following sections provide information on how to get started using safety levers.

###### Topics

- [Concepts for safety levers](#concepts-for-safety-levers "#concepts-for-safety-levers")
- [Working with safety levers](#working-with-safety-levers "#working-with-safety-levers")

## Concepts for safety levers

A safety lever can be engaged or disengaged.

- If disengaged, FIS experiments are allowed. By default, safety levers are disengaged.
- If engaged, in-progress experiments are stopped and no new experiments are allowed to start.

An experiment affected by a safety lever will end in one of the following statuses:

- **Stopped**, if the experiment was running when the safety lever was engaged.
- **Cancelled**, if the experiment was started when the safety lever was already engaged.

You cannot resume or rerun an experiment that has been stopped or cancelled. However, you can start a new experiment using the same experiment template once the safety lever is disengaged.

### Saftey lever resource

Safety lever is a resource defined by the Amazon Resource Name (ARN). Safety levers include the following parameters:

- **Status**, which is either engaged or disengaged.
- **Reason**, which is a string input by the user to log why the saftey lever status was changed.

## Working with safety levers

This section will detail how to view, engage, and disengage safety levers using the AWS FIS console or the command line.

### Viewing a safety lever

You can view the state of your safety lever for your account and region by following the steps below.

###### To view a safety lever using the console

1. [Open the AWS FIS console](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/")
2. In the navigation pane, choose **Experiments**.
3. If the safety lever is engaged, you will see an alert banner across the top of the page. If there is no alert banner, the safety lever is disengaged.

###### To view a safety lever using the CLI

- Use the following command:

```
aws fis get-safety-lever --id "default"
```

A safety lever can be in one of the following states:

- **Disengaged** ‐ The safety lever is not impacting any experiments. Experiments can run freely. Safety levers are disengaged by default.
- **Engaging** ‐ The safety lever is changing from disngaged to engaged. There may still be experiments that have not been stopped yet. The safety lever cannot be changed while in this state.
- **Engaged** ‐ The safety lever is active and no experiments are running. Any new experiments that attempt to start while the safety lever is engaged will be cancelled.

### Engaging a safety lever

###### To engage a safety lever using the console

1. [Open the AWS FIS console](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/")
2. In the navigation pane, choose **Experiments**.
3. Choose the **Stop all experiments** button.
4. Enter the reason for engaging the safety lever.
5. Choose **Confirm**.

###### To enage a safety lever using the CLI

- Use the following command. Fill in the reason field with your own response.

```
aws fis  update-safety-lever-state --id "default" --state "status=engaged,reason=xxxxx"
```

### Disengaging a safety lever

###### To disengage a safety lever using the console

1. [Open the AWS FIS console](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/")
2. In the navigation pane, choose **Experiments**.
3. Choose the **Disengage safety lever** button.
4. Enter the reason for disengaging the safety lever.
5. Choose **Confirm**.

###### To disenage a safety lever using the CLI

- Use the following command:

```
aws fis  update-safety-lever-state --id "default" --state "status=disengaged,reason=recovered"
```
