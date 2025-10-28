# Launch a GPU container instance for Amazon ECS

To use a GPU instance on Amazon ECS on Amazon EC2, you need to create a launch template, a user
data file, and launch the instance.

You can then run a task that uses a task definition configured for GPU.

## Use a launch template

You can create a launch template.

- Create a launch template that uses the Amazon ECS-optimized GPU AMI ID For the
  AMI. For information about how to create a launch template, see [Create a new launch template using parameters you define](../../../AWSEC2/latest/UserGuide/create-launch-template.md#create-launch-template-define-parameters "../../../AWSEC2/latest/UserGuide/create-launch-template.md#create-launch-template-define-parameters") in the
  _Amazon EC2 User Guide_.

Use the AMI ID from the previous step for the **Amazon Machine
image**. For information about how to specify the AMI ID with
the Systems Manager parameter, see [Specify a Systems Manager parameter in a launch template](../../../AWSEC2/latest/UserGuide/create-launch-template.md#use-an-ssm-parameter-instead-of-an-ami-id "../../../AWSEC2/latest/UserGuide/create-launch-template.md#use-an-ssm-parameter-instead-of-an-ami-id") in the _Amazon EC2 User Guide_.

Add the following to the **User data** in the launch
template. Replace `cluster-name` with the name of
your cluster.

```
#!/bin/bash
echo ECS_CLUSTER=`cluster-name` >> /etc/ecs/ecs.config;
echo ECS_ENABLE_GPU_SUPPORT=true >> /etc/ecs/ecs.config
```

## Use the AWS CLI

You can use the AWS CLI to launch the container instance.

1. Create a file that's called `userdata.toml`. This file is used
   for the instance user data. Replace `cluster-name`
   with the name of your cluster.

```
#!/bin/bash
echo ECS_CLUSTER=`cluster-name` >> /etc/ecs/ecs.config;
echo ECS_ENABLE_GPU_SUPPORT=true >> /etc/ecs/ecs.config
```

2. Run the following command to get the GPU AMI ID. You use this in the
   following step.

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/gpu/recommended --region `us-east-1``
```

3. Run the following command to launch the GPU instance. Remember to replace
   the following parameters:
   - Replace `subnet` with the ID of the
     private or public subnet that your instance will launch in.
   - Replace `gpu_ami` with the AMI ID from
     the previous step.
   - Replace `t3.large` with the instance type
     that you want to use.
   - Replace `region` with the
     Region code.

```
aws ec2 run-instances --key-name ecs-gpu-example \
   --subnet-id `subnet` \
   --image-id `gpu_ami` \
   --instance-type `t3.large` \
   --region `region` \
   --tag-specifications 'ResourceType=instance,Tags=[{Key=GPU,Value=example}]' \
   --user-data file://userdata.toml \
   --iam-instance-profile Name=ecsInstanceRole
```

4. Run the following command to verify that the container instance is
   registered to the cluster. When you run this command, remember to replace
   the following parameters:
   - Replace `cluster` with your cluster
     name.
   - Replace `region` with your
     Region code.

```
aws ecs list-container-instances --cluster `cluster-name` --region `region`
```
