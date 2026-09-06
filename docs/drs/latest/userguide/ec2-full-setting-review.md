

# Full launch template setting review
<a name="ec2-full-setting-review"></a>

The following sections describe each EC2 launch template field and indicate whether you can safely change it. Fields marked **Do not change** must remain at their default values for AWS Elastic Disaster Recovery to function properly.

## Top-level fields
<a name="ec2-full-setting-top-level"></a>

**Launch template name – Do not change**  
AWS Elastic Disaster Recovery automatically generates the launch template name to maintain the association between the template and its source server. Changing this name breaks the link between the source server and its launch configuration.

**Template version description – You can edit**  
You can update the version description to track changes you make to the template. This field is informational and does not affect launch behavior.

**AMI – Do not typically set**  
AWS Elastic Disaster Recovery creates the appropriate AMI from the replicated source server data during drill or recovery. Setting an AMI manually overrides this behavior and can result in an instance that does not match your source server.

**Instance type – You can edit**  
Set the instance type to use when launching drill or recovery instances. If Instance type right-sizing is active, the right-sizing value overrides this setting. If no instance type is specified, AWS Elastic Disaster Recovery uses a default value.

## Storage (volumes)
<a name="ec2-full-setting-storage"></a>

**Device name – Do not change**  
AWS Elastic Disaster Recovery uses the device name from the source server to map disks to the drill or recovery instance. Changing this value causes disk mapping failures.

**Snapshot – Do not change**  
AWS Elastic Disaster Recovery manages snapshots as part of the replication process. Specifying a different snapshot causes the launched instance to use data that does not reflect the source server state.

**Size – You can increase**  
Do not decrease the volume size below the source disk size, as this causes launch failures. You can increase the size if you need additional capacity on the recovery instance. Be aware that AWS Elastic Disaster Recovery automatically increases this value if the source disk grows larger than the value set in the launch template.

**Volume type – You can edit**  
You can change the EBS volume type. The default is `gp3`. Valid options include `gp2`, `gp3`, `io1`, `io2`, `st1`, `sc1`, and `standard`.

**IOPS – You can edit**  
You can set the provisioned IOPS for volume types that support this setting (`io1`, `io2`, and `gp3`).

**Throughput – You can edit**  
You can set the throughput (in MiB/s) for `gp3` volumes only.

**Delete on termination – You can set**  
Specify whether to delete the volume when the instance terminates. Set this based on your data retention requirements.

**Encrypted – Not used by DRS**  
The launch template Encrypted field is not used by AWS Elastic Disaster Recovery. Recovery volume encryption is determined by the EBS Encryption section of the replication settings.

**KMS key – Not used by DRS**  
The launch template KMS key field is not used by AWS Elastic Disaster Recovery. Recovery volume encryption is determined by the EBS Encryption section of the replication settings. To use a customer managed key for recovery volumes, configure it in the replication settings rather than the launch template.

**Important**  
Do not add additional disks to the launch template. Any volumes defined in the launch template that do not exist on the source server are ignored by AWS Elastic Disaster Recovery.

## Network interfaces
<a name="ec2-full-setting-network"></a>

**Device index – Do not change**  
The device index must remain set to `0` for the primary network interface. AWS Elastic Disaster Recovery requires the primary interface to be at index 0 for proper instance configuration.

**Subnet – You can edit**  
Specify the subnet in which to launch the drill or recovery instance. If you do not have a default VPC, you must set this value. For cross-AZ recovery, ensure that the subnet is not in the same Availability Zone as your source instances.

**Auto-assign public IP – You can edit**  
Specify whether to automatically assign a public IP address to the launched instance. Set this based on your network access requirements.

**Primary IP – You can edit**  
The Copy private IP feature uses this field. If you enable Copy private IP, ensure the specified IP is within the subnet's CIDR block range. Otherwise, instance launch fails.

**Security groups – You can edit**  
Specify the security groups to assign to the launched instance. Security groups can only be set if a subnet is defined.

**Delete on termination – You can set**  
Set this to **Yes** so that network interfaces are cleaned up when you terminate drill or recovery instances.

## System configuration fields – Do not change
<a name="ec2-full-setting-advanced"></a>

The following advanced detail fields must remain unchanged for AWS Elastic Disaster Recovery to function properly. Changing these values can cause launch failures or unexpected instance behavior.
+ RAM disk ID
+ Kernel
+ Nitro Enclave
+ Metadata accessible – AWS Elastic Disaster Recovery uses instance metadata to determine whether an instance is a recovery instance so that it can complete final recovery tasks.