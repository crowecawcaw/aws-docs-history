# Creating resources for Amazon ECS cluster auto scaling using the

AWS Management Console

Learn how to create the resources for cluster auto scaling using the
AWS Management Console. Where resources require a name, we use the prefix
`ConsoleTutorial` to ensure they all have unique names and to make them easy
to locate.

###### Topics

- [Prerequisites](#console-tutorial-prereqs "#console-tutorial-prereqs")
- [Step 1: Create an Amazon ECS cluster](#console-tutorial-cluster "#console-tutorial-cluster")
- [Step 2: Register a task
  definition](#console-tutorial-register-task-definition "#console-tutorial-register-task-definition")
- [Step 3: Run a task](#console-tutorial-run-task "#console-tutorial-run-task")
- [Step 4: Verify](#console-tutorial-verify "#console-tutorial-verify")
- [Step 5: Clean up](#console-tutorial-cleanup "#console-tutorial-cleanup")

## Prerequisites

This tutorial assumes that the following prerequisites have been completed:

- The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") have been completed.
- Your IAM user has the required permissions specified in the [AmazonECS_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess")
  IAM policy example.
- The Amazon ECS container instance IAM role is created. For more information, see
  [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
- The Amazon ECS service-linked IAM role is created. For more information, see
  [Using service-linked roles for
  Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md").
- The Auto Scaling service-linked IAM role is created. For more information, see
  [Service-Linked Roles for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/autoscaling-service-linked-role.md "../../../autoscaling/ec2/userguide/autoscaling-service-linked-role.md") in the
  _Amazon EC2 Auto Scaling User Guide_.
- You have a VPC and security group created to use. For more information, see
  [Create a virtual private cloud](get-set-up-for-amazon-ecs.md#create-a-vpc "get-set-up-for-amazon-ecs.md#create-a-vpc").

## Step 1: Create an Amazon ECS cluster

Use the following steps to create an Amazon ECS cluster.

Amazon ECS creates an Amazon EC2 Auto Scaling launch template and Auto Scaling group on your behalf as
part of the CloudFormation stack.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Cluster configuration**, for **Cluster
   name**, enter `ConsoleTutorial-cluster`.
4. Under **Infrastructure**, clear AWS Fargate (serverless), and
   then select **Amazon EC2 instances**. Next, configure the Auto Scaling group
   which acts as the capacity provider.
   1. Under **Auto Scaling group (ASG)** . Select **Create
      new ASG**, and then provide the following details about the
      group:
      - For **Operating system/Architecture**, choose
        **Amazon Linux 2**.
      - For **EC2 instance type**, choose
        **t3.nano**.
      - For **Capacity**, enter the minimum number
        and the maximum number of instances to launch in the Auto Scaling group.

5. (Optional) To manage the cluster tags, expand **Tags**, and
   then perform one of the following operations:

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

[Remove a tag] Choose **Remove** to the right of the tag’s
Key and Value. 6. Choose **Create**.

## Step 2: Register a task

definition

Before you can run a task on your cluster, you must register a task definition. Task
definitions are lists of containers grouped together. The following example is a simple
task definition that uses an `amazonlinux` image from Docker Hub and simply
sleeps. For more information about the available task definition parameters, see [Amazon ECS task definitions](task_definitions.md "task_definitions.md").

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**.
3. Choose **Create new task definition**, **Create new
   task definition with JSON**.
4. In the **JSON editor** box, paste the following
   contents.

```
{
    "family": "ConsoleTutorial-taskdef",
    "containerDefinitions": [
        {
            "name": "sleep",
            "image": "public.ecr.aws/amazonlinux/amazonlinux:latest",
            "memory": 20,
            "essential": true,
            "command": [
                "sh",
                "-c",
                "sleep infinity"
            ]
        }
    ],
    "requiresCompatibilities": [
        "EC2"
    ]
}
```

5. Choose **Create**.

## Step 3: Run a task

After you have registered a task definition for your account, you can run a task in
the cluster. For this tutorial, you run five instances of the
`ConsoleTutorial-taskdef` task definition in your
`ConsoleTutorial-cluster` cluster.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose
   **ConsoleTutorial-cluster**.
3. Under **Tasks**, choose **Run new
   task**.
4. In the **Environment** section, under **Compute
   options**, choose **Capacity provider
   strategy**.
5. Under **Deployment configuration**, for **Application
   type**, choose **Task**.
6. Choose **ConsoleTutorial-taskdef** from the **Family** dropdown list.
7. Under **Desired tasks**, enter 5.
8. Choose **Create**.

## Step 4: Verify

At this point in the tutorial, you should have a cluster with five tasks running and
an Auto Scaling group with a capacity provider. The capacity provider has Amazon ECS managed scaling
enabled.

We can verify that everything is working properly by viewing the CloudWatch metrics, the
Auto Scaling group settings, and finally the Amazon ECS cluster task count.

###### To view the CloudWatch metrics for your cluster

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the navigation bar at the top of the screen, select the Region.
3. On the navigation pane, under **Metrics**, choose
   **All metrics**.
4. On the **All metrics** page, under the
   **Browse** tab, choose
   `AWS/ECS/ManagedScaling`.
5. Choose **CapacityProviderName, ClusterName**.
6. Select the check box that corresponds to the
   `ConsoleTutorial-cluster`
   **ClusterName**.
7. Under the **Graphed metrics** tab, change
   **Period** to **30 seconds** and
   **Statistic** to **Maximum**.

The value displayed in the graph shows the target capacity value for the
capacity provider. It should begin at `100`, which was the target
capacity percent we set. You should see it scale up to `200`, which
will trigger an alarm for the target tracking scaling policy. The alarm will
then trigger the Auto Scaling group to scale out.

Use the following steps to view your Auto Scaling group details to confirm that the scale-out
action occurred.

###### To verify the Auto Scaling group scaled out

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation bar at the top of the screen, select the Region.
3. On the navigation pane, under **Auto Scaling**, choose
   **Auto Scaling Groups**.
4. Choose the `ConsoleTutorial-cluster` Auto Scaling group created in this
   tutorial. View the value under **Desired capacity** and view
   the instances under the **Instance management** tab to
   confirm your group scaled out to two instances.

Use the following steps to view your Amazon ECS cluster to confirm that the Amazon EC2 instances
were registered with the cluster and your tasks transitioned to a `RUNNING`
status.

###### To verify the instances in the Auto Scaling group

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the
   `ConsoleTutorial-cluster` cluster.
4. On the **Tasks** tab, confirm you see five tasks in the
   `RUNNING` status.

## Step 5: Clean up

When you have finished this tutorial, clean up the resources associated with it to
avoid incurring charges for resources that you aren't using. Deleting capacity providers
and task definitions are not supported, but there is no cost associated with these
resources.

###### To clean up the tutorial resources

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose
   **ConsoleTutorial-cluster**.
4. On the **ConsoleTutorial-cluster** page, choose the
   **Tasks** tab, and then choose **Stop**,
   **Stop all**.
5. In the navigation pane, choose **Clusters**.
6. On the **Clusters** page, choose
   **ConsoleTutorial-cluster**.
7. In the upper-right of the page, choose **Delete cluster**.
8. In the confirmation box, enter **delete
   **ConsoleTutorial-cluster\***\* and choose **Delete\*\*.
9. Delete the Auto Scaling groups using the following steps.
   1. Open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. On the navigation bar at the top of the screen, select the
      Region.
   3. On the navigation pane, under **Auto Scaling**,
      choose **Auto Scaling Groups**.
   4. Select the `ConsoleTutorial-cluster` Auto Scaling group, then
      choose **Actions**.
   5. From the **Actions** menu, choose
      **Delete**. Enter **delete** in
      the confirmation box and then choose **Delete**.
