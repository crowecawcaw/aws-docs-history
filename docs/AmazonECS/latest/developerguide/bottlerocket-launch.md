# Launching a Bottlerocket

instance for Amazon ECS

You can launch a Bottlerocket instance so that you can run your container
workloads.

You can use the AWS CLI to launch the Bottlerocket instance.

1. Create a file that's called `userdata.toml`. This file is used for the instance
   user data. Replace `cluster-name` with the name of your
   cluster.

```
[settings.ecs]
cluster = "`cluster-name`"
```

2. Use one of the commands that are included in [Retrieving Amazon ECS-optimized
   Bottlerocket AMI metadata](ecs-bottlerocket-retrieve-ami.md "ecs-bottlerocket-retrieve-ami.md")
   to get the Bottlerocket AMI ID. You use this in the following
   step.
3. Run the following command to launch the Bottlerocket instance. Remember to
   replace the following parameters:
   - Replace `subnet` with the ID of the private
     or public subnet that your instance will launch in.
   - Replace `bottlerocket_ami` with the AMI ID
     from the previous step.
   - Replace `t3.large` with the instance type
     that you want to use.
   - Replace `region` with the
     Region code.

```
aws ec2 run-instances --key-name ecs-bottlerocket-example \
   --subnet-id `subnet` \
   --image-id `bottlerocket_ami` \
   --instance-type `t3.large` \
   --region `region` \
   --tag-specifications 'ResourceType=instance,Tags=[{Key=bottlerocket,Value=example}]' \
   --user-data file://userdata.toml \
   --iam-instance-profile Name=ecsInstanceRole
```

4. Run the following command to verify that the container instance is registered
   to the cluster. When you run this command, remember to replace the following
   parameters:
   - Replace `cluster` with your cluster
     name.
   - Replace `region` with your
     Region code.

```
aws ecs list-container-instances --cluster `cluster-name` --region `region`
```

For a detailed walkthrough of how to get started with the Bottlerocket
operating system on Amazon ECS, see [Using a Bottlerocket AMI with Amazon ECS](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md") on GitHub and Getting started with
[Bottlerocket and Amazon ECS](https://aws.amazon.com/blogs/containers/getting-started-with-bottlerocket-and-amazon-ecs/ "https://aws.amazon.com/blogs/containers/getting-started-with-bottlerocket-and-amazon-ecs/") on the AWS blog site.
