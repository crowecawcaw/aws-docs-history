

# Managing FSx for ONTAP storage virtual machines
<a name="managing-svms"></a>

In FSx for ONTAP, volumes are hosted on virtual file servers called storage virtual machines (SVMs). An SVM is an isolated file server with its own administrative credentials and endpoints for administering and accessing data. When you access data in FSx for ONTAP, your clients and workstations mount a volume, SMB share, or iSCSI LUN hosted by an SVM using the SVM's endpoint (IP address).

Amazon FSx automatically creates a default SVM on your file system when you create a file system using the AWS Management Console. You can create additional SVMs on your file system at any time using the console, AWS CLI, or Amazon FSx API and SDKs. You cannot create SVMs using the ONTAP CLI or REST API.

You can join your SVMs to a Microsoft Active Directory for file access authentication and authorization. For more information, see [Working with Microsoft Active Directory in FSx for ONTAP](ad-integration-ontap.md).

## Maximum number of SVMs per file system
<a name="max-svms"></a>

The following table lists the maximum number of SVMs that you can create for a file system. The maximum number of SVMs depends on the amount of throughput capacity provisioned in megabytes per second (MBps), and also on the file system's [network type](manage-network-type.md).



- ** 1 HA pair **
  - **Amount of throughput capacity (MBps):** 128 / **Maximum number of SVMs per file system (IPv4-only mode):** 6 / **Maximum number of SVMs per file system (dual-stack mode):** 6
  - **Amount of throughput capacity (MBps):** 256 / **Maximum number of SVMs per file system (IPv4-only mode):** 6 / **Maximum number of SVMs per file system (dual-stack mode):** 6
  - **Amount of throughput capacity (MBps):** 384 / **Maximum number of SVMs per file system (IPv4-only mode):** 6 / **Maximum number of SVMs per file system (dual-stack mode):** 6
  - **Amount of throughput capacity (MBps):** 512 / **Maximum number of SVMs per file system (IPv4-only mode):** 14 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 768 / **Maximum number of SVMs per file system (IPv4-only mode):** 6 / **Maximum number of SVMs per file system (dual-stack mode):** 6
  - **Amount of throughput capacity (MBps):** 1,024 / **Maximum number of SVMs per file system (IPv4-only mode):** 14 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 1,536 / **Maximum number of SVMs per file system (IPv4-only mode):** 14 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 2,048 / **Maximum number of SVMs per file system (IPv4-only mode):** 24 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 3,072 / **Maximum number of SVMs per file system (IPv4-only mode):** 14 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 4,096 / **Maximum number of SVMs per file system (IPv4-only mode):** 24 / **Maximum number of SVMs per file system (dual-stack mode):** 11
  - **Amount of throughput capacity (MBps):** 6,144 / **Maximum number of SVMs per file system (IPv4-only mode):** 24 / **Maximum number of SVMs per file system (dual-stack mode):** 11

- **2–12 HA pairs**
  - **Amount of throughput capacity (MBps):** Any
  - **Maximum number of SVMs per file system (IPv4-only mode):** 11
  - **Maximum number of SVMs per file system (dual-stack mode):** 11



**Topics**
+ [Maximum number of SVMs per file system](#max-svms)
+ [Creating storage virtual machines (SVM)](creating-svms.md)
+ [Updating storage virtual machines (SVM)](updating-svms.md)
+ [Managing SVM Microsoft Active Directory configurations](manage-svm-ad-config-secrets-manager.md)
+ [Auditing file access](file-access-auditing.md)
+ [Setting up an SMB server in a workgroup](smb-server-workgroup-setup.md)
+ [Monitoring storage virtual machine (SVM) configuration details](viewing-svms.md)
+ [Deleting storage virtual machines (SVM)](deleting-svms.md)