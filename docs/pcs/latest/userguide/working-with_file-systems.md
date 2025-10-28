# Using network file systems with AWS PCS

You can attach network file systems to nodes launched in an AWS Parallel Computing Service (AWS PCS)
compute node group to provide a persistent location where data and files can be written and
accessed. You can use file systems provided by AWS services, including [Amazon Elastic File System](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") (Amazon EFS),
[Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md"),
[Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md"),
[Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md"),
and [Amazon File Cache](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md").
You can also use self-managed file systems, such as NFS servers.

This topic covers considerations for and examples of using network file systems with
AWS PCS.

## Considerations for using network

file systems

The implementation details for various file systems are different, but there are some common
considerations.

- The relevant file system software must be installed on the instance. For example, to use
  Amazon FSx for Lustre, the appropriate Lustre package should be present. This can be
  accomplished by including it in the compute node group AMI or using a script that runs at
  instance boot.
- There must be a network route between the shared network file system and the compute node group
  instances.
- The security group rules for both the shared network file system and the compute node group
  instances must allow connections to the relevant ports.
- You must maintain a consistent POSIX user and group namespace across
  resources that access the file systems. Otherwise, jobs and interactive processes that run on
  your PCS cluster may encounter permissions errors.
- File system mounts are done using EC2 launch templates. Errors or timeouts
  in mounting a network file system may prevent instances from becoming available to run jobs.
  This, in turn, may lead to unexpected costs. For more information about debugging launch
  templates, see [Using Amazon EC2 launch templates
  with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").

## Example network mounts

You can create file systems using Amazon EFS, Amazon FSx for Lustre, Amazon FSx for NetApp ONTAP, Amazon FSx for OpenZFS,
and Amazon File Cache. Expand the relevant section below to see an
example of each network mount.

**File system setup**

Create an Amazon EFS file system. Make sure it has a mount target in each Availability Zone
where you will launch PCS compute node group instances. Also ensure each mount
target is associated with a security group that allows inbound and outbound access from the
PCS compute node group instances. For more information, see [Mount targets and security
groups](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md") in the _Amazon Elastic File System User Guide_.

**Launch template**

Add the security group(s) from your file system setup to the launch template you will use
for the compute node group.

Include user data that uses `cloud-config` mechanism to mount the Amazon EFS file
system. Replace the following values in this script with your own details:

- `mount-point-directory` – The path on a each instance where you will
  mount Amazon EFS
- `filesystem-id` – The file system ID for the EFS file system

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
  - amazon-efs-utils

runcmd:
  - mkdir -p /`mount-point-directory`
  - echo "`filesystem-id`:/ /`mount-point-directory` efs tls,_netdev" >> /etc/fstab
  - mount -a -t efs defaults

--==MYBOUNDARY==--
```

**File system setup**

Create an FSx for Lustre file system in the VPC where you will use AWS PCS. To minimize
inter-zone transfers, deploy in a subnet in the same Availability Zone where you will launch
the majority of your PCS compute node group instances. Ensure the file system is
associated with a security group that allows inbound and outbound access from the
PCS compute node group instances. For more information on security groups, see
[File system access control with Amazon VPC](../../../fsx/latest/LustreGuide/limit-access-security-groups.md "../../../fsx/latest/LustreGuide/limit-access-security-groups.md") in the _Amazon FSx for Lustre User Guide_.

**Launch template**

Include user data that uses `cloud-config` to mount the FSx for Lustre file
system. Replace the following values in this script with your own details:

- `mount-point-directory` – The path on an instance where you want to mount FSx for Lustre
- `filesystem-id` – The file system ID for the FSx for Lustre
  file system
- `mount-name` – The mount name for the FSx for Lustre file system
- `region-code` – The AWS Region where the FSx for Lustre file system is
  deployed (must be the same as your AWS PCS system)
- (Optional) `latest` – Any version of Lustre supported
  by FSx for Lustre

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- amazon-linux-extras install -y lustre=`latest`
- mkdir -p /`mount-point-directory`
- mount -t lustre `filesystem-id`.fsx.`region-code`.amazonaws.com@tcp:/`mount-name` /`mount-point-directory`

--==MYBOUNDARY==

```

**File system setup**

Create an Amazon FSx for NetApp ONTAP file system in the VPC where you will use AWS PCS.
To minimize inter-zone transfers, deploy in a subnet in the same Availability Zone where you
will launch the majority of your AWS PCS compute node group instances. Make sure the file
system is associated with a security group that allows inbound and outbound access from the
AWS PCS compute node group instances. For more information on security groups, see
[File
System Access Control with Amazon VPC](../../../fsx/latest/ONTAPGuide/limit-access-security-groups.md "../../../fsx/latest/ONTAPGuide/limit-access-security-groups.md") in the _FSx for ONTAP User Guide_.

**Launch template**

Include user data that uses `cloud-config` to mount the root volume for an
FSx for ONTAP file system. Replace the following values in this script with your own details:

- `mount-point-directory` – The path on
  an instance where you want to mount your FSx for ONTAP volume
- `svm-id` – The SVM ID for the FSx for ONTAP
  file system
- `filesystem-id` – The file system ID
  for the FSx for ONTAP file system
- `region-code` – The AWS Region
  where the FSx for ONTAP file system is deployed (must be the same as your AWS PCS
  system)
- `volume-name` – The FSx for ONTAP volume
  name

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- mkdir -p /`mount-point-directory`
- mount -t nfs `svm-id`.`filesystem-id`.fsx.`region-code`.amazonaws.com:/`volume-name` /`mount-point-directory`

--==MYBOUNDARY==
```

**File system setup**

Create an FSx for OpenZFS file system in the VPC where you will use AWS PCS.
To minimize inter-zone transfers, deploy in a subnet in the same Availability Zone
where you will launch the majority of your AWS PCS compute node group instances. Make sure
the file system is associated with a security group that allows inbound and outbound
access from the AWS PCS compute node group instances. For more information on security
groups, see [Managing file system access
with Amazon VPC](../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md "../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md") in the _FSx for OpenZFS User Guide_.

**Launch template**

Include user data that uses `cloud-config` to mount the root volume for an
FSx for OpenZFS file system. Replace the following values in this script with your own
details:

- `mount-point-directory` – The path on an instance
  where you want to mount your FSx for OpenZFS share
- `filesystem-id` – The file system ID for the FSx for OpenZFS
  file system
- `region-code` – The AWS Region where the FSx for OpenZFS
  file system is deployed (must be the same as your AWS PCS system)

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- mkdir -p /`mount-point-directory`
- mount -t nfs -o noatime,nfsvers=4.2,sync,rsize=1048576,wsize=1048576 `filesystem-id`.fsx.`region-code`.amazonaws.com:/fsx/ /`mount-point-directory`

--==MYBOUNDARY==
```

**File system setup**

Create an [Amazon File Cache](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md") in the VPC where you will use AWS PCS. To
minimize inter-zone transfers, choose a subnet in the same Availability Zone where you will
launch the majority of your PCS compute node group instances. Ensure the File
Cache is associated with a security group that allows inbound and outbound traffic on port 988
between your PCS instances and the File Cache. For more information on security
groups, see [Cache access control with
Amazon VPC](../../../fsx/latest/FileCacheGuide/limit-access-security-groups.md "../../../fsx/latest/FileCacheGuide/limit-access-security-groups.md") in the _Amazon File Cache User Guide_.

**Launch template**

Add the security group(s) from your file system setup to the launch template you will use
for the compute node group.

Include user data that uses `cloud-config` to mount the
Amazon File Cache. Replace the following values in this script
with your own details:

- `mount-point-directory` – The path on an instance where you want to mount FSx for Lustre
- `cache-dns-name` – The Domain Name System (DNS) name for the File
  Cache
- `mount-name` – The mount name for the File Cache

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- amazon-linux-extras install -y lustre=2.12
- mkdir -p /`mount-point-directory`
- mount -t lustre -o relatime,flock `cache-dns-name`@tcp:/`mount-name` /`mount-point-directory`

--==MYBOUNDARY==
```
