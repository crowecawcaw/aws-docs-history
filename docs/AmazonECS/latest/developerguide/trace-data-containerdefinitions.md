# Specifying the AWS Distro for OpenTelemetry sidecar for AWS X-Ray integration in your task definition

The Amazon ECS console simplifies creating the AWS Distro for OpenTelemetry sidecar
container by using the **Use trace collection** option. For more
information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

If you're not using the Amazon ECS console, you can add the AWS Distro for OpenTelemetry
sidecar container to your task definition. The following task definition snippet shows
the container definition for adding the AWS Distro for OpenTelemetry sidecar for
AWS X-Ray integration.

```
{
	"family": "otel-using-xray",
	"taskRoleArn": "arn:aws:iam::111122223333:role/`AmazonECS_OpenTelemetryXrayRole`",
	"executionRoleArn": "arn:aws:iam::111122223333:role/`ecsTaskExecutionRole`",
	"containerDefinitions": [{
			"name": "`aws-otel-emitter`",
			"image": "`application-image`",
			"logConfiguration": {
				"logDriver": "awslogs",
				"options": {
					"awslogs-create-group": "true",
					"awslogs-group": "/ecs/aws-otel-emitter",
					"awslogs-region": "`us-east-1`",
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
 "--config=/etc/ecs/otel-instance-metrics-config.yaml"
 ],
 "logConfiguration": {
 "logDriver": "awslogs",
 "options": {
 "awslogs-create-group": "True",
 "awslogs-group": "/ecs/ecs-aws-otel-sidecar-collector",
 "awslogs-region": "`us-east-1`",
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
