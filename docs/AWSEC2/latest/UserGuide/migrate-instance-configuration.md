# Migrate to a new instance type by launching a new EC2 instance

You can change the instance type of an EC2 instance only if it is an EBS-backed instance
with a configuration that is compatible with the new instance type that you want. Otherwise,
if the configuration or your instance is not compatible with the new instance type, or it is
an instance store-based instance, you must launch a replacement instance that is compatible
with the instance type that you want. For more information about how compatibility is
determined, see [Compatibility for changing the instance type](resize-limitations.md "resize-limitations.md").

###### Overview of the migration process

- Back up the data on the original instance.
- Launch a new instance with a configuration that is compatible with the new instance
  type that you want, attaching any EBS volumes that were attached to your original
  instance.
- Install your application on your new instance.
- Restore any data.
- If the original instance has an Elastic IP address, you must associate it with your
  new instance to ensure that your users can continue to use your application without
  interruption.

###### To migrate an instance to a new instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Back up any data that you still need as follows:
   - Connect to your instance and copy the data on your instance store volumes
     to persistent storage.
   - [Create snapshots](../../../ebs/latest/userguide/ebs-creating-snapshot.md "../../../ebs/latest/userguide/ebs-creating-snapshot.md") of your EBS volumes so that you can create new
     volumes with the same data, or detach the volumes from the original
     instance so that you can attach them to the new instance.

3. In the navigation pane, choose **Instances**.
4. Choose **Launch instances**. When you configure the instance,
   do the following:
   1. Select an AMI that supports the instance type that you want. For example,
      you must select an AMI that supports the processor type of the new instance type.
      Also, current generation instance types require an HVM AMI.
   2. Select the new instance type that you want. If the instance type that you
      want isn't available, then it's not compatible with the configuration of the
      AMI that you selected.
   3. If you want to allow the same traffic to reach the new instance, select
      the same VPC and security group that are used with the original instance.
   4. When you're done configuring your new instance, complete the steps to
      select a key pair and launch your instance. It can take a few minutes for the
      instance to enter the `running` state.

5. If you backed up data to an EBS snapshot,
   [create a volume from the snapshot](../../../ebs/latest/userguide/ebs-creating-volume.md#ebs-create-volume-from-snapshot "../../../ebs/latest/userguide/ebs-creating-volume.md#ebs-create-volume-from-snapshot") and then [attach the volume](../../../ebs/latest/userguide/ebs-attaching-volume.md "../../../ebs/latest/userguide/ebs-attaching-volume.md") to the new instance.

To move an EBS volume from the original instance to the new instance,
[detach the volume](../../../ebs/latest/userguide/ebs-detaching-volume.md "../../../ebs/latest/userguide/ebs-detaching-volume.md")
from the original instance and then [attach the volume](../../../ebs/latest/userguide/ebs-attaching-volume.md "../../../ebs/latest/userguide/ebs-attaching-volume.md") to the new instance. 6. Install your application and any required software on the new instance. 7. Restore any data that you backed up from the instance store volumes of the
original instance. 8. If the original instance has an Elastic IP address, assign it to the new instance as
follows:

    1. In the navigation pane, choose **Elastic IPs**.
    2. Select the Elastic IP address that is associated with the original
     instance and choose **Actions**, **Disassociate
     Elastic IP address**. When prompted for confirmation, choose
     **Disassociate**.
    3. With the Elastic IP address still selected, choose
     **Actions**, **Associate Elastic IP
     address**.
    4. For **Resource type**, choose
     **Instance**.
    5. For **Instance**, choose the new instance.
    6. (Optional) For **Private IP address**, specify a private
     IP address with which to associate the Elastic IP address.
    7. Choose **Associate**.

9. (Optional) You can terminate the original instance if it's no longer needed.
   Select the instance, verify that you are about to terminate the original instance
   and not the new instance (for example, check the name or launch time), and then
   choose **Instance state**, **Terminate
   instance**.
