

# Amazon ECS API failure reasons
<a name="api_failures_messages"></a>

When an API action that you have triggered through the Amazon ECS API, console, or the AWS CLI exits with a `failures` error message, the following might assist in troubleshooting the cause. The failure returns a reason and the Amazon Resource Name (ARN) of the resource associated with the failure.

Many resources are Region-specific, so when using the console ensure that you set the correct Region for your resources. When using the AWS CLI, make sure that your AWS CLI commands are being sent to the correct Region with the `--region {{region}}` parameter.

For more information about the structure of the `Failure` data type, see [Failure](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Failure.html) in the *Amazon Elastic Container Service API Reference*.

The following are examples of failure messages that you might receive when running API commands. 



- ** `DescribeClusters` **
  - **Failure reason or Stopped reason:** `MISSING`
  - **Cause:** The specified cluster wasn't found. Verify the spelling of the cluster name.

- ** `DescribeInstances` **
  - **Failure reason or Stopped reason:** `MISSING`
  - **Cause:** The specified container instance wasn't found. Verify that you specified the cluster the container instance is registered to and that both the container instance ARN or ID is correct.

- ** `DescribeServices` **
  - **Failure reason or Stopped reason:** `MISSING`
  - **Cause:** The specified service wasn't found. Verify that the correct cluster or Region is specified and that the service ARN or name is valid.

- ** `DescribeTasks` **
  - **Failure reason or Stopped reason:** `MISSING`
  - **Cause:** The specified task wasn't found. Verify the correct cluster or Region is specified and that both the task ARN or ID is valid.

- ** `DescribeTasks`  **
  - **Failure reason or Stopped reason:** `TaskFailedToStart: RESOURCE:*` / **Cause:** For `RESOURCE:CPU` errors, the number of CPUs requested by the task are unavailable on your container instances. This generally happens when the CPU unit requirement in your task definition is larger than the CPU size of the Amazon EC2 instances defined in the Auto Scaling group mapped to the capacity provider. You need to check your capacity provider configuration.<br />For `RESOURCE:MEMORY` errors, the amount of memory requested by the task are unavailable on your container instances. This generally happens when the memory amount requirement in your task definition is larger than the supported memory on the Amazon EC2 instances defined in the Auto Scaling group mapped to the capacity provider. You need to check your capacity provider configuration.
  - **Failure reason or Stopped reason:** `TaskFailedToStart: AGENT` / **Cause:** The container instance that you attempted to launch a task onto has an agent that's currently disconnected. To prevent extended wait times for task placement, the request was rejected.<br />For information about how to troubleshoot an agent that's disconnected, see [How do I troubleshoot a disconnected Amazon ECS agent](https://repost.aws/knowledge-center/ecs-agent-disconnected-linux2-ami).
  - **Failure reason or Stopped reason:** `TaskFailedToStart: MemberOf placement constraint unsatisfied` / **Cause:** There is no container instance that meets the placement constraints defined in your task definition.
  - **Failure reason or Stopped reason:** `TaskFailedToStart: ATTRIBUTE` / **Cause:** Your task definition contains a parameter that requires a specific container instance attribute that isn't available on your container instances. For example, if your task uses the `awsvpc` network mode, but there are no instances in your specified subnets with the `ecs.capability.task-eni` attribute. For more information about which attributes are required for specific task definition parameters and agent configuration variables, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md) and [Amazon ECS container agent configuration](ecs-agent-config.md).
  - **Failure reason or Stopped reason:** TaskFailedToStart: NO ACTIVE INSTANCES / **Cause:** There are no active instances in your capacity provider. For information about how to manage your Auto Scaling groups, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) in the Amazon EC2 Auto Scaling User Guide.
  - **Failure reason or Stopped reason:** `TaskFailedToStart: EMPTY CAPACITY PROVIDER` / **Cause:** There are no instances in your cluster. This is most likely because of an empty capacity provider, or because the instances in the capacity provider are not registered to the cluster. For information about how to manage your Auto Scaling groups, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) in the Amazon EC2 Auto Scaling User Guide.

