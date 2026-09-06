

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Change target storage type
<a name="staging-disk-ref"></a>

You can change the target storage type for all disks on a source server. The available options are Amazon Elastic Block Store (Amazon EBS) and Amazon FSx for NetApp ONTAP. This change applies to all disks on the server.

When using Amazon EBS, you can also customize the Amazon EBS volume type for each individual disk or group of disks. For details, see [Change staging disk type](ebs-storage.md#staging-disk) in the [Amazon EBS configuration](ebs-storage.md).

For information on configuring FSx for ONTAP as the target storage type, see the [FSx for ONTAP configuration](fsx-ontap.md).