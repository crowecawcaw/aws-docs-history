# Creating mount targets

You need a mount target to access your file system from compute resources and you can
create a maximum of one mount target per Availability Zone. We recommend creating one mount target
per Availability Zone you operate in. When you create a file system using the S3 console, S3
Files automatically creates one mount target in every Availability Zone in your default
VPC.

You can create mount targets for the file system in one VPC at a time. If you want to
modify the VPC for your mount targets, you need to first delete all the existing mount targets
for the file system and then create a mount target in a new VPC. If the VPC has multiple
subnets in an Availability Zone, you can create a mount target in only one of those subnets.
All EC2 instances in the Availability Zone can share the single mount target.

This section explains how to use the Amazon S3 console to create a mount target
for S3 Files.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, verify you are in the
   AWS Region of the file system for which you want to create a mount
   target.
3. In the left navigation pane, choose **General
   purpose buckets**.
4. Choose a general purpose bucket your file system is attached
   to.
5. Select the **File systems** tab and
   select your desired file system.
6. Select the **Mount targets** tab and
   select **Create mount
   targets**.
7. On the Create mount target page, your default VPC will automatically be
   selected. Choose the Availability Zone and Subnet ID. The VPC, Availability
   Zone, and Subnet ID cannot be edited after mount target creation.

###### Note

The IP address type must match the IP type of the subnet. Additionally,
the IP address type overrides the IP addressing attribute of your subnet.
For example, if the IP address type is IPv4-only and the IPv6 addressing
attribute is enabled for your subnet, network interfaces created in the
subnet receive an IPv4 address from the range of the subnet. For more
information, see [Modify the IP
addressing attributes of your subnet](../../../vpc/latest/userguide/modify-subnets.md "../../../vpc/latest/userguide/modify-subnets.md"). 8. If you know the IP address where you want to place the mount target, then
enter it in the IP address box that matches the IP address type. If you don't
specify a value, S3 Files selects an unused IP address from the specified
subnet. 9. Choose your security groups to associate with the mount target. See
[Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups "s3-files-prereq-policies.md#s3-files-prereq-security-groups") in the prerequisites
to understand the security group configurations required to start using your
file system. 10. Choose **Create mount
target**.
The following `create-mount-target` example command shows how you can
use the AWS CLI to create a mount target for S3 Files.

```
aws s3files create-mount-target --region `aws-region` --file-system-id `file-system-id` --subnet-id `subnet-id`
```

Mount targets can take up to ~5 minutes to create.