- ** `GetTaskProtection` **
  - **Failure reason or Stopped reason:** `MISSING` / **Cause:** The specified task wasn't found. Verify that the cluster name or ARN and the task ARN or ID are valid.
  - **Failure reason or Stopped reason:** `TASK_NOT_VALID` / **Cause:** The specified task isn't part of an Amazon ECS service. Only Amazon ECS service-managed tasks can be protected. Verify the task ARN or ID and try again.

- ** `RunTask` or `StartTask` **
  - **Failure reason or Stopped reason:** `RESOURCE:*` / **Cause:** The resource or resources that are requested by the task are unavailable on the container instances in the cluster. If the resource is CPU, memory, ports, or elastic network interfaces, you might need to add additional container instances to your cluster.<br />For `RESOURCE:ENI` errors, your cluster doesn't have any available elastic network interface attachment points, which are required for tasks that use the `awsvpc` network mode. Amazon EC2 instances have a limit to the number of network interfaces that can be attached to them, and the primary network interface counts as one. For more information about how many network interfaces are supported for each instance type, see [IP Addresses Per Network Interface Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI) in the *Amazon EC2 User Guide*.<br />For `RESOURCE:GPU` errors, the number of GPUs requested by the task are unavailable and you might need to add GPU-enabled container instances to your cluster. For more information, see [Amazon ECS task definitions for GPU workloads](ecs-gpu.md).
  - **Failure reason or Stopped reason:** `AGENT` / **Cause:** The container instance that you attempted to launch a task onto has an agent that's currently disconnected. To prevent extended wait times for task placement, the request was rejected.<br />For information about how to troubleshoot an agent that's disconnected, see [How do I troubleshoot a disconnected Amazon ECS agent](https://repost.aws/knowledge-center/ecs-agent-disconnected-linux2-ami).
  - **Failure reason or Stopped reason:** `LOCATION` / **Cause:** The container instance that you attempted to launch a task onto is in a different Availability Zone than the subnets that you specified in your `awsVpcConfiguration`.
  - **Failure reason or Stopped reason:** `ATTRIBUTE` / **Cause:** Your task definition contains a parameter that requires a specific container instance attribute that isn't available on your container instances. For example, if your task uses the `awsvpc` network mode, but there are no instances in your specified subnets with the `ecs.capability.task-eni` attribute. For more information about which attributes are required for specific task definition parameters and agent configuration variables, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md) and [Amazon ECS container agent configuration](ecs-agent-config.md).

- ** `StartTask` **
  - **Failure reason or Stopped reason:** `MISSING` / **Cause:** The container instance that you attempted to launch the task onto can't be found. Check if the wrong cluster or Region is specified, or the container instance ARN or ID is misspelled.
  - **Failure reason or Stopped reason:** `INACTIVE` / **Cause:** The container instance that you attempted to launch a task onto was previously deregistered with Amazon ECS and can't be used.

- ** `StopServiceDeployment` **
  - **Failure reason or Stopped reason:** `ECS deployment failed`
  - **Cause:** A fraud account ran the StopServiceDeployment API.

- ** `TagResource` **
  - **Failure reason or Stopped reason:** `InvalidParameterException`
  - **Cause:** The ARN for the service that you are tagging has the short format. You must migrate to the long format. For information about how to migrate the ARN, see [Migrate an Amazon ECS short service ARN to a long ARN](service-arn-migration.md).

- ** `UpdateTaskProtection` **
  - **Failure reason or Stopped reason:** `DEPLOYMENT_BLOCKED` / **Cause:** Can't set task protection as one or more protected tasks are preventing the service deployment from reaching a steady state. Unset task protection on existing tasks or wait until task protection expires.
  - **Failure reason or Stopped reason:** `MISSING` / **Cause:** The specified task wasn't found. Verify that the cluster name or ARN and the task ARN or ID are valid.
  - **Failure reason or Stopped reason:** `TASK_NOT_VALID` / **Cause:** The specified task isn't part of an Amazon ECS service. Only Amazon ECS service-managed tasks can be protected. Verify the task ARN or ID and try again.



**Note**  
Besides the failure scenarios described here, API operations can also fail due to exceptions, resulting in error responses. For a list of such exceptions, see [Common Errors](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/CommonErrors.html).