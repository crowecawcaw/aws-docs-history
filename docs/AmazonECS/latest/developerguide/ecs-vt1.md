# Amazon ECS task definitions for video transcoding workloads

To use video transcoding workloads on Amazon ECS, register [Amazon EC2 VT1](https://aws.amazon.com/ec2/instance-types/vt1/ "https://aws.amazon.com/ec2/instance-types/vt1/") instances. After you registered these
instances, you can run live and pre-rendered video transcoding workloads as tasks on Amazon ECS.
Amazon EC2 VT1 instances use Xilinx U30 media transcoding cards to accelerate live and
pre-rendered video transcoding workloads.

###### Note

For instructions on how to run video transcoding workloads in containers other than
Amazon ECS, see the [Xilinx documentation](https://xilinx.github.io/video-sdk/v1.5/container_setup.html#working-with-docker-vt1 "https://xilinx.github.io/video-sdk/v1.5/container_setup.html#working-with-docker-vt1").

## Considerations

Before you begin deploying VT1 on Amazon ECS, consider the following:

- Your clusters can contain a mix of VT1 and non-VT1 instances.
- You need a Linux application that uses Xilinx U30 media transcoding cards with
  accelerated AVC (H.264) and HEVC (H.265) codecs.

###### Important

Applications that use other codecs might not have improved performance on
VT1 instances.

- Only one transcoding task can run on a U30 card. Each card has two devices
  that are associated with it. You can run as many transcoding tasks as there are
  cards for each of your VT1 instance.
- When creating a service or running a standalone task, you can use instance
  type attributes when configuring task placement constraints. This ensures that
  the task is launched on the container instance that you specify. Doing so helps
  ensure that you use your resources effectively and that your tasks for video
  transcoding workloads are on your VT1 instances. For more information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

In the following example, a task is run on a `vt1.3xlarge` instance
on your `default` cluster.

```
`aws ecs run-task \
 --cluster default \
 --task-definition `vt1-3xlarge-xffmpeg-processor` \
 **--placement-constraints type=memberOf,expression="attribute:ecs.instance-type == vt1.3xlarge"**`
```

- You configure a container to use the specific U30 card available on the host
  container instance. You can do this by using the `linuxParameters`
  parameter and specifying the device details. For more information, see [Task definition requirements](#ecs-vt1-requirements "#ecs-vt1-requirements").

## Using a VT1 AMI

You have two options for running an AMI on Amazon EC2 for Amazon ECS container instances. The
first option is to use the Xilinx official AMI on the AWS Marketplace. The second option is to
build your own AMI from the sample repository.

- [Xilinx offers AMIs on the AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-phvk6d4mq3hh6 "https://aws.amazon.com/marketplace/pp/prodview-phvk6d4mq3hh6").
- Amazon ECS provides a sample repository that you can use to build an AMI for
  video transcoding workloads. This AMI comes with Xilinx U30 drivers. You can
  find the repository that contains Packer scripts on [GitHub](https://github.com/aws-samples/aws-vt-baseami-pipeline "https://github.com/aws-samples/aws-vt-baseami-pipeline").
  For more information about Packer, see the [Packer documentation](https://developer.hashicorp.com/packer/docs "https://developer.hashicorp.com/packer/docs").

## Task definition requirements

To run video transcoding containers on Amazon ECS, your task definition must contain a
video transcoding application that uses the accelerated H.264/AVC and H.265/HEVC codecs.
You can build a container image by following the steps on the [Xilinx GitHub](https://xilinx.github.io/video-sdk/v1.5/container_setup.html#creating-a-docker-image-for-vt1-usage "https://xilinx.github.io/video-sdk/v1.5/container_setup.html#creating-a-docker-image-for-vt1-usage").

The task definition must be specific to the instance type. The instance types are
3xlarge, 6xlarge, and 24xlarge. You must configure a container to use specific Xilinx
U30 devices that are available on the host container instance. You can do so using the
`linuxParameters` parameter. The following table details the cards and
device SoCs that are specific to each instance type.

| Instance Type | vCPUs | RAM (GiB) | U30 accelerator cards | Addressable XCU30 SoC devices | Device Paths                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ----- | --------- | --------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vt1.3xlarge   | 12    | 24        | 1                     | 2                             | `/dev/dri/renderD128`,`/dev/dri/renderD129`                                                                                                                                                                                                                                                                                                                     |
| vt1.6xlarge   | 24    | 48        | 2                     | 4                             | `/dev/dri/renderD128`,`/dev/dri/renderD129`,`/dev/dri/renderD130`,`/dev/dri/renderD131`                                                                                                                                                                                                                                                                         |
| vt1.24xlarge  | 96    | 182       | 8                     | 16                            | `/dev/dri/renderD128`,`/dev/dri/renderD129`,`/dev/dri/renderD130`,`/dev/dri/renderD131`,`/dev/dri/renderD132`,`/dev/dri/renderD133`,`/dev/dri/renderD134`,`/dev/dri/renderD135`,`/dev/dri/renderD136`,`/dev/dri/renderD137`,`/dev/dri/renderD138`,`/dev/dri/renderD139`,`/dev/dri/renderD140`,`/dev/dri/renderD141`,`/dev/dri/renderD142`,`/dev/dri/renderD143` | ###### Important If the task definition lists devices that the EC2 instance doesn't have, the task fails to run. When the task fails, the following error message appears in the `stoppedReason`: `CannotStartContainerError: Error response from daemon: error gathering device information while adding custom device "/dev/dri/renderD`130`": no such file or directory`. |
