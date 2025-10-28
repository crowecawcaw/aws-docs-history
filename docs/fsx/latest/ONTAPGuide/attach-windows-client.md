# Mounting volumes on Microsoft Windows

clients

This section describes how to access data in your FSx for ONTAP file system with
clients running the Microsoft Windows operating system. Review the following
requirements, regardless of the type of client you are using.

This procedure assumes that the client and the file system are located in the same
VPC and AWS account. If the client is located on-premise or in a different VPC,
AWS account, or AWS Region, this procedure also assumes that you've set up
AWS Transit Gateway or a dedicated network connection using AWS Direct Connect or a private,
secure tunnel using AWS Virtual Private Network. For more information, see [Accessing data from outside the
deployment VPC](supported-fsx-clients.md#access-from-outside-deployment-vpc "supported-fsx-clients.md#access-from-outside-deployment-vpc").

We recommend that you attach volumes to your Windows clients using the SMB
protocol.

## Prerequisites

To access an ONTAP storage volume using a Microsoft Windows client, you have
to satisfy the following prerequisites:

- The SVM of the volume you are attaching must be joined to your
  organization's Active Directory, or you must be using a workgroup. For more information on
  joining your SVM to an Active Directory, see [Managing FSx for ONTAP storage virtual machines](managing-svms.md "managing-svms.md"). For more information on
  using workgroups, see [Setting up an SMB server in a workgroup](smb-server-workgroup-setup.md "smb-server-workgroup-setup.md").
- The volume you are attaching should have a security style setting of
  `NTFS`. For more information, see
  [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").

###### To mount a volume on a Windows client using SMB and Active Directory

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Create or select an Amazon EC2 instance running Microsoft Windows that is in
   the same VPC as the file system, and joined to the same Microsoft Active Directory as the
   volume's SVM.

For more information on launching an instance, see [Step 1: Launch an instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance") in the
_Amazon EC2 User Guide_.

For more information about joining an SVM to an Active Directory, see
[Managing FSx for ONTAP storage virtual machines](managing-svms.md "managing-svms.md"). 3. Connect to your Amazon EC2 Windows instance. For more information, see [Connecting to your Windows instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the
_Amazon EC2 User Guide_. 4. Open a command prompt. 5. Run the following command. Replace the following:

    * Replace `Z:` with any available drive letter.
    * Replace `DNS_NAME` with the DNS name or the IP address
     of the SMB endpoint for the volume's SVM.
    * Replace `SHARE_NAME` with the name of an SMB share.
     `C$` is the default SMB share at the root of the SVM's
     namespace, but you shouldn't mount it as that exposes storage to
     the root volume and can cause security and service disruption.
     You should provide an SMB share name to mount instead of `C$`. For
     more information about creating SMB shares, see [Managing SMB shares](create-smb-shares.md "create-smb-shares.md").

```
net use Z: \\`DNS_NAME`\`SHARE_NAME`
```

The following example uses sample values.

```
net use Z: \\corp.example.com\group_share
```

You can also use the IP address of the SVM instead of its DNS name. We recommend using the DNS name to mount clients to second-generation file
systems because it helps ensure that your clients are balanced across your file system's high-availability (HA) pairs.

```
net use Z: \\198.51.100.5\group_share
```
