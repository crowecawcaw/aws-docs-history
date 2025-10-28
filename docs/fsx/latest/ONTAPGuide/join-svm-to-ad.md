# Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API

Use the following procedure to join an existing SVM to an Active Directory.
In this procedure, the SVM is _not_ already joined to an Active Directory.

###### To join an SVM to an Active Directory (AWS Management Console)

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  Choose the SVM that you want to join to an Active Directory:

        * In the left navigation pane, choose **File systems**, and then choose the
         ONTAP file system with the SVM that you want to update.
        * Choose the **Storage virtual machines**
         tab.


        –Or–
        * To display a list of all of the available SVMs, in the left navigation pane, expand
         **ONTAP** and choose **Storage virtual
         machines**. A list of all SVMs in
         your account in the AWS Region is displayed.

    Select the SVM that you want to join to an Active Directory from the list.

3.  On the upper right of the SVM **Summary** panel, choose
    **Actions** > **Join/Update Active Directory**.
    The **Join SVM to an Active Directory** window appears.
4.  Enter the following information for the Active Directory that you are joining the SVM to:
    - The **NetBIOS name** of the Active Directory computer object to create for your SVM.
      This is the name of the SVM in Active Directory, which must be unique within your Active Directory. Don't use
      the NetBIOS name of the home domain. The NetBIOS name can't exceed 15
      characters.
    - The **fully qualified domain name (FQDN)** of your Active Directory. The domain name can't exceed 255 characters.
    - **DNS server IP addresses** – The IPv4 or IPv6 addresses of the DNS servers for your domain.
    - **Service account username** – The user name of the service
      account in your existing Active Directory. Don't include a domain prefix or suffix.
      For example, for `EXAMPLE\ADMIN`, use only `ADMIN`.
    - **Service account password** – The password for the service account.
    - **Confirm password** – The password for the service account.
    - (Optional) **Organizational Unit (OU)** – The distinguished
      path name of the organizational unit you want to join your SVM to.
    - **Delegated file system administrators group** – The name of the group
      in your Active Directory that can administer your file system.

    If you are using AWS Managed Microsoft AD, you must specify a group such as AWS Delegated FSx
    Administrators, AWS Delegated Administrators, or a custom group with delegated
    permissions to the OU.

    If you are joining to a self-managed Active Directory, use the name of the group in your Active Directory. The default group is
    `Domain Admins`.

5.  Choose **Join Active Directory** to join the SVM to the Active Directory using
    the configuration you provided.

###### To join an SVM to an Active Directory (AWS CLI)

- To join an FSx for ONTAP SVM to an Active Directory, use the [update-storage-virtual-machine](../../../cli/latest/reference/fsx/update-storage-virtual-machine.md "../../../cli/latest/reference/fsx/update-storage-virtual-machine.md") CLI command (or the equivalent [UpdateStorageVirtualMachine](../APIReference/API_UpdateStorageVirtualMachine.md "../APIReference/API_UpdateStorageVirtualMachine.md") API operation), as shown in the following
  example.

```
`aws fsx update-storage-virtual-machine \
 --storage-virtual-machine-id svm-abcdef0123456789a\
 --active-directory-configuration SelfManagedActiveDirectoryConfiguration='{DomainName="corp.example.com", \
 OrganizationalUnitDistinguishedName="OU=FileSystems,DC=corp,DC=example,DC=com",\
 FileSystemAdministratorsGroup="FSxAdmins",UserName="`FSxService`",\
 Password="`password`", \
 DnsIps=["10.0.1.18"]}',NetBiosName=amznfsx12345`
```

After successfully creating the storage virtual machine, Amazon FSx returns its
description in JSON format, as shown in the following
example.

```
`{
 "StorageVirtualMachine": {
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
 "CreationTime": 1625066825.306,
 "Endpoints": {
 "Management": {
 "DnsName": "svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
 "IpAddressses": ["198.19.0.4"]
 },
 "Nfs": {
 "DnsName": "svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
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
 "DnsName": "iscsi.svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
 "IpAddressses": ["198.19.0.7", "198.19.0.8"]
 }
 },
 "FileSystemId": "fs-0123456789abcdef0",
 "Lifecycle": "CREATED",
 "Name": "vol1",
 "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:storage-virtual-machine/fs-0123456789abcdef0/svm-abcdef0123456789a",
 "StorageVirtualMachineId": "svm-abcdef0123456789a",
 "Subtype": "default",
 "Tags": [],

 }
}`
```
