# Exporting application metrics to

Amazon Managed Service for Prometheus

Amazon ECS supports exporting your task-level CPU, memory, network, and storage metrics and
your custom application metrics to Amazon Managed Service for Prometheus. This is done by adding the AWS Distro
for OpenTelemetry sidecar container to your task definition. The Amazon ECS console
simplifies this process by adding the **Use metric collection** option
when creating a new task definition. For more information, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").

The metrics are exported to Amazon Managed Service for Prometheus and can be viewed using the Amazon Managed Grafana dashboard.
Your application must be instrumented with either Prometheus libraries or with the
OpenTelemetry SDK. For more information about instrumenting your application with the
OpenTelemetry SDK, see [Introduction to AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction") in the AWS Distro for
OpenTelemetry documentation.

When using the Prometheus libraries, your application must expose a
`/metrics` endpoint which is used to scrape the metrics data. For more
information about instrumenting your application with Prometheus libraries, see [Prometheus client
libraries](https://prometheus.io/docs/instrumenting/clientlibs/ "https://prometheus.io/docs/instrumenting/clientlibs/") in the Prometheus documentation.

## Considerations

The following should be considered when using the Amazon ECS on Fargate integration
with AWS Distro for OpenTelemetry to send application metrics to Amazon Managed Service for Prometheus.

- The AWS Distro for OpenTelemetry integration is supported for Amazon ECS
  workloads hosted on Fargate and Amazon ECS workloads hosted on Amazon EC2 instances.
  External instances aren't supported currently.
- By default, AWS Distro for OpenTelemetry includes all available
  task-level dimensions for your application metrics when exporting to
  Amazon Managed Service for Prometheus. You can also instrument your application to add additional
  dimensions. For more information, see [Getting Started with Prometheus Remote Write Exporter for Amazon Managed Service for Prometheus](https://aws-otel.github.io/docs/getting-started/prometheus-remote-write-exporter "https://aws-otel.github.io/docs/getting-started/prometheus-remote-write-exporter")
  in the AWS Distro for OpenTelemetry documentation.

## Required IAM permissions for

AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus

The Amazon ECS integration with Amazon Managed Service for Prometheus using the AWS Distro for OpenTelemetry
sidecar requires that you create a task IAM role and specify the role in your task
definition. This task IAM role must be created manually
prior to registering your task definition. For more information about creating a task role, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

We recommend that the AWS Distro for OpenTelemetry sidecar also be configured to
route container logs to CloudWatch Logs which requires a task execution IAM role be created
and specified in your task definition as well. The Amazon ECS console takes care of the
task execution IAM role on your behalf, but the task IAM role must be created
manually. For more information about creating a task execution IAM role, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

###### Important

If you're also collecting application trace data using the AWS Distro for
OpenTelemetry integration, ensure your task IAM role also contains the
permissions necessary for that integration. For more information, see [Identify Amazon ECS optimization opportunities using application trace data](trace-data.md "trace-data.md").

The following permissions are required for AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus:

- logs:PutLogEvents
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:DescribeLogStreams
- logs:DescribeLogGroups
- cloudwatch:PutMetricData

## Specifying the

AWS Distro for OpenTelemetry sidecar in your task definition

The Amazon ECS console simplifies the experience of creating the AWS Distro for
OpenTelemetry sidecar container by using the **Use metric
collection** option. For more information, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").

If you're not using the Amazon ECS console, you can add the AWS Distro for
OpenTelemetry sidecar container to your task definition manually. The following task
definition example shows the container definition for adding the AWS Distro for
OpenTelemetry sidecar for Amazon Managed Service for Prometheus integration.

```
{
	"family": "otel-using-cloudwatch",
	"taskRoleArn": "arn:aws:iam::111122223333:role/`AmazonECS_OpenTelemetryCloudWatchRole`",
	"executionRoleArn": "arn:aws:iam::111122223333:role/`ecsTaskExecutionRole`",
	"containerDefinitions": [{
			"name": "`aws-otel-emitter`",
			"image": "`application-image`",
			"logConfiguration": {
				"logDriver": "awslogs",
				"options": {
					"awslogs-create-group": "true",
					"awslogs-group": "/ecs/aws-otel-emitter",
					"awslogs-region": "`aws-region`",
					"awslogs-stream-prefix": "ecs"
				}
			},
			"dependsOn": [{
				"containerName": "aws-otel-collector",
				"condition": "START"
			}]
		},
		**{
 "name": "aws-otel-collector",
 "image": "public.ecr.aws/aws-observability/aws-otel-collector:v0.30.0",
 "essential": true,
 "command": [
 "--config=/etc/ecs/ecs-amp.yaml"
 ],
 "environment": [{
 "name": "AWS\_PROMETHEUS\_ENDPOINT",
 "value": "https://aps-workspaces.`aws-region`.amazonaws.com/workspaces/ws-`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`/api/v1/remote\_write"
 }],
 "logConfiguration": {
 "logDriver": "awslogs",
 "options": {
 "awslogs-create-group": "True",
 "awslogs-group": "/ecs/ecs-aws-otel-sidecar-collector",
 "awslogs-region": "`aws-region`",
 "awslogs-stream-prefix": "ecs"
 }
 }
 }**
	],
	"networkMode": "awsvpc",
	"requiresCompatibilities": [
		"FARGATE"
	],
	"cpu": "1024",
	"memory": "3072"
}
```
