# AWS Batch jobs as EventBridge targets

Amazon EventBridge delivers a near real-time stream of system events that describe changes in
Amazon Web Services resources. Typically, AWS Batch on Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, and AWS Fargate jobs are
available as EventBridge targets. Using simple rules, you can match events and submit AWS Batch jobs in
response to them. For more information, see [What is EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the
_Amazon EventBridge User Guide_.

You can also use EventBridge to schedule automated actions that are invoked at certain times using
**cron** or rate expressions. For more information, see [Creating
an Amazon EventBridge rule that runs on a schedule](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md") in the _Amazon EventBridge User
Guide_.

For information about how to create a rule that runs when an event matches an event pattern,
see [Creating
Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User
Guide_.

Common use cases for AWS Batch jobs as an EventBridge target include the following use cases:

- A scheduled job occurs at regular time intervals. For example, a **cron**
  job occurs only during low-usage hours when Amazon EC2 Spot Instances are less expensive.
- An AWS Batch job runs in response to an API operation that's logged in CloudTrail. For example,
  a job is submitted whenever an object is uploaded to a specified Amazon S3 bucket. Each time this
  happens, the EventBridge input transformer passes the bucket and key name of the object to AWS Batch
  parameters.

###### Note

In this scenario, all of related AWS resources must be in the same Region. This
includes resources such as the Amazon S3 bucket, EventBridge rule, and CloudTrail logs.
Before you can submit AWS Batch jobs with EventBridge rules and targets, the EventBridge service requires
several permissions to run AWS Batch jobs. When you create a rule in the EventBridge console that
specifies an AWS Batch job as a target, you can also create this role. For more information about
the required service principal and IAM permissions for this role, see [EventBridge IAM role](CWE_IAM_role.md "CWE_IAM_role.md").

###### Topics

- [Tutorial: Create a scheduled AWS Batch job](scheduled-batch-job.md "scheduled-batch-job.md")
- [Tutorial: Create a rule with an event pattern](event-pattern-batch-job.md "event-pattern-batch-job.md")
- [Tutorial: Pass event information to an AWS Batch target on a
  schedule using the EventBridge input transformer](cwe-input-transformer.md "cwe-input-transformer.md")
