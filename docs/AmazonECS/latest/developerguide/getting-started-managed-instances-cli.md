# Learn how to create a task for

Amazon ECS Managed Instances with the AWS CLI

The following steps help you set up a cluster, create a capacity provider, register a
task definition, run a Linux task, and perform other common scenarios in Amazon ECS with
Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on
how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS
AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

###### Topics

- [Prerequisites](#managed-instances-cli-prereq "#managed-instances-cli-prereq")
- [Step 1: Create a cluster](#managed-instances-cli-create-cluster "#managed-instances-cli-create-cluster")
- [Step 2: Create a Amazon ECS Managed Instances capacity provider](#managed-instances-cli-create-capacity-provider "#managed-instances-cli-create-capacity-provider")
- [Step 3: Configure the cluster's default capacity provider strategy](#managed-instances-cli-configure-cluster "#managed-instances-cli-configure-cluster")
- [Step 4: Register a
  Linux task definition](#managed-instances-cli-register-task-definition "#managed-instances-cli-register-task-definition")
- [Step 5: List task
  definitions](#managed-instances-cli-list-task-definitions "#managed-instances-cli-list-task-definitions")
- [Step 6: Create a service](#managed-instances-cli-create-service "#managed-instances-cli-create-service")
- [Step 7: List services](#managed-instances-cli-list-services "#managed-instances-cli-list-services")
- [Step 8: Describe the running
  service](#managed-instances-cli-describe-service "#managed-instances-cli-describe-service")
- [Step 9: Test](#managed-instances-cli-test "#managed-instances-cli-test")
- [Step 10: Clean up](#managed-instances-cli-clean-up "#managed-instances-cli-clean-up")

## Prerequisites

Complete the following before you start the tutorial:

- You've completed the steps in [Set up
  to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").
- The latest version of the AWS CLI is installed and configured. For more
  information about installing or upgrading the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in
  the _AWS Command Line Interface User Guide_.
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

By default, your account receives a `default` cluster.

###### Note

The benefit of using the `default` cluster that is provided for you is that you don't have to specify the `--cluster `cluster_name`` option in the subsequent commands. If you do create your own, non-default, cluster, you must specify `--cluster `cluster_name`` for each command that you intend to use with that cluster.

Create your own cluster with a unique name with the following command:

```
aws ecs create-cluster --cluster-name `managed-instances-cluster`
```

Output:

```
{
    "cluster": {
        "status": "ACTIVE",
        "defaultCapacityProviderStrategy": [],
        "statistics": [],
        "capacityProviders": [],
        "tags": [],
        "clusterName": "managed-instances-cluster",
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "registeredContainerInstancesCount": 0,
        "pendingTasksCount": 0,
        "runningTasksCount": 0,
        "activeServicesCount": 0,
        "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/managed-instances-cluster"
    }
}
```

## Step 2: Create a Amazon ECS Managed Instances capacity provider

Before you can run tasks using Amazon ECS Managed Instances, you must create a capacity provider that defines the infrastructure configuration. The capacity provider specifies the IAM roles, network configuration, and other settings for your managed instances.

Create a JSON file with your capacity provider configuration. Replace the placeholder values with your actual resource identifiers:

```
{
    "name": "managed-instances-cp",
    "cluster": "managed-instances-cluster",
    "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::`aws_account_id`:role/`ecsInfrastructureRole`",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::`aws_account_id`:instance-profile/`ecsInstanceRole`",
            "networkConfiguration": {
                "subnets": [
                    "`subnet-abcdef01234567890`",
                    "`subnet-1234567890abcdef0`"
                ],
                "securityGroups": [
                    "`sg-0123456789abcdef0`"
                ]
            },
            "storageConfiguration": {
                "storageSizeGiB": 100
            },
            "monitoring": "basic"
        }
    }
}
```

Save this configuration as `managed-instances-cp.json` and create the capacity provider:

```
aws ecs create-capacity-provider --cli-input-json file://managed-instances-cp.json
```

The command returns a description of the capacity provider after it completes its creation.

## Step 3: Configure the cluster's default capacity provider strategy

Update the cluster to use the Amazon ECS Managed Instances capacity provider as the default capacity provider strategy. This allows tasks and services to automatically use Amazon ECS Managed Instances without explicitly specifying the capacity provider.

Create a JSON file with the cluster capacity provider configuration:

```
{
    "cluster": "managed-instances-cluster",
    "capacityProviders": [
        "managed-instances-cp"
    ],
    "defaultCapacityProviderStrategy": [
        {
            "capacityProvider": "managed-instances-cp",
            "weight": 1
        }
    ]
}
```

Save this configuration as `cluster-cp-strategy.json` and update the cluster:

```
aws ecs put-cluster-capacity-providers --cli-input-json file://cluster-cp-strategy.json
```

## Step 4: Register a

Linux task definition

Before you can run a task on your cluster, you must register a task definition. Task
definitions are lists of containers grouped together. The following example is a simple
task definition that creates a PHP web app using the httpd container image hosted on
Docker Hub. For more information about the available task definition parameters, see
[Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md").

```
{
    "family": "sample-managed-instances",
    "networkMode": "awsvpc",
    "containerDefinitions": [
        {
            "name": "managed-instances-app",
            "image": "public.ecr.aws/docker/library/httpd:latest",
            "portMappings": [
                {
                    "containerPort": 80,
                    "hostPort": 80,
                    "protocol": "tcp"
                }
            ],
            "essential": true,
            "entryPoint": [
                "sh",
                "-c"
            ],
            "command": [
                "/bin/sh -c \"echo '<html><head><title>Amazon ECS Sample App</title><style>body {margin-top: 40px; background-color: #333;} </style></head><body><div style=color:white;text-align:center><h1>Amazon ECS Sample App</h1><h2>Congratulations!</h2><p>Your application is now running on a container in Amazon ECS using Amazon ECS Managed Instances.</p></div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
            ]
        }
    ],
    "requiresCompatibilities": [
        "MANAGED_INSTANCES"
    ],
    "cpu": "256",
    "memory": "512"
}
```

Save the task definition JSON as a file and pass it with the `--cli-input-json file://`path_to_file.json`` option.

To use a JSON file for container definitions:

```
aws ecs register-task-definition --cli-input-json file://$HOME/tasks/managed-instances-task.json
```

The **register-task-definition** command returns a description of the task definition after it completes its registration.

## Step 5: List task

definitions

You can list the task definitions for your account at any time with the **list-task-definitions** command. The output of this command shows the `family` and `revision` values that you can use together when calling **run-task** or **start-task**.

```
aws ecs list-task-definitions
```

Output:

```
{
    "taskDefinitionArns": [
        "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-managed-instances:1"
    ]
}
```

## Step 6: Create a service

After you have registered a task for your account, you can create a service for the registered task in your cluster. For this example, you create a service with one instance of the `sample-managed-instances:1` task definition running in your cluster. The task requires a route to the internet, so there are two ways you can achieve this. One way is to use a private subnet configured with a NAT gateway with an elastic IP address in a public subnet. Another way is to use a public subnet and assign a public IP address to your task. We provide both examples below.

Example using a private subnet:

```
aws ecs create-service --cluster `managed-instances-cluster` --service-name `managed-instances-service` --task-definition sample-managed-instances:1 --desired-count 1 --network-configuration "awsvpcConfiguration={subnets=[`subnet-abcd1234`],securityGroups=[`sg-abcd1234`]}"
```

Example using a public subnet:

```
aws ecs create-service --cluster `managed-instances-cluster` --service-name `managed-instances-service` --task-definition sample-managed-instances:1 --desired-count 1 --network-configuration "awsvpcConfiguration={subnets=[`subnet-abcd1234`],securityGroups=[`sg-abcd1234`],assignPublicIp=ENABLED}"
```

The **create-service** command returns a description of the service after it completes its creation.

## Step 7: List services

List the services for your cluster. You should see the service that you created in the previous section. You can take the service name or the full ARN that is returned from this command and use it to describe the service later.

```
aws ecs list-services --cluster managed-instances-cluster
```

Output:

```
{
    "serviceArns": [
        "arn:aws:ecs:`region`:`aws_account_id`:service/managed-instances-cluster/managed-instances-service"
    ]
}
```

## Step 8: Describe the running

service

Describe the service using the service name retrieved earlier to get more information about the task.

```
aws ecs describe-services --cluster managed-instances-cluster --services managed-instances-service
```

If successful, this will return a description of the service failures and services.
For example, in the `services` section, you will find information on
deployments, such as the status of the tasks as running or pending. You may also find
information on the task definition, the network configuration and time-stamped events.
In the failures section, you will find information on failures, if any, associated with
the call.

The output will show that the service is using the Amazon ECS Managed Instances capacity provider:

```
{
    "services": [
        {
            "capacityProviderStrategy": [
                {
                    "capacityProvider": "managed-instances-cp",
                    "weight": 1,
                    "base": 0
                }
            ],
            "networkConfiguration": {
                "awsvpcConfiguration": {
                    "subnets": [
                        "`subnet-abcd1234`"
                    ],
                    "securityGroups": [
                        "`sg-abcd1234`"
                    ],
                    "assignPublicIp": "ENABLED"
                }
            },
            "enableECSManagedTags": false,
            "loadBalancers": [],
            "deploymentController": {
                "type": "ECS"
            },
            "desiredCount": 1,
            "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/managed-instances-cluster",
            "serviceArn": "arn:aws:ecs:`region`:`aws_account_id`:service/managed-instances-service",
            "serviceName": "managed-instances-service",
            "taskDefinition": "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-managed-instances:1"
        }
    ],
    "failures": []
}
```

## Step 9: Test

To test your deployment, you need to find the public IP address of the managed instance running your task.

### Testing task deployed using public subnet

First, get the task ARN from your service:

```
aws ecs list-tasks --cluster managed-instances-cluster --service managed-instances-service
```

The output contains the task ARN:

```
{
    "taskArns": [
        "arn:aws:ecs:`region`:`aws_account_id`:task/managed-instances-cluster/`EXAMPLE`"
    ]
}
```

Describe the task to get the container instance ARN. Use the task ARN for the `tasks` parameter:

```
aws ecs describe-tasks --cluster managed-instances-cluster --tasks arn:aws:ecs:`region`:`aws_account_id`:task/managed-instances-cluster/`EXAMPLE`
```

The output shows the task is running on Amazon ECS Managed Instances and includes the container instance ARN:

```
{
    "tasks": [
        {
            "launchType": "MANAGED_INSTANCES",
            "capacityProviderName": "managed-instances-cp",
            "containerInstanceArn": "arn:aws:ecs:`region`:`aws_account_id`:container-instance/managed-instances-cluster/`CONTAINER_INSTANCE_ID`",
            "taskArn": "arn:aws:ecs:`region`:`aws_account_id`:task/managed-instances-cluster/`EXAMPLE`",
            "taskDefinitionArn": "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-managed-instances:1"
        }
    ]
}
```

Describe the container instance to get the EC2 instance ID:

```
aws ecs describe-container-instances --cluster managed-instances-cluster --container-instances `CONTAINER_INSTANCE_ID`
```

The output includes the EC2 instance ID:

```
{
    "containerInstances": [
        {
            "ec2InstanceId": "`i-1234567890abcdef0`",
            "capacityProviderName": "managed-instances-cp",
            "containerInstanceArn": "arn:aws:ecs:`region`:`aws_account_id`:container-instance/managed-instances-cluster/`CONTAINER_INSTANCE_ID`"
        }
    ]
}
```

Describe the EC2 instance to get the public IP address:

```
aws ec2 describe-instances --instance-ids `i-1234567890abcdef0`
```

The public IP address is in the output:

```
{
    "Reservations": [
        {
            "Instances": [
                {
                    "PublicIpAddress": "`198.51.100.2`",
                    "InstanceId": "`i-1234567890abcdef0`"
                }
            ]
        }
    ]
}
```

Enter the public IP address in your web browser and you should see a webpage that displays the **Amazon ECS** sample application running on Amazon ECS Managed Instances.

### Testing task deployed using private subnet

For tasks deployed in private subnets, you can use Amazon ECS Exec to connect to the container and test the deployment from within the instance. Follow the same steps as above to get the task ARN, then use ECS Exec:

```
aws ecs execute-command --cluster managed-instances-cluster \
    --task arn:aws:ecs:`region`:`aws_account_id`:task/managed-instances-cluster/`EXAMPLE` \
    --container managed-instances-app \
    --interactive \
    --command "/bin/sh"
```

After the interactive shell is running, you can test the web server:

```
curl localhost
```

You should see the HTML equivalent of the **Amazon ECS** sample application webpage.

## Step 10: Clean up

When you are finished with this tutorial, you should clean up the associated resources to avoid incurring charges for unused resources.

Delete the service:

```
aws ecs delete-service --cluster managed-instances-cluster --service managed-instances-service --force
```

Wait for the service to be deleted and all tasks to stop, then delete the capacity provider:

```
aws ecs delete-capacity-provider --capacity-provider managed-instances-cp
```

Delete the cluster:

```
aws ecs delete-cluster --cluster managed-instances-cluster
```

###### Note

The managed instances are automatically terminated when the capacity provider is
deleted. You don't need to manually terminate the EC2 instances.
