

# Amazon ECS task definitions for AWS Neuron machine learning workloads
<a name="ecs-inference"></a>

You can use [Amazon EC2 Trn1](https://aws.amazon.com/ec2/instance-types/trn1/), [Amazon EC2 Trn2](https://aws.amazon.com/ec2/instance-types/trn2/), [Amazon EC2 Inf1](https://aws.amazon.com/ec2/instance-types/inf1/) (Inf1 is only supported on EC2 launch type), and [Amazon EC2 Inf2](https://aws.amazon.com/ec2/instance-types/inf2/) instances with your clusters for machine learning workloads.

Amazon EC2 Trn1 and Trn2 instances are powered by [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) chips. These instances provide high performance and low cost training for machine learning in the cloud. You can train a machine learning inference model using a machine learning framework with AWS Neuron on a Trn1 or Trn2 instance. Then, you can run the model on an Inf1 instance (Inf1 is only supported on EC2 launch type), or an Inf2 instance to use the acceleration of the AWS Inferentia chips.

The Amazon EC2 Inf1 instances and Inf2 instances are powered by [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) chips They provide high performance and lowest cost inference in the cloud.

Machine learning models are deployed to containers using [AWS Neuron](https://aws.amazon.com/ai/machine-learning/neuron/), which is a specialized Software Developer Kit (SDK). The SDK consists of a compiler, runtime, and profiling tools that optimize the machine learning performance of AWS machine learning chips. AWS Neuron supports popular machine learning frameworks such as TensorFlow, PyTorch, and Apache MXNet.

## Considerations
<a name="ecs-inference-considerations"></a>

Before you begin deploying Neuron on Amazon ECS, consider the following:
+ Depending on the launch type, your clusters can contain a mix of Trn1, Trn2, Inf1, Inf2, and other instances.
+ You need a Linux application in a container that uses a machine learning framework that supports AWS Neuron.
**Important**  
Applications that use other frameworks might not have improved performance on Trn1, Trn2, Inf1, and Inf2 instances.
+ Amazon ECS supports two approaches for configuring Neuron device access:
  + **Managed Neuron device allocation** – Use the `resourceRequirements` parameter with type `NeuronDevice` in your container definition. Amazon ECS automatically discovers and assigns Neuron devices to your containers. Available on Managed Instances only. For more information, see [Managed Neuron device allocation](#ecs-inference-managed).
  + **Manual Neuron device specification** – Use the `linuxParameters.devices` parameter to explicitly specify Neuron device paths. Available on both EC2 launch type and Managed Instances. For more information, see [Manual Neuron device specification](#ecs-inference-ec2).
**Important**  
Use only one approach consistently to avoid conflicts.

## Managed Neuron device allocation
<a name="ecs-inference-managed"></a>

With Managed Instances, you can use the `resourceRequirements` parameter in your container definition to request Neuron devices. Amazon ECS automatically discovers Neuron devices on the instance, assigns them to your task, and configures the container with access to all Neuron devices on the instance. Because the task requires exclusive access to all devices, only one Neuron task runs per instance.

**Note**  
`Inf1` instances are only supported on the EC2 launch type. To use Inf1 instances, see [Manual Neuron device specification](#ecs-inference-ec2).

### Neuron instance selection
<a name="ecs-inference-managed-instance-selection"></a>

To select Neuron-enabled instance types for your Managed Instances workloads, use the `instanceRequirements` object in the launch template of the capacity provider. You can use the following attributes to select Neuron-enabled instances:
+ `acceleratorManufacturers` – Use `amazon-web-services` to select instances with AWS accelerators (includes Inferentia and Trainium).
+ `acceleratorNames` – Use `inferentia2`, `trainium`, or `trainium2` to select specific accelerator chips.
+ `allowedInstanceTypes` – Use `inf*` and `trn*` to select Neuron instance types by name.

The following example uses `allowedInstanceTypes`:

```
{
    "instanceRequirements": {
        "allowedInstanceTypes": ["inf*", "trn*"]
    }
}
```

### Task definition
<a name="ecs-inference-managed-task-def"></a>

To request Neuron devices in your task definition, add a `resourceRequirements` entry with type `NeuronDevice` and value `ALL`. This gives the container exclusive access to all Neuron devices on the instance.

The following constraints apply:
+ At most one container definition can specify `NeuronDevice` in `resourceRequirements`.
+ You can't combine `resourceRequirements` with type `NeuronDevice` and `linuxParameters.devices` for Neuron devices in the same task definition.

After your task starts, you can verify the Neuron device assignment by calling the `DescribeTasks` API operation. The response includes a `neuronDeviceIds` field on each container that shows the IDs of the assigned Neuron devices. You can also call the `DescribeContainerInstances` API operation to view `NEURON_DEVICES` in the `registeredResources` and `remainingResources` fields for the container instance.

For an example task definition, see [Example Neuron task definitions](ecs-inference-task-def.md).

## Manual Neuron device specification
<a name="ecs-inference-ec2"></a>

With this approach, you manually specify AWS Trainium or AWS Inferentia device paths in your task definition using the `linuxParameters.devices` parameter. This approach works on both the EC2 launch type and Managed Instances.

Only one inference or inference-training task can run on each [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) or [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) chip. You can run as many tasks as there are chips on the instance by assigning different devices to each task.

For the EC2 launch type, you can use instance type attributes when you configure task placement constraints to ensure that the task is launched on the instance type you specify. For more information, see [How Amazon ECS places tasks on container instances](task-placement.md).

### Task definition requirements
<a name="ecs-inference-requirements"></a>

The task definition must be specific to a single instance type. You must configure a container to use specific AWS Trainium or AWS Inferentia devices that are available on the host container instance. You can do so using the `linuxParameters` parameter. The following table details the chips that are specific to each instance type.


| Instance Type | vCPUs | RAM (GiB) | AWS ML accelerator chips | Device Paths | 
| --- | --- | --- | --- | --- | 
| trn1.2xlarge | 8 | 32 | 1 | /dev/neuron0 | 
| trn1.32xlarge | 128 | 512 | 16 |  /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3, /dev/neuron4, /dev/neuron5, /dev/neuron6, /dev/neuron7, /dev/neuron8, /dev/neuron9, /dev/neuron10, /dev/neuron11, /dev/neuron12, /dev/neuron13, /dev/neuron14, /dev/neuron15  | 
| trn2.48xlarge | 192 | 2048 | 16 |  /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3, /dev/neuron4, /dev/neuron5, /dev/neuron6, /dev/neuron7, /dev/neuron8, /dev/neuron9, /dev/neuron10, /dev/neuron11, /dev/neuron12, /dev/neuron13, /dev/neuron14, /dev/neuron15  | 
| inf1.xlarge | 4 | 8 | 1 | /dev/neuron0 | 
| inf1.2xlarge | 8 | 16 | 1 | /dev/neuron0 | 
| inf1.6xlarge | 24 | 48 | 4 | /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3 | 
| inf1.24xlarge | 96 | 192 | 16 |  /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3, /dev/neuron4, /dev/neuron5, /dev/neuron6, /dev/neuron7, /dev/neuron8, /dev/neuron9, /dev/neuron10, /dev/neuron11, /dev/neuron12, /dev/neuron13, /dev/neuron14, /dev/neuron15  | 
| inf2.xlarge | 4 | 16 | 1 | /dev/neuron0 | 
| inf2.8xlarge | 32 | 128 | 1 | /dev/neuron0 | 
| inf2.24xlarge | 96 | 384 | 6 | /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3, /dev/neuron4, /dev/neuron5 | 
| inf2.48xlarge | 192 | 768 | 12 | /dev/neuron0, /dev/neuron1, /dev/neuron2, /dev/neuron3, /dev/neuron4, /dev/neuron5, /dev/neuron6, /dev/neuron7, /dev/neuron8, /dev/neuron9, /dev/neuron10, /dev/neuron11 | 

For an example task definition, see [Example Neuron task definitions](ecs-inference-task-def.md).

### Managed Instances
<a name="ecs-inference-manual-mi"></a>

Managed Instances automatically use an AMI that includes the Neuron driver. No additional AMI configuration is required.

### EC2 launch type
<a name="ecs-inference-manual-ec2"></a>

Amazon ECS provides an Amazon ECS optimized AMI that's based on Amazon Linux 2023 for AWS Trainium and AWS Inferentia workloads. It comes with the AWS Neuron drivers and runtime for Docker. This AMI makes running machine learning inference workloads easier on Amazon ECS.

We recommend using the Amazon ECS-optimized Amazon Linux 2023 (Neuron) AMI when launching your Amazon EC2 Trn1, Inf1, and Inf2 instances. 

You can retrieve the current Amazon ECS-optimized Amazon Linux 2023 (Neuron) AMI using the AWS CLI with the following command.

```
aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/neuron/recommended
```