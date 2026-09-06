

# Tutorial: Sending Amazon Simple Notification Service alerts for failed job events
<a name="batch_sns_tutorial"></a>

In this tutorial, you configure an Amazon EventBridge event rule that only captures job events where the job has moved to a `FAILED` status. At the end of this tutorial, you can optionally also submit a job to this job queue. This is to test that you have configured your Amazon SNS alerts correctly.

## Prerequisites
<a name="batch_sns_prereq"></a>

This tutorial assumes that you have a working compute environment and job queue that are ready to accept jobs. If you don't have a running compute environment and job queue to capture events from, follow the steps in [Getting started with AWS Batch tutorials](Batch_GetStarted.md) to create one. 

**Topics**
+ [Prerequisites](#batch_sns_prereq)
+ [Tutorial: Create and subscribe to an Amazon SNS topic](batch_sns_create_topic.md)
+ [Tutorial: Register an event rule](batch_sns_reg_rule.md)
+ [Tutorial: Test your rule](batch_sns_test_rule.md)
+ [Alternate rule: Batch job queue blocked](#test_blocked_job_queue)

## Alternate rule: Batch job queue blocked
<a name="test_blocked_job_queue"></a>

To create an event rule that monitors for *batch job queue blocked*, repeat these tutorials with the following alterations:

1. **In [Tutorial: Create and subscribe to an Amazon SNS topic](batch_sns_create_topic.md) **, use {{BlockedJobQueue}} as the topic name.

1. **In [Tutorial: Register an event rule](batch_sns_reg_rule.md) **, use the following pattern in the JSON editor:

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