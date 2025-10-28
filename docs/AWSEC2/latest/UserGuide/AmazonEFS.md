# Use Amazon EFS with Amazon EC2 Linux instances

###### Note

Amazon EFS is not supported on Windows instances.

Amazon EFS provides scalable file storage for use with Amazon EC2. You can use an EFS file system as
a common data source for workloads and applications running on multiple instances. For more
information, see the [Amazon Elastic File System product page](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/").

This tutorial shows you how to create and attach an Amazon EFS file system using the Amazon EFS
Quick Create wizard during instance launch. For a tutorial on how to create a file system using the
Amazon EFS console, see [Getting
started with Amazon Elastic File System](../../../efs/latest/ug/getting-started.md "../../../efs/latest/ug/getting-started.md") in the _Amazon Elastic File System User Guide_.

###### Note

When you create an EFS file system using EFS Quick Create, the file system is created with the
following service recommended settings:

- [Automatic backups enabled](../../../efs/latest/ug/awsbackup.md "../../../efs/latest/ug/awsbackup.md").
- [Manage mount targets](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md")
  in the selected VPC.
- [General Purpose performance mode](../../../efs/latest/ug/performance.md#performancemodes "../../../efs/latest/ug/performance.md#performancemodes").
- [Bursting throughput mode](../../../efs/latest/ug/performance.md#throughput-modes "../../../efs/latest/ug/performance.md#throughput-modes").
- [Encryption of data at rest enabled](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md")
  using your default key for Amazon EFS (`aws/elasticfilesystem`).
- [Amazon EFS lifecycle
  management enabled](../../../efs/latest/ug/lifecycle-management-efs.md "../../../efs/latest/ug/lifecycle-management-efs.md") with a 30-day policy.

###### Tasks

- [Create an EFS file system using Amazon EFS Quick Create](#quick-create "#quick-create")
- [Test the EFS file system](#efs-test-file-system "#efs-test-file-system")
- [Delete the EFS file system](#efs-clean-up "#efs-clean-up")

## Create an EFS file system using Amazon EFS Quick Create

You can create an EFS file system and mount it to your instance when you launch your
instance using the Amazon EFS Quick Create feature of the Amazon EC2 [launch instance wizard](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

###### To create an EFS file system using Amazon EFS Quick Create

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch instance**.
3. (Optional) Under **Name and tags**, for **Name**, enter a name to
   identify your instance.
4. Under **Application and OS Images (Amazon Machine Image)**, choose a Linux operating
   system, and then for **Amazon Machine Image (AMI)**, select a Linux AMI.
5. Under **Instance type**, for **Instance type**, select an instance
   type or keep the default.
6. Under **Key pair (login)**, for **Key pair name**, choose an existing
   key pair or create a new one.
7. Under **Network settings**, choose **Edit** (at right), and then for
   **Subnet**, select a subnet.

###### Note

You must select a subnet before you can add an EFS file system. 8. Under **Configure storage**, choose **Edit** (at bottom right), and
then do the following:

    1. For **File systems**, ensure that **EFS** is selected, and
     then choose **Create new shared file system**.
    2. For **File system name** enter a name for the Amazon EFS file system, and then
     choose **Create file system**.
    3. For **Mount point**, specify a custom mount point or keep the default.
    4. To enable access to the file system, select **Automatically create and attach security
     groups**. By selecting this checkbox, the following security groups will be automatically
     created and attached to the instance and the mount targets of the file system:




    	* Instance security group – Includes an outbound rule that allows traffic over the
    	 NFS 2049port, but includes no inbound rules.
    	* File system mount targets security group – Includes an inbound rule that allows traffic
    	 over the NFS 2049 port from the instance security group (described above), and an outbound rule
    	 that allows traffic over the NFS 2049 port.
    ###### Note

    Alternatively, you can manually create and attach the security groups. If you want to manually
     create and attach the security groups, clear **Automatically create and attach the required
     security groups**.
    5. To automatically mount the shared file system when the instance launches, select **Automatically
     mount shared file system by attaching required user data script**. To view the user data that is
     automatically generated, expand **Advanced details**, and scroll down to **User
     data**.


    ###### Note

    If you added user data before selecting this checkbox, the original user data is overwritten by
     the automatically generated user data.

9. Configure any other instance configuration settings as needed.
10. In the **Summary** panel, review your instance configuration, and then choose
    **Launch instance**. For more information, see [Launch an EC2 instance using the launch
    instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

## Test the EFS file system

You can connect to your instance and verify that the file system is mounted to the
directory that you specified (for example, /mnt/efs).

###### To verify that the file system is mounted

1. Connect to your instance. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. From the terminal window for the instance, run the **df -T** command to
   verify that the EFS file system is mounted.

```
`$` `df -T``Filesystem Type 1K-blocks Used Available Use% Mounted on
/dev/xvda1 ext4 8123812 1949800 6073764 25% /
devtmpfs devtmpfs 4078468 56 4078412 1% /dev
tmpfs tmpfs 4089312 0 4089312 0% /dev/shm
`efs-dns` nfs4 9007199254740992 0 9007199254740992 0% `/mnt/efs``
```

Note that the name of the file system, shown in the example output as
`efs-dns`, has the following form.

```
`file-system-id`.efs.`aws-region`.amazonaws.com:/
```

3. (Optional) Create a file in the file system from the instance, and then verify that
   you can view the file from another instance.
   1. From the instance, run the following command to create the file.

   ```
   `$` `sudo touch `/mnt/efs`/test-file.txt`
   ```

   2. From the other instance, run the following command to view the file.

   ````
   `$` `ls `/mnt/efs```test-file.txt`
   ````

## Delete the EFS file system

If you no longer need your file system, you can delete it.

###### To delete the file system

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Select the file system to delete.
3. Choose **Actions**, **Delete file
   system**.
4. When prompted for confirmation, enter the file system ID and choose
   **Delete file system**.
