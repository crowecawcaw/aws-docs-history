# Task retirement and maintenance for AWS Fargate on Amazon ECS

AWS is responsible for maintaining the underlying infrastructure for AWS Fargate. AWS
determines when a platform version revision needs to be replaced with a new revision for
the infrastructure. This is known as task retirement. AWS sends a task retirement
notification when a platform version revision is retired. We routinely update our
supported platform versions to introduce a new revision containing updates to the
Fargate runtime software and underlying dependencies such as the operating system and
container runtime. After a newer revision is made available, we retire the older revision
in order to ensure all customer workloads run on the most up to date revision of the
Fargate platform version. When a revision is retired, all tasks running on that
revision are stopped.

Amazon ECS tasks can be categorized as either service tasks or standalone tasks. Service tasks
are deployed as part of a service and controlled by the Amazon ECS schedule. For more
information, see [Amazon ECS services](ecs_services.md "ecs_services.md"). Standalone
tasks are tasks started by the Amazon ECS `RunTask` API, either directly or by an
external scheduler such as scheduled tasks (which are started by Amazon EventBridge), AWS Batch,
or AWS Step Functions. You do not need to take any actions in response to task retirement for
your service tasks because the Amazon ECS scheduler automatically replaces the tasks.

For standalone tasks, you may need to perform additional handling in response to task
retirement. For more information, see [Can Amazon ECS automatically handle
standalone tasks?](#task-retirement-standalone-tasks "#task-retirement-standalone-tasks").

For service tasks, you do not need to take any action to task retirement unless you
want to replace these tasks before AWS does. When the Amazon ECS scheduler stops the tasks, it
uses the `maximumPercent` and launches a new task in an attempt to maintain the
desired count for the service. Follow best practices to minimize the impact of task retirement. The default
`maximumPercent` value for a service using the REPLICA service scheduler is
200%. Therefore, when AWS Fargate starts retiring tasks, Amazon ECS first schedules a new task,
and then waits for it to be running, before retiring an old task. When you set the
`maximumPercent` value to 100%, Amazon ECS stops the task first, then replaces
it.

For standalone task retirement, AWS stops the task on or after the task retirement
date. Amazon ECS doesn’t launch a replacement task when a task is stopped. If you need these tasks
to continue to run, you need to stop the running tasks and launch a replacement task
before the time indicated in the notification. Therefore, we recommend that customers
monitor the state of standalone tasks and if required, implement logic to replace the
stopped tasks.

When a task is stopped in any of the scenarios, you can run `describe-tasks`.
The `stoppedReason` in the response is `ECS is performing maintenance on the
 underlying infrastructure hosting the task`.

Task maintenance applies when there is a new platform version revision needs to be
replaced with a new revision. If there is an issue with an underlying Fargate host,
Amazon ECS replaces the host without a task retirement notice.

## Task retirement notice overview

When AWS marks a platform version revision as needing to be retired, we identify all
of the tasks that are running on that platform version revision in all
Regions.

The following illustration shows the lifecycle of a Fargate platform version
revision from a new revision launch to the platform revision retirement.

![Diagram showing the Fargate task retirement lifecycle.](images/fargate-task-retirement.png)

The following information provides details.

- After a new platform version revision is launched, all new tasks are scheduled
  on this revision.
- Existing tasks that have been scheduled and running remain on the revision
  they were originally placed on for the duration of the task and aren't migrated
  to the new revision.
- New tasks, for example as part of an update to a service or Fargate task
  retirement, are placed on to latest platform version revision available at the
  time of launch.

Task retirement notifications are sent through AWS Health Dashboard as well as
through an email to the registered email address and includes the following
information:

- The task retirement date - The task is stopped on or after this date.
- For standalone tasks, the IDs of the tasks.
- For service tasks, the ID of the cluster where the service runs and the IDs of
  the service.
- The next steps you need to take.

Typically, we send one notification each for service and standalone tasks in each
AWS Region. However, in certain cases you might receive more than one event for each
task type, for example when there are too many tasks to be retired that will surpass
limits in our notification mechanisms.

You can identify tasks scheduled for retirement in the following ways:

- The Health Dashboard

AWS Health notifications can be sent through Amazon EventBridge to archival storage
such as Amazon Simple Storage Service, take automated actions such as run an AWS Lambda function, or
other notification systems such as Amazon Simple Notification Service. For more information, see [Monitoring AWS Health events with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md"). For sample
configuration to send notifications to Amazon Chime, Slack, or Microsoft Teams, see
the [AWS Health
Aware](https://github.com/aws-samples/aws-health-aware "https://github.com/aws-samples/aws-health-aware") repository on GitHub.

The following is a sample EventBridge event.

```
{
    "version": "0",
    "id": "3c268027-f43c-0171-7425-1d799EXAMPLE",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-08-16T23:18:51Z",
    "region": "us-east-1",
    "resources": [
        "cluster|service",
        "cluster|service"
    ],
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/ECS/AWS_ECS_TASK_PATCHING_RETIREMENT/AWS_ECS_TASK_PATCHING_RETIREMENT_test1",
        "service": "ECS",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "7988399e2e6fb0b905ddc88e0e2de1fd17e4c9fa60349577446d95a18EXAMPLE",
        "lastUpdatedTime": "Wed, 16 Aug 2023 23:18:52 GMT",
        "eventRegion": "us-east-1",
        "eventTypeCode": "AWS_ECS_TASK_PATCHING_RETIREMENT",
        "eventTypeCategory": "scheduledChange",
        "startTime": "Wed, 16 Aug 2023 23:18:51 GMT",
        "endTime": "Fri, 18 Aug 2023 23:18:51 GMT",
        "eventDescription": [
            {
                "language": "en_US",
                "latestDescription": "\\nA software update has been deployed to Fargate which includes CVE patches or other critical patches. No action is required on your part. All new tasks launched automatically uses the latest software version. For existing tasks, your tasks need to be restarted in order for these updates to apply. Your tasks running as part of the following ECS Services will be automatically updated beginning Wed, 16 Aug 2023 23:18:51 GMT.\\n\\nAfter Wed, 16 Aug 2023 23:18:51 GMT, the ECS scheduler will gradually replace these tasks, respecting the deployment settings for your service. Typically, services should see little to no interruption during the update and no action is required. When AWS stops tasks, AWS uses the minimum healthy percent (1) and launches a new task in an attempt to maintain the desired count for the service. By default, the minimum healthy percent of a service is 100 percent, so a new task is started first before a task is stopped. Service tasks are routinely replaced in the same way when you scale the service or deploy configuration changes or deploy task definition revisions. If you would like to control the timing of this restart you can update the service before Wed, 16 Aug 2023 23:18:51 GMT, by running the update-service command from the ECS command-line interface specifying force-new-deployment for services using Rolling update deployment type. For example:\\n\\n$ aws ecs update-service -service service_name \\\n--cluster cluster_name -force-new-deployment\\n\\nFor services using Blue/Green deployment type with AWS CodeDeploy:\\nPlease refer to create-deployment document (2) and create new deployment using same task definition revision.\\n\\nFor further details on ECS deployment types, please refer to ECS Deployment Developer Guide (1).\\nFor further details on Fargate's update process, please refer to the AWS Fargate User Guide (3).\\nIf you have any questions or concerns, please contact AWS Support (4).\\n\\n(1) https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\\n(2) https://docs.aws.amazon.com/cli/latest/reference/deploy/create-deployment.html\\n(3) https://docs.aws.amazon.com/AmazonECS/latest/userguide/task-maintenance.html\\n(4) https://aws.amazon.com/support\\n\\nA list of your affected resources(s) can be found in the 'Affected resources' tab in the 'Cluster/ Service' format in the AWS Health Dashboard. \\n\\n"
            }
        ],
      "affectedEntities": [
                {
                    "entityValue": "arn:aws:ecs:eu-west-1:111222333444:task/examplecluster/00805ce1d81940b5a37398e5a2c23333"
                },
                {
                    "entityValue": "arn:aws:ecs:eu-west-1:111222333444:task/examplecluster/00805ce1d81940b5a37398e5a2c25555"
                }
            }
        ]
    }
}
```

- Email

An email is sent to the registered email for the AWS account ID.

For information about how to prepare for task retirement, see [Prepare for AWS Fargate task retirement on Amazon ECS](prepare-task-retirement.md "prepare-task-retirement.md") .

## Can I opt-out of task retirement?

No. As part of the AWS shared responsibility model, AWS is responsible for managing
and maintaining the underlying infrastructure for AWS Fargate. This includes
performing periodic platform updates to ensure security and stability. These updates are
automatically applied by AWS and are not something customers can opt-out of. This is a
key benefit of using a AWS Fargate compared to running your workloads on
EC2 instances, the responsibility for maintaining the underlying platform is
handled by AWS. This model allows you to focus on your applications rather than infrastructure
maintenance. By automatically applying these platform updates, AWS is able to keep the
Fargate environment up-to-date and secure, without any action required from you as the
customer. This helps provide a reliable and secure containerized environment for running
your workloads on Fargate.

## Can I get task retirement notifications through

other AWS services?

AWS sends a task retirement notification to the Health Dashboard and to the primary email
contact on the AWS account. The Health Dashboard provides a number of integrations into other
AWS services, including EventBridge. You can use EventBridge to automate the visibility of the
notices (For example. forwarding the message to a ChatOps tool). For more information,
see [Solution overview: Capturing task retirement notifications](https://aws.amazon.com/blogs/containers/improving-operational-visibility-with-aws-fargate-task-retirement-notifications/ "https://aws.amazon.com/blogs/containers/improving-operational-visibility-with-aws-fargate-task-retirement-notifications/").

## Can I change a task retirement after it is

scheduled?

No. The schedule is based on the task retirement wait time which has a default of 7
days. If you need more time, you can choose to configure the wait period to 14 days. For
more information, see [Step 2: Capture task retirement notifications to
alert teams and take actions](prepare-task-retirement.md#prepare-task-retirement-capture-task-events "prepare-task-retirement.md#prepare-task-retirement-capture-task-events").

As of 12/18/2025, Amazon ECS enables you to configure [Amazon EC2 event windows](../../../AWSEC2/latest/UserGuide/event-windows.md "../../../AWSEC2/latest/UserGuide/event-windows.md") for your Fargate tasks. If
you need precise control over the exact timing of task retirements, for example, scheduling them over
weekends to avoid disruption during business hours, you can configure Amazon EC2 event windows for your tasks,
services, or clusters, see [Step 1: Set the task wait time or use Amazon EC2 event windows](prepare-task-retirement.md#prepare-task-retirement-set-time "prepare-task-retirement.md#prepare-task-retirement-set-time"). Note that the change in this configuration applies to
retirements that will be scheduled in the future. Currently scheduled retirements are not impacted. Furthermore,
when you configure an Amazon EC2 event window for your Fargate tasks, it takes precedence over your task retirement
wait time configuration. If you have any further concerns, contact Support.

## How does Amazon ECS handle tasks that are

part of a service?

For service tasks, you do not need to take any action in response to task retirement
unless you want to replace these tasks before AWS does. When the Amazon ECS scheduler stops
the tasks, it uses the minimum healthy percent and launches a new task in an attempt to
maintain the desired count for the service. To minimalize the impact of Fargate task
retirement, workloads should be deployed following Amazon ECS best practices. For example,
when deploying a stateless application as an Amazon ECS service, such as a web or API server,
customers should deploy multiple task replicas and set the minimumHealthyPercent to
100%. By default, the minimum healthy percent of a service is 100 percent. Therefore,
when Fargate starts retiring tasks, Amazon ECS first schedules a new task and waits for it
to be running, before retiring an old task. Service tasks are routinely replaced as part
of task retirement in the same way when you scale the service, deploy configuration
changes, or deploy task definition revisions. To prepare for the task retirement
process, see [Prepare for AWS Fargate task retirement on Amazon ECS](prepare-task-retirement.md "prepare-task-retirement.md") .

## Can Amazon ECS automatically handle

standalone tasks?

No. AWS can't create a replacement task for standalone tasks which are started by
`RunTask`, scheduled tasks (for example through EventBridge Scheduler), AWS Batch, or
AWS Step Functions. Amazon ECS manages only tasks that are part of a service.

## Troubleshooting service availability during task retirement

If Amazon ECS cannot start a replacement task during task retirement, your service availability may be impacted. This can occur due to incorrect customer configuration, such as:

- Missing or incorrectly configured IAM roles
- Insufficient capacity in the target subnets
- Security group misconfigurations
- Task definition errors

When Amazon ECS cannot launch replacement tasks, the retired tasks are stopped without replacement, reducing your service's available capacity and potentially causing service disruption. Monitor your service's task count and Amazon CloudWatch metrics to ensure replacement tasks are successfully launched during retirement events.
