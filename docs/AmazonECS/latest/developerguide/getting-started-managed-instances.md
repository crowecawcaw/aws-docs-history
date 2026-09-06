

# Learn how to create a task for Amazon ECS Managed Instances
<a name="getting-started-managed-instances"></a>

Learn how to use Amazon ECS with Amazon ECS Managed Instances to run a containerized application.

## Prerequisites
<a name="getting-started-prerequisites"></a>

 Complete the following before you start the tutorial: 
+ You've completed the steps in [Set up to use Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html).
+ The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md) have been completed.
+ You have the required IAM roles for Amazon ECS Managed Instances. This includes:
  + Infrastructure role - Allows Amazon ECS to make calls to AWS services on your behalf to manage Amazon ECS Managed Instances infrastructure.

    For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md).
  + Instance profile - Provides permissions for the Amazon ECS container agent and Docker daemon running on managed instances.

    The instance role name must include `ecsInstanceRole` as a prefix to match the `iam:PassRole` action in the infrastructure role. 

    For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md).
+ You have a VPC and security group created to use. This tutorial uses a container image hosted on Amazon ECR Public so your instances must have internet access. To give your instances a route to the internet, use one of the following options:
  + Use a private subnet with a NAT gateway that has an elastic IP address.
  + Use a public subnet and assign a public IP address to the instances.

  For more information, see [Create a virtual private cloud](get-set-up-for-amazon-ecs.md#create-a-vpc).

  For information about security groups and rules, see [Default security groups for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#DefaultSecurityGroup) and [Example rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#security-group-rule-examples) in the *Amazon Virtual Private Cloud User Guide*.
+ (Optional) AWS CloudShell is a tool that gives customers a command line without needing to create their own EC2 instance. For more information, see [What is AWS CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) in the *AWS CloudShell User Guide*.

## Step 1: Create a cluster
<a name="getting-started-step1"></a>

1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose **Create cluster**.

1. Under **Cluster configuration**, for **Cluster name**, enter a unique name for your cluster.

1. Under **Infrastructure**, choose **Fargate and Managed EC2**.

1. Configure the Managed Instances settings:

   1. For **Infrastructure role**, select the IAM role you created for Managed Instances infrastructure management.

   1. For **Instance profile**, select the `ecsInstanceRole` you created.

   1. For **Instance attributes**, choose **Use ECS defaults**.

1. Under **Networking**, configure the VPC and subnets for your Managed Instances:

   1. For **VPC**, select the VPC that hosts the Managed Instances.

   1. For **Subnets**, select one or more subnets where your Managed Instances will be launched.

   1. For **Security groups**, select one or more security groups.

1. (Optional) To add tags to your cluster, expand **Tags**, and then configure your tags.

1. Choose **Create**.

## Step 2: Create a task definition
<a name="getting-started-step2"></a>

A task definition is a blueprint for your application. Each time you launch a task in Amazon ECS, you specify a task definition. The service then knows which Docker image to use for containers, how many containers to use in the task, and the resource allocation for each container. Follow these steps to create a task definition:

1. In the navigation pane, choose **Task Definitions**.

1. Choose **Create new task definition**, **Create new task definition with JSON**.

1. Copy and paste the following JSON into the editor, replacing the pre-populated JSON:

   Replace **account-id** with your AWS account ID and **region** with the Region you're using.

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

1. Choose **Create**.

## Step 3: Create a service
<a name="getting-started-step3"></a>

An Amazon ECS service allows you to run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster. Follow these steps to create a service:

1. In the navigation pane, choose **Clusters**, and then select the **managed-instance-tutorial** cluster.

1. From the **Services** tab, choose **Create**.

1. For **Task definition family**, choose **managed-instance-tutorial**.

1. For **Service name**, enter **managed-instance-tutorial-service**.

1. Under **Environment**, Choose **Capacity provider strategy**.

1. Under **Networking**, configure the following:

   1. Choose an existing VPC or create a new one.

   1. For **Subnets**, choose the subnets to use.

   1. For **Security groups**, either choose an existing security group or create a new one that allows inbound traffic on port 80.

1. Choose **Create**.

## Step 4: View your service
<a name="getting-started-step4"></a>

After your service has launched, you can view it to learn more about it and test it.

1. Choose the **managed-instance-tutorial-service** service.

1. From the **Tasks** tab, choose the task ID of the running task.

1. Under **Network**, in **Public IP**, choose **Open address**.

1. You should see the Apache HTTP Server test page, which confirms that the web server is running properly.

## Step 5: Clean up
<a name="getting-started-step5"></a>

When you're finished with this tutorial, you should clean up the associated resources to avoid incurring charges for resources that you're not using.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, select the **managed-instance-tutorial** cluster.

1. Choose the **Services** tab.

1. Select the **managed-instance-tutorial-service** service, and then choose **Delete**.

1. At the confirmation prompt, enter **delete** and then choose **Delete**.

1. After the service is deleted, choose **Clusters** in the navigation pane.

1. On the **Clusters** page, select the **managed-instance-tutorial** cluster, and then choose **Delete cluster**.

1. At the confirmation prompt, enter **delete managed-instance-tutorial** and then choose **Delete**.