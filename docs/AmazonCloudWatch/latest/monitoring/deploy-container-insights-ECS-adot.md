# Setting up Container Insights on

Amazon ECS using AWS Distro for OpenTelemetry

Use this section if you want to use AWS Distro for OpenTelemetry to set up CloudWatch
Container Insights on an Amazon ECS cluster. For more information about AWS Distro for Open
Telemetry, see [AWS Distro for
OpenTelemetry](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/").

These steps assume that you already have a cluster running Amazon ECS. For more information
about using AWS Distro for Open Telemetry with Amazon ECS and setting up an Amazon ECS cluster for
this purpose, see [Setting up AWS
Distro for OpenTelemetry Collector in Amazon Elastic Container Service](https://aws-otel.github.io/docs/setup/ecs "https://aws-otel.github.io/docs/setup/ecs").

## Step 1: Create a

task role

The first step is creating a task role in the cluster that the AWS OpenTelemetry
Collector will use.

###### To create a task role for AWS Distro for OpenTelemetry

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies** and then choose
   **Create policy**.
3. Choose the **JSON** tab and copy in the following
   policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:DescribeLogGroups",
 "ssm:GetParameters"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. Choose **Review policy**.
5. For name, enter `AWSDistroOpenTelemetryPolicy`, and then
   choose **Create policy**.
6. In the left navigation pane, choose **Roles** and then choose
   **Create role**.
7. In the list of services, choose **Elastic Container
   Service**.
8. Lower on the page, choose **Elastic Container Service Task**
   and then choose **Next: Permissions**.
9. In the list of policies, search for
   **AWSDistroOpenTelemetryPolicy**.
10. Select the check box next to
    **AWSDistroOpenTelemetryPolicy**.
11. Choose **Next: Tags** and then choose **Next:
    Review.**
12. For **Role name** enter
    `AWSOpenTelemetryTaskRole` and then choose **Create
    role**.

## Step 2:

Create a task execution role

The next step is creating a task execution role for the AWS OpenTelemetry
Collector.

###### To create a task execution role for AWS Distro for OpenTelemetry

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles** and then choose
   **Create role**.
3. In the list of services, choose **Elastic Container
   Service**.
4. Lower on the page, choose **Elastic Container Service Task**
   and then choose **Next: Permissions**.
5. In the list of policies, search for
   **AmazonECSTaskExecutionRolePolicy** and then select the check
   box next to **AmazonECSTaskExecutionRolePolicy**.
6. In the list of policies, search for
   **CloudWatchLogsFullAccess** and then select the check box next
   to **CloudWatchLogsFullAccess**.
7. In the list of policies, search for **AmazonSSMReadOnlyAccess**
   and then select the check box next to
   **AmazonSSMReadOnlyAccess**.
8. Choose **Next: Tags** and then choose **Next:
   Review.**
9. For **Role name** enter
   `AWSOpenTelemetryTaskExecutionRole` and then choose
   **Create role**.

## Step 3: Create

a task definition

The next step is creating a task definition.

###### To create a task definition for AWS Distro for OpenTelemetry

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**
3. Choose **Create new task definition**, **Create new
   task definition**.
4. For **Task definition family**, specify a unique name for the
   task definition.
5. Configure your containers, and then choose **Next**.
6. Under **Metrics and logging**, select **Use metric
   collection**.
7. Choose **Next**.
8. Choose **Create**.

For more information about using the AWS OpenTelemetry collector with Amazon ECS, see
[Setting up AWS Distro for
OpenTelemetry Collector in Amazon Elastic Container Service](https://aws-otel.github.io/docs/setup/ecs "https://aws-otel.github.io/docs/setup/ecs").

## Step 4: Run

the task

The final step is running the task that you've created.

###### To run the task for AWS Distro for OpenTelemetry

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the left navigation pane, choose **Task Definitions** and
   then select the task that you just created.
3. Choose **Actions**, **Deploy**, **Run
   task**.
4. Choose **Deploy**, **Run task**.
5. In the **Compute options** section, from **Existing
   cluster**, choose the cluster.
6. Choose **Create**.
7. Next, you can check for the new metrics in the CloudWatch console.
8. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
9. In the left navigation pane, choose **Metrics**.

You should see a **ECS/ContainerInsights** namespace. Choose
that namespace and you should see eight metrics.
