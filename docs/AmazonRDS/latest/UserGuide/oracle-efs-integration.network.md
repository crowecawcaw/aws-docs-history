

# Configuring network permissions for RDS for Oracle integration with Amazon EFS
<a name="oracle-efs-integration.network"></a>

For RDS for Oracle to integrate with Amazon EFS, make sure that your DB instance has network access to an EFS file system. For more information, see [Controlling network access to Amazon EFS file systems for NFS clients](https://docs.aws.amazon.com/efs/latest/ug/NFS-access-control-efs.html) in the *Amazon Elastic File System User Guide*.

**Topics**
+ [Controlling network access with security groups](#oracle-efs-integration.network.inst-access)
+ [Controlling network access with file system policies](#oracle-efs-integration.network.file-system-policy)

## Controlling network access with security groups
<a name="oracle-efs-integration.network.inst-access"></a>

You can control your DB instance access to EFS file systems using network layer security mechanisms such as VPC security groups. To allow access to an EFS file system for your DB instance, make sure that your EFS file system meets the following requirements:
+ An EFS mount target exists in every Availability Zone used by an RDS for Oracle DB instance.

  An *EFS mount target* provides an IP address for an NFSv4 endpoint at which you can mount an EFS file system. You mount your file system using its DNS name, which resolves to the IP address of the EFS mount target in the used by the Availability Zone of your DB instance. 

  You can configure DB instances in different AZs to use the same EFS file system. For Multi-AZ, you need a mount point for each AZ in your deployment. You might need to move a DB instance to a different AZ. For these reasons, we recommend that you create an EFS mount point in each AZ in your VPC. By default, when you create a new EFS file system using the console, RDS creates mount targets for all AZs.
+ A security group is attached to the mount target.
+ The security group has an inbound rule to allow the network subnet or security group of the RDS for Oracle DB instance on TCP/2049 (Type NFS).

For more information, see [Creating Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#configure-efs-network-access) and [Creating and managing EFS mount targets and security groups](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) in the *Amazon Elastic File System User Guide*.

## Controlling network access with file system policies
<a name="oracle-efs-integration.network.file-system-policy"></a>

Amazon EFS integration with RDS for Oracle works with the default (empty) EFS file system policy. The default policy doesn't use IAM to authenticate. Instead, it grants full access to any anonymous client that can connect to the file system using a mount target. The default policy is in effect whenever a user-configured file system policy isn't in effect, including at file system creation. For more information, see [Default EFS file system policy](https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html#default-filesystempolicy) in the *Amazon Elastic File System User Guide*.

To strengthen access to your EFS file system for all clients, including RDS for Oracle, you can configure IAM permissions. In this approach, you create a file system policy. For more information, see [Creating file system policies](https://docs.aws.amazon.com/efs/latest/ug/create-file-system-policy.html) in the *Amazon Elastic File System User Guide*.