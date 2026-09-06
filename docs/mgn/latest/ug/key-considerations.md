

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launch template key considerations
<a name="key-considerations"></a>

There are several key considerations when configuring your EC2 launch template. Review these key considerations as well as the [full launch settings](detailed-considerations.md) before creating your launch template.

1. **Instance Type** – Ensure that you select an instance type that matches the hardware requirements of your source server. AWS Transform MGN always uses the instance type that is set on the Amazon EC2 launch template unless the **Instance right-sizing** feature is activated.
**Note**  
If you change your instance type and do not deactivate the instance right-sizing feature, then AWS Transform MGN uses the instance type determined by the **Instance right-sizing** feature and not the instance type you chose in the EC2 launch template. MGN verifies the instance type once per hour, as a result, if you did not deactivate the instance right-sizing feature, the first time instance launch may still use the instance type you set in the EC2 launch template, but any subsequent launches use the right-sizing instance.
The available capacity for each Amazon EC2 instance type varies by Availability Zone and Region, and may be subject to your specific AWS account limits. For mission-critical workloads consider using [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) to guarantee capacity for specific instance types. Note that additional costs apply when reserving capacity.

1. **Subnet** – You can select an existing subnet or create a new subnet. 
**Note**  
Customers that do not have a default VPC must modify the EC2 launch template and explicitly define the subnet in which to launch. Failure to do so results in errors when launching test or cutover instances.

1. **Private IP** – If you use the **Copy private IP** feature, then do not add your own IP to the EC2 launch template. Private IP is not supported for IPv6.

1. **Private IP and Subnet** – Each subnet contains a CIDR block of IP ranges. If you use the **Copy private IP** feature, then ensure that this IP is included in the CIDR block range. Otherwise, instance launch fails.

1. **Private IP and ENI** – Make sure that you deactivate the **Copy private IP** feature if you wish to define an ENI to use on the EC2 launch template.

1. **Network interfaces** – The EC2 launch template only supports two network interfaces. If you require more than two network interfaces, you need to define them after the test or cutover instance has been launched. This can be done through a post launch action.

   If you wish to use an Elastic IP, you must create an ENI to specify the IP and then edit the Network interfaces to use the ENI. Learn more about working with Elastic network interfaces in [the Amazon EC2 User Guide.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

1. **Networking platform** – AWS Transform MGN only supports **Virtual Private Cloud (VPC)**. EC2-Classic is **not** supported. Do **not** add any security groups under the network platform.

1. **Custom device name** – Do not alter this field. AWS Transform MGN uses the device name as defined on the source server to map disks on the test or cutover instance. You can use this field to identify your disks. 

1. **Disks** – You cannot add disks to the EC2 launch template. Any disks that are added that do not exist on the source machine are ignored by AWS Transform MGN. 

1. **Launch template name** – Do not alter this field. AWS Transform MGN automatically names this field.

1. **System tag** – Do not alter this field. MGN automatically adds system tags that match the EC2 launch template to the specific source server. You can recognize which source server the launch template is matched with by the **ID** field.

1. **Automatic cleanup** – MGN deletes the EC2 launch template and launch configuration for machines that have been disconnected from AWS Transform MGN or machines for which the cutover has been finalized 90 minutes after disconnect or cutover finalization. This aids in ensuring that your account does not surpass the AWS 5000 EC2 launch template limit.
**Note**  
When using FSx for ONTAP as the target storage type, the FSx for ONTAP split clone operation may take longer than 90 minutes. In this case, the EC2 instance and launch template are cleaned up within the standard 90-minute window, but the replica FSx for ONTAP volume may remain active until the split clone operation completes.

1. **Volumes** – For each storage volume, the service uses the user-selected values. If no matching volume exists in the launch template, the service uses the default value. If the launch template includes a volume that does not exist in the source server, the system disregards the specific volume.

    If you delete the EC2 launch template, the service creates a new one with default values. 

    
**Note**  
You can set a per-volume KMS key directly in the EC2 launch template's storage section. If set, the launch template KMS key takes precedence over the replication snapshot's key. Alternatively, you can configure encryption through the [EBS Encryption](ebs-storage.md#ebs-encryption) section of the replication settings.