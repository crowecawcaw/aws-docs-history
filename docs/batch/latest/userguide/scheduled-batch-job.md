# Tutorial: Create a scheduled AWS Batch job

The following procedure covers how to create a scheduled AWS Batch job and the required EventBridge
IAM role.

###### To create a scheduled AWS Batch job with EventBridge

###### Note

This procedure works for all AWS Batch on Amazon ECS, Amazon EKS, and AWS Fargate jobs.

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Rules**.
4. Choose **Create rule**.
5. For **Name**, specify a unique name for your compute environment. The
   name can contain up to 64 characters. It can contain uppercase and lowercase letters,
   numbers, hyphens (-), and underscores (\_).

###### Note

A rule can't have the same name as another rule in the same Region and on the same
event bus. 6. (Optional) For **Description**, enter a description for the
rule. 7. For **Event bus**, choose the event bus that you want to associate
with this rule. If you want this rule to match events that come from your account, select
**default**. When an AWS service in your account emits an event, it
always goes to your account's default event bus. 8. (Optional) Turn off the rule on the selected bus if you don't want to run the rule
immediately. 9. For **Rule type**, choose **Schedule**. 10. Choose **Continue to create rule** or
**Next**. 11. For **Schedule pattern**, do one of the following:

    * Choose **A fine-grained schedule that runs at a specific time, such as
     8:00 a.m. PST on the first Monday of every month** and then enter a cron
     expression. For more information, see [Cron Expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-cron-expressions "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-cron-expressions") in the *Amazon EventBridge User Guide*.
    * Choose **A schedule that runs at a regular rate, such as every 10
     minutes.** and then enter a rate expression.

12. Choose **Next**.
13. For **Target types**, choose
    **AWS service**.
14. For **Select a target**, choose **Batch job queue**.
    Then, configure the following:
    - **Job queue:** Enter the Amazon Resource Name (ARN) of the job queue to schedule
      your job in.
    - **Job definition:** Enter the name and revision or full ARN of
      the job definition to use for your job.
    - **Job name:** Enter a name for your job.
    - **Array size:** (Optional) Enter an array size for your job to
      run more than one copy. For more information, see [Array jobs](array_jobs.md "array_jobs.md").
    - **Job attempts:** (Optional) Enter the number of times to retry
      your job if it fails. For more information, see [Automated job retries](job_retries.md "job_retries.md").

15. For **Batch job queue** target types, EventBridge needs permission to send
    events to the target. EventBridge can create the IAM role needed for your rule to run. Do one
    of the following:
    - To create an IAM role automatically, choose **Create a new role for this
      specific resource**.
    - To use an IAM role that you've already created, choose **Use existing
      role**.

16. (Optional) Expand **Additional settings**.
    1.  For **Configure target input**, choose how the text from an event
        is processed before it's passed to the target.
    2.  For **Maximum age of event**, specify the time interval for how
        long unprocessed events are kept.
    3.  For **Retry attempts**, enter the number of times that an event
        is retried.
    4.  For **Dead-letter queue,** choose an option for how unprocessed
        events are handled. If necessary, specify the Amazon SQS queue to use as the dead-letter
        queue.

17. (Optional) Choose **Add another target** to add another target for
    this rule.
18. Choose **Next**.
19. (Optional) For **Tags**, choose **Add new tag** to
    add a resource label for the rule. For more information, see [Amazon
    EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md").
20. Choose **Next**.
21. For **Review and create**, review the configuration
    steps. If you need to make changes, choose **Edit**. When
    you're finished, choose **Create rule**.
    For more information about creating rules, see [Creating an Amazon EventBridge rule
    that runs on a schedule](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md") in the _Amazon EventBridge User Guide_.
