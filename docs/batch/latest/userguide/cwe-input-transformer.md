

# Tutorial: Pass event information to an AWS Batch target on a schedule using the EventBridge input transformer
<a name="cwe-input-transformer"></a>

You can use the EventBridge input transformer to pass event information to AWS Batch in a job submission. This can be especially valuable if you invoke jobs as a result of other AWS event information. One example is an object upload to an Amazon S3 bucket. You can also use a job definition with parameter substitution values in the container's command. The EventBridge input transformer can provide the parameter values based on the event data. 

Then, afterwards, you create an AWS Batch event target that parses information from the event that starts it and transforms it into a `parameters` object. When the job runs, the parameters from the trigger event are passed to the command of the job container.

**Note**  
In this scenario, all of the AWS resources (such as Amazon S3 buckets, EventBridge rules, and CloudTrail logs) must be in the same Region.

**To create an AWS Batch target that uses the input transformer**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. From the navigation bar, select the AWS Region to use.

1. In the navigation pane, choose **Rules**.

1. Choose **Create rule**.

1. For **Name**, specify a unique name for your compute environment. The name can contain up to 64 characters. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).
**Note**  
A rule can't have the same name as another rule in the same AWS Region and on the same event bus.

1. (Optional) For **Description**, enter a description for the rule.

1. For **Event bus**, choose the event bus that you want to associate with this rule. If you want this rule to match events that come from your account, select **default**. When an AWS service in your account emits an event, it always goes to your account's default event bus.

1. (Optional) Turn off the rule on the selected bus if you don't want to run the rule immediately.

1. For **Rule type**, choose **Schedule**.

1. Choose **Continue to create rule** or **Next**.

1. For **Schedule pattern**, do one of the following:
   + Choose **A fine-grained schedule that runs at a specific time, such as 8:00 a.m. PST on the first Monday of every month** and then enter a cron expression. For more information, see [Cron Expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-cron-expressions) in the *Amazon EventBridge User Guide*.
   + Choose **A schedule that runs at a regular rate, such as every 10 minutes.** and then enter a rate expression.

1. Choose **Next**.

1. For **Target types**, choose **AWS service**.

1. For **Select a target**, choose **Batch job queue**. Then, configure the following:
   + **Job queue:** Enter the Amazon Resource Name (ARN) of the job queue to schedule your job in.
   + **Job definition:** Enter the name and revision or full ARN of the job definition to use for your job.
   + **Job name:** Enter a name for your job.
   + **Array size:** (Optional) Enter an array size for your job to run more than one copy. For more information, see [Array jobs](array_jobs.md).
   + **Job attempts:** (Optional) Enter the number of times to retry your job if it fails. For more information, see [Automated job retries](job_retries.md).

1. For **Batch job queue** target types, EventBridge needs permission to send events to the target. EventBridge can create the IAM role needed for your rule to run. Do one of the following:
   + To create an IAM role automatically, choose **Create a new role for this specific resource**.
   + To use an IAM role that you've already created, choose **Use existing role**.

1. (Optional) Expand **Additional settings**.

1. In the **Additional settings** section, for **Configure target input**, choose **Input Transformer**.

1. Choose **Configure input transformer**.

1. (Optional) For **Sample event**:

   1. For **Sample event type**, choose **AWS events**.

   1. For **Sample events**, choose **Batch Job State Change**.

1. In the **Target input transformer** section, for **Input path**, specify the values to parse from the triggering event. For example, to parse **Batch Job State Change** event, use the following JSON format.

   ```
   {
       "instance": "$.detail.jobId",
       "state": "$.detail.status"
   }
   ```

1. For **Template**, enter the following.

   ```
   {
       "instance": <jobId> ,
       "status": <status>
   }
   ```

1. Choose **Confirm**.

1. For **Maximum age of event**, specify the time interval for how long unprocessed events are kept.

1. For **Retry attempts**, enter the number of times that an event is retried.

1. For **Dead-letter queue,** choose an option for how unprocessed events are handled. If necessary, specify the Amazon SQS queue to use as the dead-letter queue.

1. (Optional) Choose **Add another target** to add an additional target.

1. Choose **Next**.

1. (Optional) For **Tags**, choose **Add new tag** to add a resource label. For more information, see [Amazon EventBridge tags](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tagging.html) in the *Amazon EventBridge User Guide*.

1. Choose **Next**.

1. For **Review and create**, review the configuration steps. If you need to make changes, choose **Edit**. After you're finished, choose **Create rule**.