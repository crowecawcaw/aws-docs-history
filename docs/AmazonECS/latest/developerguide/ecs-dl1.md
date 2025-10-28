# Amazon ECS task definitions for deep learning instances

To use deep learning workloads on Amazon ECS, register [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/ "https://aws.amazon.com/ec2/instance-types/dl1/") instances to your clusters. Amazon EC2
DL1 instances are powered by Gaudi accelerators from Habana Labs (an Intel company). Use
the Habana SynapseAI SDK to connect to the Habana Gaudi accelerators. The SDK supports
the popular machine learning frameworks, TensorFlow and PyTorch.

## Considerations

Before you begin deploying DL1 on Amazon ECS, consider the following:

- Your clusters can contain a mix of DL1 and non-DL1 instances.
- When creating a service or running a standalone task, you can use instance
  type attributes specifically when you configure task placement constraints
  to ensure that your task is launched on the container instance that you
  specify. Doing so ensures that your resources are used effectively and that
  your tasks for deep learning workloads are on your DL1 instances. For more
  information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

The following example runs a task on a `dl1.24xlarge` instance
on your `default` cluster.

```
`aws ecs run-task \
 --cluster default \
 --task-definition ecs-dl1-task-def \
 **--placement-constraints type=memberOf,expression="attribute:ecs.instance-type == dl1.24xlarge"**`
```

## Using a DL1 AMI

You have three options for running an AMI on Amazon EC2 DL1 instances for
Amazon ECS:

- AWS Marketplace AMIs that are provided by Habana [here](https://aws.amazon.com/marketplace/pp/prodview-h24gzbgqu75zq "https://aws.amazon.com/marketplace/pp/prodview-h24gzbgqu75zq").
- Habana Deep Learning AMIs that are provided by Amazon Web Services. Because it's not
  included, you need to install the Amazon ECS container agent separately.
- Use Packer to build a custom AMI that's provided by the [GitHub
  repo](https://github.com/aws-samples/aws-habana-baseami-pipeline "https://github.com/aws-samples/aws-habana-baseami-pipeline"). For more information, see [the Packer
  documentation](https://developer.hashicorp.com/packer/docs "https://developer.hashicorp.com/packer/docs").
