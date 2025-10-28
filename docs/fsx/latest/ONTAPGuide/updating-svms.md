# Updating storage virtual machines (SVM)

You can update the following storage virtual machine (SVM) configuration properties using
the Amazon FSx console, AWS CLI, and Amazon FSx API:

- SVM administrative account password.
- SVM Active Directory (AD) configuration – You can join an SVM to an AD, or
  modify the AD configuration of an SVM already joined to an AD. For more information,
  see [Managing SVM Active Directory configurations](manage-svm-ad-config.md "manage-svm-ad-config.md").

###### To update the SVM administrator account credentials (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose the SVM to update as follows:
   - In the left navigation pane, choose **File systems**, and then choose the
     ONTAP file system for which you want to update an SVM.
   - Choose the **Storage virtual machines**
     tab.

   –Or–
   - To display a list of all the SVMs available in your AWS account in the current AWS Region,
     expand **ONTAP** and choose **Storage virtual machines**.

3. Choose the storage virtual machine that you want to update.
4. Choose **Actions > Update administrator password**.
   The **Update SVM administrative credentials** window appears.
5. Enter the new password for the `vsadmin` user, and confirm it.
6. Choose **Update credentials** to save the new password.

###### To update the SVM administrator account credentials (CLI)

- To update the configuration of an FSx for ONTAP SVM, use the
  [update-storage-virtual-machine](../../../cli/latest/reference/fsx/update-storage-virtual-machine.md "../../../cli/latest/reference/fsx/update-storage-virtual-machine.md") CLI command (or the
  equivalent [UpdateStorageVirtualMachine](../APIReference/API_UpdateStorageVirtualMachine.md "../APIReference/API_UpdateStorageVirtualMachine.md") API operation), as shown in
  the following
  example.

```
`aws fsx update-storage-virtual-machine \
--storage-virtual-machine-id svm-abcdef01234567890 \
--svm-admin-password `new-svm-password` \`
```

After successfully creating the storage virtual machine, Amazon FSx returns its
description in JSON format, as shown in the following
example.

```
{
  "StorageVirtualMachine": {
    "CreationTime": 1625066825.306,
    "Endpoints": {
      "Management": {
        "DnsName": "svm-abcdef01234567890.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.4"]
      },
      "Nfs": {
        "DnsName": "svm-abcdef01234567890.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.4"]
      },
      "Smb": {
        "DnsName": "amznfsx12345",
        "IpAddressses": ["198.19.0.4"]
      },
      "SmbWindowsInterVpc": {
        "IpAddressses": ["198.19.0.5", "198.19.0.6"]
      },
      "Iscsi": {
        "DnsName": "iscsi.svm-abcdef01234567890.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.7", "198.19.0.8"]
      }
    },
    "FileSystemId": "fs-0123456789abcdef0",
    "Lifecycle": "CREATING",
    "Name": "vol1",
    "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:storage-virtual-machine/fs-0123456789abcdef0/svm-abcdef01234567890",
    "StorageVirtualMachineId": "svm-abcdef01234567890",
    "Subtype": "default",
    "Tags": [],
    "ActiveDirectoryConfiguration": {
      "NetBiosName": "amznfsx12345",
      "SelfManagedActiveDirectoryConfiguration": {
        "UserName": "Admin",
        "DnsIps": [
          "10.0.1.3",
          "10.0.91.97"
        ],
        "OrganizationalUnitDistinguishedName": "OU=Computers,OU=customer-ad,DC=customer-ad,DC=example,DC=com",
        "DomainName": "customer-ad.example.com"
      }
    }
  }
}
```
