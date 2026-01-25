# Learn how to create an Amazon ECS

Windows task for Fargate

Get started with Amazon ECS on AWS Fargate by using Fargate for
your tasks in the Regions where Amazon ECS supports AWS Fargate.

Complete the following steps to get started with Amazon ECS on AWS Fargate.

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

You can create a new cluster called **windows** that uses the default
VPC.

###### To create a cluster with the AWS Management Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, for **Cluster
   name**, enter **windows**.
6. (Optional) To turn on Container Insights, expand **Monitoring**, and then
   turn on **Use Container Insights**.
7. (Optional) To help identify your cluster, expand **Tags**,
   and then configure your tags.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

[Remove a tag] Choose **Remove** to the right of the tag’s
Key and Value. 8. Choose **Create**.

## Step 2: Register a Windows

task definition

Before you can run Windows containers in your Amazon ECS cluster, you must register a task
definition. The following task definition example displays a simple webpage on port 8080
of a container instance with the `mcr.microsoft.com/windows/servercore/iis`
container image.

###### To register the sample task definition with the AWS Management Console

1. In the navigation pane, choose **Task definitions**.
2. Choose **Create new task definition**, **Create new
   task definition with JSON**.
3. Copy and paste the following example task definition into the box and then
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
                    "hostPort": 80,
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ],
    "memory": "4096",
    "cpu": "2048",
    "networkMode": "awsvpc",
    "family": "windows-simple-iis-2019-core",
    "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
    "runtimePlatform": {"operatingSystemFamily": "WINDOWS_SERVER_2019_CORE"},
    "requiresCompatibilities": ["FARGATE"]
}
```

4. Verify your information and choose **Create**.

## Step 3: Create a service with

your task definition

After you have registered your task definition, you can place tasks in your cluster
with it. The following procedure creates a service with your task definition and places
one task in your cluster.

###### To create a service from your task definition with the console

1. In the navigation pane, choose **Clusters**, and then select
   the cluster you created in [Step 1: Create a cluster](#create_fargate_windows_cluster-v2 "#create_fargate_windows_cluster-v2").
2. From the **Services** tab, choose
   **Create**.
3. Under **Deployment configuration**, specify how your
   application is deployed.
   1. For **Task definition**, choose the task definition
      you created in [Step 2: Register a Windows
      task definition](#register_fargate_windows_task_def_console "#register_fargate_windows_task_def_console").
   2. For **Service name**, enter a name for your
      service.
   3. For **Desired tasks**, enter
      **1**.

4. Under **Networking**, you can create a security group or
   choose an existing group. Ensure that the security group you use has the inbound
   rule listed under [Prerequisites](#first-run-prereqs-windows "#first-run-prereqs-windows").
5. Choose **Create**.

## Step 4: View your service

After your service has launched a task into your cluster, you can view the service and
open the IIS test page in a browser to verify that the container is running.

###### Note

It can take up to 15 minutes for your container instance to download and extract
the Windows container base layers.

###### To view your service

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. Choose the cluster where you ran the service.
4. In the **Services** tab, under **Service
   name**, choose the service you created in [Step 3: Create a service with
   your task definition](#create_fargate_windows_service_console "#create_fargate_windows_service_console").
5. Choose the **Tasks** tab, and then choose the task in your
   service.
6. On the task page, in the
   **Configuration** section, under **Public
   IP**, choose **Open address**.

## Step 5: Clean Up

When you are finished using an Amazon ECS cluster, you should clean up the resources
associated with it to avoid incurring charges for resources that you are not
using.

Some Amazon ECS resources, such as tasks, services, clusters, and container instances,
are cleaned up using the Amazon ECS console. Other resources, such as Amazon EC2 instances,
Elastic Load Balancing load balancers, and Auto Scaling groups, must be cleaned up manually in the Amazon EC2
console or by deleting the CloudFormation stack that created them.

1. In the navigation pane, choose **Clusters**.
2. On the **Clusters** page, select the cluster you created for
   this tutorial.
3. Choose the **Services** tab.
4. Select the service, and then choose **Delete**.
5. At the confirmation prompt, enter **delete** and then choose
   **Delete**.

Wait until the service is deleted. 6. Choose **Delete Cluster**. At the confirmation prompt, enter
**delete `cluster-name`**, and
then choose **Delete**. Deleting the cluster cleans up the
associated resources that were created with the cluster, including Auto Scaling groups,
VPCs, or load balancers.
