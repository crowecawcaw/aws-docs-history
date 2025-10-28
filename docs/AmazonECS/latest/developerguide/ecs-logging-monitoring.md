# Logging and Monitoring in Amazon Elastic Container Service

Monitoring is an important part of maintaining the reliability, availability, and performance of
Amazon Elastic Container Service and your AWS solutions. You should collect monitoring data from all of the parts of your AWS
solution so that you can more easily debug a multi-point failure if one occurs. AWS provides several
tools for monitoring your Amazon ECS resources and responding to potential incidents:

**Amazon CloudWatch Alarms**

Watch a single metric over a time period that you specify, and perform one or more actions
based on the value of the metric relative to a given threshold over a number of time periods.
The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms
do not invoke actions simply because they are in a particular state; the state must have
changed and been maintained for a specified number of periods. For more information, see [Monitor Amazon ECS using CloudWatch](cloudwatch-metrics.md "cloudwatch-metrics.md").

For services with tasks that use Fargate, you can use CloudWatch
alarms to scale in and scale out the tasks in your service based on CloudWatch metrics, such as CPU
and memory utilization. For more information, see [Automatically scale your Amazon ECS service](service-auto-scaling.md "service-auto-scaling.md").

For clusters with tasks or services using EC2, you can use CloudWatch
alarms to scale in and scale out the container instances based on CloudWatch metrics, such as cluster
memory reservation.

**Amazon CloudWatch Logs**

Monitor, store, and access the log files from the containers in your Amazon ECS tasks by
specifying the `awslogs` log driver in your task definitions. For more information,
see [Using
the awslogs driver](using_awslogs.md "using_awslogs.md").

You can also monitor, store, and access the operating system and Amazon ECS
container agent log files from your Amazon ECS container instances. This method for accessing logs
can be used for containers using EC2..

**Amazon CloudWatch Events**

Match events and route them to one or more target functions or streams to make changes,
capture state information, and take corrective action. For more information, see [Automate responses to Amazon ECS errors using EventBridge](cloudwatch_event_stream.md "cloudwatch_event_stream.md") in this guide
and [EventBridge is the evolution of Amazon CloudWatch Events](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md") in the _Amazon EventBridge User Guide_.

**AWS CloudTrail Logs**

CloudTrail provides a record of actions taken by a user, role, or an AWS service in Amazon ECS. Using
the information collected by CloudTrail, you can determine the request that was made to Amazon ECS, the IP
address from which the request was made, who made the request, when it was made, and additional
details. For more information, see [Log Amazon ECS API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**AWS Trusted Advisor**

Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS
customers. Trusted Advisor inspects your AWS environment and then makes recommendations when
opportunities exist to save money, improve system availability and performance, or help close
security gaps. All AWS customers have access to five Trusted Advisor checks. Customers with a
Business or Enterprise support plan can view all Trusted Advisor checks.

For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor") in the _Support User Guide_.

**AWS Compute Optimizer**

AWS Compute Optimizer is a service that analyzes the configuration and utilization metrics
of your AWS resources. It reports whether your resources are optimal, and
generates optimization recommendations to reduce the cost and improve the
performance of your workloads.

For more information, see [AWS Compute Optimizer recommendations for Amazon ECS](ecs-recommendations.md "ecs-recommendations.md").

Another important part of monitoring Amazon ECS involves manually monitoring those items that the CloudWatch alarms
don't cover. The CloudWatch, Trusted Advisor, and other AWS console dashboards provide an at-a-glance view of the
state of your AWS environment. We recommend that you also check the log files on your container instances
and the containers in your tasks.
