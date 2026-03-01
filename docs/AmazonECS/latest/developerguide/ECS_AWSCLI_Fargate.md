# Creating an Amazon ECS Linux task for the Fargate with the AWS CLI

The following steps help you set up a cluster, register a task definition, run a Linux
task, and perform other common scenarios in Amazon ECS with the AWS CLI. Use
the latest version of the AWS CLI. For more information on how to upgrade to the latest
version, see [Installing or updating to the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

###### Topics

- [Prerequisites](#ECS_AWSCLI_Fargate_prereq "#ECS_AWSCLI_Fargate_prereq")
- [Step 1: Create a Cluster](#ECS_AWSCLI_Fargate_create_cluster "#ECS_AWSCLI_Fargate_create_cluster")
- [Step 2: Register a Linux Task Definition](#ECS_AWSCLI_Fargate_register_task_definition "#ECS_AWSCLI_Fargate_register_task_definition")
- [Step 3: List Task Definitions](#ECS_AWSCLI_Fargate_list_task_definitions "#ECS_AWSCLI_Fargate_list_task_definitions")
- [Step 4: Create a Service](#ECS_AWSCLI_Fargate_create_service "#ECS_AWSCLI_Fargate_create_service")
- [Step 5: List Services](#ECS_AWSCLI_Fargate_list_services "#ECS_AWSCLI_Fargate_list_services")
- [Step 6: Describe the Running Service](#ECS_AWSCLI_Fargate_describe_service "#ECS_AWSCLI_Fargate_describe_service")
- [Step 7: Test](#ECS_AWSCLI_Fargate_test "#ECS_AWSCLI_Fargate_test")
- [Step 8: Clean Up](#ECS_AWSCLI_Fargate_clean_up "#ECS_AWSCLI_Fargate_clean_up")

## Prerequisites

This tutorial assumes that the following prerequisites have been completed.

- The latest version of the AWS CLI is installed and configured. For more
  information about installing or upgrading your AWS CLI, [Installing or updating to the
  latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") have been completed.
- Your IAM user has the required permissions specified in the [AmazonECS_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess")
  IAM policy example.
- You have a VPC and security group created to use. This tutorial uses a
  container image hosted on Amazon ECR Public so your task must have internet access. To
  give your task a route to the internet, use one of the following options.

      + Use a private subnet with a NAT gateway that has an elastic IP
       address.
      + Use a public subnet and assign a public IP address to the task.

  For more information, see [Create a virtual private cloud](get-set-up-for-amazon-ecs.md#create-a-vpc "get-set-up-for-amazon-ecs.md#create-a-vpc").

For information about security groups and rules, see, [Default security groups for your VPCs](../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup "../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup") and [Example rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#security-group-rule-examples "../../../vpc/latest/userguide/VPC_SecurityGroups.md#security-group-rule-examples") in the _Amazon Virtual Private Cloud User
Guide_.

- If you follow this tutorial using a private subnet, you can use Amazon ECS Exec to
  directly interact with your container and test the deployment. You will need to
  create a task IAM role to use ECS Exec. For more information on the task IAM
  role and other prerequisites, see [Monitor Amazon ECS containers with Amazon ECS Exec](ecs-exec.md "ecs-exec.md").
- (Optional) AWS CloudShell is a tool that gives customers a command line without
  needing to create their own EC2 instance. For more information, see [What is AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in
  the _AWS CloudShell User Guide_.

## Step 1: Create a Cluster

By default, your account receives a `default` cluster.

###### Note

The benefit of using the `default` cluster that is provided for you is
that you don't have to specify the `--cluster
 `cluster_name`` option in the subsequent
 commands. If you do create your own, non-default, cluster, you must specify
 `--cluster `cluster_name`` for each command
that you intend to use with that cluster.

Create your own cluster with a unique name with the following command:

```
`aws ecs create-cluster --cluster-name `fargate-cluster``
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
        "clusterName": "fargate-cluster",
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
        "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/`fargate-cluster`"
    }
}
```

## Step 2: Register a Linux Task Definition

Before you can run a task on your ECS cluster, you must register a task definition.
Task definitions are lists of containers grouped together. The following example is a
simple task definition that creates a PHP web app using the httpd container image hosted
on Docker Hub. For more information about the available task definition parameters, see
[Amazon ECS task definitions](task_definitions.md "task_definitions.md"). For this
tutorial, the `taskRoleArn` is only needed if you are deploying the task in a
private subnet and wish to test the deployment. Replace the `taskRoleArn`
with the IAM task role you created to use ECS Exec as mentioned in [Prerequisites](#ECS_AWSCLI_Fargate_prereq "#ECS_AWSCLI_Fargate_prereq").

```
 {
        "family": "sample-fargate",
        "networkMode": "awsvpc",
        `"taskRoleArn": "arn:aws:iam::aws_account_id:role/execCommandRole",`
        "containerDefinitions": [
            {
                "name": "fargate-app",
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
                    "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
                ]
            }
        ],
        "requiresCompatibilities": [
            "FARGATE"
        ],
        "cpu": "256",
        "memory": "512"
}
```

Save the task definition JSON as a file and pass it with the
``--cli-input-json`
 file://`path_to_file.json`` option.

To use a JSON file for container definitions:

```
`aws ecs register-task-definition --cli-input-json `file://$HOME/tasks/fargate-task.json``
```

The **register-task-definition** command returns a description of the
task definition after it completes its registration.

## Step 3: List Task Definitions

You can list the task definitions for your account at any time with the
**list-task-definitions** command. The output of this command shows
the `family` and `revision` values that you can use together when
calling **run-task** or **start-task**.

```
`aws ecs list-task-definitions`
```

Output:

```
{
    "taskDefinitionArns": [
        "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-fargate:1"
    ]
}
```

## Step 4: Create a Service

After you have registered a task for your account, you can create a service for the
registered task in your cluster. For this example, you create a service with one
instance of the `sample-fargate:1` task definition running in your cluster.
The task requires a route to the internet, so there are two ways you can achieve this.
One way is to use a private subnet configured with a NAT gateway with an elastic IP
address in a public subnet. Another way is to use a public subnet and assign a public IP
address to your task. We provide both examples below.

Example using a private subnet. The `enable-execute-command` option is
needed to use Amazon ECS Exec.

```
`aws ecs create-service --cluster `fargate-cluster` --service-name `fargate-service` --task-definition `sample-fargate:1` --desired-count `1` --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[`subnet-abcd1234`],securityGroups=[`sg-abcd1234`]}" --enable-execute-command`
```

Example using a public subnet.

```
`aws ecs create-service --cluster `fargate-cluster` --service-name `fargate-service` --task-definition `sample-fargate:1` --desired-count `1` --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[`subnet-abcd1234`],securityGroups=[`sg-abcd1234`],assignPublicIp=`ENABLED`}"`
```

The **create-service** command returns a description of the task
definition after it completes its registration.

## Step 5: List Services

List the services for your cluster. You should see the service that you created in the
previous section. You can take the service name or the full ARN that is returned from
this command and use it to describe the service later.

```
`aws ecs list-services --cluster `fargate-cluster``
```

Output:

```
{
    "serviceArns": [
        "arn:aws:ecs:`region`:`aws_account_id`:service/fargate-cluster/fargate-service"
    ]
}
```

## Step 6: Describe the Running Service

Describe the service using the service name retrieved earlier to get more information
about the task.

```
`aws ecs describe-services --cluster `fargate-cluster` --services `fargate-service``
```

If successful, this will return a description of the service failures and services.
For example, in the `services` section, you will find information on
deployments, such as the status of the tasks as running or pending. You may also find
information on the task definition, the network configuration and time-stamped events.
In the failures section, you will find information on failures, if any, associated with
the call. For troubleshooting, see [Service Event Messages](service-event-messages.md "service-event-messages.md"). For more information about the service description,
see [Describe Services](../APIReference/API_DescribeServices.md "../APIReference/API_DescribeServices.md").

```
{
    "services": [
        {
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
            "launchType": "FARGATE",
            "enableECSManagedTags": false,
            "loadBalancers": [],
            "deploymentController": {
                "type": "ECS"
            },
            "desiredCount": 1,
            "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/fargate-cluster",
            "serviceArn": "arn:aws:ecs:`region`:`aws_account_id`:service/fargate-service",
            "deploymentConfiguration": {
                "maximumPercent": 200,
                "minimumHealthyPercent": 100
            },
            "createdAt": 1692283199.771,
            "schedulingStrategy": "REPLICA",
            "placementConstraints": [],
            "deployments": [
                {
                    "status": "PRIMARY",
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
                    "pendingCount": 0,
                    "launchType": "FARGATE",
                    "createdAt": 1692283199.771,
                    "desiredCount": 1,
                    "taskDefinition": "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-fargate:1",
                    "updatedAt": 1692283199.771,
                    "platformVersion": "1.4.0",
                    "id": "ecs-svc/9223370526043414679",
                    "runningCount": 0
                }
            ],
            "serviceName": "fargate-service",
            "events": [
                {
                    "message": "(service fargate-service) has started 2 tasks: (task 53c0de40-ea3b-489f-a352-623bf1235f08) (task d0aec985-901b-488f-9fb4-61b991b332a3).",
                    "id": "92b8443e-67fb-4886-880c-07e73383ea83",
                    "createdAt": 1510811841.408
                },
                {
                    "message": "(service fargate-service) has started 2 tasks: (task b4911bee-7203-4113-99d4-e89ba457c626) (task cc5853e3-6e2d-4678-8312-74f8a7d76474).",
                    "id": "d85c6ec6-a693-43b3-904a-a997e1fc844d",
                    "createdAt": 1510811601.938
                },
                {
                    "message": "(service fargate-service) has started 2 tasks: (task cba86182-52bf-42d7-9df8-b744699e6cfc) (task f4c1ad74-a5c6-4620-90cf-2aff118df5fc).",
                    "id": "095703e1-0ca3-4379-a7c8-c0f1b8b95ace",
                    "createdAt": 1510811364.691
                }
            ],
            "runningCount": 0,
            "status": "ACTIVE",
            "serviceRegistries": [],
            "pendingCount": 0,
            "createdBy": "arn:aws:iam::`aws_account_id`:user/`user_name`",
            "platformVersion": "LATEST",
            "placementStrategy": [],
            "propagateTags": "NONE",
            "roleArn": "arn:aws:iam::`aws_account_id`:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
            "taskDefinition": "arn:aws:ecs:`region`:`aws_account_id`:task-definition/sample-fargate:1"
        }
    ],
    "failures": []
}
```

## Step 7: Test

### Testing task deployed using public subnet

Describe the task in the service so that you can get the Elastic Network Interface
(ENI) for the task.

First, get the task ARN.

```
`aws ecs list-tasks --cluster `fargate-cluster` --service `fargate-service``
```

The output contains the task ARN.

```
{
    "taskArns": [
        **"arn:aws:ecs:us-east-1:123456789012:task/fargate-service/EXAMPLE**
    ]
}
```

Describe the task and locate the ENI ID. Use the task ARN for the
`tasks` parameter.

```
`aws ecs describe-tasks --cluster `fargate-cluster` --tasks `arn:aws:ecs:us-east-1:123456789012:task/service/EXAMPLE``
```

The attachment information is listed in the output.

```
{
    "tasks": [
        {
            "attachments": [
                {
                    "id": "d9e7735a-16aa-4128-bc7a-b2d5115029e9",
                    "type": "ElasticNetworkInterface",
                    "status": "ATTACHED",
                    "details": [
                        {
                            "name": "subnetId",
                            "value": "subnetabcd1234"
                        },
                        {
                            "name": "networkInterfaceId",
                            "value": "**eni-0fa40520aeEXAMPLE**"
                        },
                    ]
                }
…
}
```

Describe the ENI to get the public IP address.

```
`aws ec2 describe-network-interfaces --network-interface-id `eni-0fa40520aeEXAMPLE``
```

The public IP address is in the output.

```
{
    "NetworkInterfaces": [
        {
            "Association": {
                "IpOwnerId": "amazon",
                "PublicDnsName": "ec2-34-229-42-222.compute-1.amazonaws.com",
                "PublicIp": "**198.51.100.2**"
            },
…
}

```

Enter the public IP address in your web browser and you should see a webpage that
displays the **Amazon ECS** sample application.

### Testing task deployed using private subnet

Describe the task and locate `managedAgents` to verify that the
`ExecuteCommandAgent` is running. Note the
`privateIPv4Address` for later use.

```
`aws ecs describe-tasks --cluster `fargate-cluster` --tasks `arn:aws:ecs:us-east-1:123456789012:task/fargate-service/EXAMPLE``
```

The managed agent information is listed in the output.

```
{
     "tasks": [
        {
            "attachments": [
                {
                    "id": "d9e7735a-16aa-4128-bc7a-b2d5115029e9",
                    "type": "ElasticNetworkInterface",
                    "status": "ATTACHED",
                    "details": [
                        {
                            "name": "subnetId",
                            "value": "subnetabcd1234"
                        },
                        {
                            "name": "networkInterfaceId",
                            "value": "eni-0fa40520aeEXAMPLE"
                        },
                        {
                            "name": "privateIPv4Address",
                            "value": "`10.0.143.156`"
                        }
                    ]
                }
            ],
     ...
     "containers": [
         {
         ...
        "managedAgents": [
                        {
                            "lastStartedAt": "2023-08-01T16:10:13.002000+00:00",
                            "name": "ExecuteCommandAgent",
                            "lastStatus": "RUNNING"
                        }
                ],
        ...
    }
```

After verifying that the `ExecuteCommandAgent` is running, you can
run the following command to run an interactive shell on the container in the task.

```
  `aws ecs execute-command --cluster `fargate-cluster` \
 --task  `arn:aws:ecs:us-east-1:123456789012:task/fargate-service/EXAMPLE`  \
 --container  `fargate-app` \
 --interactive \
 --command "/bin/sh"`
```

After the interactive shell is running, run the following commands to install
cURL.

```
`apt update`
```

```
`apt install curl`
```

After installing cURL, run the following command using the private IP address you
obtained earlier.

```
 `curl `10.0.143.156``
```

You should see the HTML equivalent of the **Amazon ECS** sample application webpage.

```
<html>
    <head>
     <title>Amazon ECS Sample App</title>
     <style>body {margin-top: 40px; background-color: #333;} </style>
    </head>
      <body>
      <div style=color:white;text-align:center>
      <h1>Amazon ECS Sample App</h1>
      <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>
      </div>
      </body>
</html>
```

## Step 8: Clean Up

When you are finished with this tutorial, you should clean up the associated resources
to avoid incurring charges for unused resources.

Delete the service.

```
`aws ecs delete-service --cluster `fargate-cluster` --service `fargate-service` --force`
```

Delete the cluster.

```
`aws ecs delete-cluster --cluster `fargate-cluster``
```
