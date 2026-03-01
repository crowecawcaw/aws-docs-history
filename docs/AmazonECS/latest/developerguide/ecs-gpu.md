# Amazon ECS task definitions for GPU workloads

Amazon ECS supports workloads that use GPUs, when you create clusters with container instances
that support GPUs. Amazon EC2 GPU-based container instances that use the p2, p3, p5, g3, g4, and
g5 instance types provide access to NVIDIA GPUs. For more information, see [Linux Accelerated Computing
Instances](../../../ec2/latest/instancetypes/ac.md "../../../ec2/latest/instancetypes/ac.md") in the _Amazon EC2 Instance Types guide_.

Amazon ECS provides a GPU-optimized AMI that comes with pre-configured NVIDIA kernel drivers
and a Docker GPU runtime. For more information, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md").

You can designate a number of GPUs in your task definition for task placement
consideration at a container level. Amazon ECS schedules to available container instances that
support GPUs and pin physical GPUs to proper containers for optimal performance.

The following Amazon EC2 GPU-based instance types are supported. For more information, see
[Amazon EC2 P2 Instances](https://aws.amazon.com/ec2/instance-types/p2/ "https://aws.amazon.com/ec2/instance-types/p2/"), [Amazon EC2 P3 Instances](https://aws.amazon.com/ec2/instance-types/p3/ "https://aws.amazon.com/ec2/instance-types/p3/"), [Amazon EC2 P4d Instances](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/"), [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/"), [Amazon EC2 G3 Instances](https://aws.amazon.com/ec2/instance-types/g3/ "https://aws.amazon.com/ec2/instance-types/g3/"), [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/ "https://aws.amazon.com/ec2/instance-types/g4/"), [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/"), [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/ "https://aws.amazon.com/ec2/instance-types/g6/"), and [Amazon EC2 G6e Instances](https://aws.amazon.com/ec2/instance-types/g6e/ "https://aws.amazon.com/ec2/instance-types/g6e/").

| Instance type | GPUs | GPU memory (GiB) | vCPUs | Memory (GiB) |
| ------------- | ---- | ---------------- | ----- | ------------ |
| p3.2xlarge    | 1    | 16               | 8     | 61           |
| p3.8xlarge    | 4    | 64               | 32    | 244          |
| p3.16xlarge   | 8    | 128              | 64    | 488          |
| p3dn.24xlarge | 8    | 256              | 96    | 768          |
| p4d.24xlarge  | 8    | 320              | 96    | 1152         |
| p5.48xlarge   | 8    | 640              | 192   | 2048         |
| g3s.xlarge    | 1    | 8                | 4     | 30.5         |
| g3.4xlarge    | 1    | 8                | 16    | 122          |
| g3.8xlarge    | 2    | 16               | 32    | 244          |
| g3.16xlarge   | 4    | 32               | 64    | 488          |
| g4dn.xlarge   | 1    | 16               | 4     | 16           |
| g4dn.2xlarge  | 1    | 16               | 8     | 32           |
| g4dn.4xlarge  | 1    | 16               | 16    | 64           |
| g4dn.8xlarge  | 1    | 16               | 32    | 128          |
| g4dn.12xlarge | 4    | 64               | 48    | 192          |
| g4dn.16xlarge | 1    | 16               | 64    | 256          |
| g5.xlarge     | 1    | 24               | 4     | 16           |
| g5.2xlarge    | 1    | 24               | 8     | 32           |
| g5.4xlarge    | 1    | 24               | 16    | 64           |
| g5.8xlarge    | 1    | 24               | 32    | 128          |
| g5.16xlarge   | 1    | 24               | 64    | 256          |
| g5.12xlarge   | 4    | 96               | 48    | 192          |
| g5.24xlarge   | 4    | 96               | 96    | 384          |
| g5.48xlarge   | 8    | 192              | 192   | 768          |
| g6.xlarge     | 1    | 24               | 4     | 16           |
| g6.2xlarge    | 1    | 24               | 8     | 32           |
| g6.4xlarge    | 1    | 24               | 16    | 64           |
| g6.8xlarge    | 1    | 24               | 32    | 128          |
| g6.16.xlarge  | 1    | 24               | 64    | 256          |
| g6.12xlarge   | 4    | 96               | 48    | 192          |
| g6.24xlarge   | 4    | 96               | 96    | 384          |
| g6.48xlarge   | 8    | 192              | 192   | 768          |
| g6.metal      | 8    | 192              | 192   | 768          |
| gr6.4xlarge   | 1    | 24               | 16    | 128          |
| g6e.xlarge    | 1    | 48               | 4     | 32           |
| g6e.2xlarge   | 1    | 48               | 8     | 64           |
| g6e.4xlarge   | 1    | 48               | 16    | 128          |
| g6e.8xlarge   | 1    | 48               | 32    | 256          |
| g6e16.xlarge  | 1    | 48               | 64    | 512          |
| g6e12.xlarge  | 4    | 192              | 48    | 384          |
| g6e24.xlarge  | 4    | 192              | 96    | 768          |
| g6e48.xlarge  | 8    | 384              | 192   | 1536         |
| gr6.8xlarge   | 1    | 24               | 32    | 256          |

You can retrieve the Amazon Machine Image (AMI) ID for Amazon ECS-optimized AMIs by querying
the AWS Systems Manager Parameter Store API. Using this parameter, you don't need to manually look up
Amazon ECS-optimized AMI IDs. For more information about the Systems Manager Parameter Store API, see
[GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md"). The user that you
use must have the `ssm:GetParameter` IAM permission to retrieve the
Amazon ECS-optimized AMI metadata.

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/gpu/recommended --region `us-east-1``
```

## Considerations

###### Note

The support for g2 instance family type has been deprecated.

The p2 instance family type is only supported on versions earlier than
`20230912` of the Amazon ECS GPU-optimized AMI. If you need to continue
to use p2 instances, see [What to do if you need a P2 instance](#p2-instance "#p2-instance").

In-place updates of the NVIDIA/CUDA drivers on both these instance family types
will cause potential GPU workload failures.

We recommend that you consider the following before you begin working with GPUs on
Amazon ECS.

- Your clusters can contain a mix of GPU and non-GPU container instances.
- You can run GPU workloads on external instances. When registering an external
  instance with your cluster, ensure the `--enable-gpu` flag is
  included on the installation script. For more information, see [Registering an external instance to an Amazon ECS cluster](ecs-anywhere-registration.md "ecs-anywhere-registration.md").
- You must set `ECS_ENABLE_GPU_SUPPORT` to `true` in your
  agent configuration file. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").
- When running a task or creating a service, you can use instance type
  attributes when you configure task placement constraints to determine the
  container instances the task is to be launched on. By doing this, you can more
  effectively use your resources. For more information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

The following example launches a task on a `g4dn.xlarge` container
instance in your default cluster.

```
`aws ecs run-task --cluster default --task-definition ecs-gpu-task-def \
 **--placement-constraints type=memberOf,expression="attribute:ecs.instance-type == g4dn.xlarge"** --region us-east-2`
```

- For each container that has a GPU resource requirement that's specified in the
  container definition, Amazon ECS sets the container runtime to be the NVIDIA
  container runtime.
- The NVIDIA container runtime requires some environment variables to be set in
  the container to function properly. For a list of these environment variables,
  see [Specialized Configurations with Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html?highlight=environment%20variable "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html?highlight=environment%20variable"). Amazon ECS sets the
  `NVIDIA_VISIBLE_DEVICES` environment variable value to be a list
  of the GPU device IDs that Amazon ECS assigns to the container. For the other
  required environment variables, Amazon ECS doesn't set them. So, make sure that your
  container image sets them or they're set in the container definition.
- The p5 instance type family is supported on version `20230929` and
  later of the Amazon ECS GPU-optimized AMI.
- The g4 instance type family is supported on version `20230913` and
  later of the Amazon ECS GPU-optimized AMI. For more information, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md"). It's not
  supported in the Create Cluster workflow in the Amazon ECS console. To use these
  instance types, you must either use the Amazon EC2 console, AWS CLI, or API and
  manually register the instances to your cluster.
- The p4d.24xlarge instance type only works with CUDA 11 or later.
- The Amazon ECS GPU-optimized AMI has IPv6 enabled, which causes issues when using
  `yum`. This can be resolved by configuring `yum` to use
  IPv4 with the following command.

```
`echo "ip_resolve=4" >> /etc/yum.conf`
```

- When you build a container image that doesn't use the NVIDIA/CUDA base
  images, you must set the `NVIDIA_DRIVER_CAPABILITIES` container
  runtime variable to one of the following values:

      + `utility,compute`
      + `all`

  For information about how to set the variable, see [Controlling the NVIDIA Container Runtime](https://sarus.readthedocs.io/en/stable/user/custom-cuda-images.html#controlling-the-nvidia-container-runtime "https://sarus.readthedocs.io/en/stable/user/custom-cuda-images.html#controlling-the-nvidia-container-runtime") on the NVIDIA
  website.

- GPUs are not supported on Windows containers.

## Share GPUs

When you want to share GPUs, you need to configure the following.

1. Remove GPU resource requirements from your task definitions so that Amazon ECS does
   not reserve any GPUs that should be shared.
2. Add the following user data to your instances when you want to share GPUs.
   This will make nvidia the default Docker container runtime on the container
   instance so that all Amazon ECS containers can use the GPUs. For more information see
   [Run
   commands when you launch an EC2 instance with user data input](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md") in the
   _Amazon EC2 User Guide_.

```
const userData = ec2.UserData.forLinux();
 userData.addCommands(
 'sudo rm /etc/sysconfig/docker',
 'echo DAEMON_MAXFILES=1048576 | sudo tee -a /etc/sysconfig/docker',
 'echo OPTIONS="--default-ulimit nofile=32768:65536 --default-runtime nvidia" | sudo tee -a /etc/sysconfig/docker',
 'echo DAEMON_PIDFILE_TIMEOUT=10 | sudo tee -a /etc/sysconfig/docker',
 'sudo systemctl restart docker',
);
```

3. Set the `NVIDIA_VISIBLE_DEVICES` environment variable on your
   container. You can do this by specifying the environment variable in your task
   definition. For information on the valid values, see [GPU Enumeration](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html#gpu-enumeration "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html#gpu-enumeration") on the NVIDIA documentation site.

## What to do if you need a P2 instance

If you need to use P2 instance, you can use one of the following options to continue
using the instances.

You must modify the instance user data for both options. For more information see
[Run
commands when you launch an EC2 instance with user data input](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md") in the
_Amazon EC2 User Guide_.

**Use the last supported GPU-optimized AMI**

You can use the `20230906` version of the GPU-optimized AMI, and add the
following to the instance user data.

Replace cluster-name with the name of your cluster.

```
#!/bin/bash
echo "exclude=*nvidia* *cuda*" >> /etc/yum.conf
echo "ECS_CLUSTER=`cluster-name`" >> /etc/ecs/ecs.config
```

**Use the latest GPU-optimized AMI, and update the user
data**

You can add the following to the instance user data. This uninstalls the Nvidia
535/Cuda12.2 drivers, and then installs the Nvidia 470/Cuda11.4 drivers and fixes the
version.

```
#!/bin/bash
yum remove -y cuda-toolkit* nvidia-driver-latest-dkms*
tmpfile=$(mktemp)
cat >$tmpfile <<EOF
[amzn2-nvidia]
name=Amazon Linux 2 Nvidia repository
mirrorlist=\$awsproto://\$amazonlinux.\$awsregion.\$awsdomain/\$releasever/amzn2-nvidia/latest/\$basearch/mirror.list
priority=20
gpgcheck=1
gpgkey=https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/7fa2af80.pub
enabled=1
exclude=libglvnd-*
EOF

mv $tmpfile /etc/yum.repos.d/amzn2-nvidia-tmp.repo
yum install -y system-release-nvidia cuda-toolkit-11-4 nvidia-driver-latest-dkms-470.182.03
yum install -y libnvidia-container-1.4.0 libnvidia-container-tools-1.4.0 nvidia-container-runtime-hook-1.4.0 docker-runtime-nvidia-1

echo "exclude=*nvidia* *cuda*" >> /etc/yum.conf
nvidia-smi
```

**Create your own P2 compatible GPU-optimized
AMI**

You can create your own custom Amazon ECS GPU-optimized AMI that is compatible with P2
instances, and then launch P2 instances using the AMI.

1. Run the following command to clone the `amazon-ecs-ami
repo`.

```
git clone https://github.com/aws/amazon-ecs-ami
```

2. Set the required Amazon ECS agent and source Amazon Linux AMI versions in
   `release.auto.pkrvars.hcl` or
   `overrides.auto.pkrvars.hcl`.
3. Run the following command to build a private P2 compatible EC2 AMI.

Replace region with the Region with the instance
Region.

```
REGION=`region` make al2keplergpu
```

4. Use the AMI with the following instance user data to connect to the Amazon ECS
   cluster.

Replace cluster-name with the name of your cluster.

```
#!/bin/bash
echo "ECS_CLUSTER=`cluster-name`" >> /etc/ecs/ecs.config
```
