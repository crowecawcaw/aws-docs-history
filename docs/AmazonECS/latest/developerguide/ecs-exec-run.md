

# Running commands using ECS Exec
<a name="ecs-exec-run"></a>

You can use Amazon ECS Exec to collect diagnostic information related to your containers and troubleshoot errors that are encountered throughout the lifecycle of your containers.

## Prerequisites
<a name="ecs-exec-run-prerequisites"></a>

Before you start using ECS Exec, make sure that you have completed these actions:
+ Review the considerations. For more information, see [Considerations](ecs-exec.md#ecs-exec-considerations)
+ Configure ECS Exec for your tasks and services. For more information, see [Configuring ECS Exec](ecs-exec.md#ecs-exec-enabling-and-using)
+ **Install and configure the AWS CLI**. For more information, see [Get started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
+ **Install Session Manager plugin for the AWS CLI**. For more information, see [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html).
+ **Configure a task role with appropriate permissions**. You must use a task role with the appropriate permissions for ECS Exec. For more information, see [Task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).
+ **Verify version requirements**. ECS Exec has version requirements depending on whether your tasks are hosted on Amazon EC2 or AWS Fargate:
  + If you're using Amazon EC2, you must use an Amazon ECS optimized AMI that was released after January 20th, 2021, with an agent version of 1.50.2 or greater. For more information, see [Amazon ECS optimized AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).
  + If you're using AWS Fargate, you must use platform version `1.4.0` or higher (Linux) or `1.0.0` (Windows). For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-fargate.html).

## Using the console for service tasks
<a name="ecs-exec-run-using-console"></a>

You can use the console to run commands using ECS Exec.

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, choose the service.

   The service details page displays.

1. On the service details page, choose **Tasks**. Then, choose the task.

1. Under **Containers**, choose the container where you want to use ECS Exec.

1. To run commands:, do one of the following:
   + Choose **Connect**. 

     A CloudShell session displays where you can run your commands.
   + Choose the arrow, and then choose **Copy AWS CLI command**.

     You can then run the commands locally.

**Expected results**

If the connection is successful, you should see an interactive shell prompt from your container. You can now run commands directly in the container environment. To exit the session, choose **End Session**.

## Using the console for standalone tasks
<a name="ecs-exec-run-using-console-standalone-tasks"></a>

You can use the console to run commands using ECS Exec.

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Tasks** section, choose the task.

   The task details page displays.

1. Under **Containers**, choose the container where you want to use ECS Exec.

1. To run commands:, do one of the following:
   + Choose **Connect**. 

     A CloudShell session displays where you can run your commands.
   + Choose the arrow, and then choose **Copy AWS CLI command**.

     You can then run the commands locally.

**Expected results**

If the connection is successful, you should see an interactive shell prompt from your container. You can now run commands directly in the container environment. To exit the session, choose **End Session**.

## Using the command shell
<a name="ecs-exec-run-using-command-shell"></a>

You can use the command shell to run commands using ECS Exec.

After you have confirmed the `ExecuteCommandAgent` is running, you can open an interactive shell on your container using the following command. If your task contains multiple containers, you must specify the container name using the `--container` flag. Amazon ECS only supports initiating interactive sessions, so you must use the `--interactive` flag.

The following command will run an interactive `/bin/sh` command against a container named {{{{container-name}}}} for a task with an ID of {{task-id}}.

The {{task-id}} is the Amazon Resource Name (ARN) of the task.

```
aws ecs execute-command --cluster {{cluster-name}} \
    --task {{task-id}} \
    --container {{container-name}} \
    --interactive \
    --command {{"/bin/sh"}}
```

**Expected results**

If the command is successful, you should see an interactive shell prompt from your container. You can now run commands directly in the container environment. To exit the session, type `exit` or press `Ctrl+D`.