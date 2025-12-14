# SAP Shared File Systems

###### Topics

- [Select Shared Storage](#select-storage-type-nw-rhel "#select-storage-type-nw-rhel")
- [Create file systems](#create-filesystems-nw-rhel "#create-filesystems-nw-rhel")
- [Create mount point directories](#create-mount-dirs-nw-rhel "#create-mount-dirs-nw-rhel")
- [Update /etc/fstab](#update-fstab-nw-rhel "#update-fstab-nw-rhel")
- [Temporarily mount ASCS and ERS directories for installation (classic only)](#temp-mount-dirs-nw-rhel "#temp-mount-dirs-nw-rhel")

## Select Shared Storage

SAP NetWeaver high availability deployments require shared file systems. On Linux, you can use either [Amazon Elastic File System](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") or [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/"). Choose between these options based on your requirements for resilience, performance, and cost. For detailed setup information, see [Getting started with Amazon Elastic File System](../../../efs/latest/ug/getting-started.md "../../../efs/latest/ug/getting-started.md") or [Getting started with Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/getting-started.md "../../../fsx/latest/ONTAPGuide/getting-started.md").

We recommend sharing a single Amazon EFS or FSx for ONTAP file system across multiple SIDs within an account.

The file system’s DNS name is the simplest mounting option. When connecting from an Amazon EC2 instance, the DNS automatically resolves to the mount target’s IP address in that instance’s Availability Zone. You can also create an alias (CNAME) to help identify the shared file system’s purpose. Throughout this document, we use `<nfs.fqdn>`.

Examples:

- `file-system-id.efs.aws-region.amazonaws.com`
- `svm-id.fs-id.fsx.aws-region.amazonaws.com`
- `qas_sapmnt_share.example.com`

###### Note

Review the `enableDnsHostnames` and `enableDnsSupport` DNS attributes for your VPC. For more information, see [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating").

## Create file systems

The following shared file systems are covered in this document:

| NFS Location Structure   | NFS Location Example | File System Location Structure   | File System Location Example |
| ------------------------ | -------------------- | -------------------------------- | ---------------------------- |
| <SID>\_sapmnt            | `RHX_sapmnt`         | /sapmnt/<SID>                    | `/sapmnt/RHX`                |
| <SID>\_ASCS<ascs_sys_nr> | `RHX_ASCS00`         | /usr/sap/<SID>/ASCS<ascs_sys_nr> | `/usr/sap/RHX/ASCS00`        |
| <SID>\_ERS<ers_sys_nr>   | `RHX_ERS10`          | /usr/sap/<SID>/ERS<ers_sys_nr>   | `/usr/sap/RHX/ERS10`         |

The following options can differ depending on how you architect and operate your systems:

- ASCS and ERS mount points - In simple-mount architecture, you can share the entire `/usr/sap/<SID>` directory. This document uses separate mount points to simplify migration and follow SAP’s recommendation for local application server executables when co-hosting ASCS/ERS.
- Transport directory - `/usr/sap/trans` is optional for ASCS installations. Add this shared directory if your change management processes require it.
- Home directory - This document uses local home directories to ensure `<sid>adm` access during NFS issues. Consider a shared home directory if you need consistent user environments across nodes.
- NFS location naming - The "NFS Location" names are arbitrary and can be chosen based on your naming conventions (e.g., `myEFSMount1`, `prod_sapmnt`, etc.). The "File system location" follows the standard SAP directory structure and should use the parameter references shown.

For more information, see [SAP System Directories on UNIX](https://help.sap.com/docs/SAP_NETWEAVER_750/ff18034f08af4d7bb33894c2047c3b71/2744f17a26a74a8abfd202c4f5dc9a0f.html "https://help.sap.com/docs/SAP_NETWEAVER_750/ff18034f08af4d7bb33894c2047c3b71/2744f17a26a74a8abfd202c4f5dc9a0f.html").

Using the NFS ID created in the previous step, temporarily mount the root directory of the NFS. `/mnt` is available by default; it can also be substituted with another temporary location.

###### Note

The following commands use the NFS location names from the table above. Replace `<SID>_sapmnt`, `<SID>_ASCS<ascs_sys_nr>`, and `<SID>_ERS<ers_sys_nr>` with your chosen NFS location names and parameter values.

```
# mount <nfs.fqdn>:/ /mnt
# mkdir -p /mnt/<SID>_sapmnt
# mkdir -p /mnt/<SID>_ASCS<ascs_sys_nr>
# mkdir -p /mnt/<SID>_ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# mount fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/ /mnt
# mkdir -p /mnt/RHX_sapmnt
# mkdir -p /mnt/RHX_ASCS00
# mkdir -p /mnt/RHX_ERS10
```

During SAP installation, the `<sid>adm` user and proper directory ownership will be created. Until then, we need to ensure the installation process has sufficient access. Set temporary permissions on the directories:

```
# chmod 777 /mnt/<SID>_sapmnt /mnt/<SID>_ASCS<ascs_sys_nr> /mnt/<SID>_ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# chmod 777 /mnt/RHX_sapmnt /mnt/RHX_ASCS00 /mnt/RHX_ERS10
```

The SAP installation process will automatically set the correct ownership and permissions for operational use.

Unmount the temporary mount:

```
# umount /mnt
```

## Create mount point directories

This is applicable to both cluster nodes. Create the directories for the required mount points (permanent or cluster controlled):

```
# mkdir /sapmnt
# mkdir /usr/sap/<SID>/ASCS<ascs_sys_nr>
# mkdir /usr/sap/<SID>/ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# mkdir /sapmnt
# mkdir /usr/sap/RHX/ASCS00
# mkdir /usr/sap/RHX/ERS10
```

## Update /etc/fstab

This is applicable to both cluster nodes. `/etc/fstab` is a configuration table containing the details required for mounting and unmounting file systems to a host.

Add the file systems not managed by the cluster to `/etc/fstab`.

For both **simple-mount** and **classic** architectures, prepare and append an entry for the `sapmnt` file system to `/etc/fstab`:

```
<nfs.fqdn>/<SID>_sapmnt    /sapmnt    nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
```

**Simple-mount only** – prepare and append entries for the ASCS and ERS file systems to `/etc/fstab`:

```
<nfs.fqdn>:/<SID>_ASCS<ascs_sys_nr>   /usr/sap/<SID>/ASCS<ascs_sys_nr>  nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
<nfs.fqdn>:/<SID>_ERS<ers_sys_nr>     /usr/sap/<SID>/ERS<ers_sys_nr>    nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_sapmnt    /sapmnt               nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ASCS00    /usr/sap/RHX/ASCS00   nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ERS10     /usr/sap/RHX/ERS10    nfs    nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport    0    0
```

Verify that your mount options are:

- Compatible with your operating system version
- Supported by your chosen NFS file system type (EFS or FSx for ONTAP)
- Aligned with current SAP recommendations

Consult SAP and AWS documentation for the latest mount option recommendations.

Use the following command to mount the file systems defined in `/etc/fstab`:

```
# mount -a
```

Use the following command to check that the required file systems are available:

```
# df -h
```

## Temporarily mount ASCS and ERS directories for installation (classic only)

This is only applicable to the classic architecture. Simple-mount architecture has these directories permanently available in `/etc/fstab`.

Mount ASCS and ERS directories for installation.

Use the following command on the instance where you plan to install ASCS:

```
# mount <nfs.fqdn>:/<SID>_ASCS<ascs_sys_nr>  /usr/sap/<SID>/ASCS<ascs_sys_nr>
```

Use the following command on the instance where you plan to install ERS:

```
# mount <nfs.fqdn>:/<SID>_ERS<ers_sys_nr>  /usr/sap/<SID>/ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# mount fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ASCS00  /usr/sap/RHX/ASCS00
# mount fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ERS10   /usr/sap/RHX/ERS10
```
