# Configuring Amazon ECS to listen for CloudWatch Events events

Learn how to set up a simple Lambda function that listens for task
events and writes them out to a CloudWatch Logs log stream.

## Prerequisite: Set up a test cluster

If you do not have a running cluster to capture events from, follow the steps in [Creating an Amazon ECS cluster for Fargate workloads](create-cluster-console-v2.md "create-cluster-console-v2.md") to create one. At the end of this tutorial,
you run a task on this cluster to test that you have configured your Lambda function
correctly.

## Step 1: Create the Lambda function

In this procedure, you create a simple Lambda function to serve as a target for Amazon ECS
event stream messages.

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. On the **Author from scratch** screen, do the
   following:
   1. For **Name**, enter a value.
   2. For **Runtime**, choose your version of Python, for
      example, **Python 3.9**.
   3. For **Role**, choose **Create a new role with
      basic Lambda permissions**.

4. Choose **Create function**.
5. In the **Function code** section, edit the sample code to
   match the following example:

```
import json

def lambda_handler(event, context):
    if event["source"] != "aws.ecs":
       raise ValueError("Function only supports input from events with a source type of: aws.ecs")

    print('Here is the event:')
    print(json.dumps(event))
```

This is a simple Python 3.9 function that prints the event sent by Amazon ECS. If
everything is configured correctly, at the end of this tutorial, you see that
the event details appear in the CloudWatch Logs log stream associated with this Lambda
function. 6. Choose **Save**.

## Step 2: Register an event rule

Next, you create a CloudWatch Events event rule that captures task events coming from your Amazon ECS
clusters. This rule captures all events coming from all clusters within the account
where it is defined. The task messages themselves contain information about the event
source, including the cluster on which it resides, that you can use to filter and sort
events programmatically.

###### Note

When you use the AWS Management Console to create an event rule, the console automatically adds
the IAM permissions necessary to grant CloudWatch Events permission to call your Lambda
function. If you are creating an event rule using the AWS CLI, you need to grant this
permission explicitly. For more information, see [Events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") and [Amazon EventBridge event
patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge User Guide_.

###### To route events to your Lambda function

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the navigation pane, choose **Events**,
   **Rules**, **Create rule**.
3. For **Event Source**, choose **ECS** as the
   event source. By default, the rule applies to all Amazon ECS events for all of your
   Amazon ECS groups. Alternatively, you can select specific events or a specific Amazon ECS
   group.
4. For **Targets**, choose **Add target**, for
   **Target type**, choose **Lambda
   function**, and then select your Lambda function.
5. Choose **Configure details**.
6. For **Rule definition**, type a name and description for your
   rule and choose **Create rule**.

## Step 3: Create a task definition

Create a task definition.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task Definitions**.
3. Choose **Create new Task Definition**, **Create new
   revision with JSON**.
4. Copy and paste the following example task definition into the box and then
   choose **Save**.

```
{
   "containerDefinitions": [
      {
         "command": [
            "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
         ],
         "entryPoint": [
            "sh",
            "-c"
         ],
         "essential": true,
         "image": "public.ecr.aws/docker/library/httpd:2.4",
         "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
               "awslogs-group" : "/ecs/fargate-task-definition",
               "awslogs-region": "us-east-1",
               "awslogs-stream-prefix": "ecs"
            }
         },
         "name": "sample-fargate-app",
         "portMappings": [
            {
               "containerPort": 80,
               "hostPort": 80,
               "protocol": "tcp"
            }
         ]
      }
   ],
   "cpu": "256",
   "executionRoleArn": "arn:aws:iam::`012345678910`:role/ecsTaskExecutionRole",
   "family": "fargate-task-definition",
   "memory": "512",
   "networkMode": "awsvpc",
   "runtimePlatform": {
        "operatingSystemFamily": "LINUX"
    },
   "requiresCompatibilities": [
       "FARGATE"
    ]
}
```

5. Choose **Create**.

## Step 4: Test your rule

Finally, you create a CloudWatch Events event rule that captures task events coming from your
Amazon ECS clusters. This rule captures all events coming from all clusters within the
account where it is defined. The task messages themselves contain information about the
event source, including the cluster on which it resides, that you can use to filter and
sort events programmatically.

###### To test your rule

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Choose **Task definitions**.
3. Choose **console-sample-app-static**, and then choose
   **Deploy**, **Run new task**.
4. For **Cluster**, choose default, and then choose
   **Deploy**.
5. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
6. On the navigation pane, choose **Logs** and select the log
   group for your Lambda function (for example,
   **/aws/lambda/**`my-function`).
7. Select a log stream to view the event data.
