# Set up FireLens to send logs to CloudWatch Logs

FireLens for Amazon ECS enables you to use task definition parameters to route logs to
Amazon CloudWatch Logs for log storage and analytics. FireLens works with [Fluent Bit](https://fluentbit.io/ "https://fluentbit.io/") and [Fluentd](https://www.fluentd.org/ "https://www.fluentd.org/"). We provide an AWS for Fluent Bit image, or you can use your own
Fluent Bit or Fluentd image. Creating Amazon ECS task definitions with a FireLens configuration
is supported using the AWS SDKs, AWS CLI, and AWS Management Console. For more information about CloudWatch Logs,
see [What is
CloudWatch Logs?](../logs/WhatIsCloudWatchLogs.md "../logs/WhatIsCloudWatchLogs.md").

There are key considerations when using FireLens for Amazon ECS. For more information, see
[Considerations](../../../AmazonECS/latest/developerguide/using_firelens.md#firelens-considerations "../../../AmazonECS/latest/developerguide/using_firelens.md#firelens-considerations").

To find the AWS for Fluent Bit images, see [Using the AWS for
Fluent Bit image](../../../AmazonECS/latest/developerguide/firelens-using-fluentbit.md "../../../AmazonECS/latest/developerguide/firelens-using-fluentbit.md").

To create a task definition that uses a FireLens configuration, see [Creating a task definition that uses a FireLens configuration](../../../AmazonECS/latest/developerguide/firelens-taskdef.md "../../../AmazonECS/latest/developerguide/firelens-taskdef.md").

**Example**

The following task definition example demonstrates how to specify a log configuration
that forwards logs to a CloudWatch Logs log group. For more information, see [What
Is Amazon CloudWatch Logs?](../logs/WhatIsCloudWatchLogs.md "../logs/WhatIsCloudWatchLogs.md") in the _Amazon CloudWatch Logs User Guide_.

In the log configuration options, specify the log group name and the Region it exists
in. To have Fluent Bit create the log group on your behalf, specify
`"auto_create_group":"true"`. You can also specify the task ID as the log
stream prefix, which assists in filtering. For more information, see [Fluent Bit Plugin for CloudWatch Logs](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/blob/mainline/README.md "https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/blob/mainline/README.md").

```
{
	"family": "firelens-example-cloudwatch",
	"taskRoleArn": "arn:aws:iam::`123456789012`:role/`ecs_task_iam_role`",
	"containerDefinitions": [
		{
			"essential": true,
			"image": "906394416424.dkr.ecr.`us-west-2`.amazonaws.com/aws-for-fluent-bit:latest",
			"name": "log_router",
			"firelensConfiguration": {
				"type": "fluentbit"
			},
			"logConfiguration": {
				"logDriver": "awslogs",
				"options": {
					"awslogs-group": "firelens-container",
					"awslogs-region": "`us-west-2`",
					"awslogs-create-group": "true",
					"awslogs-stream-prefix": "`firelens`"
				}
			},
			"memoryReservation": `50`
		 },
		 {
			 "essential": true,
			 "image": "nginx",
			 "name": "app",
			 "logConfiguration": {
				 "logDriver":"awsfirelens",
				 "options": {
					"Name": "cloudwatch_logs",
					"region": "`us-west-2`",
					"log_key": "log",
                                 "log_group_name": "/aws/ecs/containerinsights/`my-cluster`/`application`",
					"auto_create_group": "true",
					"log_stream_name": "`my-task-id`"
				}
			},
			"memoryReservation": `100`
		}
	]
}
```
