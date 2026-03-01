# Exporting application metrics to Amazon CloudWatch

Amazon ECS on Fargate supports exporting your custom application metrics to Amazon CloudWatch as
custom metrics. This is done by adding the AWS Distro for OpenTelemetry sidecar
container to your task definition. The Amazon ECS console simplifies this process by adding
the **Use metric collection** option when creating a new task
definition. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

The application metrics are exported to CloudWatch Logs with log group name
`/aws/ecs/application/metrics` and the metrics can be viewed in the
`ECS/AWSOTel/Application` namespace. Your application must be
instrumented with the OpenTelemetry SDK. For more information, see [Introduction to AWS Distro for
OpenTelemetry](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction") in the AWS Distro for OpenTelemetry documentation.

## Considerations

The following should be considered when using the Amazon ECS on Fargate integration
with AWS Distro for OpenTelemetry to send application metrics to Amazon CloudWatch.

- This integration only sends your custom application metrics to CloudWatch. If
  you want task-level metrics, you can turn on Container Insights in the Amazon ECS cluster
  configuration. For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").
- The AWS Distro for OpenTelemetry integration is supported for Amazon ECS
  workloads hosted on Fargate and Amazon ECS workloads hosted on Amazon EC2 instances.
  External instances aren't currently supported.
- CloudWatch supports a maximum of 30 dimensions per metric. By default, Amazon ECS
  defaults to including the `TaskARN`, `ClusterARN`,
  `LaunchType`, `TaskDefinitionFamily`, and
  `TaskDefinitionRevision` dimensions to the metrics. The
  remaining 25 dimensions can be defined by your application. If more than 30
  dimensions are configured, CloudWatch can't display them. When this occurs, the
  application metrics will appear in the `ECS/AWSOTel/Application`
  CloudWatch metric namespace but without any dimensions. You can instrument your
  application to add additional dimensions. For more information, see [Using CloudWatch metrics with AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/getting-started/cloudwatch-metrics "https://aws-otel.github.io/docs/getting-started/cloudwatch-metrics") in the
  AWS Distro for OpenTelemetry documentation.

## Required IAM permissions for AWS Distro for OpenTelemetry integration with Amazon CloudWatch

The Amazon ECS integration with AWS Distro for OpenTelemetry requires that you create
a task IAM role and specify the role in your task definition. We recommend that
the AWS Distro for OpenTelemetry sidecar also be configured to route container
logs to CloudWatch Logs which requires a task execution IAM role be created and specified in
your task definition as well. The Amazon ECS console takes care of the task execution
IAM role on your behalf, but the task IAM role must be created manually and
added to your task definition. For more information about the task execution IAM
role, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

###### Important

If you're also collecting application trace data using the AWS Distro for
OpenTelemetry integration, ensure your task IAM role also contains the
permissions necessary for that integration. For more information, see [Identify Amazon ECS optimization opportunities using application trace data](trace-data.md "trace-data.md").

If your application requires any additional permissions, you should add them
to this policy. Each task definition may only specify one task IAM role. For
example, if you are using a custom configuration file stored in Systems Manager, you
should add the `ssm:GetParameters` permission to this IAM
policy.

###### To create the service role for Elastic Container Service (IAM console)

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  For **Trusted entity type**, choose **AWS service**.
4.  For **Service or use case**, choose **Elastic Container Service**, and then choose the **Elastic Container Service Task** use case.
5.  Choose **Next**.
6.  In the **Add permissions** section, search for **AWSDistroOpenTelemetryPolicyForXray**, then
    select the policy.
7.  (Optional) Set a [permissions
    boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
    not service-linked roles.

        1. Open the **Set permissions boundary** section, and then choose
        **Use a permissions boundary to control the maximum role permissions**.


        IAM includes a list of the AWS managed and customer-managed policies in your account.
        2. Select the policy to use for the permissions boundary.

8.  Choose **Next**.
9.  Enter a role name or a role name suffix to help you identify the purpose of the role.

###### Important

When you name a role, note the following:

    * Role names must be unique within your AWS account, and can't be made unique by case.


    For example, don't create roles named both `PRODROLE` and
     `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
    * You can't edit the name of the role after it's created because other entities might reference the role.

10. (Optional) For **Description**, enter a description for the role.
11. (Optional) To edit
    the use cases and permissions for the role, in the **Step 1: Select trusted
    entities** or **Step 2: Add permissions** sections, choose **Edit**.
12. (Optional) To help identify, organize, or search for the role, add tags as key-value pairs. For more
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

## Specifying the AWS Distro for OpenTelemetry sidecar in your task definition

The Amazon ECS console simplifies the experience of creating the AWS Distro for
OpenTelemetry sidecar container by using the **Use metric
collection** option. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

If you're not using the Amazon ECS console, you can add the AWS Distro for
OpenTelemetry sidecar container to your task definition manually. The following task
definition example shows the container definition for adding the AWS Distro for
OpenTelemetry sidecar for Amazon CloudWatch integration.

```
{
	"family": "otel-using-cloudwatch",
	"taskRoleArn": "arn:aws:iam::111122223333:role/`AmazonECS_OpenTelemetryCloudWatchRole`",
	"executionRoleArn": "arn:aws:iam::111122223333:role/`ecsTaskExecutionRole`",
	"containerDefinitions": [
	   {
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
 "--config=/etc/ecs/ecs-cloudwatch.yaml"
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
