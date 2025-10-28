# Learn how to create a task for

Amazon ECS Managed Instances

Learn how to use Amazon ECS with Amazon ECS Managed Instances to run a containerized
application.

## Prerequisites

Complete the following before you start the tutorial:

- You've completed the steps in [Set up
  to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").
- The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") have been completed.
- You have the required IAM roles for Amazon ECS Managed Instances. This includes:
  - Infrastructure role - Allows Amazon ECS to make calls
    to AWS services on your behalf to manage Amazon ECS Managed Instances infrastructure.

  For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
  - Instance profile - Provides permissions for the
    Amazon ECS container agent and Docker daemon running on managed instances.

  The instance role name must include `ecsInstanceRole` as a
  prefix to match the `iam:PassRole` action in the
  infrastructure role.

  For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md "managed-instances-instance-profile.md").

- You have a VPC and security group created to use. This tutorial uses a container image hosted on Amazon ECR Public so your instances must have internet access. To give your instances a route to the internet, use one of the following options:

      + Use a private subnet with a NAT gateway that has an elastic IP address.
      + Use a public subnet and assign a public IP address to the instances.

  For more information, see [Create a virtual private cloud](get-set-up-for-amazon-ecs.md#create-a-vpc "get-set-up-for-amazon-ecs.md#create-a-vpc").

For information about security groups and rules, see [Default security groups for your VPCs](../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup "../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup") and [Example rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#security-group-rule-examples "../../../vpc/latest/userguide/VPC_SecurityGroups.md#security-group-rule-examples") in the _Amazon Virtual Private Cloud User Guide_.

- (Optional) AWS CloudShell is a tool that gives customers a command line without needing to create their own EC2 instance. For more information, see [What is AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in the _AWS CloudShell User Guide_.

## Step 1: Create a cluster

1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create cluster**.
5. Under **Cluster configuration**, for **Cluster name**, enter a unique name for your cluster.
6. Under **Infrastructure**, choose **Fargate and Managed
   EC2**.
7. Configure the Managed Instances settings:
   1. For **Infrastructure role**, select the IAM role you created for Managed Instances infrastructure management.
   2. For **Instance profile**, select the `ecsInstanceRole` you created.
   3. For **Instance attributes**, choose **Use ECS
      defaults**.

8. Under **Networking**, configure the VPC and subnets for your Managed Instances:
   1. For **VPC**, select the VPC that hosts the Managed
      Instances.
   2. For **Subnets**, select one or more subnets where your Managed Instances will be launched.
   3. For **Security groups**, select one or more security
      groups.

9. (Optional) To add tags to your cluster, expand **Tags**, and then configure your tags.
10. Choose **Create**.

## Step 2: Create a task definition

A task definition is a blueprint for your application. Each time you launch a task in Amazon ECS, you specify a task definition. The service then knows which Docker image to use for containers, how many containers to use in the task, and the resource allocation for each container. Follow these steps to create a task definition:

1. In the navigation pane, choose **Task Definitions**.
2. Choose **Create new task definition**, **Create new task definition with JSON**.
3. Copy and paste the following JSON into the editor, replacing the pre-populated JSON:

Replace `account-id` with your AWS account ID and `region` with the Region you're using.

```
{
  "family": "managed-instance-tutorial",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::account-id:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "sample-app",
      "image": "public.ecr.aws/docker/library/httpd:latest",
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
          "awslogs-group": "/ecs/managed-instance-tutorial",
          "awslogs-region": "region",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": [
    "MANAGED_INSTANCES"
  ],
  "cpu": "1024",
  "memory": "2048"
}
```

4. Choose **Create**.

## Step 3: Create a service

An Amazon ECS service allows you to run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster. Follow these steps to create a service:

1. In the navigation pane, choose **Clusters**, and then select the `managed-instance-tutorial` cluster.
2. From the **Services** tab, choose **Create**.
3. For **Task definition family**, choose **managed-instance-tutorial**.
4. For **Service name**, enter `managed-instance-tutorial-service`.
5. Under **Environment**, Choose **Capacity provider strategy**.
6. Under **Networking**, configure the following:
   1. Choose an existing VPC or create a new one.
   2. For **Subnets**, choose the subnets to use.
   3. For **Security groups**, either choose an existing security group or create a new one that allows inbound traffic on port 80.

7. Choose **Create**.

## Step 4: View your service

After your service has launched, you can view it to learn more about it and test it.

1. Choose the `managed-instance-tutorial-service` service.
2. From the **Tasks** tab, choose the task ID of the running task.
3. Under **Network**, in **Public IP**, choose **Open address**.
4. You should see the Apache HTTP Server test page, which confirms that the web server is running properly.

## Step 5: Clean up

When you're finished with this tutorial, you should clean up the associated resources to avoid incurring charges for resources that you're not using.

1. In the navigation pane, choose **Clusters**.
2. On the **Clusters** page, select the `managed-instance-tutorial` cluster.
3. Choose the **Services** tab.
4. Select the `managed-instance-tutorial-service` service, and then choose **Delete**.
5. At the confirmation prompt, enter `delete` and then choose **Delete**.
6. After the service is deleted, choose **Clusters** in the navigation pane.
7. On the **Clusters** page, select the `managed-instance-tutorial` cluster, and then choose **Delete cluster**.
8. At the confirmation prompt, enter `delete managed-instance-tutorial` and then choose **Delete**.
