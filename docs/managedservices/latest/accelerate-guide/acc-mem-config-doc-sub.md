# Accelerate Configuration profile: pseudoparameter substitution

In either of the configuration profiles, you can specify pseudoparameters that are substituted in place as follows:

- Global - anywhere in the profile:
  - ${AWS::AccountId}: Replaced with your AWS account ID
  - ${AWS::Partition}: Replaced with the partition of the AWS Region the resource is in (this is 'aws' for most Regions); for more information, see the
    entry for partition in the
    [ARN reference](https://docs.amazonaws.cn/en_us/general/latest/gr/aws-arns-and-namespaces.html "https://docs.amazonaws.cn/en_us/general/latest/gr/aws-arns-and-namespaces.html").
  - ${AWS::Region}: Replaced with the Region name of the Region that your resource is deployed to (for example us-east-1)

- In an **AWS::EC2::Instance** resource type block:
  - ${EC2::InstanceId}: (**identifier**) replaced by the instance ID of your Amazon EC2 instance.
  - ${EC2::InstanceName}: replaced by the name of your Amazon EC2 instance.

- In an **AWS::EC2::Instance::Disk** resource type block:
  - ${EC2::InstanceId}: (**identifier**) Replaced by the instance ID of your Amazon EC2 instance.
  - ${EC2::InstanceName}: Replaced by the name of your Amazon EC2 instance.
  - ${EC2::Disk::Device}: (**identifier**) Replaced by the name of the disk. (Linux only, on instances managed by the
    [CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")).
  - ${EC2::Disk::FSType}: (**identifier**) Replaced by the file system type of the disk. (Linux only, on instances managed by the
    [CloudWatchAgent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")).
  - ${EC2::Disk::Path}: (**identifier**) Replaced by the disk path. On Linux, this is the mount point
    of the disk (for example, /), while in Windows this is the drive label (for example, c:/ ) (only on an instance managed by the
    [CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")).
  - ${EC2::Disk::UUID}: (**identifier**) Replaced by a generated UUID that uniquely identifies the
	 disk, this must be specified in the name of the alarm, as an alarm under AWS::EC2::Instance::Disk resource type will create one alarm per volume. Specifying
	 ${EC2::Disk::UUID} will maintain uniqueness of alarm names.

- In an **AWS::EKS::Cluster** resource type block:
  - ${EKS::ClusterName}: (**identifier**) replaced by the name of your EKS Cluster.

- In an **AWS::OpenSearch::Domain** resource type block:
  - ${OpenSearch::DomainName}: (**identifier**) replaced by the name of your EKS Domain.

- In an **AWS::ElasticLoadBalancing::LoadBalancer** resource type block:
  - ${ElasticLoadBalancing::LoadBalancer::Name}: (**identifier**) replaced by the name of your V1 Load Balancer.

- In an **AWS::ElasticLoadBalancingV2::LoadBalancer** resource type block:
  - ${ElasticLoadBalancingV2::LoadBalancer::Arn}: (**identifier**) replaced by the ARN of your V2 Load Balancer.
  - ${ElasticLoadBalancingV2::LoadBalancer::Name}: (**identifier**) replaced by the name of your V2 Load Balancer.
  - ${ElasticLoadBalancingV2::LoadBalancer::FullName}: (**identifier**) replaced by the full name of your V2 Load Balancer.

- In an **AWS::ElasticLoadBalancingV2::LoadBalancer::TargetGroup** resource type block:
  - ${ElasticLoadBalancingV2::TargetGroup::FullName}: (**identifier**) replaced by the target group name of your V2 Load Balancer.
  - ${ElasticLoadBalancingV2::TargetGroup::UUID}: (**identifier**) replaced by a generated UUID for your V2 Load Balancer.

- In an **AWS::EC2::NatGateway** resource type block:
  - ${NatGateway::NatGatewayId}: (**identifier**) replaced by the NAT Gateway ID.

- In an **AWS::RDS::DBInstance** resource type block:
  - ${RDS::DBInstanceIdentifier}: (**identifier**) replaced by your RDS DB instance identifier.

- In an **AWS::RDS::DBCluster** resource type block:
  - ${RDS::DBClusterIdentifier}: (**identifier**) replaced by your RDS DB cluster identifier.

- In an **AWS::Redshift::Cluster** resource type block:
  - ${Redshift::ClusterIdentifier}: (**identifier**) replaced by your Redshift cluster identifier.

- In an **AWS::Synthetics::Canary** resource type block:
  - ${Synthetics::CanaryName}: (**identifier**) replaced by the name of your CloudWatch Synthetics canary.

- In an **AWS::EC2::VPNConnection** resource type block:
  - ${AWS::EC2::VpnConnectionId}: (**identifier**) replaced by your VPN ID.

- In an **AWS::EFS::FileSystem** resource type block:
  - ${EFS::FileSystemId}: (**identifier**) Replaced by the file system ID of your EFS file system.

- In an **AWS::FSx::FileSystem::ONTAP** resource type block:
  - ${FSx::FileSystemId}: (**identifier**) Replaced by the file system ID of your FSX filesystem.
  - ${FSx::FileSystem::Throughput}: Replaced by the throughput of your FSX file system.
  - ${FSx::FileSystem::Iops}: Replaced by the IOPS of the FSX file system.

- In an **AWS::FSx::FileSystem::ONTAP::Volume** resource type block:
  - ${FSx::FileSystemId}: (**identifier**) Replaced by the file system ID of your FSX file system.
  - ${FSx::ONTAP::VolumeId}: (**identifier**) Replaced by the volume ID.

- In an **AWS::FSx::FileSystem::Windows** resource type block:
  - ${FSx::FileSystemId}: (**identifier**) Replaced by the file system ID of your FSX file system.
  - ${FSx::FileSystem::Throughput}: Replaced by the throughput of your FSX file system.

###### Note

All parameters marked with **identifier** are used as a prefix for
the name of created alarms, unless you specify that identifier in the alarm name.
