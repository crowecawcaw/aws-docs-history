# Troubleshooting Amazon ECS Managed Instances

Use the following procedures to troubleshoot Amazon ECS Managed Instances, including common issues, diagnostic techniques, and resolution steps.

## Prerequisites

Before troubleshooting Amazon ECS Managed Instances, ensure that you have the following requirements in place.

- The AWS CLI is installed and configured with appropriate permissions

For more information, see [Installing or
updating to the latest version of the AWS Command Line Interface](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

- Access to a cluster with Amazon ECS Managed Instances capacity provider. For more information, see [Creating a cluster for
  Amazon ECS Managed Instances](create-cluster-managed-instances.md "create-cluster-managed-instances.md").

## Common troubleshooting scenarios

### Viewing Amazon ECS Managed Instances container agent logs

You can view these Amazon ECS log files in Amazon ECS Managed Instances by connecting to a privileged container running in the instance.

#### Diagnostic steps

**Deploy a debug container with privileges and Linux capabilities as an Amazon ECS task:**

Set the following environment variables.

Replace the `user-input` with your values.

```
export ECS_CLUSTER_NAME="`your-cluster-name`"
export AWS_REGION="`your-region`"
export ACCOUNT_ID="`your-account-id`"
```

Create a task definition using a CLI JSON file called
`node-debugger.json`.

```
cat << EOF > node-debugger.json
{
  "family": "node-debugger",
  "taskRoleArn": "arn:aws:iam::${ACCOUNT_ID}:role/ecsTaskExecutionRole",
  "executionRoleArn": "arn:aws:iam::${ACCOUNT_ID}:role/ecsTaskExecutionRole",
  "cpu": "256",
  "memory": "1024",
  "networkMode": "host",
  "pidMode": "host",
  "requiresCompatibilities": ["MANAGED_INSTANCES", "EC2"],
  "containerDefinitions": [
    {
      "name": "node-debugger",
      "image": "public.ecr.aws/amazonlinux/amazonlinux:2023",
      "essential": true,
      "privileged": true,
      "command": ["sleep", "infinity"],
      "healthCheck": {
          "command": ["CMD-SHELL", "echo debugger || exit 1"],
          "interval": 30,
          "retries": 3,
          "timeout": 5
      },
      "linuxParameters": {
        "initProcessEnabled": true
      },
      "mountPoints": [
        {
          "sourceVolume": "host-root",
          "containerPath": "/host",
          "readOnly": false
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/aws/ecs/node-debugger",
          "awslogs-create-group": "true",
          "awslogs-region": "${AWS_REGION}",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "volumes": [
    {
      "name": "host-root",
      "host": {
        "sourcePath": "/"
      }
    }
  ]
}
EOF
```

Register, and then run the task. Run the following commands.

```
aws ecs register-task-definition --cli-input-json file://node-debugger.json

TASK_ARN=$(aws ecs run-task \
  --cluster $ECS_CLUSTER_NAME \
  --task-definition node-debugger \
  --enable-execute-command \
  --capacity-provider-strategy capacityProvider=managed-instances-default,weight=1 \
  --query 'tasks[0].taskArn' --output text)

# Wait for task to be running
aws ecs wait tasks-running --cluster $ECS_CLUSTER_NAME --tasks $TASK_ARN
```

Connect to the container. Run the following command.

```
aws ecs execute-command \
  --cluster $ECS_CLUSTER_NAME \
  --task $TASK_ARN \
  --container node-debugger \
  --interactive \
  --command "/bin/sh"
```

**Check the Amazon ECS agent logs:**

In the interactive session of the container, run the following commands:

```
# Install required tools
yum install -y util-linux-core

# View ECS agent logs
nsenter -t 1 -m -p cat /var/log/ecs/ecs-agent.log | tail -50

# Check agent registration
nsenter -t 1 -m -p grep "Registered container instance" /var/log/ecs/ecs-agent.log

Example Output:

{"level":"info","time":"2025-10-16T12:39:37.665","msg":"Registered container instance with cluster!"}

# Verify capabilities
nsenter -t 1 -m -p grep "Response contained expected value for attribute" /var/log/ecs/ecs-agent.log
```

**Check agent metrics:**

Run the following command to view the logs.

```
# View metrics logs
nsenter -t 1 -m -p cat /var/log/ecs/metrics.log | tail -20
```

### Task placement issues

The following are symptoms of task placement issues:

- Tasks stuck in PENDING state
- Tasks failing to start on Amazon ECS Managed Instances
- Insufficient resources errors

#### Diagnostic steps

Run the following commands to diagnose task placement issues and gather information about cluster capacity, container instances, and system services:

```
# Check cluster capacity
aws ecs describe-clusters --clusters `cluster-name` --include STATISTICS

# Check cluster capacity providers
aws ecs describe-clusters --clusters `cluster-name` --include STATISTICS --query 'clusters[].capacityProviders'

# List container instances
aws ecs list-container-instances --cluster `cluster-name`

# Check container instance details
aws ecs describe-container-instances --cluster `cluster-name` --container-instances `container-instance-arn`

# Check container instance remaining resources CPU/Mem
aws ecs describe-container-instances --cluster $ECS_CLUSTER_NAME --container-instances `container-instance-arn` --query 'containerInstances[].remainingResources'

# Check container instance Security Group
aws ecs describe-container-instances --cluster $ECS_CLUSTER_NAME --container-instances `container-instance-arn` --query 'containerInstances[].ec2InstanceId' --output text
aws ec2 describe-instances --instance-ids `instance-id` --query 'Reservations[0].Instances[0].SecurityGroups'
aws ec2 describe-security-groups --group-ids security-`group-id`
```

**System service monitoring:**

```
# Check Containerd status
nsenter -t 1 -m -p systemctl status containerd.service

# Check Amazon ECS container agent status
nsenter -t 1 -m -p systemctl status ecs
```

#### Resolution

To resolve task placement issues, follow these steps to ensure proper configuration and capacity:

- Verify task resource requirements vs available capacity
- Check placement constraints and strategies
- Ensure Amazon ECS Managed Instances capacity provider is configured
- Ensure that the task and container instance security group have an outbound rule that allow traffic for the Amazon ECS agent management endpoints

### Networking issues

The following are synptoms of networking issues:

- Tasks unable to reach external services
- DNS resolution problems

#### Diagnostic steps

**Network connectivity tests:**

From the debug container, run the following commands:

###### Note

Confirm the security group attached to your capacity provider or Amazon ECS task is permitting the traffic.

```
# Install DNS Utility
yum install bind-utils -y

# Test DNS resolution
nslookup amazon.com

# Test external connectivity
curl -I https://amazon.com
```

### Resource constraints

The following are synptoms of networking issues:

- Tasks killed due to memory limits
- CPU throttling
- Disk space issues

#### Diagnostic steps

Run commands to monitory the resources and container limits.

**Resource monitoring:**

```
# Check memory usage
nsenter -t 1 -m -p free -h

# Check disk usage
nsenter -t 1 -m -p lsblk

# Check disk usage
nsenter -t 1 -m -p df -h
```

**Container Limits:**

```
# Check OOM kills
nsenter -t 1 -m -p dmesg | grep -i "killed process"
```

### Container instance agent disconnect issue

The following are symptoms of container instance agent disconnect issues:

- Container instances showing as disconnected in the Amazon ECS console
- Tasks failing to be placed on specific instances
- Agent registration failures in logs

#### Diagnostic steps

If there is an existing privilege task running on the host that ECS Exec can
access, run the following commands to diagnose agent connectivity issues:

```
# check service status
nsenter -t 1 -m -p systemctl restart ecs
nsenter -t 1 -m -p systemctl restart containerd

# restart stopped services
nsenter -t 1 -m -p systemctl restart ecs
nsenter -t 1 -m -p systemctl restart containerd
```

Otherwise, force deregister the Amazon ECS Managed Instances. Run the following command:

```
# list ECS Managed Instance container
aws ecs list-container-instances --cluster managed-instances-cluster --query 'containerInstanceArns' --output text

# deregister the specific container instance
aws ecs deregister-container-instance \
    --cluster $ECS_CLUSTER_NAME \
    --container-instance container-instance-arn \
    --force
```

#### Resolution

To resolve agent disconnect issues, follow these steps:

- Verify IAM role permissions for the container instance
- Check security group rules allow outbound HTTPS traffic to ECS endpoints
- Ensure network connectivity to AWS services
- Restart the ECS agent service if necessary: `nsenter -t 1 -m -p systemctl restart ecs`
- Verify the ECS_CLUSTER configuration in /etc/ecs/ecs.config matches your cluster name

## Log Analysis in Amazon ECS Managed Instances

### System logs

Use the following commands to examine system logs and identify potential issues with the managed instance:

```
# Check system messages
nsenter -t 1 -m -p journalctl --no-pager -n 50

# Check kernel logs
nsenter -t 1 -m -p dmesg | tail -20

# Check for disk space errors
nsenter -t 1 -m -p journalctl --no-pager | grep -i "no space\|disk full\|enospc"
```

## Use the EC2 AWS CLI to get the console output from a Amazon ECS Managed Instance

Use the Amazon EC2 instance ID to retrieve the console output.

Replace the `user-input` with your values.

```
aws ec2 get-console-output --instance-id `instance-id` --latest --output text
```

## Cleanup

Run the following to stop the deug task and deregister the task definition.

```
# Stop debug task
aws ecs stop-task --cluster $ECS_CLUSTER_NAME --task $TASK_ARN

# Deregister task definition (optional)
aws ecs deregister-task-definition --task-definition node-debugger
```

## Additional resources

For more information about troubleshooting Amazon ECS Managed Instances, see the following resources:

- [Troubleshooting Amazon ECS Amazon ECS Managed Instances errors](managed-instances-errors.md "managed-instances-errors.md")
- [Amazon ECS troubleshooting](troubleshooting.md "troubleshooting.md")
- [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md")
- [Monitor Amazon ECS containers with ECS Exec](ecs-exec.md "ecs-exec.md")
