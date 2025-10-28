# Tutorial: Schedule a recurring experiment

With AWS Fault Injection Service (AWS FIS), you can perform fault injection experiments on your AWS
workloads. These experiments run on templates that contain one or more actions to run on
specified targets. When you also use Amazon EventBridge, you can schedule your
experiments as a one-time task or recurring tasks.

Use this tutorial to create an EventBridge schedule that runs an AWS FIS experiment template
every 5 minutes.

###### Tasks

- [Prerequisites](#recurring-experiment-prerequisites "#recurring-experiment-prerequisites")
- [Step 1: Create an IAM role and policy](#recurring-experiment-step1 "#recurring-experiment-step1")
- [Step 2: Create an Amazon EventBridge Scheduler](#recurring-experiment-step2 "#recurring-experiment-step2")
- [Step 3: Verify your experiment](#recurring-experiment-step3 "#recurring-experiment-step3")
- [Step 4: Clean up](#recurring-experiment-step4 "#recurring-experiment-step4")

## Prerequisites

Before beginning this tutorial, must have an AWS FIS experiment template that you want
to run on a schedule. If you already have a working experiment template, make note of
the template ID and AWS Region. Otherwise, you can create a template by following
the instructions in [Tutorial: Test instance stop and start using AWS FIS](fis-tutorial-stop-instances.md "fis-tutorial-stop-instances.md"), and then return
to this tutorial.

## Step 1: Create an IAM role and policy

###### To create an IAM role and policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**, and then
   **Create Role**.
3. Choose **Custom trust policy**, and then insert the following
   snippet to allow Amazon EventBridge Scheduler to assume the role on your
   behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "scheduler.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Choose **Next**. 4. Under **Add permissions**, choose **Create
policy**. 5. Choose **JSON**, and then insert the following policy.
Replace the `your-experiment-template-id` value with
the template ID of your experiment from the Prerequisites steps.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": [
 "arn:aws:fis:*:*:experiment-template/`your-experiment-template-id`",
 "arn:aws:fis:*:*:experiment/*"
 ]
 }
 ]
}`

```

You can restrict the scheduler to only run AWS FIS experiment templates that have a
specific tag value. For example, the following policy grants the
`StartExperiment` permission for all AWS FIS experiments, but restricts the scheduler to only run experiment templates that are
tagged `Purpose=Schedule`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": "arn:aws:fis:*:*:experiment/*"
 },
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": "arn:aws:fis:*:*:experiment-template/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Schedule"
 }
 }
 }
 ]
}`

```

Choose **Next: Tags**. 6. Choose **Next: Review**. 7. Under **Review policy**, name your policy
`FIS_RecurringExperiment`, and then choose **Create
policy**. 8. Under **Add permissions**, add the new
`FIS_RecurringExperiment` policy to your role, and then choose
**Next**. 9. Under **Name, review, and create**, name the role
`FIS_RecurringExperiment_role`, and then choose **Create
role**.

## Step 2: Create an Amazon EventBridge Scheduler

###### To create an Amazon EventBridge Scheduler

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Schedules**.
3. Verify that you are in the same AWS Region as your AWS FIS experiment
   template.
4. Choose **Create schedule**, and fill in the following:
   - Under **Schedule name**, insert
     `FIS_recurring_experiment_tutorial`.
   - Under **Schedule pattern**, select **Recurring schedule**.
   - Under **Schedule type**, select **Rate-based schedule**.
   - Under **Rate expression**, choose **5 minutes**.
   - Under **Flexible time window**, select **Off**.
   - (Optional) Under **Timeframe**, select your time zone.
   - Choose **Next**.

5. Under **Select target**, choose **All
   APIs**, and then search for **AWS FIS**.
6. Choose **AWS FIS**, and then select
   **StartExperiment**.
7. Under **Input**, insert the following JSON payload. Replace
   the `your-experiment-template-id` value with the
   template ID of your experiment. The `ClientToken` is a unique
   identifier for the scheduler. In this tutorial, we are using a context keyword
   allowed by Amazon EventBridge Scheduler. For more information, see
   [Adding context attributes](../../../scheduler/latest/UserGuide/managing-schedule-context-attributes.md "../../../scheduler/latest/UserGuide/managing-schedule-context-attributes.md") in the _Amazon EventBridge User Guide_.

```
{
    "ClientToken": "<aws.scheduler.execution-id>",
    "ExperimentTemplateId": "`your-experiment-template-id`"
}
```

Choose **Next**. 8. (Optional) Under **Settings**, you can set the
**Retry policy**, **Dead-letter queue
(DLQ)**, and **Encryption** settings.
Alternatively, you can keep the default values. 9. Under **Permissions**, select **Use existing
role**, and then search for
`FIS_RecurringExperiment_role`. 10. Choose **Next**. 11. Under **Review and create schedule**, review your scheduler details, and then
choose **Create schedule**.

## Step 3: Verify your experiment

###### To verify that your AWS FIS experiment ran on schedule

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the left navigation pane, choose **Experiments**.
3. Five minutes after you create your schedule, you should see your experiment
   running.

## Step 4: Clean up

###### To disable your Amazon EventBridge Scheduler

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Schedules**.
3. Select your newly created scheduler, and then choose
   **Disable**.
