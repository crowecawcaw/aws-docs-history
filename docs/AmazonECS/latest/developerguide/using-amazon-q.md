# Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console

When you use the JSON editor in the Amazon ECS console to create a task definition, you can
use Amazon Q Developer to provide AI-generated code suggestions for your task definitions.

You can use the inline chat capability to ask Amazon Q Developer to generate, explain, or refactor
task definition JSON with a conversational interface. You can inject generated suggestions
at any point in the task definition and accept or reject the changes proposed. Amazon ECS has
also enhanced the existing inline suggestions feature to utilize Amazon Q Developer.

When you create a task definition using the JSON editor, you can have Amazon Q Developer provide
recommendations to help you create a task definition more quickly. You can have
property-based inline suggestions, or use the Amazon Q Developer suggestions to
autocomplete whole blocks of sample code.

You can use this feature in Regions where Amazon Q Developer is supported. For more information, see [AWS Services by Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Prerequisites

The following are prerequisites:

- In addition to the console permissions, the user that creates the task
  definition in the console must have the
  `codewhisperer:GenerateRecommendations` permission for the
  recommendations and `q:SendMessage` to use inline chat. For more
  information, see [Permissions required for using Amazon Q Developer to provide
  recommendations in the console](console-permissions.md#amazon-q-permission "console-permissions.md#amazon-q-permission").

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task
   definitions**.
3. On the **Create new task definition** menu,
   choose **Create new task definition with
   JSON**.

The **Create task definition** page opens.

The console provides the following default template.

```
{
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "family": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            "essential": true
        }
    ],
    "volumes": [],
    "networkMode": "awsvpc",
    "memory": "3 GB",
    "cpu": "1 vCPU",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}
```

4. In the Amazon Q inline suggestions pop-up, choose
   **Allow**.

If you dismiss the pop-up, you can enable Amazon Q under the gear
icon. 5. In the JSON editor box, edit the JSON document.

To have Amazon Q create and populate the parameters, enter a comment with what
you want to add. In the example below, the comment causes Amazon Q to generate the
lines in bold.

```
{
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "family": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            "essential": true
        },
        // add an nginx container using an image from Public ECR, with port 80 open, and send logs to CloudWatch log group "myproxy"
        **{
 "name": "nginx",
 "image": "public.ecr.aws/nginx/nginx:latest",
 "essential": true,
 "portMappings": [
 {
 "containerPort": 80,
 "hostPort": 80,
 "protocol": "tcp"
 }
 ],
 "logConfiguration": {
 "logDriver": "awslogs",
 "options": {
 "awslogs-group": "myproxy",
 "awslogs-region": "us-east-1",
 "awslogs-stream-prefix": "nginx"
 }
 }
 }**

    ],
    "volumes": [],
    "networkMode": "awsvpc",
    "memory": "3 GB",
    "cpu": "1 vCPU",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}
```

6. To use the inline chate feature, you can highlight the lines, and then choose
   the star icon.

The Amazon Q Developer chat box displays.

Enter your request.

Amazon Q Developer generates, and then updates the JSON.

To accept the changes, choose **Accept All** 7. Choose **Create**.
