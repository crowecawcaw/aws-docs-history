# Sending Amazon Simple Notification Service alerts for Amazon ECS task stopped events

Configure an Amazon EventBridge event rule that only captures task events where the task has stopped
running because one of its essential containers has terminated. The event sends only task
events with a specific `stoppedReason` property to the designated Amazon SNS
topic.

## Prerequisite: Set up a test cluster

If you do not have a running cluster to capture events from, follow the steps in
[Getting started with the console using Linux containers on AWS Fargate](getting-started-fargate.md#get-started-fargate-cluster "getting-started-fargate.md#get-started-fargate-cluster") to
create one. At the end of this tutorial, you run a task on this cluster to test that you
have configured your Amazon SNS topic and EventBridge rule correctly.

## Prerequisite: Configure permissions for Amazon SNS

To allow EventBridge to publish to an Amazon SNS topic, use the aws sns get-topic-attributes and
the aws sns set-topic-attributes commands.

For information about how to add the permission, see [Amazon SNS permissions](../../../eventbridge/latest/userguide/eb-use-resource-based.md#eb-sns-permissions "../../../eventbridge/latest/userguide/eb-use-resource-based.md#eb-sns-permissions") in the _Amazon Simple Notification Service Developer Guide_

Add the following permissions:

```
{
  "Sid": "PublishEventsToMyTopic",
  "Effect": "Allow",
  "Principal": {
     "Service": "events.amazonaws.com"
  },
  "Action": "sns: Publish",
  "Resource": "arn:aws:sns:`region`:`account-id`:TaskStoppedAlert",
}
```

## Step 1: Create and subscribe to an Amazon SNS topic

For this tutorial, you configure an Amazon SNS topic to serve as an event target for your
new event rule.

For information about how to create and subscribe to an Amazon SNS topic , see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#step-create-queue "../../../sns/latest/dg/sns-getting-started.md#step-create-queue") in the _Amazon Simple Notification Service Developer Guide_ and use the following table to determine what options to select.

| Option   | Value                                               |
| -------- | --------------------------------------------------- |
| Type     | Standard                                            |
| Name     | TaskStoppedAlert                                    |
| Protocol | Email                                               |
| Endpoint | An email address to which you currently have access |

## Step 2: Register an event rule

Next, you register an event rule that captures only task-stopped events for tasks
with stopped containers.

For information about how to create and subscribe to an Amazon SNS topic , see [Create a
rule in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User
Guide_ and use the following table to determine what options to
select.

| Option        | Value                                                                                                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rule type     | Rule with an event pattern                                                                                                                                                                                                      |
| Event source  | AWS events or EventBridge partner events                                                                                                                                                                                        |
| Event pattern | Custom pattern (JSON editor)                                                                                                                                                                                                    |
| Event pattern | `<br>{<br>"source":[<br>"aws.ecs"<br>],<br>"detail-type":[<br>"ECS Task State Change"<br>],<br>"detail":{<br>"lastStatus":[<br>"STOPPED"<br>],<br>"stoppedReason":[<br>"Essential container in task exited"<br>]<br>}<br>}<br>` |
| Target type   | AWS service                                                                                                                                                                                                                     |
| Target        | SNS topic                                                                                                                                                                                                                       |
| Topic         | TaskStoppedAlert (The topic you created in Step 1)                                                                                                                                                                              |

## Step 3: Test your rule

Verify that the rule is working by running a task that exits shortly after it starts.
If your event rule is configured correctly, you receive an email message within a few
minutes with the event text. If you have an existing task definition that can satisfy
the rule requirements, run a task using it. If you do not, the following steps will walk
you through registering a Fargate task definition and running it that will.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**.
3. Choose **Create new task definition**, **Create new
   task definition with JSON**.
4. In the JSON editor box, edit your JSON file, copy the following into the
   editor.

```
{
   "containerDefinitions":[
      {
         "command":[
            "sh",
            "-c",
            "sleep 5"
         ],
         "essential":true,
         "image":"public.ecr.aws/amazonlinux/amazonlinux:latest",
         "name":"test-sleep"
      }
   ],
   "cpu":"256",
   "executionRoleArn":"arn:aws:iam::`012345678910`:role/`ecsTaskExecutionRole`",
   "family":"fargate-task-definition",
   "memory":"512",
   "networkMode":"awsvpc",
   "requiresCompatibilities":[
      "FARGATE"
   ]
}
```

5. Choose **Create**.

###### To run a task from the console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster you created in
   the prerequisites.
3. From the **Tasks** tab, choose **Run new
   task**.
4. For **Application type**, choose
   **Task**.
5. For **Task definition**, choose
   **fargate-task-definition**.
6. For **Desired tasks**, enter the number of tasks to
   launch.
7. Choose **Create**.
