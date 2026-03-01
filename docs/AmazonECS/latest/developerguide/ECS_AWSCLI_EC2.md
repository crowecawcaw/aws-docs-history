# Creating an Amazon ECS task for EC2 with the AWS CLI

The following steps help you set up a cluster, register a task definition, run a task, and
perform other common scenarios in Amazon ECS with the AWS CLI. Use the latest version of the AWS CLI.
For more information on how to upgrade to the latest version, see [Installing
or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

###### Topics

- [Prerequisites](#AWSCLI_EC2_prereq "#AWSCLI_EC2_prereq")
- [Create a cluster](#AWSCLI_EC2_create_cluster "#AWSCLI_EC2_create_cluster")
- [Launch a container instance with the Amazon ECS AMI](#AWSCLI_EC2_launch_container_instance "#AWSCLI_EC2_launch_container_instance")
- [List container instances](#AWSCLI_EC2_list_container_instances "#AWSCLI_EC2_list_container_instances")
- [Describe your container instance](#AWSCLI_EC2_describe_container_instance "#AWSCLI_EC2_describe_container_instance")
- [Register a task definition](#AWSCLI_EC2_register_task_definition "#AWSCLI_EC2_register_task_definition")
- [List task definitions](#AWSCLI_EC2_list_task_definitions "#AWSCLI_EC2_list_task_definitions")
- [Create a service](#AWSCLI_EC2_run_task "#AWSCLI_EC2_run_task")
- [List services](#AWSCLI_EC2_list_tasks "#AWSCLI_EC2_list_tasks")
- [Describe the service](#AWSCLI_EC2_describe_service "#AWSCLI_EC2_describe_service")
- [Describe the running task](#AWSCLI_EC2_describe_task "#AWSCLI_EC2_describe_task")
- [Test the web server](#AWSCLI_EC2_test_web_server "#AWSCLI_EC2_test_web_server")
- [Clean up resources](#AWSCLI_EC2_clean_up_resources "#AWSCLI_EC2_clean_up_resources")

## Prerequisites

This tutorial assumes that the following prerequisites have been completed:

- The latest version of the AWS CLI is installed and configured. For more
  information about installing or upgrading your AWS CLI, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") have been completed.
- Your IAM user has the required permissions specified in the [AmazonECS_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess") IAM policy
  example.
- You have a container instance IAM role created to use. For more informaton, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
- You have a VPC created to use. For more information, see
  [Create a virtual private cloud](get-set-up-for-amazon-ecs.md#create-a-vpc "get-set-up-for-amazon-ecs.md#create-a-vpc").
- (Optional) AWS CloudShell is a tool that gives customers a command line without
  needing to create their own EC2 instance. For more information, see [What is AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in
  the _AWS CloudShell User Guide_.

## Create a cluster

By default, your account receives a `default` cluster when you launch your
first container instance.

###### Note

The benefit of using the `default` cluster that is provided for you is
that you don't have to specify the `--cluster
 `cluster_name`` option in the subsequent
 commands. If you do create your own, non-default, cluster, you must specify
 `--cluster `cluster_name`` for each command
that you intend to use with that cluster.

Create your own cluster with a unique name with the following command:

```
aws ecs create-cluster --cluster-name `MyCluster`
```

Output:

```
{
    "cluster": {
        "clusterName": "MyCluster",
        "status": "ACTIVE",
        "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/MyCluster"
    }
}
```

## Launch a container instance with the Amazon ECS AMI

Container instances are EC2 instances that run the Amazon ECS container agent and have
been registered into a cluster. In this section, you'll launch an EC2 instance using the
ECS-optimized AMI.

###### To launch a container instance with the AWS CLI

1. Retrieve the latest ECS-optimized Amazon Linux 2 AMI ID for your AWS Region using the following command. This command uses AWS Systems Manager Parameter Store to get the latest ECS-optimized
   AMI ID. The AMI includes the Amazon ECS container agent and Docker runtime
   pre-installed.

```
aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended --query 'Parameters[0].Value' --output text | jq -r '.image_id'
```

Output:

```
`ami-abcd1234`
```

2. Create a security group that allows SSH access for managing your container instance
   and HTTP access for the web server.

```
aws ec2 create-security-group --group-name `ecs-tutorial-sg` --description "ECS tutorial security group"
```

Output:

```
{
    "GroupId": "sg-abcd1234"
}
```

3. Add an inbound rule to the security group by running the following command.

```
aws ec2 authorize-security-group-ingress --group-id `sg-abcd1234` --protocol tcp --port 80 --cidr 0.0.0.0/0
```

Output:

```
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-efgh5678",
            "GroupId": "sg-abcd1234",
            "GroupOwnerId": "123456789012",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIpv4": "0.0.0.0/0"
        }
    ]
}
```

The security group now allows SSH access from the specified IP range and HTTP access
from anywhere. In a production environment, you should restrict SSH access to your
specific IP address and consider limiting HTTP access as needed. 4. Create an EC2 key pair for SSH access to your container instance.

```
aws ec2 create-key-pair --key-name `ecs-tutorial-key` --query 'KeyMaterial' --output text > ecs-tutorial-key.pem
chmod 400 ecs-tutorial-key.pem
```

The private key is saved to your local machine with appropriate permissions for SSH
access. 5. Launch an EC2 instance using the ECS-optimized AMI and configure it to join your
cluster.

```
aws ec2 run-instances --image-id `ami-abcd1234` --instance-type `t3.micro` --key-name `ecs-tutorial-key` --security-group-ids `sg-abcd1234` --iam-instance-profile Name=ecsInstanceRole --user-data '#!/bin/bash
echo ECS_CLUSTER=MyCluster >> /etc/ecs/ecs.config'
{
    "Instances": [
        {
            "InstanceId": "i-abcd1234",
            "ImageId": "ami-abcd1234",
            "State": {
                "Code": 0,
                "Name": "pending"
            },
            "PrivateDnsName": "",
            "PublicDnsName": "",
            "StateReason": {
                "Code": "pending",
                "Message": "pending"
            },
            "InstanceType": "t3.micro",
            "KeyName": "ecs-tutorial-key",
            "LaunchTime": "2025-01-13T10:30:00.000Z"
        }
    ]
}
```

The user data script configures the Amazon ECS agent to register the instance with your
`MyCluster`. The instance uses the `ecsInstanceRole` IAM role, which provides the necessary
permissions for the agent.

## List container instances

Within a few minutes of launching your container instance, the Amazon ECS agent registers
the instance with your MyCluster cluster. You can list the container instances in a
cluster by running the following command:

```
aws ecs list-container-instances --cluster `MyCluster`
```

Output:

```
{
    "containerInstanceArns": [
        "arn:aws:ecs:us-east-1:`aws_account_id`:container-instance/`container_instance_ID`"
    ]
}
```

## Describe your container instance

After you have the ARN or ID of a container instance, you can use the
**describe-container-instances** command to get valuable information
on the instance, such as remaining and registered CPU and memory resources.

```
aws ecs describe-container-instances --cluster `MyCluster` --container-instances `container_instance_ID`
```

Output:

```
{
    "failures": [],
    "containerInstances": [
        {
            "status": "ACTIVE",
            "registeredResources": [
                {
                    "integerValue": 1024,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "CPU",
                    "doubleValue": 0.0
                },
                {
                    "integerValue": 995,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "MEMORY",
                    "doubleValue": 0.0
                },
                {
                    "name": "PORTS",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET",
                    "integerValue": 0
                },
                {
                    "name": "PORTS_UDP",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [],
                    "type": "STRINGSET",
                    "integerValue": 0
                }
            ],
            "ec2InstanceId": "`instance_id`",
            "agentConnected": true,
            "containerInstanceArn": "arn:aws:ecs:us-west-2:`aws_account_id`:container-instance/`container_instance_ID`",
            "pendingTasksCount": 0,
            "remainingResources": [
                {
                    "integerValue": 1024,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "CPU",
                    "doubleValue": 0.0
                },
                {
                    "integerValue": 995,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "MEMORY",
                    "doubleValue": 0.0
                },
                {
                    "name": "PORTS",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET",
                    "integerValue": 0
                },
                {
                    "name": "PORTS_UDP",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [],
                    "type": "STRINGSET",
                    "integerValue": 0
                }
            ],
            "runningTasksCount": 0,
            "attributes": [
                {
                    "name": "com.amazonaws.ecs.capability.privileged-container"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.17"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
                },
                {
                    "name": "com.amazonaws.ecs.capability.logging-driver.json-file"
                },
                {
                    "name": "com.amazonaws.ecs.capability.logging-driver.syslog"
                }
            ],
            "versionInfo": {
                "agentVersion": "1.5.0",
                "agentHash": "b197edd",
                "dockerVersion": "DockerVersion: 1.7.1"
            }
        }
    ]
}
```

You can also find the Amazon EC2 instance ID that you can use to monitor the instance in
the Amazon EC2 console or with the **aws ec2 describe-instances --instance-id
`instance_id`** command.

## Register a task definition

Before you can run a task on your Amazon ECS cluster, you must register a task definition.
Task definitions are lists of containers grouped together. The following example is a
simple task definition that uses an `nginx` image. For more information about
the available task definition parameters, see [Amazon ECS task definitions](task_definitions.md "task_definitions.md").

```
{
    "family": "nginx-task",
    "containerDefinitions": [
        {
            "name": "nginx",
            "image": "public.ecr.aws/ecs-sample-image/amazon-ecs-sample:latest",
            "cpu": 256,
            "memory": 512,
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 80,
                    "hostPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ],
    "requiresCompatibilities": ["EC2"],
    "networkMode": "bridge"
}
```

The above example JSON can be passed to the AWS CLI in two ways: You can save the task
definition JSON as a file and pass it with the ``--cli-input-json`
 file://`path_to_file.json`` option. Or, you
can escape the quotation marks in the JSON and pass the JSON container definitions on
the command line. If you choose to pass the container definitions on the command line,
your command additionally requires a `--family` parameter that is used to
keep multiple versions of your task definition associated with each other.

To use a JSON file for container definitions:

```
aws ecs register-task-definition --cli-input-json `file://$HOME/tasks/nginx.json`
```

The **register-task-definition** returns a description of the task
definition after it completes its registration.

```
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/nginx-task:1",
        "family": "nginx-task",
        "revision": 1,
        "status": "ACTIVE",
        "containerDefinitions": [
            {
                "name": "nginx",
                "image": "public.ecr.aws/docker/library/nginx:latest",
                "cpu": 256,
                "memory": 512,
                "essential": true,
                "portMappings": [
                    {
                        "containerPort": 80,
                        "hostPort": 80,
                        "protocol": "tcp"
                    }
                ],
                "environment": [],
                "mountPoints": [],
                "volumesFrom": []
            }
        ],
        "volumes": [],
        "networkMode": "bridge",
        "compatibilities": [
            "EC2"
        ],
        "requiresCompatibilities": [
            "EC2"
        ]
    }
}
```

## List task definitions

You can list the task definitions for your account at any time with the
**list-task-definitions** command. The output of this command shows
the `family` and `revision` values that you can use together when
calling **create-service**.

```
aws ecs list-task-definitions
```

Output:

```
{
    "taskDefinitionArns": [
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/sleep360:1",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/sleep360:2",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/nginx-task:1",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/wordpress:3",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/wordpress:4",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/wordpress:5",
        "arn:aws:ec2:us-east-1:`aws_account_id`:task-definition/wordpress:6"
    ]
}
```

## Create a service

After you have registered a task for your account and have launched a container
instance that is registered to your cluster, you can create an Amazon ECS service that runs and
maintains a desired number of tasks simultaneously using the task definition that you
registered. For this example, you place a single instance of the `nginx:1`
task definition in your MyCluster cluster.

```
aws ecs create-service --cluster `MyCluster` --service-name `nginx-service` --task-definition `nginx-task:1` --desired-count `1`
```

Output:

```
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:`aws_account_id`:service/MyCluster/nginx-service",
        "serviceName": "nginx-service",
        "clusterArn": "arn:aws:ecs:us-east-1:`aws_account_id`:cluster/MyCluster",
        "taskDefinition": "arn:aws:ecs:us-east-1:`aws_account_id`:task-definition/nginx-task:1",
        "desiredCount": 1,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "status": "ACTIVE",
        "createdAt": "2025-01-13T10:45:00.000Z"
    }
}
```

## List services

List the services for your cluster. You should see the service that you created in the
previous section. You can note the service ID or the full ARN that is returned from this
command and use it to describe the service later.

```
aws ecs list-services --cluster `MyCluster`
```

Output:

```
{
    "taskArns": [
        "arn:aws:ecs:us-east-1:`aws_account_id`:task/``task_ID``"
    ]
}
```

## Describe the service

Describe the service using the following command to get more information about the
service.

```
aws ecs describe-services --cluster `MyCluster` --services `nginx-service`
```

Output:

```
{
    "services": [
        {
            "serviceArn": "arn:aws:ecs:us-east-1:`aws_account_id`:service/MyCluster/nginx-service",
            "serviceName": "nginx-service",
            "clusterArn": "arn:aws:ecs:us-east-1:`aws_account_id`:cluster/MyCluster",
            "taskDefinition": "arn:aws:ecs:us-east-1:`aws_account_id`:task-definition/nginx-task:1",
            "desiredCount": 1,
            "runningCount": 1,
            "pendingCount": 0,
            "launchType": "EC2",
            "status": "ACTIVE",
            "createdAt": "2025-01-13T10:45:00.000Z",
            "events": [
                {
                    "id": "abcd1234-5678-90ab-cdef-1234567890ab",
                    "createdAt": "2025-01-13T10:45:30.000Z",
                    "message": "(service nginx-service) has started 1 tasks: (task abcd1234-5678-90ab-cdef-1234567890ab)."
                }
            ]
        }
    ]
}
```

## Describe the running task

After describing the service, run the following command to get more information about
the task that is running as part of your service.

```
aws ecs list-tasks --cluster `MyCluster` --service-name `nginx-service`
```

Output:

```
{
    "tasks": [
        {
            "taskArn": "arn:aws:ecs:us-east-1:`aws_account_id`:task/MyCluster/abcd1234-5678-90ab-cdef-1234567890ab",
            "clusterArn": "arn:aws:ecs:us-east-1:`aws_account_id`:cluster/MyCluster",
            "taskDefinitionArn": "arn:aws:ecs:us-east-1:`aws_account_id`:task-definition/nginx-task:1",
            "containerInstanceArn": "arn:aws:ecs:us-east-1:`aws_account_id`:container-instance/MyCluster/abcd1234-5678-90ab-cdef-1234567890ab",
            "lastStatus": "RUNNING",
            "desiredStatus": "RUNNING",
            "containers": [
                {
                    "containerArn": "arn:aws:ecs:us-east-1:`aws_account_id`:container/MyCluster/abcd1234-5678-90ab-cdef-1234567890ab/abcd1234-5678-90ab-cdef-1234567890ab",
                    "taskArn": "arn:aws:ecs:us-east-1:`aws_account_id`:task/MyCluster/abcd1234-5678-90ab-cdef-1234567890ab",
                    "name": "nginx",
                    "lastStatus": "RUNNING",
                    "networkBindings": [
                        {
                            "bindIP": "0.0.0.0",
                            "containerPort": 80,
                            "hostPort": 80,
                            "protocol": "tcp"
                        }
                    ]
                }
            ],
            "createdAt": "2025-01-13T10:45:00.000Z",
            "startedAt": "2025-01-13T10:45:30.000Z"
        }
    ]
}
```

## Test the web server

###### To test the web server

1. Retrieve the public IP address of your container instance by running the following command.

```
aws ec2 describe-instances --instance-ids `i-abcd1234` --query 'Reservations[0].Instances[0].PublicIpAddress' --output text
```

Output:

```
`203.0.113.25`
```

2. After retrieving the IP address, run the following `curl` command with the IP
   address.

```
curl http://203.0.113.25
```

Output:

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you can see this page, the nginx web server is successfully installed and working.</p>
...
</body>
</html>
```

The nginx welcome page confirms that your service is running successfully and accessible from the internet.

## Clean up resources

To avoid incurring charges, clean up the resources that you created in this tutorial.

###### To clean up resources

1. Update the service to have zero desired tasks, then delete the service.

```
aws ecs update-service --cluster `MyCluster` --service `nginx-service` --desired-count 0
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/MyCluster/nginx-service",
        "serviceName": "nginx-service",
        "desiredCount": 0,
        "runningCount": 1,
        "pendingCount": 0,
        "status": "ACTIVE"
    }
}
```

2. Wait for the running tasks to stop, then delete the service.

```
aws ecs delete-service --cluster `MyCluster` --service `nginx-service`
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/MyCluster/nginx-service",
        "serviceName": "nginx-service",
        "status": "DRAINING"
    }
}
```

3. Terminate the container instance you created.

```
aws ec2 terminate-instances --instance-ids `i-abcd1234`
{
    "TerminatingInstances": [
        {
            "InstanceId": "i-abcd1234",
            "CurrentState": {
                "Code": 32,
                "Name": "shutting-down"
            },
            "PreviousState": {
                "Code": 16,
                "Name": "running"
            }
        }
    ]
}
```

4. Clean up the security group and key pair that you created.

```
aws ec2 delete-security-group --group-id `sg-abcd1234`
aws ec2 delete-key-pair --key-name `ecs-tutorial-key`
rm `ecs-tutorial-key.pem`
```

5. Delete the Amazon ECS cluster.

```
aws ecs delete-cluster --cluster `MyCluster`
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/MyCluster",
        "clusterName": "MyCluster",
        "status": "INACTIVE"
    }
}
```
