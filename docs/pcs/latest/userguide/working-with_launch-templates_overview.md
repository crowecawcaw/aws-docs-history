

# Overview of launch templates in AWS PCS

An Amazon EC2 launch template can include more than 30 [parameters](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.html) that control how instances are configured. Most are fully compatible with AWS PCS, but there are some exceptions.

AWS PCS doesn't use the following launch template parameters, either because it manages the setting itself or because it doesn't support the parameter:
+ **Instance type/Specify instance type attributes** (`InstanceRequirements`) – AWS PCS doesn't support attribute-based instance selection.
+ **Instance type** (`InstanceType`) – Specify instance types when you create a compute node group.
+ **Advanced details/IAM instance profile** (`IamInstanceProfile`) – You provide this when you create or update the compute node group.
+ **Advanced details/Disable API termination** (`DisableApiTermination`) – AWS PCS must control the lifecycle of the compute nodes that it launches.
+ **Advanced details/Disable API stop** (`DisableApiStop`) – AWS PCS must control the lifecycle of the compute nodes that it launches.
+ **Advanced details/Stop – Hibernate behavior** (`HibernationOptions`) – AWS PCS doesn't support instance hibernation.
+ **Advanced details/Elastic GPU** (`ElasticGpuSpecifications`) – Amazon Elastic Graphics reached end of life on January 8, 2024. AWS PCS rejects a launch template that includes this parameter.
+ **Advanced details/Elastic inference** (`ElasticInferenceAccelerators`) – Amazon Elastic Inference is no longer available to new customers. AWS PCS rejects a launch template that includes this parameter.
+ **Advanced details/Specify CPU options/Threads per core** (`ThreadsPerCore`) – AWS PCS sets the number of threads per core to 1.

These parameters have special requirements that support compatibility with AWS PCS:
+ **User data** (`UserData`) – User data must be MIME multipart encoded. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md).
+ **Application and OS Images** (`ImageId`) – You can specify an AMI ID in the launch template. If you also specify an AMI ID on the compute node group, AWS PCS uses that AMI instead of the value in the launch template. The AMI must be compatible with AWS PCS. For more information, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md).
+ **Network settings/Firewall (security groups)** (`SecurityGroups`) – You can't specify security group names. Instead, specify security group IDs (`SecurityGroupIds`). If the launch template defines network interfaces, specify security group IDs for each interface instead. If you also specify security groups on the compute node group, AWS PCS uses only those security groups instead of the ones in the launch template. It doesn't add the security groups in the launch template. You can't specify security groups on the compute node group if the launch template defines network interfaces. For more information, see [Security groups in AWS PCS](working-with_networking_sg.md).
+ **Key pair (login)** (`KeyName`) – You can specify a key pair in the launch template. If you also specify an SSH key pair on the compute node group, AWS PCS uses that key pair instead of the value in the launch template.
+ **Network settings/Advanced network configuration** (`NetworkInterfaces`) – If your instances use a single network card and don't need specialized networking, AWS PCS can configure instance networking for you. To configure multiple network cards or to enable Elastic Fabric Adapter on your instances, use `NetworkInterfaces`. Each network interface must have a list of security group IDs under `Groups`. For more information, see [Multiple network interfaces in AWS PCS](working-with_networking_multi-nic.md).
+ **Advanced details/Capacity reservation** (`CapacityReservationSpecification`) – This can be set, but cannot reference a specific `CapacityReservationId` when working with AWS PCS. You can, however, reference a capacity reservation group, where that group contains one or more capacity reservations. For more information, see [Capacity Reservations in AWS PCS](working-with_capacity-reservations.md).