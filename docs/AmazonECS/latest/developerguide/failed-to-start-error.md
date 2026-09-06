

# Troubleshooting Amazon ECS TaskFailedToStart errors
<a name="failed-to-start-error"></a>

The following are some `TaskFailedToStart` error messages and actions that you can take to fix the errors. 

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## Unexpected EC2 error while attempting to Create Network Interface with public IP assignment enabled in subnet '{{subnet-id}}
<a name="subnet-error"></a>

This happens when a Fargate task that uses the `awsvpc` network mode and runs in a subnet with a public IP address, and the subnet does not have enough IP addresses.

The number of available IP addresses is available on the subnet details page in the Amazon EC2 console, or by using `[describe-subnets](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-subnets.html)`. For more information, see [View your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#view-subnet) in the *Amazon VPC User Guide*.

To fix this issue, you can create a new subnet to run your task in.

## InternalError: {{<reason>}}
<a name="internal-error-reason"></a>

This error occurs when an ENI attachment is requested. Amazon EC2 asynchronously handles the provisioning of the ENI. The provisioning process takes time. Amazon ECS has a timeout in case there are long wait times or unreported failures. There are times when the ENI is provisioned, but the report comes to Amazon ECS after the failure timeout. In this case, Amazon ECS sees the reported task failure with an in-use ENI.

## The selected task definition is not compatible with the selected compute strategy
<a name="compute-compatibility"></a>

This error occurs when you chose a task definition with a launch type that does not match the cluster capacity type. You need to select a task definition that matches the capacity provider assigned to your cluster.

## Unable to attach network interface to unused device index
<a name="compute-compatibility-cpu"></a>

This error occurs when When using `awsvpc` networking type and there is not enough CPU/memory for the task. First, check the CPU for the instances. For more information, see [Amazon EC2 instance type specifications](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-type-specifications.html) in *Amazon EC2 instance types*. Take the CPU value for the instance and multiply it by the number of ENIs for the instance. Use that value e in the task definition.

## AGENT
<a name="agent-not-started"></a>

The container instance that you attempted to launch a task onto has an agent that's currently disconnected. To prevent extended wait times for task placement, the request was rejected.

For information about how to troubleshoot an agent that's disconnected, see [How do I troubleshoot a disconnected Amazon ECS agent](https://repost.aws/knowledge-center/ecs-agent-disconnected-linux2-ami).