# Learn how to create an Amazon ECS Windows task for EC2

Get started with Amazon ECS using EC2 by registering a task
definition, creating a cluster, and creating a service in the console.

Complete the following steps to get started with Amazon ECS using the EC2 launch
type.

## Prerequisites

Before you begin, complete the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") and
that your IAM user has the permissions specified in the
`AdministratorAccess` IAM policy example.

The console attempts to automatically create the task execution IAM role, which
is required for Fargate tasks. To ensure that the console is able to
create this IAM role, one of the following must be true:

- Your user has administrator access. For more information, see [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").
- Your user has the IAM permissions to create a service role. For more
  information, see [Creating a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").
- A user with administrator access has manually created the task execution role
  so that it is available on the account to be used. For more information, see
  [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

###### Important

The security group you select when creating a service with your task definition must have port 80 open for inbound traffic. Add the
following inbound rule to your security group. For information about how to
create a security group, see [Create a security group for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/creating-security-group.md "../../../AWSEC2/latest/UserGuide/creating-security-group.md") in the _Amazon EC2 User Guide_.

- Type: HTTP
- Protocol: TCP
- Port range: 80
- Source: Anywhere (`0.0.0.0/0`)

## Step 1: Create a cluster

An Amazon ECS cluster is a logical grouping of tasks, services, and container instances.

The following steps walk you through creating a cluster with one Amazon EC2 instance
registered to it which will enable us to run a task on it. If a specific field is not
mentioned, leave the default console values.

###### To create a new cluster (Amazon ECS console)

Before you begin, assign the appropriate IAM permission. For more information, see
[Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies").

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, for **Cluster
   name**, enter a unique name.

The name can contain up to 255 letters (uppercase and lowercase), numbers, and
hyphens. 6. (Optional) To change the VPC and subnets where your tasks and services launch,
under **Networking**, perform any of the following
operations:

    * To remove a subnet, under **Subnets**, choose
     **X** for each subnet that you want to remove.
    * To change to a VPC other than the **default** VPC, under
     **VPC**, choose an existing **VPC**,
     and then under **Subnets**, select each subnet.

7. To add Amazon EC2 instances to your cluster, expand
   **Infrastructure**, and then select **Amazon EC2
   instances**. Next, configure the Amazon EC2 Auto Scaling group which acts as the capacity
   provider:
   1. To using an existing Amazon EC2 Auto Scaling group, from **Auto Scaling group
      (ASG)**, select the group.
   2. To create a Amazon EC2 Auto Scaling group, from **Auto Scaling group
      (ASG)**, select **Create new group**, and then
      provide the following details about the group:
      - For **Operating system/Architecture**, choose the
        Amazon ECS-optimized AMI for the Amazon EC2 Auto Scaling group instances.
      - For **EC2 instance type**, choose the instance
        type for your workloads. For more information about
        the different instance types, see [Amazon EC2 Instances](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

      Managed scaling works best if your Amazon EC2 Auto Scaling group uses the same or
      similar instance types.
      - For **SSH key pair**, choose the pair that proves
        your identity when you connect to the instance.
      - For **Capacity**, enter the minimum number and
        the maximum number of instances to launch in the Amazon EC2 Auto Scaling group. Amazon EC2 instances incur costs while they exist
        in your AWS resources. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

8. (Optional) To turn on Container Insights, expand **Monitoring**, and then
   turn on **Use Container Insights**.
9. (Optional) To manage the cluster tags, expand **Tags**, and
   then perform one of the following operations:

[Add a tag] Choose **Add tag** and do the
following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key
     value.

[Remove a tag] Choose **Remove** to the right of the tag’s Key and
Value. 10. Choose **Create**.

## Step 2: Register a task

definition

###### To register the sample task definition with the AWS Management Console

1. In the navigation pane, choose **Task Definitions**.
2. Choose **Create new task definition**, **Create new
   task definition with JSON**.
3. Copy and paste the following example task definition into the box, and then
   choose **Save**.

```
{
    "containerDefinitions": [
        {
            "command": ["New-Item -Path C:\\inetpub\\wwwroot\\index.html -Type file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>'; C:\\ServiceMonitor.exe w3svc"],
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "essential": true,
            "cpu": 2048,
            "memory": 4096,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "name": "sample_windows_app",
            "portMappings": [
                {
                    "hostPort": 443,
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ],
    "memory": "4096",
    "cpu": "2048",
    "family": "windows-simple-iis-2019-core",
    "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
    "runtimePlatform": {"operatingSystemFamily": "WINDOWS_SERVER_2019_CORE"},
    "requiresCompatibilities": ["EC2"]
}
```

4. Verify your information and choose **Create**.

## Step 3: Create a Service

An Amazon ECS service helps you to run and maintain a specified number of instances of a
task definition simultaneously in an Amazon ECS cluster. If any of your tasks should fail or
stop for any reason, the Amazon ECS service scheduler launches another instance of your task
definition to replace it in order to maintain the desired number of tasks in the
service. For more information on services, see [Amazon ECS services](ecs_services.md "ecs_services.md").

###### To create a service

1. In the navigation pane, choose **Clusters**.
2. Select the cluster you created in [Step 1: Create a cluster](#getting-started-ec2-cluster-v2 "#getting-started-ec2-cluster-v2").
3. On the **Services** tab, choose
   **Create**.
4. In the **Environment** section, do the following:
   1. For **Compute options**, choose Launch type.
   2. For **Launch type**, select
      **EC2**

5. In the **Deployment configuration** section, do the
   following:
   1. For **Family**, choose the task definition you
      created in [Step 2: Register a task
      definition](#getting-started-ec2-task-def-v2 "#getting-started-ec2-task-def-v2").
   2. For **Service name**, enter a name for your
      service.
   3. For **Desired tasks**, enter
      **1**.

6. Review the options and choose **Create**.
7. Choose **View service** to review your service.

## Step 4: View your Service

The service is a web-based application so you can view its containers with a web
browser.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. Choose the cluster where you ran the service.
4. In the **Services** tab, under **Service
   name**, choose the service you created in [Step 3: Create a Service](#getting-started-ec2-service-v2 "#getting-started-ec2-service-v2").
5. Choose the **Tasks** tab, and then choose the task in your
   service.
6. On the task page, in the **Configuration** section, under
   **Public IP**, choose **Open address**.
   The screen shot below is the expected output.

![Screen shot of the Amazon ECS sample application. The output indicates that "Your application is now running on Amazon ECS".](images/ECS_Sample_Application.png)

## Step 5: Clean Up

When you are finished using an Amazon ECS cluster, you should clean up the resources
associated with it to avoid incurring charges for resources that you are not
using.

Some Amazon ECS resources, such as tasks, services, clusters, and container instances,
are cleaned up using the Amazon ECS console. Other resources, such as Amazon EC2 instances,
ELB load balancers, and Amazon EC2 Auto Scaling groups, must be cleaned up manually in the Amazon EC2
console or by deleting the CloudFormation stack that created them.

1. In the navigation pane, choose **Clusters**.
2. On the **Clusters** page, select the cluster cluster you
   created for this tutorial.
3. Choose the **Services** tab.
4. Select the service, and then choose **Delete**.
5. At the confirmation prompt, enter **delete** and then choose
   **Delete**.

Wait until the service is deleted. 6. Choose **Delete Cluster**. At the confirmation prompt, enter
**delete `cluster-name`**, and
then choose **Delete**. Deleting the cluster cleans up the
associated resources that were created with the cluster, including Amazon EC2 Auto Scaling groups,
VPCs, or load balancers.
