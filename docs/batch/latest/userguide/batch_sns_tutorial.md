# Tutorial: Sending Amazon Simple Notification Service alerts for failed job events

In this tutorial, you configure an Amazon EventBridge event rule that only captures job events where the
job has moved to a `FAILED` status. At the end of this tutorial, you can optionally
also submit a job to this job queue. This is to test that you have configured your Amazon SNS alerts
correctly.

## Prerequisites

This tutorial assumes that you have a working compute environment and job queue that are ready to accept jobs.
If you don't have a running compute environment and job queue to capture events from, follow the steps in [Getting started with AWS Batch tutorials](Batch_GetStarted.md "Batch_GetStarted.md") to create one.

###### Topics

- [Tutorial: Create and subscribe to an Amazon SNS topic](batch_sns_create_topic.md "batch_sns_create_topic.md")
- [Tutorial: Register an event rule](batch_sns_reg_rule.md "batch_sns_reg_rule.md")
- [Tutorial: Test your rule](batch_sns_test_rule.md "batch_sns_test_rule.md")
- [Alternate rule: Batch job queue blocked](#test_blocked_job_queue "#test_blocked_job_queue")

## Alternate rule: Batch job queue blocked

To create an event rule that monitors for _batch job queue blocked_, repeat these tutorials with the following alterations:

1. **In [Tutorial: Create and subscribe to an Amazon SNS topic](batch_sns_create_topic.md "batch_sns_create_topic.md")**, use `BlockedJobQueue` as the topic name.
2. **In [Tutorial: Register an event rule](batch_sns_reg_rule.md "batch_sns_reg_rule.md")**, use the following pattern in the JSON editor:

```
{
   "detail-type": [
     "Batch Job Queue Blocked"
   ],
   "source": [
     "aws.batch"
   ]
}
```
