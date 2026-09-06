

# Key considerations for EC2 launch templates
<a name="ec2-key-considerations"></a>

Review the following key rules and interactions before you modify an EC2 launch template for use with AWS Elastic Disaster Recovery.

1. **Instance type** – AWS Elastic Disaster Recovery uses the instance type set on the launch template unless Instance type right-sizing is activated. If right-sizing is active, it overrides the launch template value.

1. **Subnet** – If you do not have a default VPC, you must explicitly define the subnet. Failure to do so results in errors when launching drill or recovery instances.

1. **Private IP and subnet** – If you use the Copy private IP feature, ensure that the IP is included in the subnet's CIDR block range. Otherwise, instance launch fails.

1. **Network interfaces** – AWS Elastic Disaster Recovery manages the primary network interface (device index 0). Additional network interfaces defined in the launch template are preserved and passed through at launch time.

1. **Custom device name** – Do not alter this field. AWS Elastic Disaster Recovery uses the device name as defined on the source server to map disks on the drill or recovery instance.

1. **Disks** – You cannot add disks to the EC2 launch template. Any disks added that do not exist on the source server are ignored.

1. **Launch template name** – Do not alter this field. AWS Elastic Disaster Recovery automatically generates this name.

1. **Volumes** – For each EBS volume, AWS Elastic Disaster Recovery uses the user-selected values. If no matching volume exists in the launch template, AWS Elastic Disaster Recovery uses default values. If the launch template includes a volume that does not exist on the source server, the system disregards it. If you delete the EC2 launch template, the service creates a new one with default values.

1. **Volume initialization rate** – AWS Elastic Disaster Recovery preserves `VolumeInitializationRate` values that you set on launch template Amazon EBS block device mappings. AWS Elastic Disaster Recovery passes the rate to volume creation during drill and recovery launches to accelerate volume initialization. If volume creation fails because of the rate, AWS Elastic Disaster Recovery retries without it to prevent the rate from blocking recovery. Possible failure reasons include quota limits exceeded or an unsupported Availability Zone. This feature is available only in AWS Regions and environments that support Amazon EBS volume initialization rate. For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-initialize.html).

1. **KMS key** – Encryption for recovery volumes is controlled through the EBS Encryption section of the replication settings within the AWS Elastic Disaster Recovery console. The launch template's KMS key field is not used by AWS Elastic Disaster Recovery during volume creation. To encrypt recovery volumes with a specific KMS key, configure it in the replication settings.

1. **Automatic cleanup** – AWS Elastic Disaster Recovery deletes the EC2 launch template for source servers that have been disconnected from AWS Elastic Disaster Recovery or for which recovery has been finalized.

1. **Tags** – Launch template tags always take precedence over tags set in the AWS Elastic Disaster Recovery console or tags manually added to the server.

1. **Launch template AMI** – Make sure your launch template AMI matches the boot mode of your source server. If the source uses Unified Extensible Firmware Interface (UEFI), the chosen AMI must support UEFI.