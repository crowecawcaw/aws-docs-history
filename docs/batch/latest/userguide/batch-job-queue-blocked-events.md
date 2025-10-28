# Job queue blocked

events

Anytime that AWS Batch detects a job in the `RUNNABLE` state and thus
blocking a queue, an event is created in Amazon CloudWatch Events. For more information about
supported blocked queue causes, see [Jobs stuck in a RUNNABLE status](job_stuck_in_runnable.md "job_stuck_in_runnable.md"). The same reason is also available in
the `statusReason` field in the [`DescribeJobs`](../APIReference/API_DescribeJobs.md "../APIReference/API_DescribeJobs.md") API action.

###### Example Job queue blocked event

Job queue blocked events are delivered in the following format. The
`detail` section resembles the [JobDetail](../APIReference/API_JobDetail.md "../APIReference/API_JobDetail.md") object
that's returned from a [DescribeJobs](../APIReference/API_DescribeJobs.md "../APIReference/API_DescribeJobs.md")
API operation in the _AWS Batch API Reference_. For more
information about EventBridge parameters, see [Events and Event
Patterns](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "c8f9c4b5-76e5-d76a-f980-7011e206042b",
    "detail-type": "Batch Job Queue Blocked",
    "source": "aws.batch",
    "account": "123456789012",
    "time": "2022-01-11T23:36:40Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:batch:us-east-1:123456789012:job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8",
        "arn:aws:batch:us-east-1:123456789012:job-queue/PexjEHappyPathCanary2JobQueue"
    ],
    "detail": {
        "jobArn": "arn:aws:batch:us-east-1:123456789012:job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8",
        "jobName": "event-test",
        "jobId": "4c7599ae-0a82-49aa-ba5a-4727fcce14a8",
        "jobQueue": "arn:aws:batch:us-east-1:123456789012:job-queue/PexjEHappyPathCanary2JobQueue",
        "status": "RUNNABLE",
        "statusReason": "`blocked-reason`",
        "attempts": [],
        "createdAt": 1641944200058,
        "retryStrategy": {
            "attempts": 2,
            "evaluateOnExit": []
        },
        "dependsOn": [],
        "jobDefinition": "arn:aws:batch:us-east-1:123456789012:job-definition/first-run-job-definition:1",
        "parameters": {},
        "container": {
            "image": "137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest",
            "command": [
                "sleep",
                "600"
            ],
            "volumes": [],
            "environment": [],
            "mountPoints": [],
            "ulimits": [],
            "networkInterfaces": [],
            "resourceRequirements": [
                {
                    "value": "2",
                    "type": "VCPU"
                }, {
                    "value": "256",
                    "type": "MEMORY"
                }
            ],
            "secrets": []
        },
        "propagateTags": false,
        "platformCapabilities": []
    }
}
```
