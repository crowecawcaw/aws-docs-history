# Monitoring tools for Amazon ECS

AWS provides various tools that you can use to monitor Amazon ECS. You can configure some of
these tools to do the monitoring for you, while some of the tools require manual
intervention. We recommend that you automate monitoring tasks as much as possible.

## Automated monitoring tools

You can use the following automated monitoring tools to watch Amazon ECS and report when
something is wrong:

- Amazon CloudWatch alarms – Watch a single metric over a time period that you
  specify, and perform one or more actions based on the value of the metric
  relative to a given threshold over a number of time periods. The action is a
  notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms
  do not invoke actions simply because they are in a particular state; the state
  must have changed and been maintained for a specified number of periods. For
  more information, see [Monitor Amazon ECS using CloudWatch](cloudwatch-metrics.md "cloudwatch-metrics.md").

For services with tasks that use Fargate,
you can use CloudWatch alarms to scale in and scale out the tasks in your
service based on CloudWatch metrics, such as CPU and memory utilization. For more
information, see [Automatically scale your Amazon ECS service](service-auto-scaling.md "service-auto-scaling.md").

For clusters with tasks or services using EC2,
you can use CloudWatch alarms to scale in and scale out the container
instances based on CloudWatch metrics, such as cluster memory reservation.

For your container instances that were launched with the
Amazon ECS-optimized Amazon Linux AMI, you can use CloudWatch Logs to view different logs from your container instances
in one convenient location. You must install the CloudWatch agent on your container
instances. For more information, see [Download and configure the CloudWatch agent using the command line](../../../AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.md "../../../AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.md")
in the _Amazon CloudWatch User Guide_. You must also add the
`ECS-CloudWatchLogs` policy to the `ecsInstanceRole`
role. For more information, see [Monitoring container instances permissions](instance_IAM_role.md#cwl_iam_policy "instance_IAM_role.md#cwl_iam_policy").

- Amazon CloudWatch Logs – Monitor, store, and access the log files from the containers in your
  Amazon ECS tasks by specifying the `awslogs` log driver in your task definitions. For
  more information, see [Send Amazon ECS logs to CloudWatch](using_awslogs.md "using_awslogs.md").

You can also monitor, store, and access the operating system
and Amazon ECS container agent log files from your Amazon ECS container instances. This
method for accessing logs can be used for containers using EC2.

- Amazon CloudWatch Events – Match events and route them to one or more target functions
  or streams to make changes, capture state information, and take corrective
  action. For more information, see [Automate responses to Amazon ECS errors using EventBridge](cloudwatch_event_stream.md "cloudwatch_event_stream.md") in this guide and [EventBridge is the evolution of Amazon CloudWatch Events](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md") in the
  _Amazon EventBridge User Guide_.
- Container Insights – Collect, aggregate, and summarize metrics and logs from your
  containerized applications and microservices. Container Insights collects data as performance log
  events using embedded metric format. These performance log events are entries
  that use a structured JSON schema that allow high-cardinality data to be
  ingested and stored at scale. From this data, CloudWatch creates aggregated
  metrics at the cluster, task, and service level as CloudWatch metrics. The
  metrics that Container Insights collects are available in CloudWatch automatic
  dashboards, and are also viewable in the Metrics section of the CloudWatch
  console.
- AWS CloudTrail log monitoring – Share log files between accounts, monitor
  CloudTrail log files in real time by sending them to CloudWatch Logs, write log processing
  applications in Java, and validate that your log files have not changed after
  delivery by CloudTrail. For more information, see [Log Amazon ECS API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") in this guide, and [Working with CloudTrail
  Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.
- Runtime Monitoring – Detect threats for clusters and containers within your AWS
  environment. Runtime Monitoring uses a GuardDuty security agent that adds runtime
  visibility into individual Amazon ECS workloads, for example, file access, process
  execution, and network connections.

## Manual monitoring tools

Another important part of monitoring Amazon ECS involves manually monitoring those items
that the CloudWatch alarms don't cover. The CloudWatch, Trusted Advisor, and other AWS console dashboards
provide an at-a-glance view of the state of your AWS environment. We recommend that
you also check the log files on your container instances and the containers in your
tasks.

- Amazon ECS console:
  - Cluster metrics for EC2
  - Service metrics
  - Service health status
  - Service deployment events

- CloudWatch home page:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized
       dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to monitor the services you care about.
      + Graph metric data to troubleshoot issues and discover trends.
      + Search and browse all your AWS resource metrics.
      + Create and edit alarms to be notified of problems.

- Container health check - These are commands that run locally on a container
  and validate application health and availability. You configure these per
  container in your task definition.
- AWS Trusted Advisor can help you monitor your AWS resources to improve
  performance, reliability, security, and cost effectiveness. Four Trusted Advisor checks
  are available to all users; more than 50 checks are available to users with a
  Business or Enterprise support plan. For more information, see [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/").

Trusted Advisor has these checks that relate to Amazon ECS:

    + A fault tolerance which indicates that you have a service running in a
     single Availability Zone.
    + A fault tolerance which indicates that you have not used the spread
     placement strategy for multiple Availability Zones.

- AWS Compute Optimizer is a service that analyzes the configuration and utilization metrics
  of your AWS resources. It reports whether your resources are optimal, and
  generates optimization recommendations to reduce the cost and improve the
  performance of your workloads.

For more information, see [AWS Compute Optimizer recommendations for Amazon ECS](ecs-recommendations.md "ecs-recommendations.md").

- Amazon ECS MCP server – Use AI assistants to monitor deployments,
  troubleshoot container issues, and inspect configurations using natural language. The MCP server provides real-time visibility into service health,
  analyzes task failures, and accelerates issue resolution. For more information, see
  [Amazon ECS MCP server](ecs-mcp-introduction.md "ecs-mcp-introduction.md").
